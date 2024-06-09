def exercise1(tp, fp, fn):
    if type(tp) != int:
        print(f'tp must be int')
        return
    if type(fp) != int:
        print(f'fp must be int')
        return
    if type(fn) != int:
        print(f'fn must be int')
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print(f'tp and fp and fn must be greater than zero') 
        return   
    Precision = tp/(tp + fp)
    Recall = tp/(tp + fn)
    F1_score = 2*((Precision * Recall) / (Precision + Recall))
    print(f'Precision is {Precision}')
    print(f'Recall is {Recall}')
    print(f'F1_score is {F1_score}')
    
exercise1(1, 2, 3)
exercise1(1, 'a', 3)
exercise1(1, 2, -3)