import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import convolve
import matplotlib.pyplot as plt

# Função para aplicar o filtro passa baixa
def filtro_passa_baixa(audio, fs, cutoff_freq):
    # Criar um filtro passa baixa (filtro de média móvel)
    N = int(fs / cutoff_freq)
    filtro = np.ones(N) / N  # Média móvel
    audio_filtrado = convolve(audio, filtro, mode='same')  # Convolução
    return audio_filtrado, filtro

# Carregar o arquivo de áudio
fs, audio = wav.read('testando_audio.wav')

# Certificar-se de que o áudio esteja em formato mono (um único canal)
if len(audio.shape) > 1:
    audio = audio[:, 0]  # Selecionar o primeiro canal se for estéreo

# Definir a frequência de corte para o filtro passa baixa (por exemplo, 300 Hz)
cutoff_freq = 300  # Frequência de corte em Hz

# Aplicar o filtro passa baixa no áudio
audio_filtrado, filtro = filtro_passa_baixa(audio, fs, cutoff_freq)

# Salvar o áudio filtrado em um novo arquivo
wav.write('audio_filtrado.wav', fs, np.int16(audio_filtrado))

# Plotando os gráficos
# Criação do eixo de tempo (baseado no número de amostras e taxa de amostragem)
t = np.arange(len(audio)) / fs

plt.figure(figsize=(10, 8))

# Gráfico 1: Sinal de entrada (áudio original)
plt.subplot(3, 1, 1)
plt.plot(t, audio, color='blue')
plt.title("Sinal de Entrada (Áudio Original)")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")

# Gráfico 2: Impulso do filtro (h(t))
plt.subplot(3, 1, 2)
plt.plot(filtro, color='green')
plt.title("Filtro Passa Baixa h(t)")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")

# Gráfico 3: Sinal resultante (áudio filtrado)
plt.subplot(3, 1, 3)
plt.plot(t, audio_filtrado, color='red')
plt.title("Sinal Resultante (Áudio Filtrado)")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")

# Ajuste de layout
plt.tight_layout()

# Exibir os gráficos
plt.show()

print("Filtragem concluída e áudio salvo como 'audio_filtrado.wav'")
