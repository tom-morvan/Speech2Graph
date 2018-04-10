text_list = ['je','veux','la','somme','des','charges','patronales','en','fonction','du','montant','hors','taxe','des','factures']
stripped_text = []

key_words = ['somme','moyenne','nombre','charges','patronales','d\'exploitation','sur','les','societe','hors','taxe','TTC','factures','engagements','des','montant']

#Les dictionnaires contiennent
aggregation_dict = {'somme' : 'somme', 'moyenne' : 'moyenne', 'nombre' : 'nombre'}
# aggregation_dict[aggregation_keys] = aggregation_values

metric_dict = {'charges' : [['charges','patronales'],['charges','d\'exploitation']], 'patronales': [['charges','patronales']]}
# metric_dict[metric_keys] = metric_values 

dimension_dict = {'montant' : [['montant','hors','taxe','des','factures'],['montant','TTC','des','factures'],['montant','des','engagements','hors','taxe']]}
# dimension_dict[dimension_keys] = dimension_values

filter_dict = {}
# filter_dict[filter_keys] = filter_values

aggregation = ''
dimension = ''
metric = ''
filters = ''


for token in text_list:
	if token in key_words:
		stripped_text.append(token)


for el in stripped_text :
	if el in aggregation_dict :
		aggregation = aggregation_dict[el]
	    
	    	
for el in stripped_text :
	if el in metric_dict :
		for possible_metric in metric_dict[el] :
			token_count = 0
			for token in possible_metric :
				if token in stripped_text :
					token_count +=1
				if token_count == len(possible_metric) :
					metric = possible_metric
					break 

for el in stripped_text :
	if el in dimension_dict :
		for possible_dimension in dimension_dict[el] :
			token_count = 0
			for token in possible_dimension :
				if token in stripped_text :
					token_count +=1
				if token_count == len(possible_dimension) :
					dimension = possible_dimension
					break

for el in stripped_text :
	if el in filter_dict :
		for possible_filter in filter_dict[el] :
			token_count = 0
			for token in possible_filter :
				if token in stripped_text :
					token_count +=1
				if token_count == len(possible_filter) :
					filters = possible_filter
					break

print(aggregation, metric, dimension, filters)




