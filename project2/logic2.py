# +---------+---------+---------+-------+
# |Priority |Operator |IO Symbol|Read as|
# +---------+---------+---------+-------+
# |    1    |    ¬    |    -    |  not  |
# |    2    |    ∧    |    .    |  and  |
# |    3    |    ∨    |    +    |  or   |
# |    4    |    →    |    >    |  if   |
# |    5    |    ↔    |    =    |  only |
# +---------+---------+---------+-------+

import re
import math

# (pv-q)^(pvr)
input = [{("p", True), ("q", False)}, {("p", True), ("r", True)}]

def is_valid_input(string):
    if re.match("^[a-zA-Z\s\-.+>=()]*$", string):
        return True
    else:
        return False

def strip_spaces(string):
    return re.sub(r'\s+', '', string)

#def notation_to_list(propositional_notation):
#    for i in notation
#    return propositional_list

def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]
 
def dpll(cnf, assignments={}):
 
    if len(cnf) == 0:
        return True, assignments
 
    if any([len(c)==0 for c in cnf]):
        return False, None
    
    l = __select_literal(cnf)
 
    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals
         
    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals
 
    return False, None

def random_kcnf(n_literals, n_conjuncts, k=3):
    result = []
    for _ in range(n_conjuncts):
        conj = set()
        for _ in range(k):
            index = random.randint(0, n_literals)
            conj.add((
                str(index).rjust(10, '0'),
                bool(random.randint(0,2)),
            ))
        result.append(conj)
    return result

input_string="hello tao ten khue"
if is_valid_input(input_string):
    print(strip_spaces(input_string))
