# Tournaments
from tournaments.democracy import Democracy
from tournaments.weighted_democracy import WeightedDemocracy
from tournaments.limited_weighted_democracy import LimitedWeightedDemocracy
from tournaments.highest_score import HighestScore
from tournaments.limited_highest_score import LimitedHighestScore

# Predictors
from predictors.always_not_taken import AlwaysNotTaken
from predictors.always_taken import AlwaysTaken
from predictors.bht_1_bit import Bht1Bit
from predictors.bht_2_bits import Bht2Bits
from predictors.bht_3_changes import Bht3Changes

# Programs
from programs.random import Rand
from programs.modular import Mod
from programs.modular import ModSeq
from programs.search import LinearSearch
from programs.search import BinarySearch
from programs.sorting import BubbleSort
from programs.sorting import InsertionSort
from programs.sorting import QuickSort

# Main

# Predictors list

predictors = list([AlwaysTaken(), AlwaysNotTaken(), Bht1Bit(), Bht2Bits(), Bht3Changes()])

# Tournaments list

MAX_SCORE = 15  # 4 bits
tournaments = list([HighestScore(predictors), Democracy(predictors), WeightedDemocracy(predictors),
                    LimitedHighestScore(predictors, MAX_SCORE), LimitedWeightedDemocracy(predictors, MAX_SCORE)])

# Programs' objects

p_mod = Mod()
p_mod_seq = ModSeq()
p_bubble = BubbleSort()
p_insertion = InsertionSort()
p_quick = QuickSort()
p_lin_search = LinearSearch()
p_bin_search = BinarySearch()

# Program's list

programs = [p_mod, p_mod_seq,                   # Modular
            p_bubble, p_insertion, p_quick,     # Sorting
            p_lin_search, p_bin_search]         # Search

# Parameters for the programs

r = Rand()

size = r.get_number(200, 600)
mod = r.get_number(3, 10)
r.make_vector(size)
pos = (int)((size/2) + (size/4) + (size/8) + (size/16))

# Creation of the Programs

p_mod.get_program(True, mod, size)
p_mod_seq.get_program(True, mod, r.get_vector())
p_bubble.get_program(True, r.get_vector())
p_insertion.get_program(True, r.get_vector())
p_quick.get_program(True, r.get_vector())
p_lin_search.get_program(True, r.get_vector(), r.get_vector()[pos])
p_bin_search.get_program(True, r.get_vector(), r.get_vector()[pos])

for t in tournaments:
    for p in programs:
        print(p.get_name())
        t.run_program(p.get_program())
        t.print_state()
        input()
        t.reset()
