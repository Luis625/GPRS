import json

def setup_starting_file():
    data = { "Nome do dataset" : "NaN", "Formato dos videos" : "NaN", "Metricas" : ["NaN"], "Endereco da referencia" : "NaN", "Endereco do destino" : "NaN"}
    json_file = open("json_file.json", 'w', encoding='utf-8')

    json_data = json.dumps(data)
    json_file.write(json_data)
    json_file.close()

def read_json():
    json_file = open("json_file.json", encoding='utf-8')
    json_data = json.loads(json_file.read())
    json_file.close()
    return json_data

def edit_json():
    json_file = open("json_file.json", "w", encoding='utf-8')

    data = dict()
    data["Nome do dataset"] = input("Escreva o nome do dataset:\n")
    data["Formato dos videos"] = input("Escreva o formato dos videos:\n")
    data["Metricas"] = input("Escreva as métricas a serem utilizadas separadas por vírgula:\n").split(",")
    data["Endereco da referencia"] = input("Escreva o endereço (path) do vídeo de referência. Caso não haja, escreva NaN:\n")
    data["Endereco do destino"] = input("Escreva o endereço (path) dos vídeos a serem avaliados.\n")

    # Mais tarde, fazer função de validação para garantir que as variáveis foram inicializadas corretamente.

    json_data = json.dumps(data)
    json_file.write(json_data)
    json_file.close()

def initialize():
    setup_starting_file()
    edit_json()
    return read_json()