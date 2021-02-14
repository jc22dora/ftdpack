import mysql.connector 
import webbrowser

connection = mysql.connector.connect(user='root', password='', host ='104.197.120.134', database='ftdwkey')
cursor = connection.cursor(dictionary=True)

def get_access():
    return connection, cursor

def download_csv():
    url = 'https://storage.googleapis.com/ftdbucket/ftd/ftdcln.csv'
    return webbrowser.open(url)