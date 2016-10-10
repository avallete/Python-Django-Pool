import psycopg2

from django.shortcuts import render
from django.http import HttpResponse
from django.forms import Form
from .forms import UpdateForm

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

def remove_row(connection, tablename, content):
    sql_string = ''
    curr = connection.cursor()
    i = 0
    for key, value in content.items():
        i += 1
        if i < len(content):
            sql_string += '%s.%s = %s AND ' % (tablename, key, value)
        else:
            sql_string += '%s.%s = %s' % (tablename, key, value)
    print("DELETE FROM %s WHERE %s;" % (tablename, sql_string))
    curr.execute("DELETE FROM %s WHERE %s;" % (tablename, sql_string))
    connection.commit()
    return connection

def insert_into(connection, tablename, content):
    order_string = '%s(' % tablename
    sql_string = '('
    curr = connection.cursor()
    i = 0
    for key, value in content.items():
        i += 1
        if i < len(content):
            order_string += "%s, " % key
            sql_string += "'%s', " % value
        else:
            order_string += "%s" % key
            sql_string += "'%s'" % value
    order_string += ') VALUES\n'
    sql_string += ')'
    print("INSERT INTO %s%s;" % (order_string, sql_string))
    curr.execute("INSERT INTO %s%s;" % (order_string, sql_string))
    connection.commit()
    return connection

def populate(request):
    buf = ""
    data = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'opening_crawl': None,
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'opening_crawl': "",
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
    conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    for movie in data:
        try:
            insert_into(conn, 'ex06_movies', movie)
            buf += "OK<br>"
        except Exception as e:
            buf += "Error: %s :: %s<br>" % (movie['title'], e)
            conn.rollback()
    conn.close()
    return HttpResponse(buf)

def display(request):
    conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    curr = conn.cursor()
    try:
        curr.execute("""SELECT * from ex06_movies""")
    except Exception as e:
        return HttpResponse("No data available")
    response = curr.fetchall()
    conn.close()
    if response:
        return render(request, 'ex06/display.html', {'data': response})
    else:
        return HttpResponse("No data available")

def init(request):
    conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    try:
        create_table(conn, 'ex06_movies', {
            'title': 'varchar(64) UNIQUE NOT NULL',
            'episode_nb': 'int PRIMARY KEY',
            'opening_crawl': 'text',
            'director': 'varchar(32) NOT NULL',
            'producer': 'varchar(128) NOT NULL',
            'release_date': 'date NOT NULL',
            'created': 'timestamp NOT NULL DEFAULT NOW()',
            'updated': 'timestamp NOT NULL DEFAULT NOW()'
        })
        curr = conn.cursor()
        curr.execute("""
CREATE OR REPLACE FUNCTION update_changetimestamp_column()
RETURNS TRIGGER AS $$
BEGIN
NEW.updated = now();
NEW.created = OLD.created;
RETURN NEW;
END;
$$ language 'plpgsql';
CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
update_changetimestamp_column();""")
        conn.commit()
        ret = "OK"
    except Exception as e:
        ret = str(e)
        conn.rollback()
    conn.close()
    return HttpResponse(ret)

def remove(request):
    conn = psycopg2.connect(
        database='formationdjango',
        host='localhost',
        user='djangouser',
        password='secret'
    )

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid() and request.POST['select'][0]:
            remove_row(conn, 'ex06_movies', {'episode_nb': request.POST['select'][0]})

    curr = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    form = Form()
    try:
        curr.execute("""SELECT * from ex06_movies""")
    except Exception as e:
        return HttpResponse("No data available")
    response = curr.fetchall()

    if response:
        return render(request, 'ex06/remove.html', {'data': response, 'form': form})
    else:
        return HttpResponse("No data available")

def update(request):
    form = UpdateForm()
    conn = psycopg2.connect(
        database='formationdjango',
        host='localhost',
        user='djangouser',
        password='secret'
    )
    curr = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            try:
                curr.execute("""UPDATE ex06_movies SET opening_crawl = '%s' WHERE episode_nb = %s;""" % (
                    request.POST['opening_crawl'],
                    request.POST['select'][0]
                ))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
    try:
        curr.execute("""SELECT * from ex06_movies""")
    except Exception as e:
        return HttpResponse("No data available")
    response = curr.fetchall()
    if response:
        return render(request, 'ex06/update.html', {'data': response, 'form': form})
    else:
        return HttpResponse("No data available")
