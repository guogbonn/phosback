from fastapi import FastAPI, Header, Request, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import postgres
import email_controller
import settings

import threading

import pytz # $ pip install pytz
import stripe

import json
from random import randint
from datetime import datetime


app = FastAPI()
stripe.api_key = settings.STRIPE_KEY

backend_process_state = {}

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8001",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/log_login")
async def log_login(payload: dict = Body(...)):
    try:
        conn = settings.init_db()
        cur = conn.cursor()
        postgres.create_login(payload["page_access"], cur, conn)

        return {"sucess":"sucess"}
    except Exception as e:
        email = email_controller.Email()
        email.phostrino_alert('ERROR on log_login',json.dumps({'error': str(e)}, indent=4, sort_keys=True), settings.RECEIVE_ERRORS)


@app.get("/courselist")
async def course_list():
    try:
        conn = settings.init_db()
        cur = conn.cursor()
        # add course names as needed
        dict_courses = {"Intro to Python": [] }

        for course in dict_courses.keys():
            dict_courses[course] = postgres.get_courses(course, cur)
        return dict_courses
    except Exception as e:
        email = email_controller.Email()
        email.phostrino_alert('ERROR on course list',json.dumps({'error': str(e)}, indent=4, sort_keys=True), settings.RECEIVE_ERRORS)


# @app.get("/ping/")
# async def read_items(
#     request: Request
#     ):
#     # print(request.headers)
#     return {"pong":request.headers}

def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 20000


@app.post("/create-payment-intent")
async def read_item( payload: dict = Body(...)):
    try:
        data = payload
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return {
            'clientSecret': intent['client_secret']
        }
    except Exception as e:

        return {'error':'error'}


@app.post("/unsubscribe")
async def unsubscribe( data: dict = Body(...)):
        conn = settings.init_db()
        cur = conn.cursor()
        obj = {"student_id":  data["value"]}
        postgres.unsubscribe(obj,cur,conn)
        # set student receive email to false
        # send alert to email
        # find all student with student email and unsubscribe them;
        conn.close()
        email.phostrino_alert('Unsubscriber', f'Stuend id: {data["value"]} has unsubscribed', settings.RECEIVE_ERRORS)
        return {"result": "sucess"}


@app.post("/submitEnrollment")
async def submit_enrollment( data: dict = Body(...)):
    try:
        conn = settings.init_db()
        cur = conn.cursor()

        data = data["data"]
        data["email"] = data["email"].strip()
        print(data)
        # create Login
        login_id = postgres.create_login(data["client"], cur, conn)


        # create Student
        data["login"] = login_id
        data["send_email"] = 't'

        # save failure point
        backend_process_state["data"] = data

        student_id = postgres.create_student(data, cur, conn)
        print("student_id ",student_id)


        # save failure point
        backend_process_state["data"] = data

        # # Chance of race condition where two people grab the same seat.
        # # get course  blindly trust that in the time the function started no one took the seat.
        student_seat_number = postgres.subtract_seat(data["course_id"],  cur, conn)
        data["seat_number"] = student_seat_number
        print("seat number ",student_seat_number)
        #
        #
        # create coursestudent
        data["course"] = data["course_id"]
        data["student"] = student_id
        data["amount_refunded"] = 0
        data["refunded"] = "f"
        data["refund_requested"] = "f"
        data["confirmation_code"] = "Phostrino" +  str(randint(0, 999))


        # save failure point
        backend_process_state["data"] = data
        course_student_id = postgres.create_course_student(data, cur, conn)

        # save failure point
        backend_process_state["data"] = data

        # email confirmation recipt
        email = email_controller.Email()
        # send_confirmation(data)
        receipt_email = {
        "student_name": data["name"],
        "conf" : data["confirmation_code"],
        "course_title" : "Intro to Python",
        "course_price" : str(data["amount_payed"] - 12),
        "tax": str(12),
        "sub_total" :  str(data["amount_payed"] - 12),
        "final_total" : str(data["amount_payed"]),
        "terms_link" : settings.FRONTEND_URL + 'terms.html',
        "unsubscribe_link" : settings.FRONTEND_URL + f'unsubscribe.html?class={str(student_id)}',
        "recipients": [data["email"]]

        }

        # save failure point
        backend_process_state["receipt_email"] = receipt_email

        email_threadr = threading.Thread(target=email.receipt, name="receipt", args=(receipt_email,))
        email_threadr.start()

        # # email class onboarding
        # send_class_onboarding(data)
        onboard_email = {
        "student_name": data["name"],
        "course_title" : data["course_title"],
        "course_dates" : data["course_dates"],
        "course_days" : data["course_days"],
        "course_time" : data["course_time"],
        "zoom_link"  : data["zoom_link"],
        "recipients": [data["email"]],
        "unsubscribe_link" : settings.FRONTEND_URL + f'unsubscribe.html?class={str(student_id)}',
        "terms_link" : settings.FRONTEND_URL + 'terms.html'
        }

        # save failure point
        backend_process_state["onboard_email"] = onboard_email

        # send onbard email
        email_threadW = threading.Thread(target=email.course_welcome, name="course_welcome", args=(onboard_email,))
        email_threadW.start()
        conn.close()

        return {"confirmation_code":data["confirmation_code"]}
    except Exception as e:
        email = email_controller.Email()
        email.phostrino_alert('ERROR on submitEnrollment',json.dumps({'error': str(backend_process_state)}, indent=4, sort_keys=True), settings.RECEIVE_ERRORS)
