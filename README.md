decision-trees
==============

decision trees that work with many features that assume discrete values. 
At each step the tree splits on the feature which provides the maximum information.

The decision tree algorithm used in the code is given in Introduction to Data Mining (http://www-users.cs.umn.edu/~kumar/dmbook/ch4.pdf)
We first compute the information in the system using the classified classes, then we compute the entropy for each attribute.
We then compare the information gain for each feature. The decision tree is split on the attribute that assumes the maximum information 
gain.
This process is repeated till we acquire a complete decision tree.

Sample code is provided in python. Just change the name of the file to the required filename in line 128 of file "decision tree.py" and the code is directly usable.
A sample dataset "contact_lenses_dataset.xls" is provided to show the pattern of the input dataset accepted by the code.
Modify the code as per the requirements.

In case of any problems you can write to me : akrita@live.com
