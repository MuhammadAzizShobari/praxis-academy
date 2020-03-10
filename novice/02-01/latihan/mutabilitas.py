def add_bar(items=[]):
    items.append('bar')
    return items

l = add_bar()  # l is ['bar']
l.append('foo')
add_bar() # returns ['bar', 'foo', 'bar']

from collections import namedtuple
VerbTenses = namedtuple('VerbTenses', ['past', 'present', 'future'])
# versus
class VerbTenses(object):
    def __init__(self, past, present, future):
        self.past = past,
        self.present = present
        self.future = future

