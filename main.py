from flask import Flask, request
from utils import generate_password

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/password')
def password():
    length = request.args.get('length', '10')

    if length.isdigit():
        length = int(length)
        maximum_length = 200

        if length > maximum_length:
            return f"Length should be less than {maximum_length}"
    else:
        return f'Invalid length value "{length}"'

    return generate_password(length)


@app.route('/emails/read/')
def emails_read():

    # ?ordering=EmailValue
    # ?ordering=-EmailValue
    ordering = request.args.get('ordering')

    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    if ordering:
        direction = 'DESC' if ordering.startswith('-') else 'ASC'
        column_name = ordering.replace('-', '')

        sql = f'''
        SELECT * FROM Emails ORDER BY {column_name} {direction};
        '''
    else:
        sql = f'''
        SELECT * FROM Emails;
        '''

    cur.execute(sql)
    result = cur.fetchall()

    con.close()

    return str(result)


def commit_sql(sql):
    import sqlite3
    try:
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    finally:
        con.close()


@app.route('/emails/create/')
def emails_create():
    email_value = request.args['email']
    sql = f'''
    INSERT INTO Emails (EmailValue) VALUES ('{email_value}')
    '''
    commit_sql(sql)

    return 'emails_create'


@app.route('/emails/update/')
def emails_update():
    email_value = request.args['email']
    email_id = request.args['id']

    sql = f'''
    UPDATE Emails
    SET EmailValue = '{email_value}'
    WHERE EmailID = {email_id};
    '''
    commit_sql(sql)
    return 'emails_update'


@app.route('/emails/delete/')
def emails_delete():
    email_id = request.args['id']

    sql = f'''
    DELETE FROM Emails
    WHERE EmailID = {email_id};
    '''
    commit_sql(sql)

    return 'emails_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

'''
http:// 127.0.0.1 :5000 /hello ?name=Dima&age=29

1. http/s, ftp, smtp
2. Location (IPv4)
  IPv4
  x.x.x.x
  [0-255].[0-255].[0-255].[0-255]
  3.54.34.7
  3.54.34.7.56
  3.54.34
  255.255.255.255
  0.0.0.0
  256.34.1.0
  
  IPv6
  
  unix-socket

3. PORT - 
  0 - 65535
  
4. PATH - /hello/world/

5. QUERY PARAMS

CRUD 
C - create
R - read
U - update
D - delete
'''

print(1)
print(2)
print(3)
