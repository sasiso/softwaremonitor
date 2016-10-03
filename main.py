from displayengine import displayengine
from input import samplelogparser

meta_regex = "^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6}\s[\w]+\(\d+\))"
parse_date_time_from_meta = "^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6})"
extract_thread_from_meta = "\((\d+)\)$"
extract_process_name_from_meta = "(\w+)\(\d+\)$"

meta_regex_1 = "^(\d\d\d\d-\d{1,2}-\d{1,2}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6}\s\|\s[\w]+)"
parse_date_time_from_meta_1 = "^(\d\d\d\d-\d{1,2}-\d{1,2}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6})"
extract_thread_from_meta_1 = ""
extract_process_name_from_meta_1 = "\| ([\w]+)"


def on_file_open(path):
    keywords = ["ERROR", "WARNING"]
    log_src = samplelogparser.LoggingSourceSample(keywords, path)
    log_src.setregex(meta_regex_1, parse_date_time_from_meta_1, extract_thread_from_meta_1,
                     extract_process_name_from_meta_1)

    log_src.set_date_format("%Y-%m-%d %H:%M:%S.%f")
    engine.register(log_src)


if __name__ == '__main__':
    print "Open a source log file using file open dialog"
    engine = displayengine.DisplayEngine(1000)
    engine.set_file_open_handler(on_file_open)
    """ Register Source with Engine
    """

    engine.start()
