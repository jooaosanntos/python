import json

def gravar_dados(lista):
    with open('dados.json', 'w',  encoding='utf-8') as file:
        json.dump(lista, file,  ensure_ascii=False, indent=2)
        
