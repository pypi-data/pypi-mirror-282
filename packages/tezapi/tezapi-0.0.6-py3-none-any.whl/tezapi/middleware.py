class Middleware:
    def __init__(self, route, path, method):
        self.route = route
        self.path = path
        self.method = method
