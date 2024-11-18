import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung posisi mobil
def posisi(t):
    a = 2  # percepatan dalam m/s^2
    return 0.5 * a * t**2  # s(t) = 0.5 * a * t^2

# Waktu dari 0 hingga 100 detik
t_values = np.linspace(0, 100, 1000)  # 1000 titik waktu dari 0 hingga 100 detik
s_values = posisi(t_values)  # Hitung posisi untuk setiap waktu

# Visualisasi
plt.figure(figsize=(10, 5))
plt.plot(t_values, s_values, label='Posisi (s) terhadap Waktu (t)', color='blue')
plt.title('Grafik Posisi Mobil terhadap Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Posisi (meter)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.xlim(0, 100)
plt.ylim(0, max(s_values) + 1000)
plt.show()