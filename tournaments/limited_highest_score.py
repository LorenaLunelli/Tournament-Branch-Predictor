from tournaments.highest_score import HighestScore


# @brief    Selects at every branch which predictor
#           has the right (highest score) to decide if taken or not
class LimitedHighestScore(HighestScore):
    def __init__(self, predictors, max_score=31, name='Limited Highest Score'):
        HighestScore.__init__(self, predictors, name)
        self._MAX_SCORE = max_score

    def run_program(self, program):
        for instruction in program:
            self._total_guesses += 1
            result = self._chosen.get_prediction()
            if result == instruction:
                    self._right_guesses += 1

            for predictor in self._predictors:
                # passing limited_increase=True and the maximum score for the predictors
                # and penalty=True to indicate mistakes are punished
                predictor.make_prediction(instruction, True, self._MAX_SCORE, True)

            # Update at the end of each instruction
            self._select_chosen()
