import  psycopg2
conn = psycopg2.connect(database = 'n44',
                        user = 'postgres',
                        password = '123',
                        host = 'localhost',
                        port = '5432')


cursor = conn.cursor()


# -- 1 --
# select_query1 ="""
#         select * from category;
#         """
#
#
# cursor.execute(select_query1)
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
# -- 2 --
# select_query2="""
#         select * from product;
#          """
#
# cursor.execute(select_query2)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# -- 3 --
# select_query3="""
#         select * from post;
#         """
#
# cursor.execute(select_query3)
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
# -- 4 --
# select_query4="""
#             select * from students;
#             """
#
# cursor.execute(select_query4)
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
# -- 5 --
# select_query5="""
#             select * from users
#             """
#
# cursor.execute(select_query5)
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
#
#
#
# from copy import copy, deepcopy
#
# list = [1, 2, [11, 22], [111, 222]]
# #
# # shallow_copy_list = copy(list)
# # shallow_copy_list[3][1] = 'ed'
# # print('shallow_copy_list: ', shallow_copy_list)
# #
# # deep_copy_list = deep_copy(list)
# # deep_copy_list[3][0] = 'ed'
# # print('deep_copy list: ', deep_copy_list)