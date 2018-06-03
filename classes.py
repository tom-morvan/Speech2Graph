import numpy as np
from scipy import spatial
from nltk.corpus import stopwords
from closest_word2vec import *
import random
# import polyglot
# from polyglot.text import Text, Word
# from polyglot.downloader import downloader
from stanford_nltk_parser import parse_to_pre_ontology, grammatical_seperation


class Input:

    def sentence():
        pass

class Console(Input):

    def sentence():
        return input("Please enter a sentence")    

class Voice(Input):

    def sentence():
        pass

class Test(Input):

    def __init__(self, sentence, expected_output, level):
        self.sentence = sentence
        self.expected_output = expected_output
        self.level = level
        self.result = 'na'
        self.test_id = ''
        self.name = ''

    # def __str__(self):
    #     return '{} = {}'.format(self.sentence, self.expected_output)

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

    # def __str__(self):
    #     return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelOneTest.level_one_list).sentence

    def allTests():
        return LevelOneTest.level_one_list

class LevelTwoTest(Test):
    level_two_list = []
    level_two_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 2)
        LevelTwoTest.level_two_list.append(self)
        counter += 1

    # def __str__(self):
    #     return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelTwoTest.level_Two_list).sentence

    def allTests():
        return LevelTwoTest.level_two_list

class LevelThreeTest(Test):
    level_three_list = []
    level_three_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 1)
        LevelThreeTest.level_three_list.append(self)
        counter += 1

    # def __str__(self):
    #     return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelThreeTest.level_three_list).sentence

    def allTests():
        return LevelThreeTest.level_three_list

class LevelFourTest(Test):
    level_four_list = []
    level_four_description = ''

    def __init__(self, sentence, expected_output):
        counter = 1
        super().__init__(sentence, expected_output, 1)
        LevelFourTest.level_four_list.append(self)
        counter += 1

    # def __str__(self):
    #     return '{} = {}'.format(self.sentence, self.expected_output)

    def randomSentence():
        return random.choice(LevelFourTest.level_four_list).sentence

    def allTests():
        return LevelFourTest.level_four_list

def create_level_one_tests():
    tests = [
        LevelOneTest("Je veux le nombre d’absences en fonction de l’âge des agents dont le temps de travail est supérieur à 7 heures.", [["nombre"],["absences"],[["âge des agents"]], [["temps de travail"]], ["supérieur à 7 heures"]]),
        LevelOneTest("Je veux la moyenne d’âge des agents en fonction du sexe des agents dont la date de début du poste est inférieur à 2010.", [["moyenne"],["âge des agents"],[["sexe des agents"]], [["date de début du poste"]], ["inférieur à 2010"]]),
        LevelOneTest("Donne-moi la moyenne de paie nette par catégorie hiérarchique avec le sexe des agents homme.",[["moyenne"],["paie nette"],[["catégorie hiérarchique"]], [["sexe des agents"]], ["homme"]]),
        LevelOneTest("Donnez-moi le nombre d'absences par nature d’absence pour les agents dont le nombre de jour d’absences est supérieur à trois semaines.",[["nombre"],["absences"],[["nature d’absence"]], [["nombre de jour d’absences"]], ["supérieur à trois semaines"]]),
        LevelOneTest("Calculez la moyenne du nombre d'enfants à charge des agents en fonction de l’âge des agents avec le statut marital des agents marié.",[["moyenne"],["nombre d’enfants a charge des agents"],[["âge des agents"]], [["statut marital des agents"]], ["marié"]]),
        LevelOneTest("Calculez la moyenne du montant HT des factures par intérêts des factures aux sociétés avec le montant HT des factures non nul.",[["moyenne"], ["montant HT des factures"], [["intérêts des factures aux sociétés"]],  [["montant HT des factures"]], ["non nul"]]),
        LevelOneTest("Faites la somme des absences en fonction du nombre d’heure d’absences avec le nom de l’entité Monsieur Dupont.",[["somme"],["absences"],[["nombre d’heure d’absences"]], [["nom de l’entité"]], ["Monsieur Dupont"]]),
        LevelOneTest("Je veux le nombre de foyers usagers pour le lieu Ile de France.",[["nombre"],["foyers usagers"],[], [["nom du lieu"]], ["Ile de France"]]),
        LevelOneTest("Donnez-moi le nombre de la paie mensuelle sous le nom de l’entité Madame Bovina.",[["nombre"],["paie mensuelle"],[], [["nom de l’entité"]], ["Madame Bovina"]]),
        LevelOneTest("Je veux le nombre d’inscriptions en fonction de l’âge des habitants.",[["nombre"],["inscriptions"],[["âge des habitants"]], [], []])]

