#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))



#
# The following answers the questions from Lesson 4.
#
'''
E = enron_data
print 'Number of people in ENRON dataset =', len(E) # = 146
K = E.keys()
#print 'Number of features in ENRON dataset =', len(E[K[0]])  # = 21
#F = enron_data[K[0]].keys()    # the features
#num_POI = sum([enron_data[k]['poi'] for k in K])
#print 'Number of POI in ENRON dataset =', num_POI

#print 'SKILLING JEFFREY K -->', E["SKILLING JEFFREY K"]['total_payments'] #   $8,682,716
#print 'LAY KENNETH L -->', E["LAY KENNETH L"]['total_payments']           # $103,559,793
#print 'FASTOW ANDREW S -->', E["FASTOW ANDREW S"]['total_payments']       #   $2,424,083

s = []
max_sal = -10000000.
name = ''
for k in K:
    if E[k]['salary'] != 'NaN':
        s.append(1)
        if s > max_sal:
            max_sal = E[k]['salary']
            name = k
print k + '--->', max_sal

print 'Number of people with salaries = ', sum(s)
s = []
for k in K:
    if E[k]['email_address'] != 'NaN': s.append(1)
print 'Number of people with email addresses = ', sum(s)
s = []
for k in K:
    if E[k]['total_payments'] == 'NaN': s.append(1)
print 'Number of people with NaN for "total_payments" = ', sum(s)
print 'Percentage of people with NaN for "total_payments" = ', sum(s)/float(len(K)) * 100, '%'
s = []
for k in K:
    if (E[k]['total_payments'] == 'NaN') and E[k]['poi']: s.append(1)
print 'Number of POI with NaN for "total_payments" = ', sum(s)
print 'Percentage of POI with NaN for "total_payments" = ', sum(s)/float(num_POI) * 100, '%'

print 'Number of POI + 10 = ', num_POI + 10

s = []
for k in K:
    if (E[k]['total_payments'] == 'NaN') and E[k]['poi']: s.append(1)
print 'Number of POI with NaN for "total_payments" = ', 10
print 'Percentage of POI with NaN for "total_payments" = ', 10./float(num_POI +10) * 100, '%'
'''
