import flask
from classes import *
# from test import *
from filter_values import *

def text_to_ont(sentence):
	parsed_text = ParserB.parse(sentence)

	pre_ontology_aggregation = parsed_text[0]
	pre_ontology_metric = parsed_text[1]
	pre_ontology_dimensions = parsed_text[2]
	pre_ontology_filters = parsed_text[3]

	filter_values = []
	try :
		filter_val = filter_value(sentence)
	except :
		pass
	try :
		if filter_val[0] != None :
			filter_values.append(filter_val)
	except :
		pass
	filters = []
	for filter in range(len(pre_ontology_filters)) :
		filters.append(ProjectionBOne.getFilters(pre_ontology_filters[filter],1))

	try :
		aggregation = ProjectionBOne.getAggregations(pre_ontology_aggregation,1)
	except :
		try:
			aggregation = ProjectionBOne.getAggregations(pre_ontology_aggregation,1)
		except :
			pass
	metric = ProjectionBOne.getMetrics(pre_ontology_metric,1)

	dimensions = []
	for dimension in range(len(pre_ontology_dimensions)) :
		dimensions.append(ProjectionBOne.getDimensions(pre_ontology_dimensions[dimension],1))

	return [aggregation, metric, dimensions, filters, filter_values]


def testing_results(level) :
	"""Testing function for different test levels, input must be an integer between 1 and 4"""
	results = [0,0,0,0,0,0]
	unsuccessful_text_to_onts = 0
	if level == 1 :
		for test_object in LevelOneTest.allTests() :
			try :
				output = text_to_ont(test_object.sentence)
			except :
				unsuccessful_text_to_onts += 1 
				output = [["error"], ["error"], ["error"], ["error"], ["error"]]
			if (test_object.expected_output[0] == output[0]) and (test_object.expected_output[1] == output[1]) and (test_object.expected_output[2] == output[2]) and (test_object.expected_output[3] == output[3]) and (test_object.expected_output[4] == output[4]) :
				results[0] += 1
			if test_object.expected_output[0] == output[0] :
				results[1] += 1
			if test_object.expected_output[1] == output[1] :
				results[2] += 1
			if test_object.expected_output[2] == output[2] :
				results[3] += 1
			if test_object.expected_output[3] == output[3] :
				results[4] += 1
			if test_object.expected_output[4] == output[4] :
				results[5] += 1
			print(output)
			print(test_object.expected_output)
			print("\n\n\n")
	if level == 2 :
		for test_object in LevelTwoTest.allTests() :
			try :
				output = text_to_ont(test_object.sentence)
			except :
				unsuccessful_text_to_onts += 1 
				output = [["error"], ["error"], ["error"], ["error"], ["error"]]
			if (test_object.expected_output[0] == output[0]) and (test_object.expected_output[1] == output[1]) and (test_object.expected_output[2] == output[2]) and (test_object.expected_output[3] == output[3]) and (test_object.expected_output[4] == output[4]) :
				results[0] += 1
			if test_object.expected_output[0] == output[0] :
				results[1] += 1
			if test_object.expected_output[1] == output[1] :
				results[2] += 1
			if test_object.expected_output[2] == output[2] :
				results[3] += 1
			if test_object.expected_output[3] == output[3] :
				results[4] += 1
			if test_object.expected_output[4] == output[4] :
				results[5] += 1
			print(output)
			print(test_object.expected_output)
			print("\n\n\n")

	if level == 3 :
		for test_object in LevelThreeTest.allTests() :
			try :
				output = text_to_ont(test_object.sentence)
			except :
				unsuccessful_text_to_onts += 1 
				output = [["error"], ["error"], ["error"], ["error"], ["error"]]
			if (test_object.expected_output[0] == output[0]) and (test_object.expected_output[1] == output[1]) and (test_object.expected_output[2] == output[2]) and (test_object.expected_output[3] == output[3]) and (test_object.expected_output[4] == output[4]) :
				results[0] += 1
			if test_object.expected_output[0] == output[0] :
				results[1] += 1
			if test_object.expected_output[1] == output[1] :
				results[2] += 1
			if test_object.expected_output[2] == output[2] :
				results[3] += 1
			if test_object.expected_output[3] == output[3] :
				results[4] += 1
			if test_object.expected_output[4] == output[4] :
				results[5] += 1
			print(output)
			print(test_object.expected_output)
			print("\n\n\n")
	if level == 4 :
		for test_object in LevelFourTest.allTests() :
			try :
				output = text_to_ont(test_object.sentence)
			except :
				unsuccessful_text_to_onts += 1 
				output = [["error"], ["error"], ["error"], ["error"], ["error"]]
			if (test_object.expected_output[0] == output[0]) and (test_object.expected_output[1] == output[1]) and (test_object.expected_output[2] == output[2]) and (test_object.expected_output[3] == output[3]) and (test_object.expected_output[4] == output[4]) :
				results[0] += 1
			if test_object.expected_output[0] == output[0] :
				results[1] += 1
			if test_object.expected_output[1] == output[1] :
				results[2] += 1
			if test_object.expected_output[2] == output[2] :
				results[3] += 1
			if test_object.expected_output[3] == output[3] :
				results[4] += 1
			if test_object.expected_output[4] == output[4] :
				results[5] += 1
			print(output)
			print(test_object.expected_output)
			print("\n\n\n")
	return results




print(testing_results(1))