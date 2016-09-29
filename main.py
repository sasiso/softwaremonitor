from displayengine import displayengine
from input import samplelogparser

if __name__ == '__main__':

    """
        Create a source
    """
    keywords = ["Error", "Exception", "Fatal", "Warning", "Started", "Finished", "User Actions"]
    log_src = samplelogparser.LoggingSourceSample(keywords, "sample.log")
    """ Create Engine
    """
    engine = displayengine.DisplayEngine()
    """ Register Source with Engine
    """
    engine.register(log_src)
    engine.start()


