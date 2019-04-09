import re
import math


class deduction:
    def __init__(self, clause, proof):
        self.clause = clause
        self.proof = proof


list_deduction = []
checked_pair_list = []
proved = 0


def check_clause_B_is_sub_clause_A_AND(clause_A, clause_B):
    if len(clause_B) > len(clause_A):
        return False

    list_clause_A_AND = clause_A.split('.')
    list_clause_B_AND = clause_B.split('.')

    is_equal = 1
    for i in list_clause_B_AND:
        if i not in list_clause_A_AND:
            is_equal = 0
            break
    if is_equal == 1:
        return True

    return False


def check_clause_B_is_sub_clause_A_OR(clause_A, clause_B):
    if len(clause_B) > len(clause_A):
        return False

    list_clause_A_OR = clause_A.split('+')
    list_clause_B_OR = clause_B.split('+')

    is_equal = 1
    for j in list_clause_B_OR:
        if j not in list_clause_A_OR:
            is_equal = 0
            break
    if is_equal == 1:
        return True

    return False


def check_clause_B_is_EQ_clause_A(clause_A, clause_B):
    if len(clause_B) != len(clause_A):
        return False
    else:
        return check_clause_B_is_sub_clause_A_AND(clause_A, clause_B) or check_clause_B_is_sub_clause_A_OR(clause_A, clause_B)


def nCr(n, r):
    fac = math.factorial
    return fac(n) // fac(r) // fac(n-r)


def negative_clause(clause):

    if len(clause) < 3:
        return '-{0}'.format(clause)
    else:
        return '-({0})'.format(clause)


def check_valid_syntax(clause):
    for char in clause:
        if(char < 'A' or char > 'Z'):
            if(char != '(' and char != ')' and char != '-' and char != '.'
               and char != '+' and char != '>' and char != '='):
                return False
    return True


def check_just_AND_operation(clause):
    if '+' in clause or '>' in clause or '=' in clause:
        return False
    return True


def check_just_OR_operation(clause):
    if '.' in clause or '>' in clause or '=' in clause:
        return False
    return True


def check_non_operation(clause):
    if '.' in clause or '>' in clause or '=' in clause or '+' in clause:
        return False
    return True


def remove_double_negative(clause):
    while('--' in clause):
        idx = re.search('--', clause).start()
        clause = clause[:idx]+clause[idx+2:]
    return clause


def check_is_equal(clause_A, clause_B):
    if clause_A == clause_B:
        return True
    else:
        clause_A = remove_double_negative(clause_A)
        clause_B = remove_double_negative(clause_B)
        if clause_A == clause_B:
            return True
    return False


def check_is_negative(clause_A, clause_B):
    if clause_A == clause_B:
        return False
    else:
        clause_A = remove_double_negative(clause_A)
        clause_B = remove_double_negative(clause_B)
        if clause_A == '-{0}'.format(clause_B) or clause_B == '-{0}'.format(clause_A):
            return True
    return False


def append_deduction_list(clause, proof):
    for i in range(len(list_deduction)):
        if clause == list_deduction[i].proof:
            return
    print('{0}    {1}            {2}'.format(
        len(list_deduction), clause, proof))
    list_deduction.append(deduction(clause, proof))


def input_amount_premise():
    while(1):
        amount_premise = int(input('enter amount of premise : '))
        if (amount_premise <= 0):
            print('invalid number')
        else:
            return amount_premise


def input_list_premise(amount_premise):

    while(len(list_deduction) < amount_premise):
        clause = input('input premise {0} : '.format(len(list_deduction)+1))
        clause = clause.replace(' ', '')

        if(check_valid_syntax(clause) == True):
            append_deduction_list(clause, 'PR')
        else:
            print('invalid clause, please input again')


def input_conclude():
    while(1):
        conclude = input('input conclude : ')

        if(check_valid_syntax(conclude) == True):
            if '>' in conclude:
                idx = conclude.index('>')
                clause_A = conclude[:idx]
                clause_B = conclude[idx+1:]

                append_deduction_list(clause_A, 'PRCP')
                append_deduction_list(clause_B, 'PRIP')
            else:
                append_deduction_list(negative_clause(conclude), 'PRIP')

            return conclude
        else:
            print('invalid conclude, please input again')


