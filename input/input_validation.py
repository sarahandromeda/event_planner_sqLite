from calendar import month_abbr
import time
import re
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

    def verify_type(response):
        while True:
            if re.match(r"\A[1]?[0-9]\Z", response):
                break
            else:
                Say.invalid_input(response)
                response = input()
        return response

    def verify_date(response):
        while True:
            try:
                res = time.strptime(response, '%m/%d/%y')
                break
            except ValueError:
                Say.invalid_date(response)
                response = input()
        res = f"{res.tm_year}-{res.tm_mon}-{res.tm_mday}"
        return res

    def verify_time(response):
        while True:
            try:
                res = time.strptime(response, '%I:%M %p')
                break
            except ValueError:
                Say.invalid_time(response)
                response = input()
        # Format time response to follow %H:%M:%S
        response = f"{res.tm_hour}:{res.tm_min}:{res.tm_sec}0"
        return response

    def verify_menu(response):
        while True:
            if re.match(r"\A[1-9]\Z", response):
                break
            else:
                Say.invalid_input(response)
                response = input()
        return response

    def verify_search_menu(response):
        while True:
            if re.match(r"\A[1-5]\Z", response):
                break
            else:
                Say.invalid_input(response)
                response = input()
        return response

    def verify_search_date(response):
        """
        Checks if response has a + or - modifier, then checks
        if response is a date, month, or year.
        Returns tuple of formatted date string and modifier. 
        """
        # response should be date in MM/DD/YY format
        # or a YYYY or a M
        # may have a +/- appended
        year_pattern = re.compile(r"\A\d{4}\Z")
        month_pattern = re.compile(r"\A1[0-2]|[1-9]\Z")
        suffix_pattern = re.compile(r".*\+|.*\-")

        while True:
            try:
                if re.match(suffix_pattern, response):
                    response, modifier = response.split(' ')

                if re.match(year_pattern, response):
                    res = time.strptime(response, '%Y')
                    break
                elif re.match(month_pattern, response):
                    res = time.strptime(response, '%m')
                    break
                else:
                    res = time.strptime(response, '%m/%d/%y')
                    break
            except ValueError:
                Say.invalid_input()
                response = input()
            
        response = f"{res.tm_year}-{res.tm_mon}-{res.tm_mday}"
        return (response, modifier)
    
    def verify_search_time(response):
        # response should be HH:MM AM/PM format
        # may have a +/- appended
        suffix_pattern = re.compile(r".*\+|.*\-")

        while True:
            if re.match(suffix_pattern, response):
                response, modifier = response.split(' ')

            try:
                res = time.strptime(response, '%I:%M %p')
                break
            except ValueError:
                Say.invalid_time(response)
                response = input()
        # Format time response to follow %H:%M:%S
        response = f"{res.tm_hour}:{res.tm_min}:{res.tm_sec}0"
        return (response, modifier)