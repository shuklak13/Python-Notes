import logging

# prints to stdout
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)

# prints log to stdout and also saves to specified log file
log = logging.getLogger('my_logfile')
fh = logging.FileHandler('my_logfile.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(fh)
log.addHandler(ch)

log.setLevel(logging.DEBUG)

log.info("This is information.")
log.error("This is Error!")
log.debug("This is debug...")