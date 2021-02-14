import ftd
from ftd import failuretodeliver

connection, cursor = failuretodeliver.get_access()

def test_connection():
    assert connection.server_host == '104.197.120.134'

def test_scehma():
    assert cursor.column_names == ['settlementdate', 'cusip', 'symbol', 'quantity', 'description', 'price', 'jdkey']