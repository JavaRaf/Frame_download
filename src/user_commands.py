import re
from env import data
from gifs.crud_gifs import add, send
import re
import os
from add_captions import legendar
from get_images import sync_download_frame
from upload_process import imgBB, up_to_fb, publish_image_fb
from load_ids import save_ids_to_txt
from send_frame_to_fb import enviar_frame_to_fb



def extract_frame(message, id):
    episodio, frame, captions = '', '', ''
    primeriros_dois_numeros = re.findall(r'\d+', message)

    numeros = primeriros_dois_numeros[:2]
    if len(numeros) == 2:
        episodio = numeros[0]
        frame = numeros[1]
        
        if '-t' in message:
            result = re.findall(r'"(.*?)"', message)
            captions = ' '.join(result)
    
    enviar_frame_to_fb(episodio, frame, id, captions)      


        
             
def search_command(comments_ids, comments_messages):
      for id, message in zip(comments_ids, comments_messages):
          
            if message.startswith('!dl') and '-e' in message and '-f' in message:
                extract_frame(message, id)
                                 