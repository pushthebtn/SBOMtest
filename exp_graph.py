!pip install -r requirements.txt

import numpy as np
import matplotlib.pyplot as plt

# Функция для логистической кривой
def logistic_function(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# Параметры для графиков
x = np.linspace(0, 10, 100)
L_values = [10, 20, 30]  # Разные предельные значения
k_values = [0.5, 1, 2]    # Разные коэффициенты роста
x0_values = [5, 6, 7]     # Разные сдвиги по оси x

# Строим графики
plt.figure(figsize=(10, 6))
for L in L_values:
    for k in k_values:
        for x0 in x0_values:
            y = logistic_function(x, L, k, x0)
            plt.plot(x, y, label=f'L={L}, k={k}, x0={x0}')

plt.title('Logistic Growth Curves')
plt.xlabel('Rating')
plt.ylabel('Weight')
plt.legend()
plt.grid(True)
plt.show()
