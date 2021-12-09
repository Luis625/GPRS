import json

def setup_starting_file():
    data = { "Nome do dataset" : "dataset_name", "Formato dos videos" : "video_format", "Metricas" : ["metric_1", "metric_2", "metric_3"]}
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
    json_file = open("json_file.json", encoding='utf-8')

    data = dict()
    data["Nome do dataset"] = input("Escreva o nome do dataset: ")
    data["Formato dos videos"] = input("Escreva o formato dos videos: ")
    data["Metricas"] = input("Escreva as métricas a serem utilizadas separadas por vírgula: ").split(",")

    json_data = json.dumps(data)
    json_file.write(json_data)
    json.close()

def initialize():
    setup_starting_file()
    edit_json()
    return read_json()


