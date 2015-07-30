#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """

    ### your code goes here
    predictions = [prediction[0] for prediction in predictions]
    ages = [age[0] for age in ages]
    net_worths = [net_worth[0] for net_worth in net_worths]
    
    errors = [abs(net_worths[i] - predictions[i]) for i in range(len(ages))]
    errors_sorted = errors[:];  errors_sorted.sort();  errors_sorted.reverse()
    max_error = errors_sorted[int(round(len(ages) * 0.1))]
    #print 'max_error =', max_error

    cleaned_data = [(ages[i], net_worths[i], errors[i])
                    for i in range(len(ages))
                    if errors[i] <= max_error]
    #cleaned_data = []
    #for i in range(len(ages)):
    #    print 'i =', i
    #    print 'error[',i,'] = ', error[i]
    #    if error[i] <= max_error:
    #        cleaned_data.append((ages[i], net_worths[i], errors[i]))
    
    #print 'len(cleaned_data) =', len(cleaned_data)
    
    return cleaned_data

