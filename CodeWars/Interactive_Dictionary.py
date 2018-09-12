class Dictionary(dict):
    def __init__(self):
        self={} 
    def newentry(self, word, definition):
        self[word] = definition      
    def look(self, key):
        return self[key] if key in self.keys() else "Can\'t find entry for {}".format(key)
