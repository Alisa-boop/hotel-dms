import sqlite3
import os

def initialize_database():
    """Создаёт базу данных и заполняет её данными из SQL-скрипта"""
    database_file = 'database.db'
    if os.path.exists(database_file):
        os.remove(database_file)
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    sql_script = """
    BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "report_types" (
    "id_type" INTEGER PRIMARY KEY AUTOINCREMENT,
    "type_name" TEXT NOT NULL
);

-- Очистка и предзаполнение типов отчётов
DELETE FROM "report_types";
INSERT INTO "report_types" (type_name) VALUES 
('Ежемесячный'),
('Ежеквартальный'),
('Годовой');

CREATE TABLE IF NOT EXISTS "employees" (
    "id_employee" INTEGER,
    "name" TEXT NOT NULL,
    "phone_number" TEXT,
    "email" TEXT,
    "position" TEXT,
    "department" TEXT,
    PRIMARY KEY("id_employee" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "clients" (
    "id_client" INTEGER,
    "name" TEXT NOT NULL,
    "email" TEXT,
    "contact" TEXT,
    "address" TEXT,
    PRIMARY KEY("id_client" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "services" (
    "service_id" INTEGER,
    "name" TEXT NOT NULL,
    "price" REAL,
    "description" TEXT,
    PRIMARY KEY("service_id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "contracts" (
    "id_contract" INTEGER,
    "number" TEXT,
    "date" TEXT,
    "deal_type" TEXT,
    "start_price" REAL,
    "discount" REAL,
    "deal_status" INTEGER,
    "finish_price" REAL,
    "client_id" INTEGER,
    "service_id" INTEGER,
    "employee_id" INTEGER,
    PRIMARY KEY("id_contract" AUTOINCREMENT),
    FOREIGN KEY("client_id") REFERENCES "clients"("id_client"),
    FOREIGN KEY("service_id") REFERENCES "services"("service_id"),
    FOREIGN KEY("employee_id") REFERENCES "employees"("id_employee")
);

CREATE TABLE IF NOT EXISTS "reports" (
    "id_report" INTEGER,
    "number" TEXT,
    "date" TEXT,
    "report_type_id" INTEGER,
    "description" TEXT,
    "employee_id" INTEGER,
    PRIMARY KEY("id_report" AUTOINCREMENT),
    FOREIGN KEY("report_type_id") REFERENCES "report_types"("id_type"),
    FOREIGN KEY("employee_id") REFERENCES "employees"("id_employee")
);

-- Предзаполнение таблиц
INSERT INTO "services" VALUES (1,'Подключение WI-FI',1000.0,'Услуга по подключению высокоскоростного интернета');
INSERT INTO "services" VALUES (2,'Тренажерный зал',600.0,'Доступ в тренажерный зал');
INSERT INTO "services" VALUES (3,'Бильярд, настольные игры и другие платные развлечения',1500.0,'Доступ ко всем развлечениям отеля');
INSERT INTO "services" VALUES (4,'Прокат автомобилей',5000.0,'На выбор предоставляются различные автомобили для личного использования');
INSERT INTO "services" VALUES (5,'Бар',500.0,'Осуществление доставки еды и напитков до номера');

INSERT INTO "contracts" VALUES (1,'2024-1-ПП','22.01.2024','Абонемент',600.0,10.0,0,540.0,1,2,6);
INSERT INTO "contracts" VALUES (2,'2025-2-ПП','01.09.2025','Разовая',1000.0,0.0,0,1000.0,2,1,3);
INSERT INTO "contracts" VALUES (3,'2025-3-ПП','15.03.2025','Разовая',1500.0,0.0,0,1500.0,3,3,4);
INSERT INTO "contracts" VALUES (4,'2025-4-ПП','10.04.2025','Абонемент',500.0,50.0,0,250.0,4,5,5);

INSERT INTO "employees" VALUES (1,'Вася Пупкин','+7 (999) 121-21-13','vasya@gmail.com','Менеджер','Администрация');
INSERT INTO "employees" VALUES (2,'Григорий Лепс','+7 (999) 444-55-66','grishaleps@gmail.com','Бармен','Отдел Клиенсткого Обслуживания');
INSERT INTO "employees" VALUES (3,'Алексей Долматов','+7 (999) 777-88-99','guf@gmail.com','Инженер','Отдел Ремонта и технического обслуживания');
INSERT INTO "employees" VALUES (4,'Даниил Морозов','+7 (999) 000-21-22','danyamorozkin@gmail.com','Стажер','Отдел Клиентского Обслуживания');
INSERT INTO "employees" VALUES (5,'Чахуриди Константин','+7 (999) 333-44-55','kostik@gmail.com','Бармен','Отдел Клиентского обслуживания');
INSERT INTO "employees" VALUES (6,'Алексей Заморский','+7 (999) 666-77-88','lexa@gmail.com','Тренер','Отдел Клиентского обслуживания');

INSERT INTO "clients" VALUES (1,'Игорь Дельдин','igorek@gmail.com','8 (816) 101-15-01','г. Москва, ул. Арбат, д.2, кв 15 ');
INSERT INTO "clients" VALUES (2,'Алиса Власова','vlasovaa@gmail.com','8 (999) 777-89-98','г. Москва, ул. Пушкина, д.14, кв 186');
INSERT INTO "clients" VALUES (3,'Дамир Авраменко','damirchik@gmail.com','8 (999) 555-55-66','г. Москва, ул. Маяковская, д.19, кв 1');
INSERT INTO "clients" VALUES (4,'Михаил Сартаков','mishasi@hmail.com','8 (800) 400-00-44','г. Москва, ул. Мясницкая, д.2, кв 6');

INSERT INTO "reports" (number, date, report_type_id, description, employee_id) VALUES 
('2024-01', '2024-01-31', 1, 'Отчёт за январь 2024 года', 1),
('2025-02', '2025-02-28', 1, 'Отчёт за февраль 2025 года', 2),
('2025-03', '2025-03-31', 1, 'Отчёт за март 2025 года', 3),
('2025-04', '2025-04-30', 1, 'Отчёт за апрель 2025 года', 4);

COMMIT;

"""
    
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
