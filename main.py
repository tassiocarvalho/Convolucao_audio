import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import convolve

# Função para aplicar o filtro passa baixa
def filtro_passa_baixa(audio, fs, cutoff_freq):
    # Criar um filtro passa baixa (filtro de média móvel)
    N = int(fs / cutoff_freq)
    filtro = np.ones(N) / N  # Média móvel
    audio_filtrado = convolve(audio, filtro, mode='same')  # Convolução
    return audio_filtrado

# Carregar o arquivo de áudio
fs, audio = wav.read('testando_audio.wav')

# Certificar-se de que o áudio esteja em formato mono (um único canal)
if len(audio.shape) > 1:
    audio = audio[:, 0]  # Selecionar o primeiro canal se for estéreo

# Definir a frequência de corte para o filtro passa baixa (por exemplo, 300 Hz)
cutoff_freq = 300  # Frequência de corte em Hz

# Aplicar o filtro passa baixa no áudio
audio_filtrado = filtro_passa_baixa(audio, fs, cutoff_freq)

# Salvar o áudio filtrado em um novo arquivo
wav.write('audio_filtrado.wav', fs, np.int16(audio_filtrado))

print("Filtragem concluída e áudio salvo como 'audio_filtrado.wav'")
