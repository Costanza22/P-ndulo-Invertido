# Controle de Pêndulo Invertido com Lógica Fuzzy e Redes Neurais

Este projeto visa implementar e comparar três sistemas de controle distintos para gerenciar a estabilidade de um pêndulo invertido montado sobre um carro: Sistema de Inferência Fuzzy (FIS), Genético-Fuzzy e Neuro-Fuzzy.

## Pré-requisitos

- [Python](https://www.python.org/) (versão x.x)
- [Biblioteca scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/)
- [Biblioteca TensorFlow](https://www.tensorflow.org/) (para o Sistema Neuro-Fuzzy)
- [Outras dependências]


terminal install - pip install scikit-fuzzy

from doctest import OutputChecker
from matplotlib import pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
