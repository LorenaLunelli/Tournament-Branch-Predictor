# Predictor class
class Predictor:
    def __init__(self, name=None):
        if name is None:
            self._name = 'Unspecified'
        else:
            self._name = name
        self._state = 0
        self._score = 0
        self._right_guesses = 0

    def get_name(self):
        return self._name

    # Returns the prediction
    def _prediction(self):
        pass

    # Updates the predictor state
    def _update_state(self, branch_attempt):
        pass

    # Increases the predictor score
    def _increase_score(self):
        self._score += 1

    # Decreases the predictor score
    def _decrease_score(self):
        if self._score > 0:
            self._score -= 1

    # Returns the prediction and makes the necessary changes
    def make_prediction(self, branch_attempt, limited_increase=False, max_score=0, penalty=False):
        result = self._prediction()
        if result == branch_attempt:
            # Increase right guesses value, to avoid penalty for limited cases. (Useful for plotting)
            self._right_guesses += 1
            if not limited_increase or self._score < max_score:
                self._increase_score()
        else:
            if penalty:
                self._decrease_score()
        self._update_state(branch_attempt)
        return result

    # Just get the prediction, without updating state or score
    def get_prediction(self):
        return self._prediction()

    def get_score(self):
        return self._score

    def get_right_guesses(self):
        return self._right_guesses

    def clean(self):
        self._score = 0
        self._right_guesses = 0
        self._state = 0
