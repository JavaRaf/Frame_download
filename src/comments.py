import httpx
from time import time, sleep
import asyncio
from env import data
from os import environ


def get_comments_from_posts():
    comments_ids = []
    comments = []
    
    #comments_ids.append(data.post_priority)
    #comments_ids.append('controll comment')
    
    dados = {'fields': 'comments.limit(100)', 'limit': '100', 'access_token': data.FB_TOKEN}
    try:
        
        while data.init < data.max:
            response = httpx.get(f'{data.fb_url}/{environ.get("PAGE_ID")}/posts/', params=dados, timeout=10)
            if response.status_code == 200:
                response_data = response.json()
                
                for item in response_data.get('data', []):
                    comments_data = item.get('comments', {}).get('data', [])
                    if len(comments_data) >= 1:
                        for comment in comments_data:
                            if 'id' in comment:
                                comments.append(comment.get('message'))
                                comments_ids.append(comment.get('id'))
                
                # Check for pagination
                if 'paging' in response_data and 'next' in response_data['paging']:
                    after = response_data['paging']['cursors'].get('after', '')
                    dados['after'] = after
                    data.init += 1
                else:
                    break
            else:
                print(f"Failed to get posts: {response.status_code}")
                break
            
            sleep(1)
              
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error occurred: {exc}")
    except Exception as exc:
        print(f"An error occurred: {exc}")
                
    data.init = 0
    return comments_ids, comments


#-------------------------------------------------------------------------------------------------------------------------------------------------------

async def fetch_comments(session: httpx.AsyncClient, post_id: str, semaphore: asyncio.Semaphore) -> dict:

    url = f'{data.fb_url}/{post_id}/comments?limit=50&access_token={data.FB_TOKEN}'
    async with semaphore:
        try:
            response = await session.get(url, timeout=20)
            response.raise_for_status()
            return response.json()
            
        except httpx.HTTPStatusError as exc:
            print(f"HTTP error occurred for post_id {post_id}: {exc}")
            print(response.content.decode('utf-8'))
            time.sleep(10)
        except asyncio.CancelledError:
            print(f"Request for post_id {post_id} was cancelled.")
            time.sleep(10)
            raise  # Re-raise the CancelledError to propagate it
        except Exception as exc:
            print(f"An error occurred for post_id {post_id}: {exc}")
            time.sleep(10)
        return {}  # Return an empty dictionary in case of errors

async def get_comments_from_another_comments(new_ids):
    
    
    if data.sub_comments_interval >= 3:
        
        comments_ids = []
        messages = []

        semaphore = asyncio.Semaphore(100)  # Limit of 100 concurrent requests

        async with httpx.AsyncClient() as session:
            tasks = [fetch_comments(session, post_id, semaphore) for post_id in new_ids]
            responses = await asyncio.gather(*tasks, return_exceptions=True)  # Return exceptions for better error handling

            for response_data in responses:
                if isinstance(response_data, dict) and 'data' in response_data:
                    for item in response_data['data']:
                        if item:
                            comments_ids.append(item.get('id', ''))
                            messages.append(item.get('message', ''))
 
        data.sub_comments_interval = 0
        return comments_ids, messages

    else:
        print(f'\nA busca por respostas aos comentarios so sera feita daqui a {3 - data.sub_comments_interval} ciclos\n')
        data.sub_comments_interval += 1
        return [], []


#---------------------------------------------------------------------------------------------------------------------------------------------------------