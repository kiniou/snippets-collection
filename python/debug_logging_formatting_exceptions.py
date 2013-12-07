# This snippets helps to detect what's missing in your message format when using
# logging module
#
# (seen at http://stackoverflow.com/questions/2477934/easy-way-to-find-not-enough-arguments-in-python-logging-library)

from pprint import pprint, pformat
import sys, traceback
def print_log_record_on_error(func):
    def wrap(self, record):
        try:
            return func(self, record)
        except:
            print >>sys.stderr,"Unable to create log message fmt=%r, msg=%r, msgargs=%r " % (
                                getattr(self, '_fmt', '?'), record.msg, record.args)
            print >>sys.stderr,''.join(traceback.format_stack())
            raise
    return wrap
logging.Formatter.format = print_log_record_on_error(logging.Formatter.format)
