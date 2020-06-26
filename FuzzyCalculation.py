# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:39:30 2020

@author: Janusz
"""
import pandas as pd

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


df = pd.read_csv("scaledChampionsData.csv") 

df.drop('Unnamed: 0', axis=1, inplace=True)







fHP = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'fHP')


fMEANHP = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'fMEANHP')



fPoints = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'fPoints')



fHP['poor'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.2)
fHP['mediocre'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.4)
fHP['average'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.6)
fHP['decent'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 0.8)
fHP['good'] = fuzz.gbellmf(fHP.universe, 0.025, 0.95, 1.0)




fMEANHP['poor'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.2)
fMEANHP['mediocre'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.4)
fMEANHP['average'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.6)
fMEANHP['decent'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 0.8)
fMEANHP['good'] = fuzz.gbellmf(fMEANHP.universe, 0.025, 0.95, 1.0)

# fSuits['hearts'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesHearts.get()))
# fSuits['tiles'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesTiles.get()))
# fSuits['clovers'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesClovers.get()))
# fSuits['pikes'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, float(counterPreferencesPikes.get()))
# fSuits['xd'] = fuzz.gbellmf(fSuits.universe, 0.025, 0.95, 4.3)


fPoints['poor'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.2)
fPoints['mediocre'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.4)
fPoints['average'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.6)
fPoints['decent'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 0.8)
fPoints['good'] = fuzz.gbellmf(fPoints.universe, 0.025, 0.95, 1.0)



# fPoints.view()



# fPoints.automf(5)












rule1 = ctrl.Rule(fMEANHP['good'] & fHP['good'], fPoints['good'])
rule2 = ctrl.Rule(fMEANHP['good'] & fHP['decent'], fPoints['good'])
rule3 = ctrl.Rule(fMEANHP['good'] & fHP['average'], fPoints['decent'])
rule4 = ctrl.Rule(fMEANHP['good'] & fHP['mediocre'], fPoints['decent'])
rule5 = ctrl.Rule(fMEANHP['good'] & fHP['poor'], fPoints['average'])


rule6 = ctrl.Rule(fMEANHP['decent'] & fHP['good'], fPoints['good'])
rule7 = ctrl.Rule(fMEANHP['decent'] & fHP['decent'], fPoints['decent'])
rule8 = ctrl.Rule(fMEANHP['decent'] & fHP['average'], fPoints['decent'])
rule9 = ctrl.Rule(fMEANHP['decent'] & fHP['mediocre'], fPoints['average'])
rule10 = ctrl.Rule(fMEANHP['decent'] & fHP['poor'], fPoints['mediocre'])


rule11 = ctrl.Rule(fMEANHP['average'] & fHP['good'], fPoints['decent'])
rule12 = ctrl.Rule(fMEANHP['average'] & fHP['decent'], fPoints['average'])
rule13 = ctrl.Rule(fMEANHP['average'] & fHP['average'], fPoints['average'])
rule14 = ctrl.Rule(fMEANHP['average'] & fHP['mediocre'], fPoints['average'])
rule15 = ctrl.Rule(fMEANHP['average'] & fHP['poor'], fPoints['poor'])

rule16 = ctrl.Rule(fMEANHP['mediocre'] & fHP['good'], fPoints['decent'])
rule17 = ctrl.Rule(fMEANHP['mediocre'] & fHP['decent'], fPoints['average'])
rule18 = ctrl.Rule(fMEANHP['mediocre'] & fHP['average'], fPoints['mediocre'])
rule19 = ctrl.Rule(fMEANHP['mediocre'] & fHP['mediocre'], fPoints['mediocre'])
rule20 = ctrl.Rule(fMEANHP['mediocre'] & fHP['poor'], fPoints['poor'])

rule21 = ctrl.Rule(fMEANHP['poor'] & fHP['good'], fPoints['average'])
rule22 = ctrl.Rule(fMEANHP['poor'] & fHP['decent'], fPoints['mediocre'])
rule23 = ctrl.Rule(fMEANHP['poor'] & fHP['average'], fPoints['mediocre'])
rule24 = ctrl.Rule(fMEANHP['poor'] & fHP['mediocre'], fPoints['poor'])
rule25 = ctrl.Rule(fMEANHP['poor'] & fHP['poor'], fPoints['poor'])

rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
         rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
         rule20, rule21, rule22, rule23, rule24, rule25]


# for i in range(1,26,1):
#     print("rule"+"%d"%i, end= ", ")


tanksPreferencesRulebase = ctrl.ControlSystem(rules)


    

    
    
    
    

    
tanksPreferences = ctrl.ControlSystemSimulation(tanksPreferencesRulebase)



PreferencePoints = [0] * 5



for i in range(1,5):

    
    
    
    tanksPreferences.input['fMEANHP'] = 1
    tanksPreferences.input['fHP'] = 1
    tanksPreferences.compute()
    
    
    PreferencePoints[i] = tanksPreferences.output['fPoints']

