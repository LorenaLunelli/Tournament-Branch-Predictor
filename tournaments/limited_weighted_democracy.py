from tournaments.weighted_democracy import WeightedDemocracy


# @brief    Selects at every branch if taken or not
#           based on the predictors votes
class LimitedWeightedDemocracy(WeightedDemocracy):
    def __init__(self, predictors, max_score=31, name='Limited Weighted Democracy'):
        WeightedDemocracy.__init__(self, predictors, name)
        self._MAX_SCORE = max_score

    def run_program(self, program):
        for instruction in program:
            for predictor in self._predictors:
                # passing limited_increase=True, the maximum score for the predictors
                # and penalty=True to indicate mistakes are punished
                predictor.make_prediction(instruction, True, self._MAX_SCORE, True)
            self._total_guesses += 1
            self._select_chosen_guess()
            if self._chosen_guess == instruction:
                self._right_guesses += 1
            self._prev = instruction
