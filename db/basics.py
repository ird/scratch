import psycopg2
import sys


def main():
    con = None
    try:
        con = psycopg2.connect(database='testdb', user='david')
        cur = con.cursor()
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        print(ver)
    except psycopg2.DatabaseError as e:
        print('Error: ', e)
        sys.exit(1)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    main()
