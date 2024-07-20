import os


class data:
    
    post_priority: str = '136437712888196_122186265332068249' # id de um post fixado na pagida
  
    # facebook
    FB_TOKEN: str = os.environ.get('FB_TOKEN')
    fb_version: str = 'v19.0'
    fb_url = f'https://graph.facebook.com/{fb_version}'
    
    # github
    REPO_FRAMES_NAME: str = 'SNF'  # nome do repositorio onde estao os frames
    GITHUB_FRAMES_BRANCH: str = 'master' # branch dos frames
    
    REPO_OWNER: str = os.environ.get('REPO_OWNER')  # seu nome de usuario do github

    git_this_branch: str = os.environ.get('BRANCH') # THIS_BRANCH
    GIT_PAT: str = os.environ.get('GIT_PAT')  
    
    # tenor token
    TENOR_TOKEN: str = os.environ.get('TENOR_TOKEN')
    
    # imgBB
    img_url = 'https://api.imgbb.com/1/upload'
    IMG_TOKEN: str = os.environ.get('IMG_TOKEN')
   
    
    # outros 
    init: int = 0  # usado para pegar os posts_ids
    max: int = 5  # cada interação pega no maximo 100 comentarios por post
    
    sub_comments_interval: int = 3  # controla o numero de rquests para sub_comments
    #select a random gif for comment 
    random_gif = []