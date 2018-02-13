import requests, json, nltk

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
try:
    print(r.recognize_google(audio, language='fr-FR'))
except:
    pass

#r_post = requests.post('https://vision.staging.mantic.fr/auth/login', json={"email": "inno@mantic.fr", "password": "inno"})
#token = json.loads(r_post.text)['data']['token']
#r_get = requests.get('https://vision.staging.mantic.fr/graph/get_metrics', headers={'Authorization': str(token)})
#print(r_get.status_code)
#r_text = r_get.text
#r_json = json.loads(r_text)
#metric_list = []
#for el in r_json :
#    metric_list.append([el['aggregations'],el['field']])
##print(metric_list_json)
#
#
#r_get = requests.get('https://vision.staging.mantic.fr/graph/get_filters_and_dimensions?metric=structure_level', headers={'Authorization': str(token)})
#print(r_get.status_code)
#r_text = r_get.text
#r_json = json.loads(r_text)
#dimension_list = []
#for el in r_json['dimensions'] :
#    dimension_list.append(el['field'])
#filters_list = []
#for el in r_json['filters'] :
#    if 'values' in el:
#        filters_list.append([el['field'],el['values']])
#    else :
#        filters_list.append([el['field']])




translation = {
    'absence': 'absences',
    'absence_type': "natures d'absence",
    'absence_nb_days': "nombre de jours d'absence",
    'absence_nb_hours': "nombre d'heures d'absence",
    'absence_end_date': "date de fin d'absence",
    'absence_start_date': "date de début d'absence",
   ' absence_time_evolution': 'temps, absences en cours',

    'activity': 'activités municipales',
    'activity_name': 'nom des activités',
    'activity_type': "type d'activité",

    'adress': 'adresse',
    'adress_end_date': "date de déménagement à l'adresse",
    'adress_start_date': "date d'emménagement à l'adresse",

    'agent': 'agents',
    'agent_birthday': 'date de naissance des agents',
    'agent_age': 'âge des agents',
    'agent_marital_status': 'statut marital des agents',
    'agent_nb_children': "nombre d'enfants à charge des agents",
    'agent_sex': 'sexe des agents',
    'agent_time_evolution': 'temps, agents employés',
    'attendance': 'présences hebdomadaires des agents',
    'attendance_nb_hours_overtime': 'heures supplémentaires hebdomadaires',
    'attendance_nb_hours_worked': "nombre d'heures hebdomadaires",
    'attendance_week_monday': 'semaine de présence',

    'engagement': 'engagements',
    'engagement_creation_date': 'date du début de contrat',
    'engagement_delivery_date': 'date de livraison',
    'engagement_duration': 'durée démarrage - livraison',
    'engagement_amount_full_tax': 'montant des engagements TTC',
    'engagement_amount_no_tax': 'montant des engagements HT',
    'engagement_time_evolution': 'temps, engagements en cours',

    'household': 'foyers usagers',
    'household_nb_children': "nombre d'enfants par foyer",
    'household_quotient': 'quotient familial',
    'household_quotient_slice': 'tranche de quotient familial',
    'household_status': 'type de foyer',
    'household_time_evolution': 'temps des foyers',

    'invoice_household': 'factures aux foyers usagers',
    'invoice_household_amount': 'montants des factures aux foyers',
    'invoice_household_amount_paid': 'montants payés des factures aux foyers',
    'invoice_household_payment_date': 'date de paiement des factures aux foyers',
    'invoice_household_creation_date': "date d'émission des factures aux foyers",
    'invoice_household_time_evolution': 'temps, factures en cours',

    'invoice_household_line': 'détail facture',
    'invoice_household_line_amount': 'montant des lignes de factures aux foyers',
    'invoice_household_line_amount_paid':
        'montant payé des lignes de factures aux foyers',

    'invoice_professional': 'factures aux sociétés',
    'invoice_professional_amount_no_tax': 'montant HT des factures',
    'invoice_professional_amount_full_tax': 'montant TTC des factures',

    'invoice_professional_interests': 'intérêts des factures aux sociétés (€)',
    'invoice_professional_interests_pct':
        'intérêts des factures aux sociétés (%)',
    'invoice_professional_date': 'date des factures',
    'invoice_professional_reception_date': 'date de reception des factures',
    'invoice_professional_creation_date': "date d'enregistrement des factures",
    'invoice_professional_validation_date': 'date de service fait',
    'invoice_professional_payment_date': 'date de paiement des factures',
    'invoice_professional_mandate_date': 'date de mandatement des factures',
    'invoice_professional_reception_mandate_duration': 'durée reception - mandat',
    'invoice_professional_reception_validation_duration':
        'durée reception - validation',
    'invoice_professional_reception_payment_duration':
        'durée reception - paiement',
    'invoice_professional_validation_mandate_duration':
        'durée validation - mandat',
    'invoice_professional_validation_payment_duration':
        'durée validation - paiement',
    'invoice_professional_time_evolution': 'temps, factures en cours',

    'job': 'affectation agent',
    'job_category': 'catégorie hiérarchique',
    'job_end_date': 'date de fin du poste',
    'job_start_date': 'date de début du poste',
    'job_work_load': 'temps de travail',
    'job_type': 'statut agent',
    'job_label': "type d'emploi",
    'job_time_evolution': 'temps, affectations en cours',

    'organization': 'tiers',
    'organization_name': 'nom des tiers',
    'organization_type': 'type de tiers',

    'pay_period': 'paie mensuelle',
    'pay_period_amount_agent': 'paie nette',
    'pay_period_amount_employer': 'charges patronales',
    'pay_period_end_date': 'fin de période de paie',
    'pay_period_start_date': 'début de période de paie',
    'pay_period_extra_hours': "nombre d'heures supplémentaires",
    'pay_period_extra_hours_cost': 'coût des heures supplémentaires',

    'place': 'lieu',
    'place_name': 'nom du lieu',

    'person': 'habitants',
    'person_age': 'âge des habitants',
    'person_birthday': 'date de naissance des habitants',
    'person_sex': 'sexe des habitants',

    'quotient': 'quotients familiaux',
    'quotient_quotient_slice': 'tranche de quotient familial',
    'quotient_value': 'quotient familial',
    'quotient_start_date': "date d'effet du quotient",
    'quotient_end_date': 'date de fin du quotient',

    'registration': 'inscriptions',
    'registration_end_date': "date de fin de l'inscription",
    'registration_start_date': "date de début de l'inscription",
    'registration_consumption': 'consommations',

    'consumption': 'consommations',
    'consumption_value': 'valeur des consommations',
    'consumption_date': 'date des consommations',

    'salary_detail': 'détail paie agents',
    'salary_detail_amount_agent': 'détails du salaire net',
    'salary_detail_amount_employer':
        'détails des charges patronales des salaires',

    'salary_line': 'détail paie agents',
    'salary_line_code': 'code rubrique de paie',
    'salary_type': 'type de paie des salaires',

    'structure': 'entités de travail',
    'structure_level': "niveau hiérarchique de l'entité",
    'structure_name': "nom de l'entité",
    'AREA_GRAPH_NODE': 'une courbe',
        'ART': 'art',
        'BAR_GRAPH_NODE': 'une barre',
        'BUDGET_GRAPH_TOOLTIP':
            "Cliquez sur {{graphNode}} pour plus d'information",
        'CANTEEN': 'cantine',
        'CANTEEN_LEISURE_CENTER': 'cantine centre aéré',
        'CANTEEN_SCHOOL': 'cantine scolaire',
        'CANTEEN_SCHOOL_UNRESERVED': 'cantine scolaire sans reservation',
        'CONTRACTOR': 'contractuel',
        'DANCE': 'danse',
        'DAYCARE': 'garderie',
        'DAYCARE_NURSERY': 'garderie maternelle',
        'DAYCARE_PRIMARY': 'garderie primaire',
        'DIRECTED_STUDIES': 'études dirigiées',
        'ELECTED': 'élu',
        'FIELD_TRIP': 'sortie scolaire',
        'FIELD_TRIP_CULTURE': 'sortie scolaire culture',
        'FIELD_TRIP_SCIENCE': 'sortie scolaire science',
        'FIELD_TRIP_SEA': 'sortie scolaire mer',
        'FULL': 'temps plein',
        'INTERN': 'stagiaire',
        'LEISURE_CENTER': 'centre aéré',
        'LEISURE_CENTER_UNRESERVED': 'centre aéré sans reservation',
        'MISC': 'divers',
        'MUSIC_ACADEMY': 'conservatoire',
        'NOT_FULL': 'temps non complet',
        'NOT_TENURE': 'non titulaire',
        'NO_FIXED_DURATION': 'sans durée fixe',
        'NURSERY': 'maternelle',
        'PART': 'temps partiel',
        'PART_50': '50%',
        'PART_60': '60%',
        'PART_70': '70%',
        'PART_80': '80%',
        'PART_90': '90%',
        'PERISCOLAR': 'périscolaire',
        'PERISCOLAR_NURSERY': 'périscolaire maternelle',
        'PERISCOLAR_NURSERY_UNRESERVED':
        ''    'périscolaire maternelle sans réservation',
        'PERISCOLAR_PRIMARY': 'périscolaire primaire',
        'PERISCOLAR_PRIMARY_UNRESERVED': 'périscolaire primaire sans réservation',
        'PIE_GRAPH_NODE': 'une portion',
        'PRIMARY_SCHOOL': 'école primaire',
        'SENIOR': 'senior',
        'SPORT': 'sport',
        'SPORT_CULTURE': 'sport et culture',
        'EXCEPTIONAL': 'congé exceptionnel',
        'UNIONS': 'représentation syndicale',
        'SPORT_CULTURE_ADULTS': 'sport et culture adultes',
        'STUDY': 'études',
        'STUDY_ART_ADULTS': "cours d'art adultes",
        'STUDY_ENGLISH_ADULTS': "cours d'anglais",
        'STUDY_HISTORY': "cours d'histoire",
        'STUDY_LANGUAGES': 'cours de langues',
        'TEACHER': 'enseignant',
        'TENURE_HOLDER': 'titulaire',
        'TREE_GRAPH_NODE': 'un cercle',
        'accommodation': 'Logement',
        'accommodation_age': "Ancienneté d'emménagement",
        'accommodation_status': 'Statut des logements',
        'accommodation_subs': 'Allocation logement',
        'accomodation_age': "Ancienneté d'emménagement",
        'accomodation_subs': 'Allocation logement',
        'ac': 'Avec pièce climatisée',
        'acc_subs_type': "Type d'allocation logement",
        'accident': 'accident',
        'age': 'Age',
        'age_2': 'Âge (découpe 2)',
        'age_3': 'Âge (découpe 3)',
        'age_4': 'Âge (découpe 4)',
        'age_5': 'Âge (découpe 5)',
        'age_6': 'Âge (découpe 6)',
        'age_7': 'Âge (découpe 7)',
        'agriculture': 'Agriculture',
        'all': 'Dépenses & Recettes',
        'average': 'la moyenne',
        'bathroom': "Salle d'eau",
        'bathroom_wc': "Salle d'eau et WC",
        'birth_subs': 'Prime naissance ou adoption',
        'boarding_school': 'Internat',
        'budget_execution': 'éxecution comptable',
        'budget_movement': 'mouvements budgétaire',
        'business': 'Commerces',
        'business_demography': 'Entreprises',
        'business_shop': 'Commerces',
        'cable': 'Câble',
        'cantin': 'Cantine',
        'car': "Disposant d'une voiture",
        'cars': 'Nombre de voitures',
        'childhood': 'petite enfance',
        'children': 'enfance',
        'children_nb': "Nombre d'enfants",
        'clca_subs': 'CLCA',
        'cmg_assistante': 'CMG Assistante Maternelle',
        'cmg_garde': 'CMG Garde à domicile',
        'cmg_structure': 'CMG Structure versable',
        'cmg_subs': 'Allocations CMG',
        'cmg_type': 'Catégories de CMG',
        'cohabiting': 'concubinage',
        'communication': 'Télécommunications',
        'complementary_family_subs': 'Complement Familial',
        'connection_speed': 'Vitesse de connection',
        'contractor': 'contrat',
        'cost': 'dépenses',
        'covered': 'Abrité',
        'cpe': 'Avec classe pré-élementaire',
        'cpge': 'CPGE',
        'culture': 'culture',
        'day': 'jour',
        'death_relative': "mort d'un proche",
        'default': 'Défaut',
        'demography': 'Démographie',
        'demography_mobility': 'Mobilité',
        'department': 'service',
        'department_type': 'nom du service',
        'disabled_child_subs': "Allocation Education de l'Enfant Handicapé",
        'disease': 'maladie',
        'divorced': 'divorcé',
        'dsl': 'DSL',
        'economic_development': 'développement économique',
        'education': 'Education',
        'education_youth': 'jeunesse',
        'elected': 'élus',
        'elections': 'Elections',
        'electricity': 'Avec électricité',
        'employees': 'Nombre de salariés',
        'employment': 'Emploi',
        'empty_accomodation': 'Logements vacants',
        'epci_level': 'EPCI',
        'equal': '=',
        'executive': 'Cadres',
        'expense': 'dépenses',
        'expense_cost': 'coûts',
        'expense_type': 'type de coûts',
        'expenses': 'Dépenses',
        'familial_status': 'Status familial',
        'family_subs': 'Allocations Familiales',
        'family_support_subs': 'Allocation Soutien Familial',
        'female': 'femmes',
        'finance': 'Finances',
        'finances': 'finances',
        'fisc_ref_age': 'Âge du référent fiscal',
        'formation': 'formation',
        'ftth': 'Fibre',
        'full': 'temps plein',
        'gender': 'Sexe',
        'general_administration': 'administration générale',
        'greater': '>',
        'greater_or_equal': '>=',
        'health': 'santé',
        'heating': 'Chauffage',
        'heating_option': 'Type de chauffage',
        'hlm_empty': 'HLM loués vides',
        'holiday': 'vacances',
        'holidays': 'vacances',
        'hot_water': 'Avec eau chaude',
        'hot_water_option': "Type d'accès",
        'in_': '=',
        'incomes': 'Revenus',
        'incomes_salary': 'Salaires',
        'individual': 'Individuelles',
        'industry': "Secteur d'activité",
        'industry_2': "Secteur d'activité (autre découpe)",
        'information_system': "systèmes d'informations",
        'intern': 'stagiaire',
        'island': 'Résidences insulaires',
        'island_accommodation': "Type d'habitation",
        'justice': 'Justice',
        'law': 'juridique',
        'leisure': 'Loisirs',
        'lit': 'Éclairé',
        'location': 'Lieu passé',
        'long_sickness': 'longue maladie',
        'long_time': 'longue absence',
        'low_revenue': 'Bas Revenus',
        'low_revenue_ref': 'Bas Revenus (Référence)',
        'lower': '<',
        'lower_or_equal': '<=',
        'mains_drainage': "Tout-à-l'égout",
        'male': 'hommes',
        'marital_status': 'Statut marital',
        'married': 'marrié',
        'misc': 'divers',
        'mask_misc': 'administration générale',
        'month': 'mois',
        'no_fixed_duration': 'sans horaire fixe',
        'not_equal': '!=',
        'not_full': 'temps non complet',
        'not_in': '≠',
        'not_tenure': 'non titulaire',
        'number': 'le nombre',
        'options': 'Types',
        'pacs': 'pacs',
        'paje': 'PAJE Versable',
        'paje_rights': 'Droits versable PAJE',
        'parent_leave': 'congé maternité/paternité',
        'parking': "Disposant d'un emplacement de stationnement",
        'parks': 'parcs',
        'part50': 'partiel 50%',
        'part60': 'partiel 60%',
        'part70': 'partiel 70%',
        'part80': 'partiel 80%',
        'part90': 'partiel 90%',
        'part': 'temps partiel',
        'poverty': 'Pauvreté',
        'pregnancy': 'grossesse',
        'prevention': 'prevention',
        'public': 'Champ',
        'public_service': 'Services Publics',
        'qualification': 'Diplôme',
        'quarter': 'trimestre',
        'real_estate': 'immobilier',
        'religion': 'fête religieuse',
        'rep': 'REP',
        'revenue': 'Revenus',
        'revenues': 'Recettes',
        'rh': 'ressources humaines',
        'rooms': 'Par pièce(s)',
        'rpic': 'RPIC',
        'rpid': 'RPID',
        'rsa': 'RSA',
        'rsa_type': 'Catégories de RSA',
        'rtt': 'RTT',
        'safety': 'sécurité',
        'salaried': 'Salariat',
        'school_subs': 'Allocation Rentrée Scolaire',
        'sector': 'Privé/Public',
        'seniors': 'seniors',
        'separated': 'séparé',
        'sick_child': 'enfant malade',
        'sick_relative': 'proche malade',
        'sickness': 'maladie',
        'similar_city': 'Niveau des villes similaires',
        'single': 'célibataire',
        'social': 'social',
        'sphere_pres_prod': 'Sphère Productive/Présentielle',
        'sport_center': "Type d'infrastructure",
        'sport_units': "Type d'équipement",
        'sports': 'sports',
        'standing': 'Standing',
        'status_emp': "Status de l'emploi",
        'status_ns': 'Status non salarié',
        'status_occupants': 'Status des occupants',
        'street_cleaning': 'nettoyage',
        'strike': 'grève',
        'study': 'étudeds',
        'subs_share_in_revenue': 'Part des prestations CAF dans les revenus',
        'sum': 'la somme',
        'teacher': 'enseignant',
        'technical_services': 'services techniques',
        'tenure_holder': 'titulaire',
        'tourism': 'Tourisme',
        'tp': 'Temps partiel',
        'trade': 'Dont commerce',
        'traffic': 'transports',
        'training': 'formation',
        'transportation': 'transports',
        'unjustified': 'injustifié',
        'urbanism': 'urbanisme',
        'wedding': 'marriage',
        'wedding_relative': "marriage d'un proche",
        'week': 'semaine',
        'widow': 'veuf',
        'workplace': 'Lieu de travail',
        'workplace_salaried': 'Type de contrat',
        'year': 'année',
        'HOLIDAYS': 'congés',
        'SICKNESS': 'maladie',
        'LONG_SICKNESS': 'longue maladie',
        'SICK_CHILD': 'enfant malade',
        'SICK_RELATIVE': 'proche malade',
        'DEATH_RELATIVE': "décès d'un proche",
        'PARENT_LEAVE': 'congé parental',
        'PREGNANCY': 'grossesse',
        'STRIKE': 'grève',
        'UNJUSTIFIED': 'injustifié',
        'TRAFFIC': 'embouteillages',
        'WEDDING': 'marriage',
        'WEDDING_RELATIVE': "marriage d'un proche",
        'FORMATION': 'formation',
        'RELIGION': 'fête religieuse',
        'ACCIDENT': 'accident',
        'LONG_TIME': 'longue absence',
        'RTT': 'rtt',
        'SINGLE': 'célibataire',
        'MARRIED': 'marrié',
        'DIVORCED': 'divorcé',
        'SEPARATED': 'séparé',
        'WIDOW': 'veuf',
        'PACS': 'PACS',
        'COHABITING': 'concubinage',
        'services': 'Services à la population',
        'this_year': 'cette année',
        'this_month': 'ce mois-ci',
        'this_quarter': 'ce trimestre',
        'last_year': "l'an dernier",
        'last_month': 'le mois dernier',
        'last_quarter': 'le trimestre dernier',
        'pick_date': 'choisir la date',
        "absence": "absences",
     "absence_type": "natures d'absence",
     "absence_nb_days": "nombre de jours d'absence",
     "absence_nb_hours": "nombre d'heures d'absence",
     "absence_end_date": "date de fin d'absence",
     "absence_start_date": "date de début d'absence",
     "absence_time_evolution": "temps, absences en cours",
    "absence_cost":"coût d'absence",
    "activity":"activités municipales",
    "activity_name":"nom des activités",
    "activity_type":"type d'activité",
    "adress":"adresse",
    "adress_end_date":"date de déménagement à l'adresse",
    "adress_start_date":"date d'emménagement à l'adresse",
    "agent":"agents",
    "agent_birthday":"date de naissance des agents",
    "agent_age":"âge des agents",
    "agent_marital_status":"statut marital des agents",
    "agent_nb_children":"nombre d'enfants à charge des agents",
    "agent_sex":"sexe des agents",
    "agent_time_evolution":"temps, agents employés",
     "attendance": "présences hebdomadaires des agents",
     "attendance_nb_hours_overtime": "heures supplémentaires hebdomadaires",
     "attendance_nb_hours_worked": "nombre d'heures hebdomadaires",
     "attendance_week_monday": "semaine de présence",
     "engagement": "engagements",
     "engagement_creation_date": "date du début de contrat",
     "engagement_delivery_date": "date de livraison",
     "engagement_duration": "durée démarrage - livraison",
     "engagement_amount_full_tax": "montant des engagements TTC",
     "engagement_amount_no_tax": "montant des engagements HT",
     "engagement_time_evolution": "temps, engagements en cours",
     "household": "foyers usagers",
     "household_nb_children": "nombre d'enfants par foyer",
     "household_quotient": "quotient familial",
     "household_quotient_slice": "tranche de quotient familial",
     "household_status": "type de foyer",
     "household_time_evolution": "temps des foyers",
     "invoice_household": "factures aux foyers usagers",
     "invoice_household_amount": "montants des factures aux foyers",
     "invoice_household_amount_paid": "montants payés des factures aux foyers",
     "invoice_household_payment_date": "date de paiement des factures aux foyers",
     "invoice_household_creation_date": "date d'émission des factures aux foyers",
     "invoice_household_time_evolution": "temps, factures en cours",
     "invoice_household_line": "détail facture",
     "invoice_household_line_amount": "montant des lignes de factures aux foyers",
     "invoice_household_line_amount_paid": "montant payé des lignes de factures aux foyers",
     "invoice_professional": "factures aux sociétés",
     "invoice_professional_amount_no_tax": "montant HT des factures",
     "invoice_professional_amount_full_tax": "montant TTC des factures",
     "invoice_professional_interests": "intérêts des factures aux sociétés (€)",
     "invoice_professional_interests_pct": "intérêts des factures aux sociétés ( % )",
     "invoice_professional_date": "date des factures",
     "invoice_professional_reception_date": "date de reception des factures",
     "invoice_professional_creation_date": "date d'enregistrement des factures",
     "invoice_professional_validation_date": "date de service fait",
     "invoice_professional_payment_date": "date de paiement des factures",
     "invoice_professional_mandate_date": "date de mandatement des factures",
     "invoice_professional_reception_mandate_duration": "durée reception - mandat",
     "invoice_professional_reception_validation_duration": "durée reception - validation",
     "invoice_professional_reception_payment_duration": "durée reception - paiement",
     "invoice_professional_validation_mandate_duration": "durée validation - mandat",
     "invoice_professional_validation_payment_duration": "durée validation - paiement",
     "invoice_professional_time_evolution": "temps, factures en cours",
    "job":"affectation agent",
    "job_category":"catégorie hiérarchique",
    "job_end_date":"date de fin du poste",
    "job_start_date":"date de début du poste",
    "job_work_load":"temps de travail",
    "job_type":"statut agent",
    "job_label":"type d'emploi",
    "job_time_evolution":"temps, affectations en cours",
     "job_duration": "durée du poste",
     "organization": "tiers",
     "organization_name": "nom des tiers",
     "organization_type": "type de tiers",
     "pay_period": "paie mensuelle",
     "pay_period_amount_agent": "paie nette",
     "pay_period_amount_employer": "charges patronales",
     "pay_period_end_date": "fin de période de paie",
     "pay_period_start_date": "début de période de paie",
     "pay_period_extra_hours": "nombre d'heures supplémentaires",
     "pay_period_extra_hours_cost": "coût des heures supplémentaires",
     "pay_period_distance_to_work": "distance domicile - travail",
     "pay_period_cost_replacement": "coût du remplacement",
     "place": "lieu",
     "place_name": "nom du lieu",
     "person": "habitants",
     "person_age": "âge des habitants",
     "person_birthday": "date de naissance des habitants",
     "person_sex": "sexe des habitants",
     "quotient": "quotients familiaux",
     "quotient_quotient_slice": "tranche de quotient familial",
     "quotient_value": "quotient familial",
     "quotient_start_date": "date d'effet du quotient",
     "quotient_end_date": "date de fin du quotient",
     "registration": "inscriptions",
     "registration_end_date": "date de fin de l'inscription",
     "registration_start_date": "date de début de l'inscription",
     "registration_consumption": "consommations",
     "consumption": "consommations",
     "consumption_value": "valeur des consommations",
     "consumption_date": "date des consommations",
     "salary_detail": "détail paie agents",
     "salary_detail_amount_agent": "détails du salaire net",
     "salary_detail_amount_employer": "détails des charges patronales des salaires",
     "salary_line": "détail paie agents",
     "salary_line_code": "code rubrique de paie",
     "salary_type": "type de paie des salaires",
     "structure": "entités de travail",
     "structure_level": "niveau hiérarchique de l'entité",
     "structure_name": "nom de l'entité",
     "market": "marché",
     "market_nature": "nature du marché",
     "market_procedure": "procédure du marché",
     "market_price_type": "type de prix du marché",
     "market_amount_no_tax": "montant HT du marché",
     "market_amount_full_tax": "montant TTC du marché",
     "market_notification_date": "date de notification du marché",
     "market_publication_date": "date de publication du marché",
     "market_duration": "durée du marché",
     "market_cpv_code": "code CPV du marché",
     "market_modification_amount_no_tax": "montant HT de l'amendement au marché",
     "market_modification_publication_date": "date de la publication de l'amendement au marché",
     "market_modification_signature_date": "date de la signature de l'amendement au marché",
     "budget_line": "ligne budgétaire",
     "budget_line_label": "nom ligne de budget",
     "budget_line_reference": "code ligne de budget",
     "budget_line_date": "Année budgétaire",
     "budget_line_amount_prevision": "montant prévisionnel",
     "budget_line_amount_actual": "montant réalisé",
     "budget_line_type": "colonne du budget"
}

