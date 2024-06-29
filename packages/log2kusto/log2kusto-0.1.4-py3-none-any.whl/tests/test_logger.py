import logging
from log2kusto.kusto_handler import KustoHandler

def get_extra_field(keyname, val):
    return {keyname:val}

def send_info(log:str, dimensions:str = ''):
    d = get_extra_field("dimensions", dimensions )
    logger.info(log, extra=d)

def send_warn(log:str, dimensions:str = ''):
    d = get_extra_field("dimensions", dimensions )
    logger.warning(log, extra=d)

def send_error(log:str, dimensions:str = ''):
    d = get_extra_field("dimensions", dimensions )
    logger.error(log, extra=d)

def send_critical(log:str, dimensions:str = ''):
    d = get_extra_field("dimensions", dimensions )
    logger.critical(log, extra=d)
class CustomFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', validate=True, attributes_list=[]):
        super().__init__(fmt, datefmt, style, validate)
        self.attributes = attributes_list

    def format(self, record):
        #print("in format")
        for attr in self.attributes:
            #print(attr)
            if not hasattr(record, attr):
                setattr(record, attr, '')
        return super().format(record)

#https://docs.python.org/3/library/logging.html#logrecord-attributes
logrecord_attributes_list = ['asctime', 'levelname', 'funcName', 'module', 'message']
custom_attributes_list = ['dimensions', 'project_name']
all_attributes_list = logrecord_attributes_list + custom_attributes_list
formatter = CustomFormatter('%(' + ((')s' + " ; " + '%(').join(all_attributes_list)) + ')s', "%Y-%m-%d %H:%M:%S", \
                            attributes_list=all_attributes_list)

kusto_handler = KustoHandler('https://ingest-vmainsight.kusto.windows.net/', 'vmadbexp', 'log_test', all_attributes_list)
kusto_handler.setLevel(logging.INFO)
kusto_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(kusto_handler)

#logger = logging.LoggerAdapter(logger, {"project_name":"test"})

while True:
    log = input("> ")
    if log.strip().lower() != "quit":
        send_info(log, "extra message")
        send_warn(log, "key1:val1, key2:val2")
        send_error(log)
        send_critical(log, "exception")
    else:
        break

logger.handlers[0].flush_writes()

