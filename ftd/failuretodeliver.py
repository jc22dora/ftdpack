import mysql.connector 
import webbrowser

connection = mysql.connector.connect(user='root', password='', host ='104.197.120.134', database='ftdwkey')
cursor = connection.cursor()

def get_access():
    return connection, cursor

def download_csv():
    url = 'https://storage.googleapis.com/ftdbucket/ftd/ftdcln.csv'
    return webbrowser.open(url)

def ftd_schema():
    return cursor.column_names

def most_recent_settlementdate():
    cursor = connection.cursor(buffered=True, dictionary=True)
    cursor.execute("SELECT settlementdate FROM ftdwkey ORDER BY settlementdate DESC LIMIT 1")
    settlementdate = cursor.fetchone()
    cursor = connection.cursor()
    return settlementdate['settlementdate']
