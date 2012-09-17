from wtforms import TextField
from invenio.sherpa_romeo import SherpaRomeoSearch, SherpaRomeoXMLParser

__all__ = ['JournalField']

class JournalField(TextField):

    def __init__(self, name, **kwargs):
        super(JournalField, self).__init__(name, **kwargs)

    def pre_validate(self):
        return dict(error=0, errorMessage='')

    def autocomplete(self):
        value = self.data

        s = SherpaRomeoSearch()
        response = s.searchTitle(value)
        return response
