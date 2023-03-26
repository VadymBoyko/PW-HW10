from mongoengine import *
import psycopg2

connect(host="mongodb+srv://test_HW08:test_08@cluster0.yfciewx.mongodb.net/HW08", ssl=True)

conn = psycopg2.connect(
    host="127.0.0.1",
    database="hw10",
    user="postgres",
    password="12345678"
)


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField())
    meta = {'allow_inheritance': True}


authors = Author.objects
quotes = Quote.objects

cursor = conn.cursor()

query = "INSERT INTO app_homework10_author (fullname, birthday, birth_place, bio, user_id) VALUES (%s, %s, %s, %s, 1);"
for a in authors:
    data = (a.fullname, a.born_date, a.born_location, a.description)
    cursor.execute(query, data)

query = "INSERT INTO app_homework10_quote (quote, author_id, user_id) VALUES (%s, %s, 1);"
search_author_query = "SELECT * FROM app_homework10_author WHERE fullname = %s;"

for q in quotes:
    search_author_data = (q.author.fullname,)
    cursor.execute(search_author_query, search_author_data)
    author_id = cursor.fetchall()[0][0]
    data = (q.quote, author_id)
    cursor.execute(query, data)

conn.commit()
cursor.close()
conn.close()











