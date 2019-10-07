import logging
import logstash
import sys

host = 'localhost'

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('35.170.246.177', 5959, version=1))

logger.error('python-logstash: test logstash error message')
logger.info('python-logstash: test logstash info message')
logger.warning('python-logstash: test logstash warning message')

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('results.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra)