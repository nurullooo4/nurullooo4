

#     Muhitdinov Nurullo 
#     n48

#        ---1-masala---

import psycopg2

host = 'localhost'
user = 'postgres'
password = '123'
database = 'n48'
port = 5432

conn = psycopg2.connect(host = host,
                        user = user,
                        password = password,
                        database= database,
                        port = port)

curr = conn.cursor()


create_table_query = """ CREATE TABLE if not exists product (
    id serial primary key,
    name varchar(222) not null,
    price integer not null,
    color varchar(222) not null,
    image text
);
    """

curr.execute(create_table_query)
conn.commit()

#          ---2-masala---

def product_insert():
    name = str(input("Enter prodyct name:"))
    price = int(input("Enter product price:"))
    color = str(input("Enter product color:"))
    image = str(input("Enter product image:"))
    insert_into_query = 'INSERT INTO product(name,price,color,image) values (%s,%s,%s,%s);'
    insert_into_params = (name,price,color,image)
    curr.execute(insert_into_query,insert_into_params)
    conn.commit()
    print( 'insert 0 1')


# product_insert()
    


def select_all_products():
    select_product = 'SELECT * FROM product;'
    curr.execute(select_product)
    rows = curr.fetchall()
    for row in rows:
        print(row)


# select_all_products()
        

def update_product():
    select_all_products()
    _id = int(input(" product id:"))
    name = str(input(" new product:"))
    price = int(input(" product price:"))
    color = str(" product color:")
    image = str(" product url :")
    update_query = 'update product set name = %s, price = %s,color =%S,image =%s where id = %s;'
    update_params = (_id,name,price,color,image)
    curr.execute(update_query,update_params)
    conn.commit()
    print(' Update ')

#update_product()
    

def delete_product():
    select_all_products()
    _id = int(input('Enter product id:'))
    delete_query = 'delete from product where id = %s;'
    curr.execute(delete_query,(_id,))
    conn.commit()
    print(' delete product')


#delete_product()
    

#        ---3-masala---
    

class Alphabet:
    def __init__(self):
        self.harflar = 'ABCDEFGHIJKLMNOPQRSTUYWXZ'  

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.harflar):
            harf = self.harflar[self.index]
            self.index += 1
            return harf
        else:
            raise StopIteration

alphabet = Alphabet()

for harf in alphabet:
    print(harf) 



#       ---4-masala---
    


import threading
import time 


def print_number():
    for  i in range (1,5):
        print(i)
        time.sleep(2)
        
#print_number()

def print_letters():
    for char in 'ABCDE':
        print(char)
        time.sleep(2)
       
number_threads =threading.Thread(target=print_number)
letters_threads = threading.Thread(target=print_letters)

number_threads.start()
letters_threads.start()

number_threads.join()
letters_threads.join()


#         ---5-masala---

import psycopg2

database = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '123',
    'database': 'n48',
    'port': 5432
}

class DbConnect:
    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = psycopg2.connect(**self.database)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()



class Product:
    def __init__(self, id: int|None= None, name:str|None =None, price:int|None =None, color:str|None=None,image:str|None=None):
        self.id = id
        self.name = name
        self.price  = price
        self.color = color
        self.image = image
        
    def save(self):
        with DbConnect(database) as cursor:
            insert_query = 'INSERT INTO product(name, price, color, image) values (%s, %s,%s, %s);'
            insert_params = (self.name, self.price, self.color,self.image,)
            cursor.execute(insert_query, insert_params)



#          ---6-masala---


import psycopg2

database = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '123',
    'database': 'n48',
    'port': 5432
}
class DbConnect:
    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = psycopg2.connect(**self.database)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

# with DbConnect() as manager:
#     print('--\--\--')




#          ---7-masala---
        
import requests


database = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '123',
    'database': 'n48',
    'port': 5432
}


product_url = requests.get('https://dummyjson.com/products')


product_list = product_url.json()['products']
query = '''insert into products() values(%s,%s,%s);'''
for product in product_list:
    cursor.execute(query, (product['name'], product['price'], product['']))
