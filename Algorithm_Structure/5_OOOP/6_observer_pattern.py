class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0} {1}".format(self.name, message))


class Publisher(object):
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

if __name__ == "__main__":
    pub = Publisher()

    astin = Subscriber("Astin")
    james = Subscriber("James")
    jeff = Subscriber("Jeff")

    pub.register(astin)
    pub.register(james)
    pub.register(jeff)

    pub.dispatch("It's lunch time")
    pub.unregister(jeff)
    pub.dispatch("Finish")