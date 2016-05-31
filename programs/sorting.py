from programs.program import Program


class Sort(Program):
    def __init__(self, name):
        Program.__init__(self, name)

    def _run(self, vec=None):
        pass

    def get_program(self, run_new=False, vec=None):
        if run_new:
            if not vec:
                vec = []
            self._run(vec)
        return self._program


class BubbleSort(Sort):
    def __init__(self):
        Sort.__init__(self, 'Bubble Sort')

    def _run(self, vec=None):
        self._reset()

        if not vec:
            vec = []
        for i in range(0, len(vec) - 1):
            self._program.append(True)
            for j in range(0, len(vec) - 1 - i):
                self._program.append(True)
                if vec[j] > vec[j + 1]:
                    self._program.append(True)
                    vec[j], vec[j + 1] = vec[j + 1], vec[j]
                else:
                    self._program.append(False)
            self._program.append(False)
        self._program.append(False)


class InsertionSort(Sort):
    def __init__(self):
        Sort.__init__(self, 'Insertion Sort')

    def _run(self, vec=None):
        self._reset()

        if not vec:
            vec = []
        for index in range(1, len(vec)):
            self._program.append(True)
            current = vec[index]
            pos = index

            while pos > 0 and vec[pos - 1] > current:
                self._program.append(True)
                vec[pos], pos = vec[pos - 1], pos - 1
            self._program.append(False)

            vec[pos] = current
        self._program.append(False)


class QuickSort(Sort):
    def __init__(self):
        Program.__init__(self, 'Quick Sort')

    def __partition(self, vec, first, last):
        pivot = vec[first]
        left_mark = first + 1
        right_mark = last
        done = False

        while not done:
            self._program.append(True)
            while left_mark <= right_mark and vec[left_mark] <= pivot:
                self._program.append(True)
                left_mark += 1
            self._program.append(False)

            while vec[right_mark] >= pivot and right_mark >= left_mark:
                self._program.append(True)
                right_mark -= 1
            self._program.append(False)

            if right_mark < left_mark:
                self._program.append(True)
                done = True

            else:
                self._program.append(False)
                vec[left_mark], vec[right_mark] = vec[right_mark], vec[left_mark]
        self._program.append(False)
        vec[first], vec[right_mark] = vec[right_mark], vec[first]
        return right_mark

    def __quick_sort(self, vec, first, last):
        if first < last:
            self._program.append(True)
            split = self.__partition(vec, first, last)

            self.__quick_sort(vec, first, split - 1)
            self.__quick_sort(vec, split + 1, last)
        else:
            self._program.append(False)

    def _run(self, vec=None):
        if not vec:
            vec = []
        self._reset()
        self.__quick_sort(vec, 0, len(vec) - 1)
