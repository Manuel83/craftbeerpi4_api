from logging.handlers import RotatingFileHandler
from time import localtime, strftime

from cbpi_api.extension import CBPiExtension
import logging
logging.basicConfig(level=logging.INFO)

class CBPiSensor(CBPiExtension):
    def __init__(self, *args, **kwds):
        CBPiExtension.__init__(self, *args, **kwds)
        self.logger = logging.getLogger(__file__)

        self.data_logger = logging.getLogger('cbpi.sensor.%s' % self.id)
        self.data_logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler('sensor_%s.log' % self.id, maxBytes=2000, backupCount=10)
        self.data_logger.addHandler(handler)


    def log_data(self, value):
        formatted_time = strftime("%Y-%m-%d %H:%M:%S", localtime())

        self.data_logger.debug("%s,%s" % (formatted_time, value))


    def init(self):
        self.logger.warning("Sensor Init not implemented")
        pass

    async def run(self, cbpi):
        self.logger.warning("Sensor Init not implemented")

    def state(self):
        pass