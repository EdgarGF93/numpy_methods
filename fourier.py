import matplotlib.pyplot as plt
import numpy as np

DT = 0.001
MAX_FREQ = 1 / DT
T0 = 0
TF = 1

FREQUENCY_1 = 20
PERIOD_1 = 1 / FREQUENCY_1

FREQUENCY_2 = 50
PERIOD_2 = 1 / FREQUENCY_2

FREQUENCY_3 = 200
PERIOD_3 = 1 / FREQUENCY_3

AMPLITUDE_NOISE_1 = 1
AMPLITUDE_NOISE_2 = 0.1

temps = np.arange(T0, TF, DT)
n = len(temps)
freqs = np.linspace(0, 1/DT, n)

noise_1 = np.random.random(size=(len(temps))) * AMPLITUDE_NOISE_1 * 2 - AMPLITUDE_NOISE_1
noise_2 = np.random.random(size=(len(temps))) * AMPLITUDE_NOISE_2 * 2 - AMPLITUDE_NOISE_2

y1 = np.sin(2 * np.pi * FREQUENCY_1 * temps)
y2 = np.sin(2 * np.pi * FREQUENCY_2 * temps)
y3 = np.sin(2 * np.pi * FREQUENCY_3 * temps)

y_clean = y1 + y2 + y3
y_noisy = y1 + y2 + y3 + noise_1 + noise_2

# plt.plot(t,y_clean, label='clean')
# plt.plot(t,y_noisy, label='noisy')
# plt.show()


fhat = np.fft.fft(y_noisy, n=10)

print(fhat)
print(fhat[0])
print(np.conj(fhat[0]))

PSD = fhat * np.conj(fhat) / n

# plt.plot(freqs, PSD)
# plt.xlim([0,freqs[int(n / 2)]])
# plt.show()