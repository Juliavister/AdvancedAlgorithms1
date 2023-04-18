import matplotlib.pyplot as plt
import numpy as np

brute_force_data = np.array([0.000178, 0.000624, 0.0007739])
fsm_data = np.array([0.0001428, 0.00033, 0.0004649])
kmp_data = np.array([0.001630, 0.001619, 0.001732])
sunday_data = np.array([0.000219, 0.000134229, 0.00011277])
gusfield_z_data = np.array([0.001910, 0.002005, 0.002432])
rabin_karp_data = np.array([0.0043661, 0.003900, 0.003969])

pattern_lengths = np.array([46, 96, 130])

plt.plot(pattern_lengths, brute_force_data, label='Brute Force')
plt.plot(pattern_lengths, fsm_data, label='FSM')
plt.plot(pattern_lengths, kmp_data, label='KMP')
plt.plot(pattern_lengths, sunday_data, label='Sunday')
plt.plot(pattern_lengths, gusfield_z_data, label='Gusfield Z')
plt.plot(pattern_lengths, rabin_karp_data, label='Rabin Karp')

plt.xlabel('Pattern Length')
plt.ylabel('Time (s)')
plt.legend()

plt.show()