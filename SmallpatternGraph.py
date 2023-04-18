import matplotlib.pyplot as plt
import numpy as np

brute_force_data = np.array([0.00032, 0.00041, 0.00059])
fsm_data = np.array([0.00019, 0.00029, 0.00035])
kmp_data = np.array([0.0016, 0.0017, 0.00182])
sunday_data = np.array([0.00062, 0.00079, 0.000333])
gusfield_z_data = np.array([0.002018, 0.001918, 0.002090])
rabin_karp_data = np.array([0.00316, 0.0027, 0.00288])

pattern_lengths = np.array([4,7,9])

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

