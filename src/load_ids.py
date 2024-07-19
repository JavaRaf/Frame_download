def check_ids(ids, comments):
    new_ids = []
    new_comments = []
    
    try:
        with open('src/responded_ids.txt', 'r', encoding='utf-8') as file:
            responded_ids = file.read().splitlines()
            
            for id, comment in zip(ids, comments):
                if id not in responded_ids: # verifica se o id nao foi respondido
                    if id not in new_ids: # verifica se o id ja esta nos novos ids
                        new_ids.append(id)
                        new_comments.append(comment)
            
        
        return new_ids, new_comments
    
    except FileNotFoundError:
        with open('src/responded_ids.txt', 'w', encoding='utf-8') as file:
            print("Arquivo responded_ids não encontrado\ncriando um")
            return [], []
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []

def save_ids_to_txt(id_comentario):
    try:
        with open('src/responded_ids.txt', 'a') as file:
            file.write(f"{id_comentario}\n")
        print(f"id salvo em responded_ids")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o id: {e}")

