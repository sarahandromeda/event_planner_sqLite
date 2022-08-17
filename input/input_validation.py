import time
from display.message import Say

class InputVerification:
    def verify(response):
        """
        Requirement verification. Verifies that input response is not an empty
        string. 
        Function will ask user repeatedly for an input, if it is left blank,
        inside a loop eventually returning the response when valid. 
        """
        # Loop until response is not an empty string
        while not response:
            Say.invalid_input(response) 
            response = input()
        return response

    def verify_date(response):
        while True:
            try:
                time.strptime(response, '%Y-%m-%d')
                break
            except ValueError:
                Say.invalid_date(response)
                response = input()
        return response

    def verify_time(response):
        while True:
            try:
                res = time.strptime(response, '%I:%M %p')
                break
            except ValueError:
                Say.invalid_time(response)
                response = input()
        # Format time response to follow %H:%M:%S
        response = f"{res.tm_hour}:{res.tm_min}:{res.tm_sec}"
        return response
