# Divisor de Arquivos MP3

O Divisor de Arquivos MP3 é uma ferramenta em Python para dividir arquivos MP3 em segmentos menores. Este é muito importante como ferramenta para vários projetos.

## Uso

Para usar o Divisor de Arquivos MP3, siga as instruções abaixo:

1. **Requisitos de Instalação:**

   Certifique-se de ter instalado as dependências necessárias. Caso não a tenha instalado, você pode instalar as dependências usando o seguinte comando em seu terminal:

   ```shell
   pip install pydub
   ```
2. **Executando o código:**

    É necessário que vc tenha o arquivo de audio que pretendes dividir no mesmo diretório de sua aplicação. Posteriormente, abra o código e altere a seguinte linha com o nome real de seu arquivo ***.mp3***, ou seja, substitua o nome ***"split_mp3.mp3"*** pelo nome de seu arquivo de audio.

    ```python
    if __name__ == "__main__":
        
        # Substitua pelo nome do seu arquivo MP3
        arquivo_entrada = "split_mp3.mp3"

        # Tamanho do trecho em segundos  
        comprimento_trecho_segundos = 1300  
    ```
3. **Resultados:**
    O código irá dividir seu arquivo MP3 em segmentos menores de aproximadamente 20 MB e irá armazená-los no diretório ***"segmentos_MP3"***  no mesmo diretório do arquivo original# split_audio

## Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Você pode criar pull requests para corrigir erros ou adicionar recursos novos.

## Autor
Este projeto foi desenvolvido por Marcello Pojucan, você pode entrar em contato com o autor através do seu perfil no GitHub.

## Licença
Este projeto é distribuído sob a licença GNU AGPL. Consulte o arquivo LICENSE.md ou o link: [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) para obter mais detalhes.


