# +---------+---------+---------+-------------+
# |Priority |Operator |IO Symbol| Name        |
# +---------+---------+---------+-------------+
# |    1    |    ¬    |    -    | negation    |
# |    2    |    ∧    |    .    | conjunction |
# |    3    |    ∨    |    +    | disjunction |
# |    4    |    →    |    >    | implication |
# |    5    |    ↔    |    =    | equivalence |
# +---------+---------+---------+-------------+

import re
import math

def is_valid_input(input_string):
    if re.match("^[a-zA-Z\s\-.+>=()]*$", input_string):
        return True
    else:
        print("Invalid syntax")
        return False

def strip_spaces(input_string):
    return re.sub(r'\s+', '', input_string)

def print_underline(string):
        print('\033[4m' + string + '\033[0m')

def enum(**enums):
    return type('Enum', (), enums)
    conn = enum(ONLY = "only", IF="if", AND="and", OR='or' , NOT = "not")

def eliminate_implications():
    # Input:  (A ∨ B) → (¬B ∧ A)
    # Output: (¬A ∨ ¬B) ∧ ¬B ∧ (¬B ∨ A)

def to_cnf(string):
    if is_instance(s, str): s = expr(s)
    string = eliminate_implications(s) # Steps 1, 2 from p. 215
    string = move_not_inwards(s) # Step 3
    return distribute_and_over_or(s) # Step 4

input_string="(A +B) > C.D"
if is_valid_input(input_string):
    print_underline(strip_spaces(input_string))
