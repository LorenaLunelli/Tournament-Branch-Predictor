from programs.program import Program


class Search(Program):
    def __init__(self, name):
        Program.__init__(self, name)

    def _run(self, vec=None, item=None):
        pass

    def get_program(self, run_new=False, vec=None, item=None):
        if not vec:
            vec = []
        if run_new:
            self._run(vec, item)
        return self._program


class LinearSearch(Search):
    def __init__(self):
        Search.__init__(self, 'Linear Search')

    def _run(self, vec=None, item=None):
        self._reset()

        if not vec:
            vec = []
        vec.sort()

        pos = 0
        found = False
        vec_size = len(vec)
        while (pos < vec_size) and (not found) and not (vec[pos] > item):
            self._program.append(True)
            if vec[pos] == item:
                self._program.append(True)
                found = True
            else:
                self._program.append(False)
                pos += 1
        self._program.append(False)


class BinarySearch(Search):
    def __init__(self):
        Search.__init__(self, 'Binary Search')

    def _run(self, vec=None, item=None):
        self._reset()

        if not vec:
            vec = []
        vec.sort()

        first = 0
        last = len(vec) - 1
        found = False
        while not found:
            self._program.append(True)
            if last < first:
                self._program.append(True)
                continue
            self._program.append(False)
            middle = (first + last) // 2
            if vec[middle] < item:
                self._program.append(True)
                first += 1
            elif vec[middle] > item:
                self._program.append(False)
                self._program.append(True)
                last -= 1
            else:
                self._program.append(False)
                found = True
