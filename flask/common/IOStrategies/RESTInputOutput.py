class RESTInputOutput:
    def __init__(self, io):
        self.io = io

    def Input(self, field, defval=None):
        return self.io.json.get(field, defval)

    def Output(self, student):
        print(student)