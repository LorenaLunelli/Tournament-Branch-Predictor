from predictors.predictor import Predictor


# @brief    Always predict branch as taken
class AlwaysTaken(Predictor):
    def __init__(self):
        Predictor.__init__(self, 'AlwaysTaken')

    def _prediction(self):
        return True