def create_level_two_tests():
    tests = [
        LevelTwoTest("Je veux la moyenne d’absences en fonction de l’âge des agents dont le temps de travail est supérieur à 7h.", [["nombre"],["absences"],[["âge des agents"]], [["temps de travail"]], ["supérieur à 7h"]]),
        LevelTwoTest("Je veux l’âge moyen des agents en fonction du sexe des agents avec la date de début du poste est inférieur à 2010.", [["moyenne"],["âge des agents"],[["sexe des agents"]], [["date de début du poste"]], ["inférieur à 2010"]]),
        LevelTwoTest("Donne-moi la paie nette en moyenne par catégorie hiérarchique avec le sexe des agents homme.", [["moyenne"],["paie nette"],[["catégorie hiérarchique"]], [["sexe des agents"]], ["homme"]]),
        LevelTwoTest("-Donnez-moi les absences par nature d’absence avec le nombre de jour d’absences supérieur à trois semaines.", [["somme"],["absences"],[["nature d’absence"]], [["nombre de jour d’absences"]], ["supérieur à trois semaines"]]),
        LevelTwoTest("Calculez le nombre d'enfants à charge des agents moyenné sur l’âge des agents avec le statut marital des agents marié.", [["moyenne"],["nombre d’enfants a charge des agents"],[["âge des agents"]], [["statut marital des agents"]], ["marié"]]),
        LevelTwoTest("Calculez le montant HT moyen des factures par intérêts des factures aux sociétés avec le montant HT des factures non nul.", [["moyenne"], ["montant HT des factures"], [["intérêts des factures aux sociétés"]],  [["montant HT des factures"]], ["non nul"]]),
        LevelTwoTest("Faites les absences au total en fonction du nombre d’heure d’absences avec le nom de l’entité Monsieur Dupont", [["somme"],["absences"],[["nombre d’heure d’absences"]], [["nom de l’entité"]], ["Monsieur Dupont"]]),
        LevelTwoTest("Je veux le nombre d’absences des agents avec un temps de travail supérieur à 7 heures en fonction de l’âge des agents.", [["nombre"],["absences"],[["âge des agents"]], [["temps de travail"]], ["supérieur à 7h"]]),
        LevelTwoTest("Je veux la moyenne d’âge des agents avec la date de début du poste inférieur à 2010 en fonction du sexe des agents.", [["moyenne"],["âge des agents"],[["sexe des agents"]], [["date de début du po]ste"]], ["inférieur à 2010"]]),
        LevelTwoTest("Donne-moi la moyenne de paie nette avec le sexe des agents homme par catégorie hiérarchique.", [["moyenne"],["paie nette"],[["catégorie hiérarchique"]], [["sexe des agents"]], ["homme"]]),
        LevelTwoTest("Donnez-moi la somme des absences avec le nombre de jour d’absences supérieur à trois semaines en fonction de la nature d’absence.", [["somme"],["absences"],[["nature d’absence"]], [["nombre de jour d’absences"]], ["supérieur à trois semaines"]]),
        LevelTwoTest("Calculez la moyenne du nombre d'enfants à charge des agents avec le statut marital des agents marié en fonction de l’âge des agents.", [["moyenne"],["nombre d’enfants a charge des agents"],[["âge des agents"]], [["statut marital des agents"]], ["marié"]]),
        LevelTwoTest("Calculez la moyenne du montant HT des factures sachant le montant HT des factures non nul en fonction des intérêts des factures aux sociétés.", [["moyenne"], ["montant HT des factures"], [["intérêts des factures aux sociétés"]],  [["montant HT des factures"]], ["non nul"]]),
        LevelTwoTest("Faites la somme des absences pour le nom de l’entité Monsieur Dupont en fonction du nombre d’heure d’absences.", [["somme"],["absences"],[["nombre d’heure d’absences"]], [["nom de l’entité"]], ["Monsieur Dupont"]])]

