from programs.program import Program


class Modular(Program):
    def __init__(self, name):
        Program.__init__(self, name)


class Mod(Modular):
    def __init__(self):
        Modular.__init__(self, 'Mod')

    def _run(self, mod=0, size=0):
        self._reset()
        for n in range(size):
            self._program.append(True)
            if n % mod == 0:
                self._program.append(True)
            else:
                self._program.append(False)
        self._program.append(False)

    def get_program(self, run_new=False, mod=0, size=0):
        if run_new:
            self._run(mod, size)
        return self._program


class ModSeq(Modular):
    def __init__(self):
        Modular.__init__(self, 'Mod in Vector')

    def _run(self, mod=0, vec=None):
        self._reset()
        if not vec:
            vec = []
        for n in vec:
            self._program.append(True)
            if n % mod == 0:
                self._program.append(True)
            else:
                self._program.append(False)
        self._program.append(False)

    def get_program(self, run_new=False, mod=0, vec=None):
        if not vec:
            vec = []
        if run_new:
            self._run(mod, vec)
        return self._program
