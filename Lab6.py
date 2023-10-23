import sqlite3

def get_records(table, field):
    conn = sqlite3.connect('goods.db')  #Взял какую-то бд из интернета для проверки
    cursor = conn.cursor()

    query = f"SELECT * FROM {table} WHERE {field} IS NOT NULL"
    cursor.execute(query)

    records = cursor.fetchall()

    conn.close()

    return records

table = 'products'
field = 'product_name'

result = get_records(table, field)

for record in result:
    print(record)