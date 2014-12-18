from collective.cover.interfaces import IGridSystem
from collective.cover.layout import Deco16Grid


class Bootstrap3(Deco16Grid):

    ncolumns = 12
    title = u'Bootstrap 3'

    def columns_formatter(self, columns):
        prefix = 'col-md-'
        for column in columns:
            width = column['data']['column-size'] if 'data' in column else 1
            column['class'] = self.column_class + ' ' + (prefix + str(width))

        return columns