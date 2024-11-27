import numpy as np
from scipy.io.wavfile import read, write

# Função para realizar convolução manualmente
def convolucao_manual(audio, resposta_impulso):
    # Tamanho dos sinais
    len_audio = len(audio)
    len_impulso = len(resposta_impulso)
    
    # Criar um vetor de saída para o áudio resultante
    output_length = len_audio + len_impulso - 1
    resultado = np.zeros(output_length)
    
    # Realizar a convolução manual
    for i in range(len_audio):
        resultado[i:i+len_impulso] += audio[i] * resposta_impulso
        
    return resultado

# Carregar o áudio original e a resposta ao impulso
fs_audio, audio = read('audio_original.wav')  # Substitua com o caminho do seu arquivo de áudio
fs_impulso, impulso_resposta = read('impulse_response.wav')  # Substitua com o caminho do arquivo IR

# Verificar se as taxas de amostragem são compatíveis
if fs_audio != fs_impulso:
    raise ValueError("As taxas de amostragem devem ser iguais.")

# Convoluir os dois sinais
audio_reverberado = convolucao_manual(audio, impulso_resposta)

# Garantir que os valores do áudio não ultrapassem o intervalo de inteiros de 16 bits
audio_reverberado = np.clip(audio_reverberado, -32768, 32767).astype(np.int16)

# Salvar o áudio resultante
write('audio_com_eco.wav', fs_audio, audio_reverberado)
print("Áudio com reverberação salvo como 'audio_com_eco.wav'")