def create_level_three_tests():
    tests = [
        LevelThreeTest("Je veux les absences des agents avec un temps de travail supérieur à 7h en fonction de l’âge des agents.", [["nombre"],["absences"],["âge des agents"], ["temps de travail"], ["supérieur à 7h"]]),
        LevelThreeTest("Je veux l’âge des agents en moyenne avec la date de début du poste inférieur a 2010 en fonction du sexe des agents.", [["moyenne"],["âge des agents"],["sexe des agents"], ["date de début du poste"], ["inférieur à 2010"]]),
        LevelThreeTest("Donnes-moi la paie nette moyenne des agents homme par catégorie hiérarchique.", [["moyenne"],["paie nette"],["catégorie hiérarchique"],["sexe des agents"], ["homme"]]),
        LevelThreeTest("Donnez-moi les absences avec le nombre de jour d’absences supérieur à trois semaines en fonction de la nature d’absence.", [["somme"],["absences"],["nature d’absence"], ["nombre de jour d’absences"], ["supérieur à trois semaines"]]),
        LevelThreeTest("Calculez le nombre d'enfants en moyenne à charge des agents avec le statut marital des agents marié en fonction de l’âge des agents.", [["moyenne"],["nombre d’enfants a charge des agents"],["âge des agents"], ["statut marital des agents"], ["marié"]]),
        LevelThreeTest("Calculez le montant HT moyenné des factures sachant le montant HT des factures non nul en fonction des intérêts des factures aux sociétés.", [["moyenne"], ["montant HT des factures"], ["intérêts des factures aux sociétés"],  ["montant HT des factures"], ["non nul"]]),
        LevelThreeTest("Je veux toutes les absences pour le nom de l’entité Monsieur Dupont en fonction du nombre d’heure d’absences.", [["somme"],["absences"],["nombre d’heure d’absences"], ["nom de l’entité"], ["Mnsieur Dupont"]])]

def create_level_four_tests():
    tests = [
        LevelFourTest("Pour un temps de travail supérieur a 7h, je veux les absences des agents en fonction de l’âge des agents.", [["nombre"],["absences"],["âge des agents"], ["temps de travail"], ["supérieur à 7h"]]),
        LevelFourTest("Quelle est la moyenne de l’âge des agents avec la date de début du poste inférieur a 2010 en fonction du sexe des agents ?", [["moyenne"], ["âge des agents"],["sexe des agents"], ["date de début du poste"], ["inférieur à 2010"]]),
        LevelFourTest("Combien touche en moyenne les agents en fonction de leur catégorie hiérarchique ?", [["moyenne"], ["paie nette"],["catégorie hiérarchique"], [], []]),
        LevelFourTest("Combien touche en moyenne les hommes en fonction de leur catégorie hiérarchique ?", [["moyenne"], ["paie nette"],["catégorie hiérarchique"], ["sexe des agents"], ["homme"]])]



create_level_one_tests()
create_level_two_tests()
create_level_three_tests()
create_level_four_tests()


class Parser:

    def parse(text):
        pass

class ParserA(Parser): 

    def parse(text):
        """Parses the text into sub groups of words, returns a list of the subgroups"""
        agregation = []
        metric = []
        dimension= [[]]
        filters = [[]]
        
        text = Text(text, hint_language_code='fr')
        pos_tags = text.pos_tags
        
        
        #Finding the agregation
        verb_counter = 0        
        noun = None
        i = 0
        
        while noun == None and i < len(pos_tags):
            
            if pos_tags[i][1] == 'VERB':
                verb_counter += 1
                
            if verb_counter > 0:
                
                if pos_tags[i][1] == 'NOUN':
                    noun = pos_tags[i][0]
                    agregation_pos = i
                    
            i += 1
            
        agregation.append(noun)
        
        #Finding the metric    
        i = agregation_pos + 1
        
        while i < len(pos_tags) and pos_tags[i][1] != 'ADP':
            
            metric.append(pos_tags[i][0])
            i += 1
        
        end_metric_pos = i - 1
        
        #Finding the dimensions
        i = end_metric_pos + 1
        dimension_counter = 0

        while i < len(pos_tags) and pos_tags[i][1] != 'CONJ':
            print(pos_tags[i][1])
            
            if pos_tags[i][0] == 'et':
                dimension_counter += 1
                dimension.append([])
            
            else :
                dimension[dimension_counter].append(pos_tags[i][0])
            
            i += 1
            
        end_dimension_pos = i-1
        
        #Finding the filters
        i = end_dimension_pos + 1
        filter_counter = 0
        
        while i < len(pos_tags) :
            
            if pos_tags[i][0] == 'et':
                filter_counter += 1
                filters.append([])
            
            else :
                filters[filter_counter].append(pos_tags[i][0])
            
            i += 1
            
        return([agregation,metric,dimension,filters])
    
