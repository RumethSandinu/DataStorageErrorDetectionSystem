import sys

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# define antecedents and consequent
data_redundancy = ctrl.Antecedent(np.arange(0, 101, 1), 'data_redundancy')
degradation_level = ctrl.Antecedent(np.arange(0, 101, 1), 'degradation_level')
error_history_rate = ctrl.Antecedent(np.arange(0, 101, 1), 'error_history_rate')
error_likelihood = ctrl.Consequent(np.arange(0, 101, 1), 'error_likelihood')

# define membership function ranges using trapisiam
data_redundancy['low'] = fuzz.trapmf(data_redundancy.universe, [0, 0, 30, 50])
data_redundancy['medium'] = fuzz.trapmf(data_redundancy.universe, [30, 50, 60, 80])
data_redundancy['high'] = fuzz.trapmf(data_redundancy.universe, [60, 80, 100, 100])

degradation_level['low'] = fuzz.trapmf(degradation_level.universe, [0, 0, 30, 50])
degradation_level['medium'] = fuzz.trapmf(degradation_level.universe, [30, 50, 60, 80])
degradation_level['high'] = fuzz.trapmf(degradation_level.universe, [60, 80, 100, 100])

error_history_rate['low'] = fuzz.trapmf(error_history_rate.universe, [0, 0, 30, 50])
error_history_rate['medium'] = fuzz.trapmf(error_history_rate.universe, [30, 50, 60, 80])
error_history_rate['high'] = fuzz.trapmf(error_history_rate.universe, [60, 80, 100, 100])

error_likelihood['low'] = fuzz.trapmf(error_likelihood.universe, [0, 0, 30, 50])
error_likelihood['medium'] = fuzz.trapmf(error_likelihood.universe, [30, 50, 60, 80])
error_likelihood['high'] = fuzz.trapmf(error_likelihood.universe, [60, 80, 100, 100])

# define rules
rule1 = ctrl.Rule(data_redundancy['low'] & degradation_level['low'] & error_history_rate['low'], error_likelihood['medium'])
rule2 = ctrl.Rule(data_redundancy['low'] & degradation_level['low'] & error_history_rate['medium'], error_likelihood['medium'])
rule3 = ctrl.Rule(data_redundancy['low'] & degradation_level['low'] & error_history_rate['high'], error_likelihood['high'])

rule4 = ctrl.Rule(data_redundancy['low'] & degradation_level['medium'] & error_history_rate['low'], error_likelihood['low'])
rule5 = ctrl.Rule(data_redundancy['low'] & degradation_level['medium'] & error_history_rate['medium'], error_likelihood['medium'])
rule6 = ctrl.Rule(data_redundancy['low'] & degradation_level['medium'] & error_history_rate['high'], error_likelihood['medium'])

rule7 = ctrl.Rule(data_redundancy['low'] & degradation_level['high'] & error_history_rate['low'], error_likelihood['medium'])
rule8 = ctrl.Rule(data_redundancy['low'] & degradation_level['high'] & error_history_rate['medium'], error_likelihood['high'])
rule9 = ctrl.Rule(data_redundancy['low'] & degradation_level['high'] & error_history_rate['high'], error_likelihood['high'])


rule10 = ctrl.Rule(data_redundancy['medium'] & degradation_level['low'] & error_history_rate['low'], error_likelihood['low'])
rule11 = ctrl.Rule(data_redundancy['medium'] & degradation_level['low'] & error_history_rate['medium'], error_likelihood['medium'])
rule12 = ctrl.Rule(data_redundancy['medium'] & degradation_level['low'] & error_history_rate['high'], error_likelihood['medium'])

rule13 = ctrl.Rule(data_redundancy['medium'] & degradation_level['medium'] & error_history_rate['low'], error_likelihood['medium'])
rule14 = ctrl.Rule(data_redundancy['medium'] & degradation_level['medium'] & error_history_rate['medium'], error_likelihood['medium'])
rule15 = ctrl.Rule(data_redundancy['medium'] & degradation_level['medium'] & error_history_rate['high'], error_likelihood['medium'])

rule16 = ctrl.Rule(data_redundancy['medium'] & degradation_level['high'] & error_history_rate['low'], error_likelihood['medium'])
rule17 = ctrl.Rule(data_redundancy['medium'] & degradation_level['high'] & error_history_rate['medium'], error_likelihood['medium'])
rule18 = ctrl.Rule(data_redundancy['medium'] & degradation_level['high'] & error_history_rate['high'], error_likelihood['high'])

rule19 = ctrl.Rule(data_redundancy['high'] & degradation_level['low'] & error_history_rate['low'], error_likelihood['low'])
rule20 = ctrl.Rule(data_redundancy['high'] & degradation_level['low'] & error_history_rate['medium'], error_likelihood['low'])
rule21 = ctrl.Rule(data_redundancy['high'] & degradation_level['low'] & error_history_rate['high'], error_likelihood['medium'])

rule22 = ctrl.Rule(data_redundancy['high'] & degradation_level['medium'] & error_history_rate['low'], error_likelihood['low'])
rule23 = ctrl.Rule(data_redundancy['high'] & degradation_level['medium'] & error_history_rate['medium'], error_likelihood['medium'])
rule24 = ctrl.Rule(data_redundancy['high'] & degradation_level['medium'] & error_history_rate['high'], error_likelihood['medium'])

rule25 = ctrl.Rule(data_redundancy['high'] & degradation_level['high'] & error_history_rate['low'], error_likelihood['medium'])
rule26 = ctrl.Rule(data_redundancy['high'] & degradation_level['high'] & error_history_rate['medium'], error_likelihood['medium'])
rule27 = ctrl.Rule(data_redundancy['high'] & degradation_level['high'] & error_history_rate['high'], error_likelihood['high'])

# create the control system
error_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20,rule21, rule22, rule23, rule24, rule25, rule26, rule27])

# create a simulation with the control system
error = ctrl.ControlSystemSimulation(error_ctrl)

while True:
    # compute sample input
    redundancy = input("\u001b[34m[I]\u001b[0m Enter the data redundancy : ")
    while True:
        if redundancy.lower() == 'q':
            sys.exit()
        try:
            redundancy = float(redundancy)
            break
        except:
            print("\u001b[31m[E]\u001b[0m Input must be a neumerical value")
            redundancy = input("\u001b[34m[I]\u001b[0m Enter the data redundancy : ")

    degradation_level = input("\u001b[34m[I]\u001b[0m Enter the degradation level : ")
    while True:
        if degradation_level.lower() == 'q':
            sys.exit()
        try:
            degradation_level = float(degradation_level)
            break
        except:
            print("\u001b[31m[E]\u001b[0m Input must be a neumerical value")
            degradation_level = input("\u001b[34m[I]\u001b[0m Enter the degradation level : ")

    error_rate = input("\u001b[34m[I]\u001b[0m Enter error history rate : ")
    while True:
        if error_rate.lower() == 'q':
            sys.exit()
        try:
            error_rate = float(error_rate)
            break
        except:
            print("\u001b[31m[E]\u001b[0m Input must be a neumerical value")
            error_rate = input("\u001b[34m[I]\u001b[0m Enter error history rate : ")


    error.input['data_redundancy'] = redundancy
    error.input['degradation_level'] = degradation_level
    error.input['error_history_rate'] = error_rate
    error.compute()

    print("\u001b[34m[O]\u001b[0m Error likelihood : ", end="")
    print(error.output['error_likelihood'])
    print()
    error_likelihood.view(sim=error)