from roboflow import Roboflow
import shutil
import os

f = open("api_key_roboflow")
api_key = f.read().strip()
print(api_key)

rf = Roboflow(api_key=api_key)
project = rf.workspace("custom-thxhn").project("fire-wrpgm")
dataset = project.version(8).download("yolov8")
destination_folder = "./../datasets/fire_dataset_yolov8"
original_location = dataset.location

try:
    # Se la cartella di destinazione esiste già, la rimuoviamo per evitare errori
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
        print(f"Cartella di destinazione esistente '{destination_folder}' rimossa.")

    # Sposta la cartella scaricata nella nuova destinazione
    shutil.move(original_location, destination_folder)
    print(f"✅ Dataset spostato con successo in: {destination_folder}")

    # Ora puoi aggiornare il file data.yaml se necessario, oppure usare il nuovo percorso
    # per il training del tuo modello.
    # Ad esempio, il nuovo percorso del file di configurazione è:
    # new_yaml_path = os.path.join(destination_folder, 'data.yaml')
    # print(f"Il file di configurazione si trova ora in: {new_yaml_path}")

except Exception as e:
    print(f"Si è verificato un errore durante lo spostamento dei file: {e}")

print(dataset)
