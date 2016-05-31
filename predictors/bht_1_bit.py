from predictors.predictor import Predictor


# @brief    Change state if a mistake is made
class Bht1Bit(Predictor):
    def __init__(self):
        Predictor.__init__(self, 'Bht1Bit')
    # States:
    # 0: predict not taken
    # 1: predict taken

    def _prediction(self):
        if self._state == 0:
            return False
        if self._state == 1:
            return True

    def _update_state(self, branch_attempt):
        if not branch_attempt:
            self._state = False
        else:
            self._state = True
