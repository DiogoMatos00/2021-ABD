import csv
import sys

from src.module import data

syspath = sys.path[0].split("\\")
projectpath=""

for i in range(0,len(syspath)):

    projectpath+=syspath[i]+"\\"

path_data = projectpath + "data"

def csv_Saver(csv_path):
    all_rows = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[4] == '':
                continue
            else:
                if csv_path == r".\data\Inventario_Material_camioneiros.csv":
                        idcom = row[0] 
                        a = idcom.split(".")
                        b = a[1]
                        b = list(b)
                        b.pop(0)
                        b.insert(0, '4')
                        a[1] = "".join(b)
                        row[0] = ".".join(a)
                if len(row) > 6:
                    del row[-1]
                all_rows.append(row)
    csvfile.close
    
    a = 0;
    for _ in all_rows:
        location = all_rows[a][0].split(".")
        location = " ".join(location[1])
        location = location.split(" ")
        location = check_numbers(location) #Location -> What we can get with the first Excel code i.g 1240.10.300        
        descrição_insp = all_rows[a][-1]
        descrição_insp = descrição_insp.split(";")
        csv_insert(all_rows[a])
        a += 1

def sub_secm(code):
    a = code.split(".")
    return a[1]

def encontrarid(idcom):
    a = idcom.split(".")
    a = a[2]
    a = list(a)
    a.pop(0)
    return "".join(a)

def csv_insert(info):
    sub_sec = sub_secm(info[0])
    cat_id = data.cat_id(info[3])
    id = encontrarid(info[0])
    id = int(id)

    send_info = [id, info[4], info[5], "NULL", "NULL", info[0], cat_id, sub_sec] #id, name, description, purchaseAt, endOfLife, Id_code, Id_item_categories, Sub_section_Internal_code
    data.Insert('ITEM', send_info)
    return

def check_numbers(location):
    # Scout supplies Identification
    new_location = []

    if location[0] == "0":
        new_location.append("Agrupamento")
        
    if location[0] == "1":
        new_location.append("Alcateia")
        if location[1] == "1":
            new_location.append("Branco")
        if location[1] == "2":
            new_location.append("Cinzento")
        if location[1] == "3":
            new_location.append("Castanho")
        if location[1] == "4":
            new_location.append("Preto")
        if location[1] == "5":
            new_location.append("Ruivo")

    if location[0] == "2":
        new_location.append("Expedição")
        if location[1] == "1":
            new_location.append("Pantera")
        if location[1] == "2":
            new_location.append("Mocho")
        if location[1] == "3":
            new_location.append("Falcão")
        if location[1] == "4":
            new_location.append("Leão")
        if location[1] == "5":
            new_location.append("Touro")


    if location[0] == "3":
        new_location.append("Comunidade")
        if location[1] == "1":
            new_location.append("B.P.")
        if location[1] == "2":
            new_location.append("Camões")
        if location[1] == "3":
            new_location.append("Padeira de Aljubarrota")

    if location[0] == "4":
        new_location.append("Clã")
        new_location.append("Vasco da Gama")

    return new_location

def csvrandom(path):
    all_row = csv_Saver(rf"{path_data}\{path}.csv")

def comecar():
    all_row = csv_Saver(rf"{path_data}\Inventario_Material_exploradores.csv")
    all_row = csv_Saver(rf"{path_data}\Inventario_Material_lobitos.csv")
    all_row = csv_Saver(rf"{path_data}\Inventario_Material.csv")
    all_row = csv_Saver(rf"{path_data}\Inventario_Material_pioneiros.csv")
    all_row = csv_Saver(rf"{path_data}\Inventario_Material_camioneiros.csv")