roles = {
    'sensitiveHr': 'données sensibles RH',
    'sensitiveFinance': 'données sensibles Finance',
    'sensitivePopulation': 'données sensibles Population'
}

# aggregation, metric, dimension and filters lists in french

metric_list_fr = []
dimension_list_fr = []
filters_list_fr =[]
aggregation_list_fr = ['somme', 'moyenne', 'nombre']

untranslated_metrics =[]
for el in metric_list :
    try :
        metric_list_fr.append(translation[el[1]])
    except : 
        untranslated_metrics.append(el[1])


untranslated_dimensions =[]
for el in dimension_list :
    try :
        dimension_list_fr.append(translation[el])
    except : 
        untranslated_dimensions.append(el)

untranslated_filters =[]
for el in filters_list :
    try :
        filters_list_fr.append(translation[el[0]])
    except : 
        untranslated_filters.append(el)
#print(len(metric_list_fr + dimension_list_fr +filters_list_fr))
#print(len(translation))
#print(dimension_list_fr)


#print(untranslated_filters)

entry = "Je veux la moyenne de paie nette en fonction du nom du lieu ou la nature du marché est supérieure à 50 et le nom du lieu commence par un A"
text_list = entry.split()
stripped_text = []

key_words = []
for el in metric_list_fr +dimension_list_fr + filters_list_fr + aggregation_list_fr:
    for token in nltk.word_tokenize(el) :
        key_words.append(token)
        
    


