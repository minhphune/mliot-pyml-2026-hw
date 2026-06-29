import numpy as np
import matplotlib.pyplot as plt

p_B = np.linspace(0.001, 0.2, 200)
p_pos_givenB = 0.99
p_pos_givenNB = 0.05
print(round((0.99*0.01) / (0.99*0.01 + 0.05*0.99), 4)) #Task 1

p_B_givenpos = (p_pos_givenB * p_B) / (p_pos_givenB * p_B + p_pos_givenNB * (1-p_B))

p_NB_givenNpos = ((1-p_pos_givenNB) * (1-p_B)) / ((1-p_pos_givenNB) * (1-p_B) + (1-p_pos_givenB) * p_B)

plt.plot(p_B, p_B_givenpos, label="True Positive", linewidth=2)
plt.plot(p_B, p_NB_givenNpos, label="True Negative", linewidth=2)
plt.legend()
plt.show()