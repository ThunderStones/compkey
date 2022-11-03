from connector import Connector


class CompDao:
    def __init__(self):
        self.connector = Connector().get_connection()

    def select_key(self, seed_key):
        cursor = self.connector.cursor()
        cursor.execute('SELECT * FROM comp WHERE seed_key = %s', (seed_key,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert_key(self, seed_key, comp_key, comp):
        cursor = self.connector.cursor()
        cursor.execute('INSERT INTO comp (seed_key, comp_key, comp) VALUES (%s, %s, %s)',
                       (seed_key, comp_key. comp))
        self.connector.commit()
        cursor.close()
