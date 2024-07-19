from get_images import sync_download_frame
from upload_process import imgBB, up_to_fb, publish_image_fb
from load_ids import save_ids_to_txt
from add_captions import legendar

def enviar_frame_to_fb(ep, frame, id, captions):
    
    path = sync_download_frame(ep, frame)
    
    link = ''

    help_message = f"Sorry, I couldn't find the image,\ncheck the comment and try again.\n\
    link for help:\n\n https://www.facebook.com/FrierenFrames/posts/pfbid02SQdtRHZDHczYHZEUCBEHcPAdLHUv7pVbdqaFxBkA3hJ3sYiGSjxsigmT9hosvmkTl"
    
    if 'help' in path:
       foto_id = up_to_fb(path)
       if foto_id:
            status_code = publish_image_fb(foto_id, id, help_message)
            if status_code == 200:
                print('comentario de ajuda enviado')
                save_ids_to_txt(id)
       
    elif 'frame' in path:
        
        if captions:
            path = legendar(path, captions)
            
        link = imgBB(path)
        
        img_message = f'Filename: Episode {ep}, Frame {frame} \n\n Resolution: 1920x1080 \n Link: {link}'
        
        if link:
            foto_id = up_to_fb(path)
            if foto_id:
                status_code = publish_image_fb(foto_id, id, img_message)
                if status_code == 200:
                    print('imagem enviada, comentario respondido')
                    save_ids_to_txt(id)


            


        
    







