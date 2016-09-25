from displayengine import displayengine
from input import loggingsourcesample

if __name__ == '__main__':

    """
        Create a source
    """
    log_src = loggingsourcesample.LoggingSourceSample("test.txt")
    """ Create Engine
    """
    engine = displayengine.DisplayEngine()
    """ Register Source with Engine
    """
    engine.register(log_src)


