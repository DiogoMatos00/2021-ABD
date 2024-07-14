from src.module import data                                                                        

from src.module import data
from src.controllers import app


def começar():
    print("""
                ----------------------- Bem Vindo! ---------------------------
                --------------------------------------------------------------
                ----------- PROJETO DE APLICAÇÃO DE BASE DE DADOS ------------
                --------------------------------------------------------------
    """)

    while True:
        print("""
                --------------------------------------------------------------
                ----------------------- Menu Principal -----------------------
                ------------- Selecione o número correspondente: -------------
                --------------------------------------------------------------
                ---- 1 - Povoação da base de dados a partir do Excel ---------
                ---- 2 - Comandos SQL ----------------------------------------
                ---- 3 - Consultas predefinidas ------------------------------
                ---- 4 - Sair! -----------------------------------------------
                --------------------------------------------------------------
                --------------------------------------------------------------
                """)

        command = input("Input:")
        
        
        if command == "1":
            while True:
                print("""
                --------------------------------------------------------------
                ------ 1 - Povoação da base de dados a partir do Excel -------
                ------------ Selecione o número correspondente: --------------
                --------------------------------------------------------------
                ---- 1 - Excel predefinido -----------------------------------
                ---- 2 - Custom Excel ----------------------------------------
                ---- 3 - Voltar ----------------------------------------------
                --------------------------------------------------------------
                --------------------------------------------------------------
                """)
                b = input("Input:")
                if b == "1":
                    app.comecar()

                if b == "2":
                    try:
                        nome = input("Introduza o nome do ficheiro: ")
                        app.csvrandom(nome)
                    except:
                        print("Ocorreu um erro , por favor tente outra vez")

                if b == "3":
                    break

        elif command == "2":
            while True:
                print("""
                --------------------------------------------------------------
                ---------------------- 2 - Comandos SQL ----------------------
                ------------- Selecione o número correspondente: -------------
                --------------------------------------------------------------
                ---- 1 - Inserir ---------------------------------------------
                ---- 2 - Alterar ---------------------------------------------
                ---- 3 - Remover ---------------------------------------------
                ---- 4 - Voltar ----------------------------------------------
                --------------------------------------------------------------
                --------------------------------------------------------------
                """)
                b = input("Input: ")

                if b == "1":
                    tabela = input("tabela: ")
                    if tabela == "sub_section": 
                        a1 = input("val1: ")
                        a2 = input("val2: ")
                        a2 = f"'{a2}'"
                        a3 = input("val3: ")
                        a4 = input("val4: ")
                        atrib = [a1, a2, a3, a4]

                    elif tabela == "item_inspection":
                        a0 = "Iteminspectionid.NEXTVAL"
                        a1 = input("val1: ")
                        a1 = f"TO_DATE('{a1}', 'yyyyMMdd')"
                        a2 = input("val2: ")
                        a2 = f"'{a2}'"
                        a3 = input("val3: ")
                        a3 = f"'{a3}'"
                        atrib = [a0, a1, a2, a3]

                    elif tabela == "item_categories":
                        a1 = input("val1: ")
                        a2 = input("val2: ")
                        atrib = [a1, a2]

                    elif tabela == "section":
                        a1 = input("val1: ")
                        a2 = input("val2: ")
                        a2 = f"'{a2}'"
                        atrib = [a1, a2]

                    elif tabela == "item":
                        a1 = input("val1: ")
                        a2 = input("val2: ")
                        a3 = input("val3: ")
                        a4 = input("val4: ")
                        a5 = input("val5: ")
                        a6 = input("val6: ") 
                        a7 = input("val7: ")
                        a8 = input("val8: ")
                        if a4 == "":
                            a4 = "NULL"
                        if a5 == "":
                            a5 = "NULL"
                        atrib = [a1, a2, a3, a4, a5, a6, a7, a8]   
                    try:                   
                        data.Insert(tabela, atrib)
                    except:
                        print("Ocorreu um erro, por favor tente outra vez")
                
                elif b == "2":
                    tabela = input("Introduza a tabela: ")
                    novos_atributos = []


                    if tabela == "item":
                        identificador = input("Qual o item pretende alterar: ")

                        c1 = input("Nome: ")
                        c2 = input("Descrição: ")
                        c3 = input("Data Compra: ")
                        c4 = input("Data validade: ")
                        c5 = input("ID da Categoria: ")
                        c6 = input("ID da sub-secção: ")
                        atributos = [c1, c2, c3, c4, c5, c6]
              

                    elif tabela == "item_categories":

                        identificador = input("Qual a categoria que pretende alterar: ")

                        c1 = input("ID: ")
                        c2 = input("Categoria: ")

                        atributos = [c1, c2]
                                       
                    elif tabela == "section":

                        identificador = input("Qual a secção que pretende alterar: ")

                        c1 = input("ID: ")
                        c2 = input("Secção: ")

                        atributos = [c1, c2]
                    
                    elif tabela == "sub_section":

                        identificador = input("Qual a sub-secção que pretende alterar: ")

                        c1 = input("ID: ")
                        c2 = input("Sub-Secção: ")
                        c3 = input("codigo da sub-secção: ")
                        c4 = input("codigo da secção: ")

                        atributos = [c1, c2, c3 ,c4]
                    
                    elif tabela == "item_inspection":

                        identificador = input("Qual a inspeção que pretende alterar: ")

                        c1 = input("ID: ")
                        c2 = input("data da inspeção: ")
                        c3 = input("descrição: ")
                        c4 = input("ID do item: ")

                        atributos = [c1, c2, c3 ,c4]
                    
                    try:
                        data.update(tabela, atributos, identificador)
                    except:
                        print("Ocorreu um erro , por favor tente outra vez")
                    
                elif b == "3":
                    tabela = input("Introduza a tabela: ")

                    if tabela == "item":

                        identificador = input("Qual o item pretende alterar: ")

                    elif tabela == "item_categories":

                        identificador = input("Qual a categoria que pretende alterar: ")
                    
                                            
                    elif tabela == "section":

                        identificador = input("Qual a secção que pretende alterar: ")
                    
                    elif tabela == "sub_section":

                        identificador = input("Qual a sub-secção que pretende alterar: ")
                    
                    elif tabela == "item_inspection":

                        identificador = input("Qual a inspeção que pretende alterar: ")

                    try:
                        data.delete(tabela, identificador)
                    except:
                        print("Ocorreu um erro , por favor tente outra vez")

                if b == "4":
                    break

        elif command == "3":
            while True:
                print("""
                ----------------------------------------------------------------------------------------------------------------------
                ----------------- 3 - Consultas predefinidas -------------------------------------------------------------------------
                ------------- Selecione o número correspondente:----------------------------------------------------------------------
                ----------------------------------------------------------------------------------------------------------------------
                ---- 1 - Quais os materiais de uma dada subseção ---------------------------------------------------------------------
                ---- 2 - Quais os materiais de uma dada seção ------------------------------------------------------------------------
                ---- 3 - Quais os materiais que foram inspecionados em um dado período -----------------------------------------------
                ---- 4 - Quais os materiais que foram inspecionados em um dado período de tempo que pertencem a uma dada categoria; --
                ---- 5 - Quais os materiais que nunca foram inspecionados ------------------------------------------------------------
                ---- 6 - Quantas inspeções tem cada material -------------------------------------------------------------------------
                ---- 7 - Voltar ------------------------------------------------------------------------------------------------------
                ----------------------------------------------------------------------------------------------------------------------
                ----------------------------------------------------------------------------------------------------------------------
                """)

                b = input("Input: ")

                if b == "1":
                    while True:
                        print("""
                --------------------------------------------------------------
                ----------------- 3 - Consultas predefinidas -----------------
                ------------ Selecione o número correspondente:---------------
                --------------------------------------------------------------
                ------------------------- Alcateia ---------------------------
                --------------------------------------------------------------
                ---- 10 - Geral ----------------------------------------------
                ---- 11 - Bando Branco ---------------------------------------
                ---- 12 - Bando Cinzento -------------------------------------
                ---- 13 - Bando Castanho -------------------------------------
                ---- 14 - Bando Preto ----------------------------------------
                ---- 15 - Bando Ruívo ----------------------------------------
                --------------------------------------------------------------

                ------------------------ Expedição ---------------------------
                --------------------------------------------------------------
                ---- 20 - Geral ----------------------------------------------
                ---- 21 - Patrulha Pantera------------------------------------
                ---- 22 - Patrulha Mocho--------------------------------------
                ---- 23 - Patrulha Falcão-------------------------------------
                ---- 24 - Patrulha Leão---------------------------------------
                ---- 25 - Patrulha Touro--------------------------------------
                --------------------------------------------------------------

                ------------------------ Comunidade --------------------------
                --- 30 - Geral ----------------------------------------------
                --- 31 - Equipa B.P-------------------------------------------
                --- 32 - Equipa Camões----------------------------------------
                --- 33 - Equipa Padeira de Aljubarrota-----------------------
                --------------------------------------------------------------

                ------------------------ Clã ---------------------------------
                --- 40 - Geral -----------------------------------------------
                --- 41 - Tribo Vasco da Gama----------------------------------
                --------------------------------------------------------------
                --------------------------------------------------------------
                --------------------------------------------------------------
                """)
                        b = input("Input: ")
                        data.SelectA(b)
                        break

                if b == "2":
                    while True:
                        print("""
                --------------------------------------------------------------
                ----------------- 3 - Consultas predefinidas -----------------
                ------------ Selecione o número correspondente: --------------
                --------------------------------------------------------------
                ---- 1 - Alcateia --------------------------------------------
                ---- 2 - Expedição -------------------------------------------
                ---- 3 - Comunidade ------------------------------------------
                ---- 4 - Clã -------------------------------------------------
                --------------------------------------------------------------
                --------------------------------------------------------------
                """)
                        b = input("Input: ")
                        data.SelectB(b)
                        break

                elif b=="3":
                    
                    b = input("Introduza uma data: ")
                    try:
                        data.SelectC(b)
                    except:
                        print("Ocorreu um erro , por favor tente outra vez")

                elif b=="4":
                    datainput = input("Introduza uma data: ")
                    print("""
                --------------------------------------------------------------
                ---------------------- Categorias ----------------------------
                --------------------------------------------------------------
                ---- Sede ----------------------------------------------------
                ---- Abrigo --------------------------------------------------
                ---- Cozinha -------------------------------------------------
                ---- Ferramentas ---------------------------------------------
                ---- Energizados ---------------------------------------------
                ---- Socorrismo ----------------------------------------------
                ---- Desportivos ---------------------------------------------
                ---- Diversos ------------------------------------------------
                ---- Jogos ---------------------------------------------------
                --------------------------------------------------------------
                    """)
                    cat = input("Introduza uma categoria: ")
                    data.SelectD(cat, datainput)
                elif b=="5":
                    data.SelectE()
                elif b=="6":
                    nome = input("Introduza o nome do item: ")
                    data.SelectF(nome)
                elif b=="7":
                    break

        elif command == "4":
            print("""
                --------------------------------------------------------------
                --------------- Programa encerrado com sucesso! --------------
                --------------------------------------------------------------
            """)

            break
        
        else:
            print("""
                --------------------------------------------------------------
                -------------------- Comando Inexistente! --------------------
                --------------------------------------------------------------
            """)
            continue

