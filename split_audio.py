from pydub import AudioSegment
import os

def split_mp3(arquivo_entrada, comprimento_trecho_segundos):
    # Verifique se o arquivo de entrada existe
    if not os.path.isfile(arquivo_entrada):
        print(f"O arquivo {arquivo_entrada} não foi encontrado.")
        return
    
    # Crie um diretório para armazenar os pedaços divididos
    diretorio_saida = 'segmentos_MP3'
    os.makedirs(diretorio_saida, exist_ok = True)
    
    # Carregue o arquivo MP3 de entrada
    audio = AudioSegment.from_mp3(arquivo_entrada)
    
    trecho_comprimento = comprimento_trecho_segundos * 1000  # Converta para milissegundos
    duracao_total = len(audio)
    
    numero_techo_comprimento = 0
    tempo_inicial = 0

    while tempo_inicial < duracao_total:
        tempo_final = min(tempo_inicial + trecho_comprimento, duracao_total)
        
        # Extraia o trecho atual
        trecho = audio[tempo_inicial:tempo_final]
        
        # Salve o trecho como um novo arquivo MP3
        arquivo_saida = os.path.join(diretorio_saida, f"segmento_{numero_techo_comprimento}.mp3")
        trecho.export(arquivo_saida, format = "mp3")
        
        tempo_inicial = tempo_final
        numero_techo_comprimento += 1

    print(f"{numero_techo_comprimento} segmentos em MP3 criadas com sucesso.")

if __name__ == "__main__":
    arquivo_entrada = "231018-reuniao.mp3"  # Substitua pelo nome do seu arquivo MP3
    comprimento_trecho_segundos = 1300  # Tamanho do trecho em segundos

    split_mp3(arquivo_entrada, comprimento_trecho_segundos)