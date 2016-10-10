import psycopg2
from django.http import HttpResponse

# Create your views here.

def drop_table(connection, tablename):
    curr = connection.cursor()
    print("""DROP TABLE %s""" % tablename)
    curr.execute("""DROP TABLE %s""" % tablename)
    connection.commit()

def create_table(connection, tablename, content):
    sql_string = "(\n"
    i = 0
    curr = connection.cursor()
    for key, value in content.items():
        i += 1
        if i < len(content):
            sql_string += "    %s %s,\n" % (key, value)
        else:
            sql_string += "    %s %s\n" % (key, value)
    sql_string += ")"
    curr.execute("""CREATE TABLE %s %s""" % (tablename, sql_string))
    connection.commit()
    return connection

def init(request):
    conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    try:
        create_table(conn, 'ex00_movies', {
            'title': 'varchar(64) UNIQUE NOT NULL',
            'episode_nb': 'int PRIMARY KEY',
            'opening_crawl': 'text',
            'director': 'varchar(32) NOT NULL',
            'producer': 'varchar(128) NOT NULL',
            'release_date': 'date NOT NULL',
        })
        ret = "OK"
    except Exception as e:
        ret = str(e)
    conn.close()
    return HttpResponse(ret)
