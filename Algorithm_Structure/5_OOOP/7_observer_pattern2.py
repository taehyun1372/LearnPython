class SubscriberOne(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0} {1}".format(self.name, message))

class SubscriberTwo(object):
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print("{0} {1}".format(self.name, message))

class Publisher(object):
    def __init__(self):
        self.subscribers = set()

    def register(self, callback):
        self.subscribers.add(callback)

    def unregister(self, callback):
        self.subscribers.discard(callback)

    def dispatch(self, message):
        for callback in self.subscribers:
            callback(message)


if __name__ == "__main__":
    pub = Publisher()

    astin = SubscriberOne("Astin")
    james = SubscriberOne("James")
    jeff = SubscriberTwo("Jeff")

    pub.register(astin.update)
    pub.register(james.update)
    pub.register(jeff.receive)

    pub.dispatch("It's lunch time")
    pub.unregister(jeff.receive)
    pub.dispatch("Finished")