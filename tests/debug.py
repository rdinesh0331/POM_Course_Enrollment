from utilities.customlog import custom_logger as cl
import logging


class DebugDemo():

    log = cl()

    @classmethod
    def method1(cls):
        cls.log.debug('Debug message')
        cls.log.info('info message')
        cls.log.error('error message')
        cls.log.warning('warning message')
        cls.log.critical('critical message')

    @staticmethod
    def method2():
        log2.debug('Debug message')
        log2.info('info message')
        log2.error('error message')
        log2.warning('warning message')
        log2.critical('critical message')

demo = DebugDemo()
demo.method1()
demo.method2()