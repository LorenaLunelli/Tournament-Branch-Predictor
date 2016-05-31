from tournaments.tournament import Tournament


# @brief    Selects at every branch if taken or not
#           based on the predictors votes
class Democracy(Tournament):
    def __init__(self, predictors, name='Democracy'):
        Tournament.__init__(self, predictors, name)
        self._chosen_guess = False
        self._prev = False

    def run_program(self, program):
        for instruction in program:
            for predictor in self._predictors:
                predictor.make_prediction(instruction)
            self._total_guesses += 1
            self._select_chosen_guess()
            if self._chosen_guess == instruction:
                self._right_guesses += 1
            self._prev = instruction

    # Tie-break = previous guess
    def _select_chosen_guess(self):
        taken = 0
        not_taken = 0
        for predictor in self._predictors:
            if predictor.get_prediction():
                taken += 1
            else:
                not_taken += 1
        if taken > not_taken:
            self._chosen_guess = True
        if taken < not_taken:
            self._chosen_guess = False
        else:
            self._chosen_guess = self._prev

    def print_state(self):
        print('\n{0} Tournament'.format(self.get_tournament_name()))
        print('{0}/{1} right guesses'.format(self._right_guesses, self._total_guesses))
        print('--------------------')
        for predictor in self._predictors:
            print('{0}: {1} points'.format(predictor.get_name(), predictor.get_score()))
        print('\n')