#initialization of the dictionaries
aggregation_dict = {'somme' : 'somme', 'moyenne' : 'moyenne', 'nombre' : 'nombre'}
# aggregation_dict[aggregation_keys] = aggregation_values

metric_dict = {}
# metric_dict[metric_keys] = metric_values 

dimension_dict = {}
# dimension_dict[dimension_keys] = dimension_values

filters_dict = {}
# filter_dict[filter_keys] = filter_values

#fills in the dictionary with each word existing in a metric/dimension/filter as a key
#the values being a list of the metrics containing that word, formated as a list of words
#for example : metric_dict contains {'âge': [['âge', 'des', 'agents'], ['âge', 'des', 'habitants']]}

for metric in metric_list_fr :
    split_metric = metric.split()
    for word in split_metric:
        try :
            metric_dict[word].append(split_metric)
        except :
            metric_dict[word] = [split_metric]

for dimension in dimension_list_fr :
    split_dimension = dimension.split()
    for word in split_dimension:
        try :
            dimension_dict[word].append(split_dimension)
        except :
            dimension_dict[word] = [split_dimension]
            
for filters in filters_list_fr :
    split_filters = filters.split()
    for word in split_filters:
        try :
            filters_dict[word].append(split_filters)
        except :
            filters_dict[word] = [split_filters]

