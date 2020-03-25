from util import entropy, information_gain, partition_classes
import numpy as np 
import ast

class DecisionTree(object):
    def __init__(self):
        # Initializing the tree as an empty dictionary or list, as preferred
        #self.tree = []
        self.tree = {}
        pass

    def learn(self, X, y):
        # TODO: Train the decision tree (self.tree) using the the sample X and labels y
        # You will have to make use of the functions in utils.py to train the tree
        
        # One possible way of implementing the tree:
        #    Each node in self.tree could be in the form of a dictionary:
        #       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
        #    For example, a non-leaf node with two children can have a 'left' key and  a 
        #    'right' key. You can add more keys which might help in classification
        #    (eg. split attribute and split value)
        gain_list = {}
        if entropy(y) != 0:
            for attr in range(len(X[0])):
                values = list(set([item[attr] for item in X]))
                for val in values:
                    X_left, X_right, y_left, y_right = partition_classes(X, y, attr, val)
                    gain_list[(attr, val)] = information_gain(y, [y_left, y_right])
            sp_attr, sp_val = list(gain_list.keys())[list(gain_list.values()).index(max(gain_list.values()))]
            X_left, X_right, y_left, y_right = partition_classes(X, y, sp_attr, sp_val)
            self.tree['split_attribute'] = sp_attr
            self.tree['split_val'] = sp_val
            self.tree['left'] = (X_left, y_left)
            self.tree['right'] = (X_right, y_right)
        pass

    def classify(self, record):
        # TODO: classify the record using self.tree and return the predicted label
        sm_input = record
        base_tree = self.tree
        def rec_classify(sm_input, base_tree):
            if isinstance(base_tree, tuple):
                class_label = max(set(base_tree[-1]), key=base_tree[-1].count)
            elif not isinstance(base_tree, tuple) and 'split_attribute' in base_tree.keys():
                if sm_input[base_tree['split_attribute']] <= base_tree['split_val']:
                    if base_tree['left']:
                        base_tree = base_tree['left']
                        class_label = rec_classify(sm_input, base_tree)
                else:
                    if base_tree['right']:
                        base_tree = base_tree['right']
                        class_label = rec_classify(sm_input, base_tree)
            return class_label
        return rec_classify(sm_input, base_tree)
        pass
