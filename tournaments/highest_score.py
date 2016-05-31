from tournaments.tournament import Tournament


# @brief    Selects at every branch which predictor
#           has the right (highest score) to decide if taken or not
class HighestScore(Tournament):
    def __init__(self, predictors, name='Highest Score'):
        Tournament.__init__(self, predictors, name)
        self._chosen = predictors[0]

    def run_program(self, program):
        for instruction in program:
            self._total_guesses += 1
            result = self._chosen.get_prediction()
            if result == instruction:
                    self._right_guesses += 1

            for predictor in self._predictors:
                predictor.make_prediction(instruction)

            # Update at the end of each instruction
            self._select_chosen()

    def _select_chosen(self):
        for predictor in self._predictors:
            if predictor.get_score() > self._chosen.get_score():
                self._chosen = predictor

    def print_chosen_and_score(self):
        print('{0}: {1}'.format(self._chosen.get_name(), self._chosen.get_score()))

    def print_state(self):
        print('\n{0} Tournament'.format(self.get_tournament_name()))
        print('[Chosen] {0}: {1} points'.format(self._chosen.get_name(), self._chosen.get_score()))
        print('{0}/{1} right guesses'.format(self._right_guesses, self._total_guesses))
        print('--------------------')
        for predictor in self._predictors:
            print('{0}: {1} points'.format(predictor.get_name(), predictor.get_score()))
        print('\n')