class ParserB(Parser):

    def parse(text):
        return parse_to_pre_ontology(text)



class Projection:

    stop = set(stopwords.words('french'))


    def getAggregations(pre_ontology_aggregation, amount):
        """Returns the "amount" closest aggregations from the input string"""
        pass

    def getMetrics(pre_ontology_metric, amount):
        """Returns the "amount" closest metrics from the input string"""
        pass

    def getDimensions(pre_ontology_dimension, amount):
        """Returns the "amount" closest dimensions from the input string"""
        pass

    def getFilters(pre_ontology_filter, amount):
        """Returns the "amount" closest dimensions from the input string"""
        pass

class ProjectionAOne(Projection):
    """Projection using word2vec technology, without removing stop words and using a cosine distance"""
    def getAggregations(pre_ontology_aggregation, amount):
        words = pre_ontology_aggregation
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
                sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # agregation vector
        results_vector = getCosineDistances(sentence_vector, aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = pre_ontology_metric
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getCosineDistances(sentence_vector, metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

        return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = pre_ontology_dimension
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getCosineDistances(sentence_vector, dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

        return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = pre_ontology_filter
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them

        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getCosineDistances(sentence_vector, filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest

        return closest_filters

class ProjectionATwo(Projection):
    """Projection using word2vec technology, without removing stop words and using a euclidean distance"""

    def getAggregations(pre_ontology_aggregation, amount):
        words = pre_ontology_aggregation
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:

            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # agregation vector
        results_vector = getEuclideanDistances(sentence_vector, aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = pre_ontology_metric
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getEuclideanDistances(sentence_vector, metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

        return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = pre_ontology_dimension
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getEuclideanDistances(sentence_vector, dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

        return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = pre_ontology_filter
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them

        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getEuclideanDistances(sentence_vector, filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest

        return closest_filters

class ProjectionAThree(Projection):
    """Projection using word2vec technology, without removing stop words and using a Minkowski distance"""
    
    def getAggregations(pre_ontology_aggregation, amount):
        words = pre_ontology_aggregation
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:

            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # agregation vector
        results_vector = getMinkowskiDistances(sentence_vector, aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = pre_ontology_metric
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getMinkowskiDistances(sentence_vector, metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

        return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = pre_ontology_dimension
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getMinkowskiDistances(sentence_vector, dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

        return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = pre_ontology_filter
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them

        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getMinkowskiDistances(sentence_vector, filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest

        return closest_filters

class ProjectionAFour(Projection):
    """Projection using word2vec technology, without removing stop words and using a Braycurtis distance"""

    def getAggregations(pre_ontology_aggregation, amount):
        words = pre_ontology_aggregation
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:

            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # agregation vector
        results_vector = getBraycurtisDistances(sentence_vector, aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = pre_ontology_metric
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getBraycurtisDistances(sentence_vector, metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

        return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = pre_ontology_dimension
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getBraycurtisDistances(sentence_vector, dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

        return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = pre_ontology_filter
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them

        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getBraycurtisDistances(sentence_vector, filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest

        return closest_filters

class ProjectionBOne(Projection):
    """Projection using word2vec technology, removing stop words and using a cosine distance"""

    def getAggregations(pre_ontology_aggregation, amount):
        words = [i for i in pre_ontology_aggregation if i not in Projection.stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            if len(word) > 2 :
                try:
                    sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them
                except:
                    print("word {} is not in list".format(word))

        # contains the vector distance between the sentence vector and each
        # aggregation vector
        results_vector = getCosineDistances(sentence_vector, no_stop_aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = [i for i in pre_ontology_metric if i not in Projection.stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            if len(word) > 2 :
                try:
                    sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them
                except:
                    print("word {} is not in list".format(word))

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getCosineDistances(sentence_vector, no_stop_metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

            return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = [i for i in pre_ontology_dimension if i not in Projection.stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            if len(word) > 2 :
                try:
                    sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them
                except:
                    print("word {} is not in list".format(word))
        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getCosineDistances(sentence_vector, no_stop_dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

            return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = [i for i in pre_ontology_filter if i not in Projection.stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            if len(word) > 2 :
                try:
                    sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them
                except:
                    print("word {} is not in list".format(word))
        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getCosineDistances(sentence_vector, no_stop_filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest
            return closest_filters

class ProjectionBTwo(Projection):
    """Projection using word2vec technology, removing stop words and using a euclidean distance"""

    def getAggregations(pre_ontology_aggregation, amount):
        words = [i for i in pre_ontology_aggregation if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:

            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # agregation vector
        results_vector = getEuclideanDistances(sentence_vector, no_stop_aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = [i for i in pre_ontology_metric if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getEuclideanDistances(sentence_vector, no_stop_metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

        return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = [i for i in pre_ontology_dimension if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getEuclideanDistances(sentence_vector, no_stop_dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

        return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = [i for i in pre_ontology_filter if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them

        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getEuclideanDistances(sentence_vector, no_stop_filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest

        return closest_filters

class ProjectionBThree(Projection):
    """Projection using word2vec technology, removing stop words and using a minkowski distance"""

    def getAggregations(pre_ontology_aggregation, amount):
        words = [i for i in pre_ontology_aggregation if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:

            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # agregation vector
        results_vector = getMinkowskiDistances(sentence_vector, no_stop_aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = [i for i in pre_ontology_metric if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getMinkowskiDistances(sentence_vector, no_stop_metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

        return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = [i for i in pre_ontology_dimension if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getMinkowskiDistances(sentence_vector, no_stop_dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

        return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = [i for i in pre_ontology_aggregation if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them

        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getMinkowskiDistances(sentence_vector, no_stop_filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest

        return closest_filters

class ProjectionBFour(Projection):
    """Projection using word2vec technology, removing stop words and using a braycurtis distance"""

    def getAggregations(pre_ontology_aggregation, amount):
        words = [i for i in pre_ontology_aggregation if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:

            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # agregation vector
        results_vector = getBraycurtisDistances(sentence_vector, no_stop_aggregation_matrix)

        closest_aggregation = []
        for _ in range(amount):
            closest_aggregation.append(
                getClosest(
                    results_vector,
                    aggregation_list_fr).decode("utf-8"))  # get the "amount" closest

        return closest_aggregation

    def getMetrics(pre_ontology_metric, amount):
        words = [i for i in pre_ontology_metric if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each metris
        # vector
        results_vector = getBraycurtisDistances(sentence_vector, no_stop_metric_matrix)

        closest_metrics = []
        for _ in range(amount):
            closest_metrics.append(
                getClosest(
                    results_vector,
                    metric_list_fr))  # get the "amount" closest

        return closest_metrics

    def getDimensions(pre_ontology_dimension, amount):
        words = [i for i in pre_ontology_dimension if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)

        # contains the vector distance between the sentence vector and each
        # dimension vector
        results_vector = getBraycurtisDistances(sentence_vector, no_stop_dimension_matrix)

        closest_dimensions = []
        for _ in range(amount):
            closest_dimensions.append(
                getClosest(
                    results_vector,
                    dimension_list_fr))  # get the "amount" closest

        return closest_dimensions

    def getFilters(pre_ontology_filter, amount):
        words = [i for i in pre_ontology_filter if i not in stop]
        # vector representation of the input sentence (initialisation)
        sentence_vector = [0 for i in range(300)]

        for word in words:
            sentence_vector = sentence_vector + getWordVector(word)  # You forgot to sum them

        # contains the vector distance between the sentence vector and each filter
        # vector
        results_vector = getBraycurtisDistances(sentence_vector, no_stop_filter_matrix)

        closest_filters = []
        for _ in range(amount):
            closest_filters.append(
                getClosest(
                    results_vector,
                    filter_list_fr))  # get the "amount" closest

        return closest_filters


# print(ParserB.parse("Je veux la moyenne d’âge des agents en fonction du sexe des agents dont la date de début du poste inférieur à 2010."))