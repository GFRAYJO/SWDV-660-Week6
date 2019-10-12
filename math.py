import math
import logging
import logstash

#DEBUG: Detailed information, typically of interest only when diagnosing problems.
#INFO: Confirmation that things are working as expected.
#WARNING: An indication that something unexpected happened, or indicative of some 
# problem in the near future (e.g.'disk space low'). The software is still working as expected.
#ERROR: Due to a more serious problem, the software has not been able to perform some function.
#CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logger = logging.getLogger('python-application-log')
logger.setLevel(logging.DEBUG)
logger.addHandler(logstash.LogstashHandler('35.170.246.177', 5959, version=1))

logger.error('python-logstash: test logstash error message')
logger.info('python-logstash: test logstash info message')
logger.warning('python-logstash: test logstash warning message')

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('results.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
 

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Unable to divide by zero')
    else:
        return result

def sqrt(x,y,n):
    n = x + y - x * y / x + y
    return math.sqrt(n)

val_1 = int(input('Enter a value: '))
val_2 = int(input('Enter a value: '))
val_3 = (val_1 + val_2 - val_1 * val_2 / val_1 + val_2)

result1 = add(val_1, val_2)
logger.debug('Add: {} + {} = {}'.format(val_1, val_2, result1))

result2 = subtract(val_1, val_2)
logger.debug('Subtract: {} + {} = {}'.format(val_1, val_2, result2))

result3 = multiply(val_1, val_2)
logger.debug('Multiply: {} + {} = {}'.format(val_1, val_2, result3))

result4 = divide(val_1, val_2)
logger.debug('Divide: {} + {} = {}'.format(val_1, val_2, result4))

result5 = math.sqrt(val_3)
logger.debug('Square Root: {} + {} - {} * {} / {} + {} = {}'.format(val_1, val_2, val_1, val_2, val_1, val_2, result5))