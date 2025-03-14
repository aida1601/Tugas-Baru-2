import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung posisi
def posisi(t):
    v = 20  # kecepatan konstan dalam m/s
    return v * t  # s(t) = v * t

# Waktu dari 0 hingga 300 detik (5 menit)
t_values = np.linspace(0, 300, 1000)  # 1000 titik waktu dari 0 hingga 300 detik
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
plt.xlim(0, 300)
plt.ylim(0, max(s_values) + 100)
plt.show()