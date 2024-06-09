import math
import random

def MAE(target, predict):
    total = 0
    for i in range(len(target)):
        total += abs(target[i] - predict[i])
    return total / len(target)

def MSE(target, predict):
    total = 0
    for i in range(len(target)):
        total += (target[i] - predict[i])**2
    return total / len(target)

def RMSE(target, predict):
    return math.sqrt(MSE(target, predict))

def exercise3():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
    else:
        num_samples = int(num_samples)
        loss_name = input('Input loss name: ')
        predict = []
        target = []
        if loss_name == 'MAE':
            for i in range(num_samples):
                y_predict = random.uniform(0, 10)
                y_target = random.uniform(0, 10)
                print(f'loss name: {loss_name}, samples: {i}, pred: {y_predict}, target: {y_target}, loss: {MAE([y_target], [y_predict])}')
            target.append(y_target)
            predict.append(y_predict)
            print(f'final MAE: {MAE(target, predict)}')
        elif loss_name == 'MSE':
            for i in range(num_samples):
                y_predict = random.uniform(0, 10)
                y_target = random.uniform(0, 10)
                print(f'loss name: {loss_name}, samples: {i}, pred: {y_predict}, target: {y_target}, loss: {MSE([y_target], [y_predict])}')
            target.append(y_target)
            predict.append(y_predict)
            print(f'final MSE: {MSE(target, predict)}')
        elif loss_name == 'RMSE':
            for i in range(num_samples):
                y_predict = random.uniform(0, 10)
                y_target = random.uniform(0, 10)
                print(f'loss name: {loss_name}, samples: {i}, pred: {y_predict}, target: {y_target}, loss: {RMSE([y_target], [y_predict])}')
            target.append(y_target)
            predict.append(y_predict)
            print(f'final RMSE: {RMSE(target, predict)}')
            
exercise3()