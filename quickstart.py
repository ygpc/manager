"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import sqlite3

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

#add to write schedule log 
#f=open('schedule.txt','w')
conn=sqlite3.connect('schedule.db')
cur=conn.cursor()
#cur.execute('''CREATE TABLE schedule (start TEXT,title TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS schedule (year TEXT,month TEXT,day TEXT,start TEXT,title TEXT)''')
cur.execute('''DELETE FROM schedule''')
#add to write schedule log 
if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
#    params=(start)
    year=start[0:4]
    month=start[5:7]
    day=start[8:10]
    start_time=start[11:16]
    cur.execute("INSERT INTO schedule VALUES(?,?,?,?,?)",(year,month,day,start_time,event['summary'],))
 #   f.write(start)
 #   f.write(event['summary'].encode('utf-8')+'\n')
#f.close()
conn.commit()
conn.close()


