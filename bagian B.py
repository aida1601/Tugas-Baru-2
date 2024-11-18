import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung posisi benda jatuh bebas
def posisi(t):
    g = 9.81  # percepatan gravitasi dalam m/s^2
    return 0.5 * g * t**2  # s(t) = 0.5 * g * t^2

# Waktu dari 0 hingga 120 detik (2 menit)
t_values = np.linspace(0, 120, 1000)  # 1000 titik waktu dari 0 hingga 120 detik
s_values = posisi(t_values)  # Hitung posisi untuk setiap waktu

# Visualisasi
plt.figure(figsize=(10, 5))
plt.plot(t_values, s_values, label='Posisi (s) terhadap Waktu (t)', color='blue')
plt.title('Grafik Posisi Benda Jatuh Bebas terhadap Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Posisi (meter)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.xlim(0, 120)
plt.ylim(0, max(s_values) + 1000)
plt.show()