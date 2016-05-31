from predictors.predictor import Predictor


# @brief    Change prediction if three mistakes are made
class Bht3Changes(Predictor):
    def __init__(self):
        Predictor.__init__(self, 'Bht3Changes')

    # States:
    # 0: strongly not taken
    # 1: not taken
    # 2: weakly not taken
    # 3: strongly taken
    # 4: taken
    # 5: weakly taken

    def _prediction(self):
        if self._state in [0, 1, 2]:
            return False
        if self._state in [3, 4, 5]:
            return True

    def _update_state(self, branch_attempt):
        if branch_attempt and self._state == 0:
            self._state = 1
            return
        if branch_attempt and self._state == 1:
            self._state = 2
            return
        if not branch_attempt and self._state == 1:
            self._state = 0
            return
        if branch_attempt and self._state == 2:
            self._state = 3
            return
        if not branch_attempt and self._state == 2:
            self._state = 0
            return
        if not branch_attempt and self._state == 3:
            self._state = 4
            return
        if branch_attempt and self._state == 4:
            self._state = 3
            return
        if not branch_attempt and self._state == 4:
            self._state = 5
            return
        if branch_attempt and self._state == 5:
            self._state = 3
            return
        if not branch_attempt and self._state == 5:
            self._state = 0
