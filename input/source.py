"""

this is base files for all the source
Any source who want to render on display engine must inherit this class
"""
import datetime


class Source(object):
    """

    """
    def start_time(self):
        """

        :return:  Return Start Time of this soruce
        """
        pass

    def get_data(self, start, end):
        """ returns data from given interval

        :param start: Begin of interval
        :param end: end of interval
        :return:
        """
        pass
