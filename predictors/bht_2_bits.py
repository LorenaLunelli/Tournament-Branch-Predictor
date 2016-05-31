from predictors.predictor import Predictor


# @brief    Change state if two mistakes are made
class Bht2Bits(Predictor):
    def __init__(self):
        Predictor.__init__(self, 'Bht2Bits')

    # States:
    # 0: strongly not taken
    # 1: weakly not taken
    # 2: weakly taken
    # 3: strongly taken

    def _prediction(self):
        if self._state == 0 or self._state == 1:
            # print '0 - 1'
            return False
        if self._state == 2 or self._state == 3:
            # print '1 - 0'
            return True

    def _update_state(self, branch_attempt):
        if branch_attempt and self._state == 0:
            # print '0 - 1'
            self._state = 1
            return
        if branch_attempt and self._state == 1:
            # print '1 - 3'
            self._state = 3
            return
        if branch_attempt and self._state == 2:
            # print '2 - 3'
            self._state = 3
            return
        if not branch_attempt and self._state == 1:
            # print '1 - 0'
            self._state = 0
            return
        if not branch_attempt and self._state == 3:
            # print '3 - 2'
            self._state = 2
            return
        if not branch_attempt and self._state == 2:
            # print '2 - 0'
            self._state = 0
