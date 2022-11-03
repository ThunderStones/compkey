from connector import Connector


class SaDao:
    def __init__(self):
        self.connector = Connector().get_connection()

    def select_key(self, seed_key):
        cursor = self.connector.cursor()
        cursor.execute('SELECT * FROM sa WHERE seed_key = %s', (seed_key,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert_key(self, seed_key, mid_key, count, comp):
        cursor = self.connector.cursor()
        cursor.execute('INSERT INTO sa (seed_key, mid_key, `count`, comp) VALUES (%s, %s, %s, %s)',
                       (seed_key, mid_key, count, comp))
        self.connector.commit()
        cursor.close()
