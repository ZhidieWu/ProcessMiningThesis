def processjson(input_dict,output_dict):
    result_dict = {}
    result_dict['DataObjects'] = []

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
        for del_i in range(len(del_index)):
            del output_dict['DataObjects'][del_index[del_i]]

    final_index = len(result_dict['DataObjects'])
    for output_index in range(len(output_dict["DataObjects"])):
        result_dict['DataObjects'].append(output_dict['DataObjects'][output_index])
        result_dict['DataObjects'][final_index]['sourceRef'] = []
        final_index = final_index + 1
    return result_dict