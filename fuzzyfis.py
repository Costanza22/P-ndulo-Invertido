import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

angle = ctrl.Antecedent(np.arange(-180, 181, 1), 'angle')
angular_velocity = ctrl.Antecedent(np.arange(-10, 11, 1), 'angular_velocity')
output = ctrl.Consequent(np.arange(-10, 11, 1), 'output')

angle['negative'] = fuzz.trimf(angle.universe, [-180, -90, 0])
angle['zero'] = fuzz.trimf(angle.universe, [-90, 0, 90])
angle['positive'] = fuzz.trimf(angle.universe, [0, 90, 180])

rule1 = ctrl.Rule(antecedent=((angle['negative'] & angular_velocity['some_condition']) |
                              (angle['zero'] & angular_velocity['some_condition']) |
                              (angle['positive'] & angular_velocity['some_condition'])),
                  consequent=output['some_effect'])


fis_system = ctrl.ControlSystem([rule1])
fuzzy_controller = ctrl.ControlSystemSimulation(fis_system)

fuzzy_controller.input['angle'] = -30
fuzzy_controller.input['angular_velocity'] = 5

fuzzy_controller.compute()

print(fuzzy_controller.output['output'])
