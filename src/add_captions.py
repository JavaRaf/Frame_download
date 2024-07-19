import subprocess


def legendar(path_to_frame, captions):
    
    if captions:
        partes = captions.split(' ')
        if len(partes) <= 5:
            backgound_size = '0x150' 
            
        elif len(partes) <= 10:
            partes.insert(5, '\n')
            captions = ' '.join(partes)
            backgound_size = '0x280'
        
        elif len(partes) <= 15:  
            partes.insert(5, '\n')
            partes.insert(10, '\n')
            captions = ' '.join(partes)
            backgound_size = '0x340'
        
        gravity = '-gravity North'
        font =   '-font font/Cooper.TTF'                     
        font_size = '-pointsize 100'                         
        backgound_color = '-background White'
        splice = f'-splice {backgound_size}'
        annotate = '-annotate +0+20'
        output_name = f'{path_to_frame}'
        
        subprocess.run(f'magick {path_to_frame} {gravity} {backgound_color} {splice} {font} {font_size} {annotate} "{captions}" {output_name}')
                        #magick for windows
        
        return output_name