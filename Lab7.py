
import sqlite3

class ORMMapper:
    def __init__(self, class_name):
        self.class_name = class_name

    def convert_to_db(self):
        class_structure = vars(self.class_name)
        field_names = list(class_structure.keys())
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.class_name.__name__} ("
        for field_name in field_names:
            field_type = class_structure[field_name].__class__.__name__
            create_table_query += f"{field_name} {field_type}, "
        create_table_query = create_table_query[:-2]
        create_table_query += ");"
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.close()

class Person:
    name = str
    age = int

mapper = ORMMapper(Person)
mapper.convert_to_db()
