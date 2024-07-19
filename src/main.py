import asyncio
from env import data
from comments import get_comments_from_posts, get_comments_from_another_comments
from page_id import get_id
import os
from time import time, sleep
from user_commands import search_command
from load_ids import check_ids


async def run_script():
    
    if os.environ.get("PAGE_ID"):
        
        start = time()
        # Get the comments from posts
        comments_ids: list[str] = []
        comments_messages: list[str] = []
        
        comments_ids, comments_messages = get_comments_from_posts()
        
        # Get the comments from other posts
        other_ids = []
        other_messages = []
        
        other_ids, other_messages = await get_comments_from_another_comments(comments_ids)
        end = time()
        
        print(f'----------------------------------------------\nA busca por comentarios levou: {end - start:.2f} segundos\n---------------------------------------------------------')
        
        # Combine comments
        comments_ids.extend(other_ids)
        comments_messages.extend(other_messages)
        
        print(f'----------------------------------------------\nRemovendo ids respondidos\n---------------------------------------------------------')
        new_ids, new_comments = check_ids(comments_ids, comments_messages)
        
        print('------------------------------------------------\nVerificando comentarios \n\n----------------------------------------------------------------')
        #--------------------------------------------------------------------------------------------------------------------------------
        search_command(new_ids, new_comments)
        

def main():
    
    # Get page_id from your facebook page
    get_id()
    
    if data.FB_TOKEN:
        print('fb token ok')
    
    else:
        print('Necessary token not provided')
        
    if data.GITHUB_TOKEN:
        print('github token ok')
    else:
        print('Necessary tokens not provided')
        
    if data.IMG_TOKEN:
        print('img token ok')
    else:
        print('Necessary img token not provided')
    
    start: float = time()
    while (time() - start) < (180 * 60):  # 3 hours
        asyncio.run(run_script())
        sleep(50)

if __name__ == '__main__':
    main()