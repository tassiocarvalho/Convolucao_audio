# Importando as bibliotecas necessárias
import numpy as np  # Para operações matemáticas e criação de arrays
import scipy.io.wavfile as wav  # Para ler e escrever arquivos WAV
from scipy.signal import convolve  # Para realizar a convolução (filtro)
import matplotlib.pyplot as plt  # Para plotar os gráficos

# Função para aplicar o filtro passa baixa
def filtro_passa_baixa(audio, fs, cutoff_freq):
    """
    Aplica um filtro passa baixa no sinal de áudio.

    Parâmetros:
    audio (ndarray): O sinal de áudio (uma lista de amplitudes de amostras).
    fs (int): A taxa de amostragem do áudio (em Hz).
    cutoff_freq (int): A frequência de corte do filtro passa baixa (em Hz).

    Retorna:
    audio_filtrado (ndarray): O sinal de áudio após a filtragem.
    filtro (ndarray): O filtro usado (resposta ao impulso).
    """
    # Calcular o número de amostras do filtro baseado na frequência de corte
    N = int(fs / cutoff_freq)  # Número de amostras no filtro baseado na frequência de corte
    filtro = np.ones(N) / N  # Filtro de média móvel, criando um vetor com N elementos com valor 1/N

    # Aplicar a convolução entre o áudio e o filtro
    audio_filtrado = convolve(audio, filtro, mode='same')  # A convolução aplica o filtro no áudio

    return audio_filtrado, filtro  # Retorna o áudio filtrado e o filtro usado

# Carregar o arquivo de áudio
fs, audio = wav.read('testando_audio.wav')  # Lê o arquivo WAV e retorna a taxa de amostragem (fs) e os dados de áudio

# Certificar-se de que o áudio está em formato mono (um único canal)
if len(audio.shape) > 1:
    audio = audio[:, 0]  # Se o áudio for estéreo, seleciona o primeiro canal (mono)

# Definir a frequência de corte para o filtro passa baixa (por exemplo, 300 Hz)
cutoff_freq = 300  # Frequência de corte em Hz, ajustando para filtrar frequências acima disso

# Aplicar o filtro passa baixa no áudio
audio_filtrado, filtro = filtro_passa_baixa(audio, fs, cutoff_freq)  # Chama a função para filtrar o áudio

# Salvar o áudio filtrado em um novo arquivo
wav.write('audio_filtrado.wav', fs, np.int16(audio_filtrado))  # Converte o áudio filtrado para o formato int16 e salva

# Plotando os gráficos
# Criação do eixo de tempo (baseado no número de amostras e taxa de amostragem)
t = np.arange(len(audio)) / fs  # Gera um vetor de tempo para o gráfico (tempo = amostras / taxa de amostragem)

plt.figure(figsize=(10, 8))  # Define o tamanho da figura dos gráficos

# Gráfico 1: Sinal de entrada (áudio original)
plt.subplot(3, 1, 1)  # Define a posição do gráfico na figura (3 linhas, 1 coluna, 1º gráfico)
plt.plot(t, audio, color='blue')  # Plota o áudio original com cor azul
plt.title("Sinal de Entrada (Áudio Original)")  # Título do gráfico
plt.xlabel("Tempo [s]")  # Rótulo do eixo X (tempo)
plt.ylabel("Amplitude")  # Rótulo do eixo Y (amplitude do sinal)

# Gráfico 2: Impulso do filtro (h(t))
plt.subplot(3, 1, 2)  # Define a posição do gráfico (3 linhas, 1 coluna, 2º gráfico)
plt.plot(filtro, color='green')  # Plota o filtro (resposta ao impulso) com cor verde
plt.title("Filtro Passa Baixa h(t)")  # Título do gráfico
plt.xlabel("Amostras")  # Rótulo do eixo X (número de amostras)
plt.ylabel("Amplitude")  # Rótulo do eixo Y (amplitude do filtro)

# Gráfico 3: Sinal resultante (áudio filtrado)
plt.subplot(3, 1, 3)  # Define a posição do gráfico (3 linhas, 1 coluna, 3º gráfico)
plt.plot(t, audio_filtrado, color='red')  # Plota o áudio filtrado com cor vermelha
plt.title("Sinal Resultante (Áudio Filtrado)")  # Título do gráfico
plt.xlabel("Tempo [s]")  # Rótulo do eixo X (tempo)
plt.ylabel("Amplitude")  # Rótulo do eixo Y (amplitude do áudio filtrado)

# Ajuste de layout
plt.tight_layout()  # Ajusta automaticamente os espaçamentos entre os gráficos para que não sobreponham

# Exibir os gráficos
plt.show()  # Exibe os gráficos na tela

# Mensagem indicando que a filtragem foi concluída
print("Filtragem concluída e áudio salvo como 'audio_filtrado.wav'")
