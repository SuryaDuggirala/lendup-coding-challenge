from twilio.twiml.voice_response import Gather, VoiceResponse, Say
import requests, urllib


url = input("ENTER URL: ")
phone_number = input("ENTER PHONE NUMBER: ")
response = VoiceResponse()
# five second default timeout
gather = Gather(action=url, method="GET")
gather.say('Enter some digits followed by five seconds of silence or the pound sign')
response.append(gather)



def process_number(number):
    if number % 3 is 0 and number % 5 is not 0:
        return "Fizz"
    elif number % 3 is not 0 and number % 5 is 0:
        return "Buzz"
    elif number % 3 is  and number % 5 is 0:
        return "Fizz Buzz"
    else:
        return number


def Fizz_Buzz_Say(number):
    ret_val = process_number(number)
    gather.say(ret_val)

    


def process_digits(res):
    num = process_digits(digits_res)
    return num


def Fizz_Buzz(url):
    # Moving forward per the Twilio documentation
    end_val = -1
    try:
        digits = response.digits 
        count = 1
        true_vals = int("".join(digits))
        while count <= true_val:
            Fizz_Buzz_Say(count)
            count += 1
    except:
        return None
            


