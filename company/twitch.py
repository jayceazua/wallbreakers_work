

#
# Your previous JavaScript content is preserved below:
#
# // We'll be building a simple EventEmitter class today that someone
# // could use to register callback functions to specific events and
# // then trigger those callbacks when the relevant event is emitted.
#
# // Example usage:
# // const e = new EventEmitter();
# // e.on('foo', () => console.log('got some apples!'));
# // e.emit('foo'); // the console should log 'got some apples!'
#
# // Step 1 - Single Callback
# class EventEmitter {
#     constructor() {

#     }
#
#     on(event, callback) {
#       callback()
#     }
#
#     emit(event) {
#       this
#     }
# }
#
# const e = new EventEmitter();
# e.on('foo', () => console.log('got some apples!'));
# e.emit('foo'); // should print 'got some apples'


from collections import defaultdict


class EventEmitter:
    def __init__(self):
        self.events = defaultdict(set)

    def on(self, event, callback):
        self.events[event].add(callback)

    def once(self, event, callback):
        pass

    def emit(self, event):

        if event in self.events:

            for callback in self.events[event]:
                callback()
        else:
            print(f"Please create it first, before calling {event}")


e = EventEmitter()

# // part 2

# const e1 = new EventEmitter();
# e.on('foo', lambda: print('got some apples 1'))
# e.on('bar', lambda: print('got some apples 2'))
# e.on('foo2', lambda: print('got some apples 3'))
# e.on('foo4', lambda: print('got some apples 4'))
# e.on('foo5', lambda: print('got some apples 5'))

# e.emit('foo')
# e.emit('foo4')
# e.emit('foo2')
# e.emit('bar')
# e.emit('foo5')


def c(): return print('got some apples 1')


t = set()
t.add(c)
t.add(c)
print(t)
# step 3 Try once
# const e = new EventEmitter();
# const c = () => console.log('nice!');
# const c1 = () => console.log('nice work!');
# e.once('bar', c);
# e.once('bar', c);
# e.once('bar', c);
# e.once('bar', c);
# e.once('bar', c1);
# e.once('bar', c1);
# e.emit('bar'); // only print nice once, and nice work once
