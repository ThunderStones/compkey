from connector import Connector


class KaDao:
    def __init__(self):
        self.connector = Connector().get_connection()

    def select_key(self, key1, key2):
        ka1 = key1 + ' ' + key2
        ka2 = key2 + ' ' + key1
        cursor = self.connector.cursor()
        cursor.execute('SELECT * FROM ka WHERE ka = %s', (ka1,))
        result = cursor.fetchall()
        cursor.close()
        if len(result) == 0:
            cursor = self.connector.cursor()
            cursor.execute('SELECT * FROM ka WHERE ka = %s', (ka2,))
            result = cursor.fetchall()
            cursor.close()
        return result

    def insert_key(self, key1, key2, count):
        ka = key1 + ' ' + key2
        cursor = self.connector.cursor()
        cursor.execute('INSERT INTO ka (ka, `count`,) VALUES (%s, %s)',
                       (ka, count))
        self.connector.commit()
        cursor.close()
