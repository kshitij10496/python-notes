class Stack(object):

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = list(items)

    def __repr__(self):
        return 'Stack({!r})'.format(self.items)
