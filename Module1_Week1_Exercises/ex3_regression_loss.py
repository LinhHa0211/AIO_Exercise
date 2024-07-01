import math
import random

def mae(target, predict):
    total = 0
    for i in range(len(target)):
        total += abs(target[i] - predict[i])
    return total / len(target)

def mse(target, predict):
    total = 0
    for i in range(len(target)):
        total += (target[i] - predict[i])**2
    return total / len(target)

def rmse(target, predict):
    return math.sqrt(mse(target, predict))

def exercise3():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
    else:
        num_samples = int(num_samples)
        loss_name = input('Input loss name: ')
        predict = []
        target = []
        if loss_name == 'mae':
            for i in range(num_samples):
                y_predict = random.uniform(0, 10)
                y_target = random.uniform(0, 10)
                print(f'loss name: {loss_name}, samples: {i}, pred: {y_predict}, target: {y_target}, loss: {mae([y_target], [y_predict])}')
            target.append(y_target)
            predict.append(y_predict)
            print(f'final mae: {mae(target, predict)}')
        elif loss_name == 'mse':
            for i in range(num_samples):
                y_predict = random.uniform(0, 10)
                y_target = random.uniform(0, 10)
                print(f'loss name: {loss_name}, samples: {i}, pred: {y_predict}, target: {y_target}, loss: {mse([y_target], [y_predict])}')
            target.append(y_target)
            predict.append(y_predict)
            print(f'final mse: {mse(target, predict)}')
        elif loss_name == 'rmse':
            for i in range(num_samples):
                y_predict = random.uniform(0, 10)
                y_target = random.uniform(0, 10)
                print(f'loss name: {loss_name}, samples: {i}, pred: {y_predict}, target: {y_target}, loss: {rmse([y_target], [y_predict])}')
            target.append(y_target)
            predict.append(y_predict)
            print(f'final rmse: {rmse(target, predict)}')
            
exercise3()