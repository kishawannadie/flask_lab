class Handler:
    def __init__(self):
        self.handlers=dict()
    
    def set_handler(self, command):
        def decorator_set_handler(handler):
            self.handlers[command] = handler
            return handler
        return decorator_set_handler
    
    def handle(self, command, data):
        if command in self.handlers: 
            return self.handlers[command](data)