class deduction:
    def __init__(self, clause, proof):
        self.clause = clause
        self.proof = proof


list_deduction = []
checked_pair_list=[]

def check_just_AND_operation(clause):
    if '+' in clause or '>' in clause or '=' in clause:
        return False
    return True


def check_just_OR_operation(clause):
    if '.' in clause or '>' in clause or '=' in clause:
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
        else:
            return False


def check_is_negative(clause_A, clause_B):
    if clause_A == clause_B:
        return False
    else:
        clause_A = remove_double_negative(clause_A)
        clause_B = remove_double_negative(clause_B)
        if clause_A == '-{0}'.format(clause_B) or clause_B == '-{0}'.format(clause_A):
            return True
        else:
            return False


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
            list_deduction.append(deduction(clause, 'PR'))
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

                list_deduction.append(deduction(clause_A, 'PRCP'))
                list_deduction.append(
                    deduction(negative_clause(clause_B), 'PRIP'))
            else:
                list_deduction.append(
                    deduction(negative_clause(conclude), 'PRIP'))

            return conclude
        else:
            print('invalid conclude, please input again')


def main():
    amount_premise = input_amount_premise()
    input_list_premise(amount_premise)
    input_conclude()

    for i in list_deduction:
        print('{0}   {1}'.format(i.clause, i.proof))


if __name__ == '__main__':
    main()
