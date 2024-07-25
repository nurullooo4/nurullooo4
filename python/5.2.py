import  psycopg2

conn = psycopg2.connect(database = 'n48',
                        user = 'postgres',
                        password = '123',
                        host = 'localhost',
                        port = 5432)

cur = conn.cursor()
#
# create_table_query ="""
#
# CREATE TABLE IF NOT EXISTS employee(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# );
# """
#
# # cur.execute(create_table_query)
# # conn.commit()
# # print("Table created successfully")
# insert_employee_query = '''
# INSERT INTO employee(title)
# values ('alkfgaf'),
#         ('wrwqgqrw'),
#         ('wethtewhhh');
# '''
# # cur.execute(insert_employee_query)
# # conn.commit()
# # rows = cur.fetchall()
# # for row in rows:
# #     print(row)
# #
#
# update_column_query = '''
#         select * from employee where id = 1;
# '''
# # cur.execute(update_column_query)
# # conn.commit()
# # rows = cur.fetchall()
# # for row in rows:
# #     print(row)
#
#
# delete_column_query = '''
#         delete from employee where id = 3;
#           '''
# #
# # cur.execute(delete_column_query)
# # conn.commit()
#
#
# cur.close()
# conn.close()
#
#
#


































