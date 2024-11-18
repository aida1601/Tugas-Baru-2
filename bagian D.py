import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung posisi benda
def posisi(t):
    v0 = 60  # kecepatan awal dalam m/s
    a = -2.25  # perlambatan dalam m/s^2
    return v0 * t + 0.5 * a * t**2  # s(t) = v0 * t + 0.5 * a * t^2

# Waktu dari 0 hingga 20 detik
t_values = np.linspace(0, 20, 1000)  # 1000 titik waktu dari 0 hingga 20 detik
s_values = posisi(t_values)  # Hitung posisi untuk setiap waktu

# Visualisasi
plt.figure(figsize=(10, 5))
plt.plot(t_values, s_values, label='Posisi (s) terhadap Waktu (t)', color='blue')
plt.title('Grafik Posisi Benda terhadap Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Posisi (meter)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.xlim(0, 20)
plt.ylim(min(s_values) - 10, max(s_values) + 10)
plt.show()