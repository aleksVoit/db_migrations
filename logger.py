import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s ')
logging.basicConfig(level=logging.INFO, format='%(name)s %(message)s')