aggregation = ''
dimension = ''
metric = ''
filters = []

#print(untranslated_filters)
#print(filters_list_fr)



for token in text_list:
	if token in key_words:
		stripped_text.append(token)



for el in stripped_text :
    if el in aggregation_dict :
        aggregation = aggregation_dict[el]
        stripped_text.remove(el)
        break
    
print(stripped_text)

find_metric = False
index_counter = 0
for el in stripped_text :
    if el in metric_dict:
        for possible_metric in metric_dict[el] :
            if stripped_text[index_counter:index_counter + len(possible_metric)] == possible_metric and find_metric == False :
                metric = possible_metric
                for token in possible_metric:
                    stripped_text.remove(token)
                find_metric = True
    index_counter += 1
                
#            token_count = 0
#            for token in possible_metric :
#                if token in stripped_text and find_metric == False:
#                    token_count +=1
#                    if token_count == len(possible_metric) :
#                        metric = possible_metric
#                        for token in possible_metric:
#                            stripped_text.remove(token)
#                        find_metric = True 
#print(stripped_text)
find_dimension = False
index_counter = 0
for el in stripped_text :
    if el in dimension_dict :
        for possible_dimension in dimension_dict[el] :
            if stripped_text[index_counter:index_counter + len(possible_dimension)] == possible_dimension and find_dimension == False:
                dimension = possible_dimension
                for token in possible_dimension:
                    stripped_text.remove(token)
                find_dimension = True
    index_counter += 1
    
print(stripped_text)
index_counter = 0
for el in stripped_text :
    if el in filters_dict :
        for possible_filters in filters_dict[el] :
            if stripped_text[index_counter:index_counter + len(possible_filters)] == possible_filters :
                filters.append(possible_filters)
                for token in possible_filters:
                    stripped_text.remove(token)
    index_counter += 1
    
print(filters)
metric_str = ''
dimension_str = ''
for word in metric :
    metric_str += word + ' '
for word in dimension :
    dimension_str += word + ' '

counter = 0
for filter in filters :
    filters_str = ''
    for word in filter :
        filters_str += word + ' '
    filters[counter] = filters_str
    counter += 1

				

print([aggregation, metric_str, dimension_str, filters])
