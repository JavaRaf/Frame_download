import httpx
from time import sleep
from env import data
from os import environ

def get_id():
    
    retries: int = 0
    max_retries: int = 3
    
    while retries < max_retries:
        try:
            response = httpx.get(f'{data.fb_url}/me?access_token={data.FB_TOKEN}', timeout=5)
            if response.status_code != 200:
                print(f"Failed to get page ID: {response.status_code} {response.content}")
                retries += 1
            else:
                page_id: str = response.json().get('id')
                if page_id:
                    environ.setdefault("PAGE_ID", page_id)  
                    break
                
        except httpx.RequestError as e:
            retries += 1
            print(f"Request error: {e}\n. Retrying...")
            sleep(3)
    
    if retries == max_retries:
        print("Failed to get page ID after maximum retries")
    