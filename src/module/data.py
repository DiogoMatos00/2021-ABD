import cx_Oracle
import sys

syspath = sys.path[0].split("\\")
projectpath=""

for i in range(0,len(syspath)):

    projectpath+=syspath[i]+"\\"

Oracle_client = projectpath+"OracleClient\instantclient_21_3"

# init oracle_client with project path
cx_Oracle.init_oracle_client(lib_dir=Oracle_client) # r - raw string because windows paths break python strings

# dsn maker - Data Source Name
IP = input("Insira o Ip do servidor: ")
PORT = input("Insira a porta do servidor: ")
SID = input("Insira o SID do servidor: ")


dsn  = f"{IP}:{PORT}/{SID}"


#user credentials
user   = "abd"
passwd = "abd"

# Connection to the Oracle DataBase
connection = cx_Oracle.connect(user=user,
                               password=passwd,
                               dsn=dsn                   
)

#Create an Cursor Object
cur = connection.cursor()

def Insert(tabela, atributos):
    tabela = tabela.upper()
    if tabela == "SUB_SECTION" or tabela == "ITEM_INSPECTION":
        cur.execute(f"INSERT INTO {tabela} VALUES ({atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]})")
    elif tabela == "ITEM":
        cur.execute(f"INSERT INTO {tabela} VALUES ({atributos[0]}, '{atributos[1]}', '{atributos[2]}', {atributos[3]}, {atributos[4]}, '{atributos[5]}', {atributos[6]}, {atributos[7]})")
    elif tabela == "SECTION" or tabela == "ITEM_CATEGORIES":
        cur.execute(f"INSERT INTO {tabela} VALUES ({atributos[0]}, {atributos[1]})")
    else:
        return "Erro!"
    connection.commit()

def update(tabela, atributos, identificador):
    if tabela == "item":
        cur.execute(f"UPDATE {tabela} SET item.name = '{atributos[0]}', item.description = '{atributos[1]}', item.purchaseat = TO_DATE('{atributos[2]}', 'yyyyMMdd'), item.endoflife = TO_DATE('{atributos[3]}', 'yyyyMMdd'), item.id_code = '{identificador}', item.id_item_categories = {atributos[4]}, item.sub_section_id = {atributos[5]} WHERE ITEM.ID_CODE = '{identificador}'")
    elif tabela == "item_categories":
        cur.execute(f"UPDATE {tabela} item_categories.id = {atributos[0]}, item_categories.category = '{atributos[1]}' WHERE item_categories.id = {identificador}")
    elif tabela == "section":
        cur.execute(f"UPDATE {tabela} SET section.id = {atributos[0]}, section.section = '{atributos[1]}' WHERE section.id = {identificador}")
    elif tabela == "sub_section":
        cur.execute(f"UPDATE {tabela} SET sub_section.id = {atributos[0]}, sub_section.sub_section = '{atributos[1]}', sub_section.internal_code = '{atributos[2]}', sub_section.id_section = {atributos[3]} WHERE sub_section.id = {identificador}")
    elif tabela == "item_inspection":
        cur.execute(f"UPDATE {tabela} SET item_inspection.id = {atributos[0]}, item_inspection.date_inspection = TO_DATE('{atributos[1]}','yyyyMMdd'), item_inspection.description = '{atributos[2]}', item_inspection.id_item = '{atributos[3]}' WHERE item_inspection.id = {identificador}")

    connection.commit()

def delete(tabela, identificador):
    if tabela == "item":
        cur.execute(f"DELETE FROM {tabela} WHERE item.id_code = '{identificador}'")
    elif tabela == "item_categories":
        cur.execute(f"DELETE FROM {tabela} WHERE item_categories.id = {identificador}")
    elif tabela == "section":
        cur.execute(f"DELETE FROM {tabela} WHERE section.id = {identificador}")
    elif tabela == "sub_section":
        cur.execute(f"DELETE FROM {tabela} WHERE sub_section.id = {identificador}")
    elif tabela == "item_inspection":
        cur.execute(f"DELETE FROM {tabela} WHERE item_inspection.id = {identificador}")
   
    connection.commit()

def Select(tabela, atributos):
    if len(atributos) == 0:
        a = cur.execute(f"SELECT * FROM {tabela}")
    elif len(atributos) == 1:
        a = cur.execute(f"SELECT {atributos[0]} FROM {tabela}")
    elif len(atributos) == 2:
        a = cur.execute(f"SELECT {atributos[0]}, {atributos[1]} FROM {tabela}")
    elif len(atributos) == 3:
        a = cur.execute(f"SELECT {atributos[0]}, {atributos[1]}, {atributos[2]} FROM {tabela}")
    elif len(atributos) == 4:
        a = cur.execute(f"SELECT {atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]} FROM {tabela}")
    elif len(atributos) == 5:
        a = cur.execute(f"SELECT {atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]}, {atributos[4]} FROM {tabela}")
    elif len(atributos) == 6:
        a = cur.execute(f"SELECT {atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]}, {atributos[4]}, {atributos[5]} FROM {tabela}")  
    elif len(atributos) == 7:
        a = cur.execute(f"SELECT {atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]}, {atributos[4]}, {atributos[5]}, {atributos[6]} FROM {tabela}")  
    elif len(atributos) == 8:
        a = cur.execute(f"SELECT {atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]}, {atributos[4]}, {atributos[5]}, {atributos[6]}, {atributos[7]} FROM {tabela}")  
    return a

def SelectA(sub_sec):
    queries = cur.execute(f"SELECT name FROM ITEM WHERE ITEM.SUB_SECTION_id = {sub_sec}")
    for row in queries:
        print(row)

def SelectB(section):
    queries = cur.execute(f"SELECT name FROM ITEM INNER JOIN SUB_SECTION ON ITEM.SUB_SECTION_ID = SUB_SECTION.ID INNER JOIN SECTION ON SECTION.ID = SUB_SECTION.ID_SECTION WHERE SECTION.ID = {section}")
    for row in queries:
        print(row)

def SelectC(data):
    queries = cur.execute(f"SELECT name FROM ITEM INNER JOIN ITEM_INSPECTION ON ITEM_INSPECTION.ID_ITEM = ITEM.ID_CODE WHERE DATE_INSPECTION = TO_DATE({data}, 'yyyyMMdd')")
    for row in queries:
        print(row)

def SelectD(cat, data):
    queries = cur.execute(f"SELECT name FROM ITEM INNER JOIN ITEM_INSPECTION ON ITEM_INSPECTION.ID_ITEM = ITEM.ID_CODE INNER JOIN ITEM_CATEGORIES ON ITEM_CATEGORIES.ID = ITEM.ID_ITEM_CATEGORIES WHERE ITEM_CATEGORIES.category = '{cat}' AND ITEM_INSPECTION.DATE_INSPECTION = TO_DATE('{data}', 'yyyyMMdd')")
    for row in queries:
        print(row)

def SelectE():
    queries = cur.execute("SELECT name FROM ITEM MINUS SELECT name FROM ITEM INNER JOIN ITEM_INSPECTION ON ITEM_INSPECTION.ID_ITEM = ITEM.ID_CODE")
    for row in queries:
        print(row)

def SelectF(nome):
    queries = cur.execute(f"SELECT COUNT(NAME) FROM ITEM INNER JOIN ITEM_INSPECTION ON ITEM.ID = ITEM_INSPECTION.ID_ITEM WHERE ITEM.NAME = '{nome}'")
    for row in queries:
        print(row)

def cat_id(name):
    queries = cur.execute("SELECT * FROM ITEM_CATEGORIES")
    for row in queries:
        if row[1] == name:
            return row[0]