import psycopg2


conn = psycopg2.connect(host='localhost',
                        port='5432',
                        user='postgres',
                        password='1234')
