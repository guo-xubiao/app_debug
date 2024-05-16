# 封装的loguru日志处理
import loguru

class Logger:
    def __init__(self, log_file):
        self.logger = loguru.logger
        self.logger.add(log_file, rotation="500 MB", retention="7 days", enqueue=True)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def remove(self):
        self.logger.remove()

