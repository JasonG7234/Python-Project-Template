# Standard imports
import logging
import sys

# Local imports
sys.path.append('./src')
import logging

LOGGING_FORMAT = "%(asctime)s | %(levelname)s | %(message)s [%(filename)s:%(lineno)d]"
LOGGING_TO_STANDARD_OUT = False
LOGGING_LEVEL = logging.INFO

def define_logger():
  """Defines the parameters of the logger for this run of the games process
      Pulls from the LOGGING_LEVEL & LOGGING_FORMAT constants
      Creates the TimedRotatingFileHandler to automatically delete logs from older runs
      Logs to console ONLY IF the LOGGING_TO_STANDARD_OUT flag is on
  """
  
  logging.basicConfig( 
    level=LOGGING_LEVEL,
    format=LOGGING_FORMAT)
  
  handler = logging.handlers.TimedRotatingFileHandler(
    f'logs/scraper.log', 
    backupCount=5)
  
  logging.addHandler(handler)
  
  if (LOGGING_TO_STANDARD_OUT):
    logging.addHandler(logging.StreamHandler(sys.stdout))

if __name__ == "__main__":
  define_logger()
  print("test")
  