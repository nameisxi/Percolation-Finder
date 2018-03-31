class Site(object):
    def __init__(self, name, width, height, connected):
        self.name = name
        self.width = width
        self.height = height
        self.connected = connected

    def getName(self):
        return self.name

    def connectSite(self):
        self.connected = True
