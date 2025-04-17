class DictIO:
    def Input(self, field, title, default=None):
        return self.source.get(field, default)

    def Output(self, item):
        return item.getData()
    