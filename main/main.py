from matplotlib import pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


angle = ctrl.Antecedent(np.arange(-90, 91, 1), 'angle')
angular_velocity = ctrl.Antecedent(np.arange(-5, 6, 1), 'angular_velocity')

angle['N'] = fuzz.trimf(angle.universe, [-90, -90, 0])
angle['Z'] = fuzz.trimf(angle.universe, [-90, 0, 90])
angle['P'] = fuzz.trimf(angle.universe, [0, 90, 90])


angular_velocity['N'] = fuzz.trimf(angular_velocity.universe, [-5, -5, 0])
angular_velocity['Z'] = fuzz.trimf(angular_velocity.universe, [-5, 0, 5])
angular_velocity['P'] = fuzz.trimf(angular_velocity.universe, [0, 5, 5])


output = ctrl.Consequent(np.arange(-1, 2, 1), 'output', defuzzify_method='centroid')

output['NL'] = fuzz.trimf(output.universe, [-1, -1, 0])
output['Z'] = fuzz.trimf(output.universe, [-1, 0, 1])
output['PL'] = fuzz.trimf(output.universe, [0, 1, 1])

rule1 = ctrl.Rule(angle['N'] & angular_velocity['N'], output['PL'])
rule2 = ctrl.Rule(angle['N'] & angular_velocity['Z'], output['PL'])
rule3 = ctrl.Rule(angle['N'] & angular_velocity['P'], output['Z'])

fuzzy_system = ctrl.ControlSystem([rule1, rule2, rule3])
fuzzy_controller = ctrl.ControlSystemSimulation(fuzzy_system)

fuzzy_controller.input['angle'] = -30
fuzzy_controller.input['angular_velocity'] = 3
fuzzy_controller.compute()

print("Output:", fuzzy_controller.output['output'])

angle.view()
angular_velocity.view()
output.view()
rule1.view()
rule2.view()
rule3.view()
plt.show()
