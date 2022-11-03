from connector import Connector


class OriginDataDao:
    def __init__(self):
        self.connector = Connector().get_connection()

    def count_key(self, key):
        cursor = self.connector.cursor()
        cursor.execute('SELECT COUNT(*) FROM origin_data WHERE LOCATE(%s, data)', (key,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def count_two_key(self, key1, key2):
        cursor = self.connector.cursor()
        cursor.execute('SELECT COUNT(*) FROM origin_data WHERE LOCATE(%s, data) AND LOCATE(%s, data)',
                       (key1, key2))
        result = cursor.fetchone()
        cursor.close()
        return result

    def count_key1_but_not_key2(self, key1, key2):
        cursor = self.connector.cursor()
        cursor.execute('SELECT COUNT(*) FROM origin_data WHERE LOCATE(%s, data) AND NOT LOCATE(%s, data)',
                       (key1, key2))
        result = cursor.fetchone()
        cursor.close()
        return result

    