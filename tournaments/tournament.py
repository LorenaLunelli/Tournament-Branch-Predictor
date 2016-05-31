from predictors.predictor import Predictor


# Tournament class
class Tournament:
    def __init__(self, predictors, name='DefaultTournament'):
        assert isinstance(predictors, list)
        assert isinstance(predictors[0], Predictor)
        self._predictors = predictors
        self._name = name
        self._right_guesses = 0
        self._total_guesses = 0

    def get_tournament_name(self):
        return self._name

    def run_program(self, program):
        pass

    def print_state(self):
        pass

    # @brief    This method returns the desired data to the respective plots
    def get_state_to_plot(self):
        data = [(p.get_name(), p.get_right_guesses()) for p in self._predictors]
        data.append(('Right guesses', self._right_guesses))

        return data

    def get_total_guesses(self):
        return self._total_guesses

    def reset(self):
        for predictor in self._predictors:
            predictor.clean()
            self._right_guesses = 0
            self._total_guesses = 0
