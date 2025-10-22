def gerar_array(caminho_entrada): #Recebe o arquivo SPED é transforma ele em um array para facil manipulação
    resultado = []

    # Leitura do arquivo preservando campos vazios
    with open(caminho_entrada, 'r', encoding='latin1') as arquivo:
        for linha in arquivo:
            linha_limpa = linha.rstrip('\n')
            campos = linha_limpa.split('|')[1:-1]  # Remove apenas os delimitadores externos
            resultado.append(campos)

    return resultado

def salvar_array(array, caminho): #Salva o arquivo na mesma pasta do original
    caminho_saida = caminho.replace('.txt', '_smartSPED.txt')

    with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
        for sub_array in array:
            linha_formatada = "|" + "|".join(sub_array) + "|"
            arquivo.write(linha_formatada + "\n")

    return caminho_saida