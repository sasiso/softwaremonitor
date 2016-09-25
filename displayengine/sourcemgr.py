"""
this class managers all the sources
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


