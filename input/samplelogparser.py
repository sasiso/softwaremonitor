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


class Parser(object):
    def __init__(self):
        pass

    @staticmethod
    def parse(keyword, filename):
        return_value = {}
        line_num = 0
        with open(filename) as f:
            for line in f:
                line_num += 1
                result = re.search(meta_regex, line)
                if result is None:
                    print "parsing failed for line %s" % line
                    continue

                found_list = []
                for a_key in keyword:
                    if a_key not in line:
                        continue
                    found_list.append(a_key)

                if not found_list:
                    continue

                meta = result.group(1)
                dt = re.search(parse_date_time_from_meta, meta).group(1)
                event = anevent.AnEvent()
                event.number = line_num
                event.keys = found_list
                event.thread = re.search(extract_thread_from_meta, meta).group(1)
                event.date_time = datetime.datetime.strptime(dt, "%d-%m-%Y %H:%M:%S.%f")
                process_name = re.search(extract_process_name_from_meta, meta).group(1)

                if process_name not in return_value:
                    return_value[process_name] = []

                return_value[process_name].append(event)

        return return_value


class LoggingSourceSample(source.Source):
    """ This class reads a log file and provides input to display engine

    """

    def __init__(self, keyword, filename):
        """

        :param filename:
        """
        self._curr_pos = datetime.datetime.now()
        self._filename = filename
        self._keywords = keyword

    def start_time(self):
        return datetime.datetime.now()

    def get_data(self, **kwargs):
        return Parser.parse(self._keywords, self._filename)


if __name__ == '__main__':
    keywords = ["Error", "Exception", "Fatal", "Warning", "Started", "Finished", "User Actions"]
    log_src = LoggingSourceSample(keywords, "sample.log")
    rv = log_src.get_data()
    for key, value in rv.iteritems():
        for a in value:
            print key + "-" + a.string()
