import psycopg2

LOCAL = True
ERROR_REPORT = True



if LOCAL:
    FRONTEND_URL = "http://localhost:8001/"
    BACKEND_URL = "http://localhost:8001/"
    STRIPE_KEY = 'sk_test_51LKBjELd2ZgM3kuXudwuSTc2uWMykaUBrrnNaImttcpeWrOacQh9h7Sp4VhDYwZR2cehyde98iOkMMFeSijNcqoA008XLZ9EV8'
    DATABASENAME = "mydb"
    DATABASEHOST = "127.0.0.1"
    DATABASEPORT = "5432"
    def init_db():
        return psycopg2.connect(database = DATABASENAME,  host = DATABASEHOST, port = DATABASEPORT)

else:
    FRONTEND_URL = "http://phostrino.com"
    BACKEND_URL = ""
    DATABASENAME = ""
    DATABASEPASSWORD = ""
    DATABASEHOST = ""
    DATABASEHOST = "127.0.0.1"
    DATABASEPORT = "5432"
    DATABASEUSER = ""
    def init_db():
        return psycopg2.connect(database =  '',  host = "127.0.0.1", port = "5432")


COMPANY_EMAIL = "support@phostrino.com"
COMPANY_EMAIL_PASSWORD = "1GPSguo3512!"

RECEIVE_ERRORS = ["support@phostrino.com","ogbonnaya83512@gmail.com"]
