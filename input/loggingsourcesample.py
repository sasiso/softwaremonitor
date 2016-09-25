"""
This is a sample implementation of a input source
- it reads a text file and provides channel data
"""
import source
import datetime
import anevent


class LoggingSourceSample(source.Source):
    """ This class reads a log file and provides input to display engine

    """

    def __init__(self, filename):
        """

        :param filename:
        """
        self._currpos = datetime.datetime.now()
        self._filename = filename

    def start_time(self):
        return datetime.datetime.now()

    def get_data(self, start, end):
        rv = {start: anevent.AnEvent(end, 0, "ABC"), end: anevent.AnEvent(end, 1, "EFG")}
        return rv



