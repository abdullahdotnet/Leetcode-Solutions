class DEqueue:
    def __init__(self):
        self.DEqueue = []

    def enqueueF(self,elem):
        self.DEqueue.insert(0,elem)
    def enqueueR(self,elem):
        self.DEqueue.append(elem)
    def dequeueF(self):
        self.DEqueue.pop(0)
    def dequeueR(self):
        self.DEqueue.pop()