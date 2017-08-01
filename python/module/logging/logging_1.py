import logging
head = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=head, filename="config.log")
logging.info("[%s]", __name__)
