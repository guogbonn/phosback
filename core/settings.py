import psycopg2
import urllib.parse as up
import os
LOCAL = os.environ['isLocal']
ERROR_REPORT = True



if LOCAL == "True":
    FRONTEND_URL = "http://localhost:8001/"
    BACKEND_URL = "http://localhost:800/"
    STRIPE_KEY = os.environ['stripe']
    # STRIPE_KEY = 'sk_test_51LKBjELd2ZgM3kuXudwuSTc2uWMykaUBrrnNaImttcpeWrOacQh9h7Sp4VhDYwZR2cehyde98iOkMMFeSijNcqoA008XLZ9EV8'
    DATABASENAME = "mydb"
    DATABASEHOST = "127.0.0.1"
    DATABASEPORT = "5432"
    def init_db():
        return psycopg2.connect(database = DATABASENAME,  host = DATABASEHOST, port = DATABASEPORT)

else:
    FRONTEND_URL = "http://phostrino.com"
    BACKEND_URL = "https://phostrino.herokuapp.com"
    STRIPE_KEY = os.environ['stripe']
    # STRIPE_KEY = 'sk_test_51LKBjELd2ZgM3kuXudwuSTc2uWMykaUBrrnNaImttcpeWrOacQh9h7Sp4VhDYwZR2cehyde98iOkMMFeSijNcqoA008XLZ9EV8'
    # DATABASENAME = ""
    # DATABASEPASSWORD = ""
    # DATABASEHOST = ""
    # DATABASEHOST = "127.0.0.1"
    # DATABASEPORT = "5432"
    # DATABASEUSER = ""
    def init_db():
        up.uses_netloc.append("postgres")
        url = up.urlparse(os.environ['dbURL'])
        # url = up.urlparse('postgres://ehomefcs:E3ZVNIBJ6f0ynoxUROeT_BdyxCI8o9Cm@isilo.db.elephantsql.com/ehomefcs')
        conn = psycopg2.connect(database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port='5432'
        )
        return conn


COMPANY_EMAIL = "support@phostrino.com"
COMPANY_EMAIL_PASSWORD = os.environ["COMPANY_EMAIL_PASSWORD"]

RECEIVE_ERRORS = ["support@phostrino.com","ogbonnaya83512@gmail.com"]
