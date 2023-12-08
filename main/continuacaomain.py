from doctest import OutputChecker
from matplotlib import pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

car_position = ctrl.Antecedent(np.arange(-50, 51, 1), 'car_position')
linear_velocity = ctrl.Antecedent(np.arange(-5, 6, 1), 'linear_velocity')

car_position['N'] = fuzz.trimf(car_position.universe, [-50, -50, 0])
car_position['Z'] = fuzz.trimf(car_position.universe, [-50, 0, 50])
car_position['P'] = fuzz.trimf(car_position.universe, [0, 50, 50])

linear_velocity['N'] = fuzz.trimf(linear_velocity.universe, [-5, -5, 0])
linear_velocity['Z'] = fuzz.trimf(linear_velocity.universe, [-5, 0, 5])
linear_velocity['P'] = fuzz.trimf(linear_velocity.universe, [0, 5, 5])

rule4 = ctrl.Rule(car_position['N'] & linear_velocity['N'],output['PL'])
rule5 = ctrl.Rule(car_position['N'] & linear_velocity['Z'],output['Z'])
rule6 = ctrl.Rule(car_position['N'] & linear_velocity['P'],output['NL'])
rule7 = ctrl.Rule(car_position['Z'] & linear_velocity['N'],output['PL'])
rule8 = ctrl.Rule(car_position['Z'] & linear_velocity['Z'],output['Z'])
rule9 = ctrl.Rule(car_position['Z'] & linear_velocity['P'],output['NL'])
rule10 = ctrl.Rule(car_position['P'] & linear_velocity['N'],output['P'])
rule11 = ctrl.Rule(car_position['P'] & linear_velocity['Z'],output['Z'])
rule12 = ctrl.Rule(car_position['P'] & linear_velocity['P'],output['NL'])


fuzzy_controller = ctrl.ControlSystemSimulation(fuzzy_system)

fuzzy_controller.input['car_position'] = -20
fuzzy_controller.input['linear_velocity'] = 4
fuzzy_controller.compute()


print("Output:", fuzzy_controller.output['output'])


car_position.view()
linear_velocity.view()
OutputChecker.view()

rule4.view()
rule5.view()
rule6.view()
rule7.view()
rule8.view()
rule9.view()
rule10.view()
rule11.view()
rule12.view()

plt.show()
