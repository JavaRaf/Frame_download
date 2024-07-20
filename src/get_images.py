from env import data
import httpx
import asyncio
import os
#async download------------------------------------------------------------------------------------
async def download_images(session, EP: str, FRAME: str) -> str:
    REPO_OWNER = 'JavaRaf'
    FRAME_PASTE = 'SNF'
    BRANCH = 'master'

    url = f'https://raw.githubusercontent.com/{REPO_OWNER}/{FRAME_PASTE}/{BRANCH}/EP-{EP}/frame_{FRAME}.jpg'
    
    headers = {
        'Authorization': f'Bearer {data.GIT_PAT}'
    }
    
    try:
        response = await session.get(url, headers=headers)
        
        if response.status_code == 200:
            # Certifique-se de que a pasta images existe
            os.makedirs('images', exist_ok=True)
            file_path = f'images/EP_{EP}_frame_{FRAME}.jpg'
            with open(file_path, 'wb') as file:
                file.write(response.content)
            
            return file_path
            
        else:
            print(f'Erro ao acessar o GitHub: {response.status_code}, URL: {url}')  # Debug print
    except Exception as e:
        print(f'Erro durante a requisição HTTP: {str(e)}, URL: {url}')  # Debug print

async def fetch_images_from_github(frames):
    async with httpx.AsyncClient() as session:
        tasks = []
        for EP, FRAME in frames:
            if EP and FRAME:
                tasks.append(download_images(session, EP, FRAME))
        
        results = await asyncio.gather(*tasks)
        return results

#sync_download ------------------------------------------------------------------------------------

def sync_download_frame(EP, FRAME) -> str:
    
    url = f'https://raw.githubusercontent.com/{data.REPO_OWNER}/{data.REPO_FRAMES_NAME}/{data.GITHUB_FRAMES_BRANCH}/EP-{EP}/frame_{FRAME}.jpg'
    
    headers = {'Authorization': f'Bearer {data.GIT_PAT}'}
    
    try:
        response = httpx.get(url, headers=headers)
        if response.status_code == 404:
            return f'images/helper/help.png'
        
        if response.status_code == 200:
            # Certifique-se de que a pasta images existe
            os.makedirs('images', exist_ok=True)
            with open(f'images/Ep_{EP}.frame_{FRAME}.jpg', 'wb') as file:
                file.write(response.content)
            
            return f'images/Ep_{EP}.frame_{FRAME}.jpg'
        
        else:
            print(f'Erro ao acessar o GitHub: {response.status_code}')
            print(response.text)  # Exibe o corpo da resposta para depuração
    except Exception as e:
        print(f'Erro durante a requisição HTTP: {str(e)}')










