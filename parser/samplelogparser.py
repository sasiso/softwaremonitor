"""

Format: 21-12-2014 21:22:59.0000 Process(12).
        DD-MM-YYYY HH:MM:SS.mmmm Process(thradid) Message

"""
import re

meta_regex = "^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6}\s[\w]+\(\d+\))"
parse_date_time_from_meta = "^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6})"
extract_thread_from_meta = "\((\d+)\)$"
extract_process_name_from_meta = "(\w+)\(\d+\)$"


class Parser(object):
    def __init__(self):
        pass

    @staticmethod
    def parse(filename):
        with open(filename) as f:
            for line in f:
                print line
                meta = re.search(meta_regex, line).group(1)
                print "meta: " + meta

                print re.search(parse_date_time_from_meta, meta).group(1)
                print re.search(extract_thread_from_meta, meta).group(1)
                print re.search(extract_process_name_from_meta, meta).group(1)


if __name__ == '__main__':
    Parser.parse("/home/satbir/softwaremonitor/trunk/parser/sample.log")




