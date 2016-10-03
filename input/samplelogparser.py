"""

Format: 21-12-2014 21:22:59.0000 Process(12).
        DD-MM-YYYY HH:MM:SS.mmmm Process(thradid) Message

"""
import re
import source
import datetime
import anevent


class LoggingSourceSample(source.Source):
    meta_regex = ""
    parse_date_time_from_meta = ""
    extract_thread_from_meta = ""
    extract_process_name_from_meta = ""
    date_format = "%d-%m-%Y %H:%M:%S.%f"
    """ This class reads a log file and provides input to display engine

    """
    zoom_start_time = start_datetime = datetime.datetime.now()
    zoom_end_time = end_datetime = datetime.datetime.now()

    def __init__(self, keyword, filename):
        """

        :param filename:
        """
        self._curr_pos = datetime.datetime.now()
        self._filename = filename
        self._keywords = keyword
        self._result = {}
        self._parsed = False
        self._pos_changed = False
        self._re_values = {}
        self._last_zoom = 0
        self._last_recenter = 0

    def setregex(self, meta, date_time, thread, process):
        self.meta_regex = meta
        self.parse_date_time_from_meta = date_time
        self.extract_thread_from_meta = thread
        self.extract_process_name_from_meta = process

    def set_date_format(self, date_format):
        self.date_format = date_format

    def start_time(self):
        """

        :return:  Return Start Time of this soruce
        """
        return self.zoom_start_time

    def end_time(self):
        """

        :return:  Return Start Time of this soruce
        """
        return self.zoom_end_time

    def get_data(self, zoom=1, recenter=0):
        if not self._parsed:
            self.parse()
            self._parsed = True

        center = self.start_datetime + ((self.end_datetime - self.start_datetime) / 2)
        center += datetime.timedelta(minutes=recenter)
        delta = (self.end_datetime - self.start_datetime) / zoom

        self.zoom_start_time = center - delta
        self.zoom_end_time = center + delta

        if self._last_recenter is not recenter or self._last_zoom is not zoom:
            self._last_recenter = recenter
            self._last_zoom = zoom
            return self.prepare()

        return self._re_values

    def prepare(self):
        print "Enter Prepare"
        self._re_values.clear()

        for key, value in self._result.iteritems():
            if self.zoom_start_time <= value[0].date_time <= self.zoom_end_time:
                self._re_values[key] = value
            else:
                self._re_values[key] = []

        print "Done Prepare"
        return self._re_values

    def parse(self):

        line_num = 0
        start_time_set = False

        with open(self._filename) as f:
            for line in f:
                line_num += 1
                result = re.search(self.meta_regex, line)
                if result is None:
                    # print "parsing failed for line %s" % line
                    continue

                meta = result.group(1)
                dt = datetime.datetime.strptime(re.search(self.parse_date_time_from_meta, meta).group(1),
                                               self.date_format)

                if not start_time_set:
                    self.start_datetime = self.end_datetime = dt
                    start_time_set = True

                if self.end_datetime < dt:
                    self.end_datetime = dt

                found_list = []
                for a_key in self._keywords:
                    if a_key not in line:
                        continue
                    found_list.append(a_key)

                if not found_list:
                    continue

                event = anevent.AnEvent()
                event.number = line_num
                event.keys = found_list
                if self.extract_thread_from_meta:
                    event.thread = re.search(self.extract_thread_from_meta, meta).group(1)

                event.date_time = dt
                process_name = re.search(self.extract_process_name_from_meta, meta).group(1)

                if process_name not in self._result:
                    self._result[process_name] = []

                self._result[process_name].append(event)

    def getpos(self, an_event):
        point_a = self.zoom_end_time
        point_b = self.zoom_start_time
        delta = point_a - point_b
        span = delta.total_seconds()

        return (an_event.date_time - point_b).total_seconds() / span

    def render_start_date(self):
        return self.zoom_start_time

    def render_end_date(self):
        return self.zoom_end_time


if __name__ == '__main__':
    keywords = ["Error", "Exception", "Fatal", "Warning", "Started", "Finished", "User Actions"]
    log_src = LoggingSourceSample(keywords, "sample.log")
    rv = log_src.get_data()
    for key, value in rv.iteritems():
        for a in value:
            print key + "-" + a.string()
