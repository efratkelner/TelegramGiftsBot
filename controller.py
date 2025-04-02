from math import sqrt
from itertools import count, islice
import model

def is_prime(number: str) -> str:
    """
    check if number is prime 
    return: 'prime' or 'not prime'
    """
    number = int(number)
    HistoryController.create(number)
    if number != 2 and number % 2 == 0:
        return 'Come on dude, you know even numbers are not prime!'
    if check_if_prime(number):
        return 'prime'
    else:
        return 'not prime'

def check_if_prime(number: int) -> bool:
    """
    check if number is prime
    :number: the number to check
    :return: true if prime else false

    """
    flag= True
    if number > 1:
     for i in range(2, number):
        if (number % i) == 0:
            flag = False
            break
    return flag
  
def is_factorial(number: str) -> str:
    """
    check if number is a result of factorial operation and returns the right sentence 
    :return: 'factorial' or 'not factorial'
    """
    number = int(number)
    HistoryController.create(number)
    if check_is_factorial(number):
        return 'factorial'
    else:
        return 'not factorial'
    
def check_is_factorial(number: int) -> bool:

    """
    check if number is a result of factorial operation
    :number: the number to check
    :return: true if a result of factorial operation else false
    """

    i = factorial = 1
    while factorial < number:
        i += 1
        factorial *= i
    return factorial == number


def is_palindrome(number: str) -> str:
    """
    check if number is palindrom and returns the right sentence 
    :return: 'palindrom' if palindrom else 'not palindrom'
    """
    HistoryController.create(int(number))
    if check_is_palindrome:
        return 'palindrome'
    else:
        return 'not palindrome'
    
def check_is_palindrome(number: str) -> bool:
 
    """
    check if number is palindrom
    :number: the number to check
    :return: true if palindrom else false
    """
    
    return number == number[::-1]


def check_is_sqrt(number: int) -> bool:
 
    """
    check if number has an integer square root
    :number: the number to check
    :return: true if has an integer square root else false
    """

    return sqrt(number) ** 2 == number


def is_sqrt(number: str) -> str:
    """
    check if number has an integer square root and returns the right sentence 
    :return: 'sqrt' if has else 'not sqrt'
    """
    number = int(number)
    HistoryController.create(number)
    if check_is_sqrt(number):
        return 'sqrt'
    else:
        return 'not sqrt'


def popular():
    """
    find the number that appeared the most in the bot history
    :return: the most popular number in the bot history
    """
    list=[]
    for i in HistoryController.get_all_history():
        list.append(i['amount'])
    amount = max(list)
    return [i['number'] for i in HistoryController.get_all_history() if i['amount'] == amount][0]


class HistoryController:
    """
    warpped class to handle the bot history
    """

    @classmethod
    def create(cls, num: int) -> None:
        """ 
        connect to function from model     
        """
        model.HistoryModelWrapper.create(num)
        
    @classmethod
    def get_all_history(cls) -> list:
        """ 
        connect to function from model
        :return: list of the user request history
        """
        return model.HistoryModelWrapper.get_all_history()
    
