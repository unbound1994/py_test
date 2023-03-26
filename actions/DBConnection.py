import os
import pymysql

from read_env import read_env


class DBConnection:

    read_env("../.env")

    def __init__(self):
        self.host = os.environ.get('MYSQL_HOST')
        self.login = os.environ.get('MYSQL_USER')
        self.passwd = os.environ.get('MYSQL_PASS')
        self.db_name = os.environ.get('MYSQL_NAME')
        self.format_set = 'utf8mb4'
        self.dbh = pymysql.connect(
                       host=f'{self.host}',
                       user=f'{self.login}',
                       password=f'{self.passwd}',
                       charset=f'{self.format_set}',
                       ssl=None,
                       cursorclass=pymysql.cursors.DictCursor
                   )

    def prepare(self, sql, data=None, *args):

        try:
            cursor = self.dbh.cursor()
            cursor.execute(sql, data)
            return cursor.fetchall()
        except SystemError as sys:
            print(SystemError('Fatal error! '), sys)
        except Exception as ex:
            print(Exception('Something went wrong: '), ex)
        except ConnectionError as ce:
            print(RuntimeError('Failed to open database because '), ce)
        finally:
            self.dbh.close()
