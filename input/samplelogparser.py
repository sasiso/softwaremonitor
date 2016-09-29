"""

Format: 21-12-2014 21:22:59.0000 Process(12).
        DD-MM-YYYY HH:MM:SS.mmmm Process(thradid) Message

"""
import re
import source
import datetime
import anevent

meta_regex = "^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6}\s[\w]+\(\d+\))"
parse_date_time_from_meta = "^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6})"
extract_thread_from_meta = "\((\d+)\)$"
extract_process_name_from_meta = "(\w+)\(\d+\)$"


class LoggingSourceSample(source.Source):
    """ This class reads a log file and provides input to display engine

    """
    start_datetime = datetime.datetime.now()
    end_datetime = datetime.datetime.now()

    def __init__(self, keyword, filename):
        """

        :param filename:
        """
        self._curr_pos = datetime.datetime.now()
        self._filename = filename
        self._keywords = keyword

    def start_time(self):
        """

        :return:  Return Start Time of this soruce
        """
        return self.start_datetime

    def end_time(self):
        """

        :return:  Return Start Time of this soruce
        """
        return self.end_datetime

    def get_data(self, **kwargs):
        return self.parse()

    def parse(self):
        return_value = {}
        line_num = 0
        start_time_set = False

        with open(self._filename) as f:
            for line in f:
                line_num += 1
                result = re.search(meta_regex, line)
                if result is None:
                    print "parsing failed for line %s" % line
                    continue

                meta = result.group(1)
                dt = datetime.datetime.strptime(re.search(parse_date_time_from_meta, meta).group(1),
                                                "%d-%m-%Y %H:%M:%S.%f")

                if not start_time_set:
                    self.start_datetime = dt
                    start_time_set = True
                else:
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
                event.thread = re.search(extract_thread_from_meta, meta).group(1)
                event.date_time = dt
                process_name = re.search(extract_process_name_from_meta, meta).group(1)

                if process_name not in return_value:
                    return_value[process_name] = []

                return_value[process_name].append(event)

        return return_value

    def getpos(self, an_event):
        point_a = self.end_datetime
        point_b = self.start_datetime
        delta = point_a - point_b
        span = delta.total_seconds()

        return (an_event.date_time - point_b).total_seconds()/span


        print str("Total Span is %d" % span)


if __name__ == '__main__':
    keywords = ["Error", "Exception", "Fatal", "Warning", "Started", "Finished", "User Actions"]
    log_src = LoggingSourceSample(keywords, "sample.log")
    rv = log_src.get_data()
    for key, value in rv.iteritems():
        for a in value:
            print key + "-" + a.string()
