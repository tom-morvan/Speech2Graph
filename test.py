import random

class Test:

    def __init__(self, sentence, expected_output, level):
        self.sentence = sentence
        self.expected_output = expected_output
        self.level = level
        self.result = 'na'
        self.test_id = ''
        self.name = ''

    def __str__(self):
        return '{} = {}'.format(self.sentence, self.expected_output)

    def set_result(self, result):
        self.result = result

class LevelOneTest(Test):
    level_one_list = []
    level_one_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 1)
        LevelOneTest.level_one_list.append(self)
        counter += 1

    def __str__(self):
        return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelOneTest.level_one_list).sentence

    def allTests(self):
        return LevelOneTest.level_one_list

    # def runTests(self):
    #     pass_all = True
    #     results = []*len(LevelOneTest.level_one_list)

    #     for i, test in enumerate(LevelOneTest.level_one_list):
    #         ####EXECUTE TEST ####
    #         if FAIL
    #             pass_all = False
    #             result[i] = 0

    #     if pass_all == True:
    #         print('Level one tests {}'.format(len(LevelOneTest.level_one_list)))
    #     else:

    #         for i len

class LevelOneTest(Test):
    level_one_list = []
    level_one_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 1)
        LevelOneTest.level_one_list.append(self)
        counter += 1

    def __str__(self):
        return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelOneTest.level_one_list).sentence

    def allTests(self):
        return LevelOneTest.level_one_list

class LevelTwoTest(Test):
    level_two_list = []
    level_two_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 2)
        LevelTwoTest.level_two_list.append(self)
        counter += 1

    def __str__(self):
        return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelTwoTest.level_Two_list).sentence

    def allTests(self):
        return LevelTwoTest.level_Two_list

class LevelThreeTest(Test):
    level_three_list = []
    level_three_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 1)
        LevelThreeTest.level_three_list.append(self)
        counter += 1

    def __str__(self):
        return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelThreeTest.level_three_list).sentence

    def allTests(self):
        return LevelThreeTest.level_thre_list

class LevelFourTest(Test):
    level_four_list = []
    level_four_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 1)
        LevelOneTest.level_four_list.append(self)
        counter += 1

    def __str__(self):
        return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelFourTest.level_four_list).sentence

    def allTests(self):
        return LevelFourTest.level_four_list

def level_one_tests():
    tests = [
        LevelOneTest("Je veux le nombre d’absences en fonctions de l’âge des agents dont le temps de travail est supérieur à 7h.", "[[le nombre],[absences],[ âge des agents], [le temps de travail]]"),
        LevelOneTest("Je veux la moyenne d’âge des agents en fonction du sexe des agents avec la date de début du poste inferieur à 2010.", "[la moyenne],[âge des agents],[sexe des agents], [la date de debout du poste]]"),
        LevelOneTest('Donne-moi la moyenne de paie nette par catégorie hiérarchique avec le sexe des agents homme.','[[la moyenne],[paie nette],[ catégorie hiérarchique], [le sexe des agents]]'),
        LevelOneTest('Donnez-moi la somme des absences par nature d’absence avec le nombre de jour d’absences supérieur à trois semaines.','[[la somme],[absences],[nature d’absence], [le nombre de jour d’absences]]'),
        LevelOneTest("Calculez la moyenne du nombre d'enfants à charge des agents en fonction de l’âge des agents avec le statut marital des agents marié.","[[la moyenne],[nombre d’enfants a charge des agents],[ âge des agents], [le statut marital des agents]]"),
        LevelOneTest("Calculez la moyenne du montant HT des factures par intérêts des factures aux sociétés avec le montant HT des factures non nul.","[[la moyenne], [montant HT des factures], [intérêts des factures aux sociétés],  [le montant HT des factures]]"),
        LevelOneTest("Faites la somme des absences en fonction du nombre d’heure d’absences avec le nom de l’entité M. Dupont.","[[la somme],[absences],[ nombre d’heure d’absences], [le nom de l’entité]]"),
        LevelOneTest('Je veux le nombre de foyers usagers pour le lieu Ile de France. ','[[le nombre],[foyers usagers],[ ], [lieu]]'),
        LevelOneTest('Donnez-moi le nombre de la paie mensuelle sous le nom de l’entité Madame Bovina.','[[le nombre],[paie mensuelle],[ ], [nom de l’entité]]'),
        LevelOneTest('Je veux le nombre d’inscriptions en fonction de l’âge des habitants.','[[le nombre],[inscriptions],[ âge des habitants], [ ]]')]


if __name__ == '__main__':
    print(LevelOneTest.randomSentence())


# def parsing(test_file):
#     tests = {}
#     with open(test_file, 'r', encoding='utf-8') as f:
#         content = f.readlines()
#     content = [x.strip() for x in content]

#     test_number = 1
#     current_test_level = 0
#     for i, line in enumerate(content) :
#         if line.startswith('Niveau'):
#             current_test_level = int(line[-1])
#             pass

#         if current_test_level == 0:
#             pass

#         if line.startswith('-') :
#             current_phrase_in = line
#             current_output = content[i+1]
#             current_test = Test(current_phrase_in,current_output, current_test_level)
#             tests.append(current_test)
#             test_number += 1
#         else:
#             pass

# class LevelTest:
#     def __init__(self,level,description):
#         self.level = level
#         self.tests = []
#         self.description = ''

#     def addTest(self,test):
#         self.tests.append(test)

#     def addCreateTest(self,sentence,expected_output)
#         t = Test(sentence,expected_output,self.level)
#         self.tests.append(test)

#     def randomSentance(self):
#         return random.choice(self.tests).sentance

# test_file = 'test_cases.txt'

# parsing(test_file)
