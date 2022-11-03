from connector import Connector


class SeedkeyDao:
    def __init__(self):
        self.connector = Connector().get_connection()

    def select_key(self, key):
        cursor = self.connector.cursor()
        cursor.execute('SELECT * FROM s WHERE seed_key = %s', (key,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert_key(self, key, count):
        cursor = self.connector.cursor()
        cursor.execute('INSERT INTO s (seed_key, `count`) VALUES (%s, %s)', (key, count,))
        self.connector.commit()
        cursor.close()

    def update_key(self, key, count):
        cursor = self.connector.cursor()
        cursor.execute('UPDATE s SET `count` = %s WHERE seed_key = %s', (count, key,))
        self.connector.commit()
        cursor.close()


if __name__ == '__main__':
    seedkey_dao = SeedkeyDao()
    # seedkey_dao.insert_key('手机', 1)
    print(seedkey_dao.select_key('手机'))
    seedkey_dao.update_key('手机', 1)
