class DictIO:
    def setSource(self, source):
        self.source = source
    
    def Input(self, field, title=None, default=None):
        return self.source.get(field, default)

    def Output(self, item):
        return item.getData()
    