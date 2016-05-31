from tournaments.democracy import Democracy


# @brief    Selects at every branch if taken or not
#           based on the predictors votes
class WeightedDemocracy(Democracy):
    def __init__(self, predictors, name='Weighted Democracy'):
        Democracy.__init__(self, predictors, name)

    # Tie-break = previous guess
    def _select_chosen_guess(self):
        taken = 0
        not_taken = 0
        for predictor in self._predictors:
            if predictor.get_prediction():
                taken += predictor.get_score()
            else:
                not_taken += predictor.get_score()
        if taken > not_taken:
            self._chosen_guess = True
        if taken < not_taken:
            self._chosen_guess = False
        else:
            self._chosen_guess = self._prev
