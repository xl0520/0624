import utilities as u

class Search(object):
    test_con = u.get_test_connection()
    def __init__(self, title=['No Title Provided'], description=['No Description Provided']):
        self._df = None
        self._df_historical = None
        self._databases_needed = None
        self.title = title
        self.description = description


