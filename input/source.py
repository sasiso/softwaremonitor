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
        return datetime.datetime.now()

    def end_time(self):
        """

        :return:  Return Start Time of this soruce
        """
        return datetime.datetime.now()

    def render_start_date(self):
        pass

    def render_end_date(self):
        pass


    def get_data(self, zoom=1, recenter=0):
        """ returns data from given interval

        :param zoom:
        :param left:
        :param right:

        :return:
        """
        pass

    def getpos(self, an_event):
        pass
