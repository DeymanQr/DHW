# import logging
import logging.config
from math import sqrt
import json

with open('log_settings.json', 'r', encoding='UTF-8') as f:
    config = json.load(f)

logging.config.dictConfig(config['logging'])
logger_ububub = logging.getLogger('main_ububub')


class Rectangle:
    def __init__(self, a, b):
        logger_ububub.debug('Start init func')
        try:
            if a < 0 or b < 0:
                logger_ububub.warning('sizes of rectangle are negative.')
            if a == 0 or b == 0:
                logger_ububub.warning('rectangle is a line (what?)')
        except TypeError:
            logger_ububub.warning('sizes of rectangle have incorrect types.')
        self.a = a
        self.b = b
        logger_ububub.debug('Created Rectangle instance')

    def area(self):
        logger_ububub.debug('Start area func')
        try:
            answ = self.a*self.b
            logger_ububub.debug(f'Get answer to area func - {answ}')
            return answ
        except TypeError as e:
            logger_ububub.error(f'Error: {e}')

    def perimeter(self):
        logger_ububub.debug('Start perimeter func')
        try:
            answ = 2 * (self.a + self.b)
            logger_ububub.debug(f'Get answer to perieter func - {answ}')
            return answ
        except TypeError as e:
            logger_ububub.error(f'Error: {e}')

    def diagonal(self):
        logger_ububub.debug('Start diagonal func')
        try:
            answ = sqrt(self.a**2 + self.b**2)
            logger_ububub.debug(f'Get answer to diagonal func - {answ}')
            return answ
        except TypeError as e:
            logger_ububub.error(f'Error: {e}')


a = Rectangle(2, 4)
print(a.area())
b = Rectangle('abc', 'def')
print(b.diagonal())
