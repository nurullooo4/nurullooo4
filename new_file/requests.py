import psycopg2
import requests
import json
import threading


conn = psycopg2.connect(database = 'n48',
                        user = 'postgres',
                        password = '123',
                        host = 'localhost',
                        port = 5432)

cur = conn.cursor()

product_url = requests.get('https://dummyjson.com/products')

# product_list = product_url.json()['products']
# query_product = '''
#     insert into products(id, title, description, category, price)
#     values (1, "Essence Mascara Lash Princess", "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.", "beauty", 9.99)
# '''

# for product in product_list:
#     cursor.execute(query_product)


def repost_url(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as f:
        json.dump(response.json(), f, indent=4)
        print(response.status_code)



urls = ['https://dummyjson.com/products', 'products.json']


threads = [
    threading.Thread(target = repost_url, args=(url, filename))
    for url, filename in urls]


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()



