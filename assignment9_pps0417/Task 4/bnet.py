import sys
from copy import deepcopy


class BayesianNetwork(object):
    def __init__(self):
        self.B = 0.001
        self.E = 0.002
        self.A_B_E = 0.95
        self.A_B_not_E = 0.94
        self.A_not_B_E = 0.29
        self.A_not_B_not_E = 0.001
        self.J_A = 0.90
        self.J_not_A = 0.05
        self.M_A = 0.70
        self.M_not_A = 0.01

    def calc_input(self, argv, truthVal, input_len, C1, C2, given):
        for count in range(1,input_len):
            if argv[count][0] == 'g':
                given = True
            elif argv[count][0] == 'B':
                if not given:
                    if argv[count][1] == 't':
                        truthVal['b'] = 1
                    C1.append('B')
                elif given:
                    if argv[count][1] == 't':
                        truthVal['b'] = 1
                    C1.append('B')
                    C2.append('B')
            elif argv[count][0] == 'E':
                if not given:
                    if argv[count][1] == 't':
                        truthVal['e'] = 1
                    C1.append('E')
                elif given:
                    if argv[count][1] == 't':
                        truthVal['e'] = 1
                    C1.append('E')
                    C2.append('E')
            elif argv[count][0] == 'A':
                if not given:
                    if argv[count][1] == 't':
                        truthVal['a'] = 1
                    C1.append('A')
                elif given:
                    if argv[count][1] == 't':
                        truthVal['a'] = 1
                    C1.append('A')
                    C2.append('A')
            elif argv[count][0] == 'J':
                if not given:
                    if argv[count][1] == 't':
                        truthVal['j'] = 1
                    C1.append('J')
                elif given:
                    if argv[count][1] == 't':
                        truthVal['j'] = 1
                    C1.append('J')
                    C2.append('J')
            elif argv[count][0] == 'M':
                if not given:
                    if argv[count][1] == 't':
                        truthVal['m'] = 1
                    C1.append('M')
                elif given:
                    if argv[count][1] == 't':
                        truthVal['m'] = 1
                    C1.append('M')
                    C2.append('M')

    def append_items(self, totalElements,numMissing,denomMissing,numPart,denoPart):
        for item in totalElements:
            if item not in numPart:
                numMissing.append(item)
            if item not in denoPart:
                denomMissing.append(item)

    def computeProbability(self, numPart, denoPart, truthVal):
        Total_Elements = ['B', 'E', 'A', 'J', 'M']
        Missing_Nums = []
        Missing_Dens = []
        self.append_items(Total_Elements, Missing_Nums, Missing_Dens, numPart, denoPart)

        numpartsum = self.Total_prob(numPart, truthVal, Missing_Nums)
        if len(denoPart) >= 1:
            denpartsum = self.Total_prob(denoPart, truthVal, Missing_Dens)
            print("P( %s | %s) = %2.12f" % (numPart, denoPart, (numpartsum / denpartsum)))
        else:
            print("P( %s ) = %2.12f" % (numPart, numpartsum))

    def Total_prob(self, part, truthVal, missingElements):
        total = 0.0
        if len(part) == 5:
            total = self.calculate(part, truthVal)
        else:
            item = missingElements.pop()
            pending_missing_elements = deepcopy(missingElements)
            pending_missing_elements1 = deepcopy(missingElements)
            part1 = deepcopy(part)
            part2 = deepcopy(part)
            part1.append(item)
            part2.append(item)
            total = self.Total_prob(part1, self.Update_Truth_Vals(truthVal, item, True), pending_missing_elements) + self.Total_prob(part2, self.Update_Truth_Vals(truthVal, item, False), pending_missing_elements1)

        return total

    def Update_Truth_Vals(self, truthVal, item, Boolean_Val):
        if Boolean_Val == True:
            truthVal[item.lower()] = 1
        else:
            truthVal[item.lower()] = 0
        return truthVal

    # Compute probability.
    def calculate(self, part, Truth_Vals):
        b = e = a = j = m = 0.0

        if Truth_Vals['b'] == 1:
            b = self.B
        elif Truth_Vals['b'] == 0:
            b = 1 - self.B
        if Truth_Vals['e'] == 1:
            e = self.E
        elif Truth_Vals['e'] == 0:
            e = 1 - self.E
        if Truth_Vals['a'] == 1:
            if Truth_Vals['b'] == 1 and Truth_Vals['e'] == 1:
                a = self.A_B_E
            elif Truth_Vals['b'] == 1 and Truth_Vals['e'] == 0:
                a = self.A_B_not_E
            elif Truth_Vals['b'] == 0 and Truth_Vals['e'] == 1:
                a = self.A_not_B_E
            elif Truth_Vals['b'] == 0 and Truth_Vals['e'] == 0:
                a = self.A_not_B_not_E
        elif Truth_Vals['a'] == 0:
            if Truth_Vals['b'] == 1 and Truth_Vals['e'] == 1:
                a = 1 - self.A_B_E
            elif Truth_Vals['b'] == 1 and Truth_Vals['e'] == 0:
                a = 1 - self.A_B_not_E
            elif Truth_Vals['b'] == 0 and Truth_Vals['e'] == 1:
                a = 1 - self.A_not_B_E
            elif Truth_Vals['b'] == 0 and Truth_Vals['e'] == 0:
                a = 1 - self.A_not_B_not_E
        if Truth_Vals['j'] == 1:
            if Truth_Vals['a'] == 1:
                j = self.J_A
            elif Truth_Vals['a'] == 0:
                j = self.J_not_A
        elif Truth_Vals['j'] == 0:
            if Truth_Vals['a'] == 1:
                j = 1 - self.J_A
            elif Truth_Vals['a'] == 0:
                j = 1 - self.J_not_A
        if Truth_Vals['m'] == 1:
            if Truth_Vals['a'] == 1:
                m = self.M_A
            elif Truth_Vals['a'] == 0:
                m = self.M_not_A
        elif Truth_Vals['m'] == 0:
            if Truth_Vals['a'] == 1:
                m = 1 - self.M_A
            elif Truth_Vals['a'] == 0:
                m = 1 - self.M_not_A

        return (b * e * a * j * m)


def main(argv):
    if len(argv) > 6:
        sys.exit(0)

    C1 = []
    C2 = []
    truthVal = {'b': 0, 'e': 0, 'a': 0, 'j': 0, 'm': 0}
    given = False
    input_len = len(argv)

    a = BayesianNetwork()
    a.calc_input(argv, truthVal, input_len, C1, C2, given)
    a.computeProbability(C1, C2, truthVal)


if __name__ == '__main__':
    main(sys.argv)
