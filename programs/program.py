class Program:
    def __init__(self, name=None):
        if name is None:
            self._Name = 'Unspecified'
        else:
            self._Name = name
        self._program = list()

    def _run(self):
        pass

    def get_program(self, run_new=False):
        pass

    def get_name(self):
        return self._Name

    def _reset(self):
        self._program = list()
