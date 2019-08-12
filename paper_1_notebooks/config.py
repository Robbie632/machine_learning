'''drop_semi_bedrock ->  boolean, if set to True then some bedrock sites deemed to be semi-bedrock sites are not used for classification
'''

bedrock_only = True
data_input_path = '../data/raw_data.csv'
drop_semi_bedrock = False
features_start = 9
features_end = -1
target = 'class'
known_idententifier_col = 'Geology'
known_identifier_value = 'samples'
unknown_identifier_value = 'Artefacts'
random_seed_state = 42