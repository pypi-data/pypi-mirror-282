from pymongo import MongoClient
import random

# MongoDB URI
uri = """mongodb+srv://corerealrex:trex123@core.x48yppq.mongodb.net/?retryWrites=true&w=majority&appName=Core"""


def genOTP(Number):
    """
    Generate an OTP for the provided phone number and store it in the database.

    Parameters:
    Number (str): The phone number for which the OTP is generated.

    Returns:
    str: Success message with the generated OTP or error message if the number is already in use.
    """
    client = MongoClient(uri)
    db = client['OTP']
    col = db['OTPs']

    try:
        gen_otp = random.randint(100000, 999999)
        add_otp = {
            "_id": Number,
            "otp": gen_otp
        }
        col.insert_one(add_otp)
        msg = f"OTP Generated Successfully\nOTP: {gen_otp}"
        return msg

    except Exception as e:
        return "This number is already in use in another session. Please choose another number."


def authOTP(Number, OTP):
    """
    Authenticate the provided OTP for the given phone number.

    Parameters:
    Number (str): The phone number to authenticate the OTP for.
    OTP (int): The OTP to be authenticated.

    Returns:
    bool: True if OTP is successfully authenticated, False otherwise.
    """
    client = MongoClient(uri)
    db = client['OTP']
    col = db['OTPs']

    try:
        got_otp = {'_id': Number, 'otp': int(OTP)}
        verify_otp = col.find_one({"_id": Number, "otp": int(OTP)})

        if got_otp == verify_otp:
            col.delete_one(verify_otp)
            return True
        else:
            return False
    except Exception as e:
        return "Error! Please Try Again Later."