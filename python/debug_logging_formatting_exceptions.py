# This snippets helps to detect what's missing in your message format when using
# logging module

from pprint import pprint, pformat
import sys
def print_log_record_on_error(func):
    def wrap(self, record):
        try:
            print >>sys.stderr,pformat(record.__dict__)
            print >>sys.stderr,pformat(self._fmt)
            return func(self, record)
        except:
            print >>sys.stderr,"Unable to create log message fmt=%r, meg=%r " % (
                                getattr(self, '_fmt', '?'), record.getMessage())
            raise
    return wrap
logging.Formatter.format = print_log_record_on_error(logging.Formatter.format)
