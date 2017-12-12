class job(object):
    def __init__(self, cmd, datafnames, datatxts):
        self.cmd = cmd
        self.data = {}
        for fname, txt in zip(datafnames, datatxts):
            self.data[fname] = txt
        self.pid = float('Inf')
        self.predecessor = None
        self.est_time = -1.0
        self.write()

    def hash_name(self):
        self._hash_name =

    def write(self):
        with open(os.expanduser('~') + '/.pch/queue', 'a') as f:
            f.write(self.json())

    def sort(self):
        with open(os.expanduser('~') + '/.pch/queue', 'r') as f:
            queuestring = f.read()
        
        with open(os.expanduser('~') + '/.pch/queue', 'w') as f:
            f.write(sortedqueuestring)
