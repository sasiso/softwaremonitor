"""

Format: 21-12-2014 21:22:59.0000 Process(12).
        DD-MM-YYYY HH:MM:SS.mmmm Process(thradid) Message

"""

meta_regex='^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6}\s[\w]+\(\d+\)'
parse_date_time_from_meta='^(\d\d{1,2}-\d\d{1,2}-\d\d{1,4}\s\d\d{1,2}:\d\d{1,2}:\d\d{1,2}.\d{1,6}\s)'
extract_treadid_from_meta='\((\d+)\)$'