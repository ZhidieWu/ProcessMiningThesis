def processjson(output_dict,input_dict):
    result_dict = {}
    result_dict['DataObjects'] = []
    state_num = 0

    # put all input object into the new json
    for input_index in range(len(input_dict["DataObjects"])):
        result_dict['DataObjects'].append(input_dict['DataObjects'][input_index])
        target_list = []
        del_index = []

        for output_index in range(len(output_dict["DataObjects"])):
        # if have same state
           if input_dict["DataObjects"][input_index]["state"] == output_dict["DataObjects"][output_index]["state"]:
                target_list.append(output_dict["DataObjects"][output_index]["targetRef"][0])
                del_index.append(output_index)
                print(target_list)
                print(del_index)
               #del output_dict["DataObjects"][output_index]
        result_dict['DataObjects'][input_index]['targetRef'] = target_list
        result_dict['DataObjects'][input_index]['label'] = 'state'+str(state_num)
        state_num = state_num + 1
        for del_i in range(len(del_index)):
            del output_dict['DataObjects'][del_index[del_i]]

    final_index = len(result_dict['DataObjects'])
    for output_index in range(len(output_dict["DataObjects"])):
        result_dict['DataObjects'].append(output_dict['DataObjects'][output_index])
        result_dict['DataObjects'][final_index]['sourceRef'] = []
        result_dict['DataObjects'][final_index]['label'] = 'state' + str(state_num)
        state_num = state_num + 1
        final_index = final_index + 1
    return result_dict

def merge_state_from_json(input_dict,text_columns):
    result_dict = {}
    result_dict['DataObjects'] = []
    result_dict['DataObjects'] = input_dict['DataObjects']
    for result_index in range(len(result_dict["DataObjects"])):
        split_state = result_dict['DataObjects'][result_index]['state'].split(',')
        new_state = result_dict['DataObjects'][result_index]['state'].split(',')
        for split_state_index in range(len(split_state)):
            feature_value = split_state[split_state_index].split('_')
            split_feature = feature_value[0]
            # text column
            if split_feature in text_columns:
                if 'True' in feature_value[1]:
                    for state_index in range(len(split_state)):
                        current_feature_value = split_state[state_index].split('_')
                        if current_feature_value[0] == split_feature and 'False' in current_feature_value[1]:
                            new_state.remove(split_state[state_index])
            # num column
            else:
                if '>' in split_feature:
                    split_list = split_feature.split('>')
                    feature_name = split_list[0]
                    feature_value = split_list[1]
                    for state_index in range(len(split_state)):
                        current_feature_value = split_state[state_index].split('>')
                        if current_feature_value[0] == feature_name and float(feature_value) > float(current_feature_value[1]):
                            new_state.remove(split_state[state_index])
                else:
                    split_list = split_feature.split('<=')
                    feature_name = split_list[0]
                    feature_value = split_list[1]
                    for state_index in range(len(split_state)):
                        current_feature_value = split_state[state_index].split('<=')
                        if current_feature_value[0] == feature_name and float(feature_value) < float(current_feature_value[1]):
                            new_state.remove(split_state[state_index])

        new_state_str = ''
        for new_state_index in range(len(new_state)):
            if new_state_index == len(new_state):
                new_state_str = new_state_str + new_state[new_state_index]
            else:
                new_state_str = new_state_str + new_state[new_state_index] + ','
        result_dict["DataObjects"][result_index]["state"]=new_state_str

    return result_dict
