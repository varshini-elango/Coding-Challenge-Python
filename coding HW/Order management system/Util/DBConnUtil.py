import pyodbc
class DBUtil:
    
    def getDBConn():
        server = r'DESKTOP-2S6KAQD\SQLEXPRESS'
        database = 'connection'
        
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        
        try:
            conn = pyodbc.connect(conn_str)
            return conn
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")



