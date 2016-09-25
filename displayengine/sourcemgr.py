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


class SourceManager(object):
    """

    """
    def __init__(self):
        """

        """
        self.sources = {}
        self._index = 0
        pass

    def register_source(self, source):
        """ Register an source with manager

        :param source: input source
        :return: index number of this source, this index can be later used to delete this source
        """
        self._index += 1
        self.sources[self._index] = source

        return self._index

    def delete_source(self, index):
        del self.sources[index]


