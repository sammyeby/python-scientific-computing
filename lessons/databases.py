import sqlite3
import json
from utils import sqlFromFile


conn = sqlite3.connect('roasterdb.sqlite')
cur = conn.cursor()

initQuery = sqlFromFile('queries/roaster/init.sql')
upUserQuery = sqlFromFile('queries/roaster/update_user.sql')
upCourseQuery = sqlFromFile('queries/roaster/update_course.sql')
upMemberQuery = sqlFromFile('queries/roaster/update_member.sql')

# Initialize DB and Tables
cur.executescript(initQuery)

fname = input('Enter Json Data File: ')

if len(fname) < 1:
    fname = 'data_sample_obj.json'

dStr = open(fname).read()
jsonData = json.loads(dStr)

for entry in jsonData:
    name = entry['name']
    email = entry['email']
    courses = entry['courses']
    # Insert into User Table
    cur.execute(upUserQuery, ( name, email ))
    # Get currently inserted User id
    cur.execute('SELECT id FROM User WHERE name = ? ', ( name, ))
    user_id = cur.fetchone()[0]
    print('User', name, email, user_id)

    for c in courses:
        role = c['role']
        title = c['title']
        print(c['role'], c['title'])
        # Insert into course Table
        cur.execute(upCourseQuery, ( title, ))
        cur.execute('SELECT id FROM Course WHERE title = ? ', ( title, ))
        course_id = cur.fetchone()[0]
        # Now Update Member Table
        cur.execute(upMemberQuery, ( user_id, course_id, role ))
        # Commit the DB updates
        conn.commit()
    conn.commit()