def implement_CON_rule(clause_A, clause_B, idx_A, idx_B):
    clause_X = '{0}.{1}'.format(clause_A, clause_B)
    prove_X = 'CON {0} {1}'.format(idx_A, idx_B)
    append_deduction_list(clause_X, prove_X)


def implement_DS_rule(clause_A, clause_B, idx_A, idx_B):
    if len(clause_A) < len(clause_B):
        clause_A, clause_B = clause_B, clause_A
    list_element_A = clause_A.split('+')

    for i in range(len(list_element_A)):
        if check_is_negative(clause_B, list_element_A[i]):
            list_element_A.pop(i)
            clause_X = '+'.join(list_element_A)
            prove_X = 'DS {0} {1}'.format(idx_A, idx_B)
            append_deduction_list(clause_X, prove_X)
            break


def check_HS_rule(clause_A, clause_B, idx_A, idx_B):
    list_A = clause_A.split('>')
    list_B = clause_B.split('>')

    if list_A[1] == list_B[0]:
        append_deduction_list(
            list_A[0]+'>'+list_B[1], 'HS {0} {1}'.format(idx_A, idx_B))
    elif list_B[1] == list_A[0]:
        append_deduction_list(
            list_B[0]+'>'+list_A[1], 'HS {0} {1}'.format(idx_A, idx_B))


def natural_deduction(clause_A, clause_B, idx_A, idx_B):
    if '>' in clause_A and '>' in clause_B:
        check_HS_rule(clause_A, clause_B, idx_A, idx_B)

    elif '>' in clause_A or '>' in clause_B:
        if '>' in clause_B:
            clause_A, clause_B = clause_B, clause_A
            idx_A, idx_B = idx_B, idx_A

        left_clause_A = clause_A.split('>')[0]
        right_clause_A = clause_A.split('>')[1]

        if check_is_equal(left_clause_A, clause_B):
            append_deduction_list(
                right_clause_A, 'MP {0} {1}'.format(idx_A, idx_B))
        elif check_is_negative(right_clause_A, clause_B):
            append_deduction_list(
                '-{0}'.format(left_clause_A), 'MT {0} {1}'.format(idx_A, idx_B))
        else:
            if len(left_clause_A) == len(clause_B):
                if check_clause_B_is_EQ_clause_A(left_clause_A, clause_B):
                    append_deduction_list(
                        left_clause_A, 'EQ {0}'.format(idx_B))
            elif len(left_clause_A) < len(clause_B):
                if check_clause_B_is_sub_clause_A_AND(clause_B, left_clause_A):
                    append_deduction_list(
                        left_clause_A, 'SIM {0}'.format(idx_B))
            else:
                if check_clause_B_is_sub_clause_A_OR(left_clause_A, clause_B):
                    append_deduction_list(
                        left_clause_A, 'ADD {0}'.format(idx_B))


def check_all_pair():
    for i in range(len(list_deduction)-1):
        for j in range(i+1, len(list_deduction)):
            if '{0} {1}'.format(i, j) not in checked_pair_list:
                checked_pair_list.append('{0} {1}'.format(i, j))
                natural_deduction(
                    list_deduction[i].clause, list_deduction[j].clause, i, j)

                # check proved or not
            for k in range(len(list_deduction)-1):
                if check_is_negative(list_deduction[-1].clause, list_deduction[k].clause):
                    implement_CON_rule(
                        list_deduction[-1].clause, list_deduction[k].clause, len(list_deduction)-1, k)
                    append_deduction_list(
                        '0', 'EQ {0}'.format(len(list_deduction)-1))
                    global proved
                    proved = 1
                    print('end')
                    return


def main():
    amount_premise = input_amount_premise()
    input_list_premise(amount_premise)
    input_conclude()

    while(1):
        if proved == 1 or nCr(len(list_deduction), 2) == len(checked_pair_list):
            break
        check_all_pair()

    for i in range(len(list_deduction)):
        print('{0}    {1}            {2}'.format(
            i, list_deduction[i].clause, list_deduction[i].proof))


if __name__ == '__main__':
    main()
