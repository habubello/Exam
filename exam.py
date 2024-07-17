import time
import threading
import psycopg2
conn = psycopg2.connect(database="homework",user="postgres",password="1234",host="localhost",port="5432")
cur = conn.cursor()




# 1 TASK
#
# create_query = """create table if not exists product(
# id serial primary key,
# name varchar(50),
# price varchar(50),
# color varchar(50),
# image varchar);"""
# cur.execute(create_query)
# conn.commit()





# 2 TASK
# class Product_method:
#     @staticmethod
#     def insert():
#         insert_query = """insert into product(name,price,color,image) values (%s,%s,%s,%s)"""
#         data1 = input("nameni kirting: ")
#         data2 = input("price kirting: ")
#         data3 = input("color kirting: ")
#         data4 = input("image urlni kiriting: ")
#         data = data1,data2,data3,data4
#         cur.execute(insert_query,data)
#         conn.commit()
#
#     @staticmethod
#     def select():
#         select_query = """select * from product"""
#         cur.execute(select_query)
#         conn.commit()
#
#     @staticmethod
#     def update():
#         update_query = """update product set name=%s where id=%s"""
#         data2 = input("Bloklamoqchi bolgan userni kiriting: ")
#         data1 = "Banned"
#         data = data1,data2
#         cur.execute(update_query, data)
#         conn.commit()
#
#     @staticmethod
#     def delete():
#         delete_query = """delete from product where id=%s;"""
#         delete_id = input("Ochirmoqchi bolgan productni IDni kiriting: ")
#         cur.execute(delete_query,delete_id)
#         conn.commit()







# 3 TASK
# class Alphabet:
#     def __init__(self,letter):
#         self.letter = letter
#
#     def __iter__(self):
#         return self
#
#     @staticmethod
#     def iter_method():
#         data = ["a","b","c","d","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z"]
#         my_iterator = iter(data)
#         for i in range(24):
#             print(next(my_iterator))







# 4 TASK
# def numbers():
#     for i in range(1, 6):
#         time.sleep(1)
#         print(i)
# def letters():
#     for i in 'abcde':
#         time.sleep(1.5)
#         print(i)
#
# thread = threading.Thread(target=numbers())
# thread2 = threading.Thread(target=letters())
# thread.start()
# thread.join()
#
# thread2.start()
# thread2.join()







# 5 TASK
# class Product:
#     def __init__(self,id,name,price, color,image):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image
#
#     @staticmethod
#     def save():
#         insert_query = """insert into product(name,price,color,image) values(%s,%s,%s,%s)"""
#         data1 = input("nameni kirting: ")
#         data2 = input("price kirting: ")
#         data3 = input("color kirting: ")
#         data4 = input("image urlni kiriting: ")
#         data = data1,data2,data3,data4
#         cur.execute(insert_query,data)
#         conn.commit()







# 6 TASK
# class DbConnect():
#     def __init(self):
#         return self

#     def __enter__(self):
#         conn = psycopg2.connect(database="homework", user="postgres", password="1234", host="localhost", port="5432")
#         cur = conn.cursor()

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return self


# 7 TASK
task = None
#   🤷‍♂️




if __name__ == "__main__":
    pass

#^Run qilayotganda ishlatshingiz uchun^