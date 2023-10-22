from kodland_db import db


#Добавляем в базу данных
#data = {'minutes': 1, 'description':'Почистить зубы', 'id': 1, 'user_id': 123}
#db.tasks.put(data)


#Выводим конкретную строку
#row = db.tasks.get('id', 1)
#print(row.description, row.minutes, row.id, row.user_id)


#Выводим все строки
#rows = db.tasks.get_all()
#for row in rows:
#    print(row.description, row.minutes, row.id);


#Меняем значение определённой ячейки
#db.tasks.update('id', 1, 'minutes', 10)


#Удаляем строку из базы 
#db.tasks.delete('id', 1)