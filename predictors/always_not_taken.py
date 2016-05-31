from predictors.predictor import Predictor


# @brief    Always predict branch as not taken
class AlwaysNotTaken(Predictor):
    def __init__(self):
        Predictor.__init__(self, 'AlwaysNotTaken')

    def _prediction(self):
        return False
