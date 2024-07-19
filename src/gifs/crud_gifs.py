import os
import json
import random

def add(string: str):
    # Divide a string no formato "tag1,tag2#link"
    tags_link = string.split('#')
    
    if len(tags_link) == 2:
        # Remove espaços e converte as tags para minúsculas
        tags = [tag.strip().lower() for tag in tags_link[0].split(',')]
        link = tags_link[1].strip()

        # Verifica se o link começa com "https://tenor.com"
        if link.startswith('https://tenor.com'):
            # Se o arquivo não existe, cria um novo arquivo JSON
            if not os.path.exists('src/gifs/gifs.json'):
                with open('src/gifs/gifs.json', 'w', encoding='utf-8') as gifs_file:
                    json.dump([], gifs_file)  # Inicializa o arquivo com uma lista vazia
                print('Criando o arquivo JSON para os gifs')

            try:
                # Abre o arquivo JSON existente e carrega o conteúdo
                with open('src/gifs/gifs.json', 'r', encoding='utf-8') as gifs_file:
                    data = json.load(gifs_file)
                
                # Adiciona o novo link e suas tags ao conteúdo
                data.append({"link": link, "tags": tags})

                # Escreve o conteúdo atualizado de volta ao arquivo
                with open('src/gifs/gifs.json', 'w', encoding='utf-8') as gifs_file:
                    json.dump(data, gifs_file, ensure_ascii=False, indent=4)
                print(f"Adicionado o link {link} com as tags {tags}")

            except Exception as e:
                print(f"Erro ao escrever no arquivo: {e}")

#-----------------------------------------------------------------------------

def remove(link):
    try:
        # Lê o arquivo JSON existente
        with open('src/gifs/gifs.json', 'r', encoding='utf-8') as gifs_file:
            data = json.load(gifs_file)
        
        # Se não há gifs salvos, retorna
        if not data:
            print("Nenhum gif salvo")
            return
        
        # Encontra o índice do gif com o link especificado
        index_to_remove = None
        for index, gif in enumerate(data):
            if gif['link'] == link:
                index_to_remove = index
                break
        
        # Se encontrou o gif, remove-o
        if index_to_remove is not None:
            data.pop(index_to_remove)
            print("Gif removido com sucesso")
        else:
            print("Link não encontrado")
        
        # Escreve o conteúdo atualizado de volta ao arquivo
        with open('src/gifs/gifs.json', 'w', encoding='utf-8') as gifs_file:
            json.dump(data, gifs_file, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Erro ao apagar o link: {e}")

#-----------------------------------------------------------------------------
            
def send(user_tags: list[str]):
    try:
        # Lê o arquivo JSON existente
        with open('src/gifs/gifs.json', 'r', encoding='utf-8') as gifs_file:
            data = json.load(gifs_file)
        
        # Se não há gifs salvos, retorna
        if not data:
            print("Nenhum gif salvo")
            return
        
        # Filtra os gifs que contêm qualquer uma das tags especificadas
        matching_gifs = [gif for gif in data if any(tag in gif['tags'] for tag in user_tags)]
        
        # Se não há gifs correspondentes, retorna
        if not matching_gifs:
            print(f"Nenhum gif encontrado com as tags {user_tags}")
            return
        
        # Seleciona aleatoriamente um gif correspondente
        selected_gif = random.choice(matching_gifs)
        
        # Retorna o link do gif selecionado
        return selected_gif['link']
    
    except Exception as e:
        print(f"Erro ao ler o arquivo gifs.json: {e}")
        return None



