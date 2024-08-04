import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

BP=ctrl.Antecedent(np.arange(80,180,1),label="Blood Pressure")
Temperature=ctrl.Antecedent(np.arange(98, 108, 1), label="Temperature")
Health_care=ctrl.Consequent(np.arange(0,100,1),label="Health Care",defuzzify_method="centroid")


BP['Normal']=fuzz.trimf(BP.universe,[80,100,120])
BP['Pre Hypertension']=fuzz.trimf(BP.universe,[90,115,140])
BP['High BP Stage 1']=fuzz.trimf(BP.universe,[100,130,160])
BP['High BP Stage 2']=fuzz.trimf(BP.universe,[110,140,170])
BP['Emergency']=fuzz.trimf(BP.universe,[130,155,180])


Temperature['Low']=fuzz.trimf(Temperature.universe, [96, 98, 100])
Temperature['Temp']=fuzz.trimf(Temperature.universe, [98, 100, 102])
Temperature['Temp High 1']=fuzz.trimf(Temperature.universe, [100, 102, 104])
Temperature['Temp High 2']=fuzz.trimf(Temperature.universe, [102, 104, 106])
Temperature['Emergency']=fuzz.trimf(Temperature.universe, [104, 106, 108])

Health_care.automf(3,names=['Good','Normal','Worst'])

rules=[]
rules.append(ctrl.Rule(BP['Normal'] & Temperature['Low'], Health_care['Good']))
rules.append(ctrl.Rule(BP['Normal'] & Temperature['Temp'], Health_care['Normal']))
rules.append(ctrl.Rule(BP['Normal'] & Temperature['Temp High 1'], Health_care['Normal']))
rules.append(ctrl.Rule(BP['Normal'] & Temperature['Temp High 2'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Normal'] & Temperature['Emergency'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Pre Hypertension'] & Temperature['Low'], Health_care['Good']))
rules.append(ctrl.Rule(BP['Pre Hypertension'] & Temperature['Temp'], Health_care['Normal']))
rules.append(ctrl.Rule(BP['Pre Hypertension'] & Temperature['Temp High 1'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Pre Hypertension'] & Temperature['Temp High 2'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Pre Hypertension'] & Temperature['Emergency'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 1'] & Temperature['Low'], Health_care['Normal']))
rules.append(ctrl.Rule(BP['High BP Stage 1'] & Temperature['Temp'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 1'] & Temperature['Temp High 1'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 1'] & Temperature['Temp High 2'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 1'] & Temperature['Emergency'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 2'] & Temperature['Low'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 2'] & Temperature['Temp'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 2'] & Temperature['Temp High 1'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 2'] & Temperature['Temp High 2'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['High BP Stage 2'] & Temperature['Emergency'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Emergency'] & Temperature['Low'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Emergency'] & Temperature['Temp'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Emergency'] & Temperature['Temp High 1'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Emergency'] & Temperature['Temp High 2'], Health_care['Worst']))
rules.append(ctrl.Rule(BP['Emergency'] & Temperature['Emergency'], Health_care['Worst']))


health_care_ctrl=ctrl.ControlSystem(rules)
health_care_sim=ctrl.ControlSystemSimulation(health_care_ctrl,clip_to_bounds=True)

# Input blood pressure values
blood_pressure_value = int(input("Enter the blood pressure value: "))
temp = int(input("Enter the temperature value: "))

health_care_sim.input['Blood Pressure']=blood_pressure_value
health_care_sim.input['Temperature']=temp

health_care_sim.compute()

print(health_care_sim.output['Health Care'])

BP.view()
Temperature.view()
Health_care.view(health_care_sim)
plt.tight_layout()
plt.show()






