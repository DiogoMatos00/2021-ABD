DROP TABLE item CASCADE CONSTRAINTS; 
DROP TABLE SECTION CASCADE CONSTRAINTS;
DROP TABLE ITEM_INSPECTION CASCADE CONSTRAINTS;
DROP TABLE SUB_SECTION CASCADE CONSTRAINTS;
DROP TABLE ITEM_CATEGORIES CASCADE CONSTRAINTS;


DROP SEQUENCE itemcategoriesid;
DROP SEQUENCE itemid;
DROP SEQUENCE Iteminspectionid;
DROP SEQUENCE subsectionic;


CREATE TABLE item_categories (
    id number(2,0) PRIMARY KEY,
    category Varchar(30)
);

CREATE TABLE SECTION(

    id NUMBER(1,0) PRIMARY KEY CHECK (id = 0 OR id = 1 OR id = 2 OR id = 3 OR id = 4),
    section VARCHAR(12) NOT NULL

);

CREATE TABLE sub_section(
    id Number(2,0) PRIMARY KEY,
    Subsection Varchar(60) NOT NULL,
    Internal_code Number(2,0) NOT NULL,
    id_section number(1,0) NOT NULL,
    CONSTRAINT fk1_sub_section foreign key (id_section) references section(id)
);

CREATE TABLE item (
    id number(2,0) NOT NULL,
    name Varchar(50) NOT NULL,
    description Varchar(255),
    purchaseAt DATE,
    endOfLife DATE,
    Id_code Varchar(11) PRIMARY KEY,
    id_item_categories number(2,0) NOT NULL,
    sub_section_id number(2,0) NOT NULL,
    CONSTRAINT fk1_item foreign key (id_item_categories) references item_categories(id),
    CONSTRAINT fk2_item foreign key (sub_section_id) references sub_section(id)
);


CREATE TABLE ITEM_INSPECTION(
    id NUMBER(1,0) PRIMARY KEY,
    date_inspection DATE NOT NULL,
    description VARCHAR(255) NOT NULL,
    id_item Varchar(11) NOT NULL,
    CONSTRAINT fk1_item_inspection foreign key (id_item) references item(id_code)
    
);

CREATE SEQUENCE itemcategoriesid
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 1000;

CREATE SEQUENCE itemid
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 1000;

CREATE SEQUENCE Iteminspectionid
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 1000;

CREATE SEQUENCE subsectionic
MINVALUE 1
START WITH 1
INCREMENT BY 1
CACHE 1000;

INSERT INTO SECTION VALUES (0, 'Agrupamento');
INSERT INTO SECTION VALUES (1, 'Alcateia');
INSERT INTO SECTION VALUES (2, 'Expedição');
INSERT INTO SECTION VALUES (3, 'Comunidade');
INSERT INTO SECTION VALUES (4, 'Clã');


INSERT INTO SUB_SECTION VALUES (10, 'Secção',  10, 1);
INSERT INTO SUB_SECTION VALUES (11, 'Bando Branco',  11, 1);
INSERT INTO SUB_SECTION VALUES (12, 'Bando Cinzento',  12, 1);
INSERT INTO SUB_SECTION VALUES (13, 'Bando Castanho',  13, 1);
INSERT INTO SUB_SECTION VALUES (14, 'Bando Preto',  14, 1);
INSERT INTO SUB_SECTION VALUES (15, 'Bando Ruivo',  15, 1);

INSERT INTO SUB_SECTION VALUES (20, 'Secção',  20, 2);
INSERT INTO SUB_SECTION VALUES (21, 'Patrulha Pantera',  21, 2);
INSERT INTO SUB_SECTION VALUES (22, 'Patrulha Mocho',  22, 2);
INSERT INTO SUB_SECTION VALUES (23, 'Patrulha Falcão',  23, 2);
INSERT INTO SUB_SECTION VALUES (24, 'Patrulha Leão',  24, 2);
INSERT INTO SUB_SECTION VALUES (25, 'Patrulha Touro',  25, 2);

INSERT INTO SUB_SECTION VALUES (30, 'Secção',  30, 3);
INSERT INTO SUB_SECTION VALUES (31, 'Equipa B.P',  31, 3);
INSERT INTO SUB_SECTION VALUES (32, 'Equipa Camões',  32, 3);
INSERT INTO SUB_SECTION VALUES (33, 'Equipa Padeira de Aljustbarrota',  33, 3);

INSERT INTO SUB_SECTION VALUES (40, 'Secção',  40, 4);
INSERT INTO SUB_SECTION VALUES (41, 'Tribo Vasco da Gama',  41, 4);

INSERT INTO SUB_SECTION VALUES (00, 'Secção',  00, 0);


INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Sede');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Abrigo');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Cozinha');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Ferramentas');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Energizados');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Socorrismo');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Desportivos');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Diversos');
INSERT INTO ITEM_CATEGORIES VALUES (itemcategoriesid.NEXTVAL, 'Jogos');


