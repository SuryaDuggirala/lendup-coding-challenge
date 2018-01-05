from twilio.twiml.voice_response import Gather, VoiceResponse, Say
import requests, urllib


url = input("ENTER URL: ")
phone_number = "(XXX) XXX-XXXX"
response = VoiceResponse()
# five second default timeout
gather = Gather(action=url, method="GET")
gather.say('Enter some digits followed by five seconds of silence or the pound sign')
response.append(gather)
# Now to get the digits response from the GET request from the gather
digits_res = requests.get(url, "Digits")


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
    gather.say(number)



def connection(url):
    
    # Do something with the digits_res and get the digits then process them
    


def process_digits(res):
    num = process_digits(digits_res)
    return num


def Fizz_Buzz(url):
    # Moving forward per the Twilio documentation
    end_val = -1
    true_val = connection(url)
    if true_val == end_val:
        return None
    else:
        count = 1
        while count <= true_val:
            Fizz_Buzz_Say(count)
            count += 1
            


