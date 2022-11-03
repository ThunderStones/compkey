import mysql.connector
from config import mysql_config


class Connector:
    def __init__(self):
        self.config = mysql_config
        self.cnx_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name='pool', **self.config)

    def get_connection(self):
        return self.cnx_pool.get_connection()
    # singlet


if __name__ == '__main__':
    connector = Connector()
    cnx = connector.get_connection()
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM origin_data where LOCATE(\'手机\', data)')
    print(cursor)
    cursor.close()
    cnx.close()
