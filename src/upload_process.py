from env import data
import httpx
from time import sleep

def imgBB(path_to_img):
    
    retries = 0
    max_retries = 3
    
    while retries < max_retries:
        try:
            
            name = path_to_img.split('.')[1]
            dados = {'key': data.IMG_TOKEN, 'name': f'{name}', 'expiration': 600000}

            with open(path_to_img, 'rb') as file:
                files = {'image': file}
                
                response = httpx.post(data.img_url, data=dados, files=files, timeout=10)
                if response.status_code == 200:
                    response_data = response.json()
                    link = response_data['data']['url']
                    
                    if link:
                        return link
                    
                else:
                    print('erro no imgbb', response.status_code)
                    print(response.text)
                    sleep(5)
                    retries += 1
                    
        except FileNotFoundError:
            print(f"O arquivo {path_to_img} não foi encontrado.")
            return None
    
    if retries == max_retries:
        print('tentativas maximas de fazer o upload para o img_bb alcançadas')
    
    return None


def up_to_fb(path_to_img: str): 
    
    retries = 0
    max_retries = 3
    
    while retries < max_retries:
        try:
            # Verificar se o caminho fornecido está correto
            with open(f'{path_to_img}', 'rb') as frame:
                files = {'file': (path_to_img, frame, 'image/jpeg')}
                
                dados = {
                    'published': 'false',
                    'access_token': data.FB_TOKEN
                }
                
                response = httpx.post(f'{data.fb_url}/me/photos', files=files, data=dados, timeout=10)
                
                if response.status_code == 200:
                    foto_id = response.json().get('id')
                    if foto_id:
                        return foto_id
                else:
                    print(f'Erro ao fazer upload: {response.status_code}, {response.text}')
                    retries += 1
            
        except FileNotFoundError:
            print(f'Arquivo {path_to_img} não encontrado')
            return ''
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
            return ''
    

def publish_image_fb(foto_id: str, id_comentario: str, message: str):
    retries = 0
    max_retries = 3
    
    while retries < max_retries:
        
        dados = {
            'message': message,
            'attachment_id': foto_id,
            'access_token': data.FB_TOKEN
        }
        response = httpx.post(f'{data.fb_url}/{id_comentario}/comments', data=dados, timeout=10)
    
        if response.status_code == 200:
            return response.status_code
        else:
            print('erro ao enviar a imagem pro fb', response.status_code, response.text)
            retries += 1

    return response.status_code