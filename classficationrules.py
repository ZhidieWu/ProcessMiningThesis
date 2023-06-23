from sklearn.tree import _tree
import numpy as np

def new_decision_tree_rules(tree, feature_names, class_names, dataobject_type,text_columns,selected_artifact):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    paths = []
    path = []

    def recurse(node, path, paths):

        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            p1, p2 = list(path), list(path)
            p1 += [f"{name} <= {np.round(threshold, 3)}"]
            recurse(tree_.children_left[node], p1, paths)
            p2 += [f"{name} > {np.round(threshold, 3)}"]
            recurse(tree_.children_right[node], p2, paths)
        else:
            path += [(tree_.value[node], tree_.n_node_samples[node])]
            paths += [path]

    recurse(0, path, paths)

    # sort by samples count
    samples_count = [p[-1][1] for p in paths]
    ii = list(np.argsort(samples_count))
    paths = [paths[i] for i in reversed(ii)]

    dictforjson = {}
    dictforjson['DataObjects'] = []
    rules = []
    label_num = 0
    for path in paths:
        DataObjects_dict = {}
        target_object_dict = {}
        source_object_dict = {}
        source_list = []
        target_list = []
        state_str = ""



        rule = "if "


        for p in path[:-1]:
            if rule != "if ":
                rule += " and "
                state_str += ","
            rule += str(p)
            #check p

            if ">" in str(p):
                feature = str(p).split(">")[0]
                split_feature = feature.split('_')[0]
                if split_feature in text_columns:
                    p = feature + ": True"
            else:
                feature = str(p).split("<=")[0]
                split_feature = feature.split('_')[0]
                if split_feature in text_columns:
                    p = feature + ": False"

            state_str += str(p)
        DataObjects_dict['state'] = state_str
        DataObjects_dict['label'] = 'state'+str(label_num)
        label_num = label_num + 1

        rule += " then "
        if class_names is None:
            rule += "response: " + str(np.round(path[-1][0][0][0], 3))
        else:
            classes = path[-1][0][0]
            l = np.argmax(classes)
            #(proba: {np.round(100.0 * classes[l] / np.sum(classes), 2)
            rule += f"class: {class_names[l]}%)"
            DataObjects_dict['artifact'] = selected_artifact
            source_target_activity = class_names[l].split(",")
            source_object_dict['name'] = str(source_target_activity[0])
            source_list.append(source_object_dict)
            target_object_dict['name'] = str(source_target_activity[1])
            target_list.append(target_object_dict)
            if dataobject_type == 'input':
                if source_target_activity[0] == 'start':
                    DataObjects_dict['targetRef'] = target_list
                    DataObjects_dict['sourceRef'] = []
                elif source_target_activity[1] == 'end':
                    DataObjects_dict['targetRef'] = []
                    DataObjects_dict['sourceRef'] = source_list
                else:
                    DataObjects_dict['targetRef'] = target_list
                    DataObjects_dict['sourceRef'] = source_list
            else:
                DataObjects_dict['sourceRef'] = source_list
        rule += f" | based on {path[-1][1]:,} samples"
        rules += [rule]
        dictforjson['DataObjects'].append(DataObjects_dict)

    return rules,dictforjson