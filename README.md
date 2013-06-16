decision-trees
==============

decision trees that work with many features that assume discrete values. 
At each step the tree splits on the feature which provides the maximum information.

The decision tree algorithm used in the code is given in Introduction to Data Mining(http://www-users.cs.umn.edu/~kumar/dmbook/ch4.pdf)
We first compute the information in the system using the classified classes, then we compute the entropy for each attribute.
We then compare the information gain for each feature. The decision tree is split on the attribute that assumes the maximum information 
gain.
This process is repeated till we acquire a complete decision tree.

Sample code is provided in python. Just change the name of the file to the required filename in line 144 of file "decision tree.py" and the code is directly usable.
A sample dataset "contact_lenses_dataset.xls" is provided to show the pattern of the input dataset accepted by the code.

In case of any suggestions/issues you can write to me : info@akrita.com

    Copyright 2013 Akrita Agarwal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    Akrita Agarwal, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
