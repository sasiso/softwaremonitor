"""
Copyright [2016] [Satbir Singh]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
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



