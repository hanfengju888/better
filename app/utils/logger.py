import logbook
from app import better
from .SingletonDecorator import SingletonDecorator

@SingletonDecorator
class Log(object):
    handler = None

    def __init__(self,name='better',filename=better.config['LOG_NAME']):
        '''

        :param name: 业务名称
        :param filename: 文件名称
        '''
        self.handler = logbook.FileHandler(filename,encoding='utf-8')
        logbook.set_datetime_format('local')
        self.logger = logbook.Logger(name)

        self.handler.push_application()

    def info(self,*args,**kwargs):
        return self.logger.info(*args,**kwargs)
    def error(self,*args,**kwargs):
        return self.logger.error(*args,**kwargs)
    def warning(self,*args,**kwargs):
        return self.logger.waring(*args,**kwargs)
    def debug(self,*args,**kwargs):
        return self.logger.debug(*args,**kwargs)