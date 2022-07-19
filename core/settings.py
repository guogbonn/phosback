import psycopg2
import urllib.parse as up
import os
LOCAL = os.environ['isLocal']
ERROR_REPORT = True



if LOCAL == "True":
    FRONTEND_URL = "http://localhost:8001/"
    BACKEND_URL = "http://localhost:800/"
    STRIPE_KEY = os.environ['stripe']
    STRIPE_PUB = os.environ['stripepub']
    DATABASENAME = "mydb"
    DATABASEHOST = "127.0.0.1"
    DATABASEPORT = "5432"
    def init_db():
        return psycopg2.connect(database = DATABASENAME,  host = DATABASEHOST, port = DATABASEPORT)

else:
    FRONTEND_URL = "https://phostrino.com"
    BACKEND_URL = "https://phostrino.herokuapp.com"
    STRIPE_KEY = os.environ['stripe']
    STRIPE_PUB = os.environ['stripepub']

    def init_db():
        up.uses_netloc.append("postgres")
        url = up.urlparse(os.environ['dbURL'])
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
