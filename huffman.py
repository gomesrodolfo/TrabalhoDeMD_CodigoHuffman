#gera tabela de frequencia 
def frequencia(arq_freq):
    tab_freq = {}
    arq = open(arq_freq, "rt")
    linha = arq.readline()
    while linha != "":
        for i in linha:
            if i in tab_freq:
                tab_freq[i] += 1
            else:
                tab_freq[i] = 1

        linha = arq.readline()

    print("Tabela de Frequencia de Caracteres")    
    arq.close()  

    return tab_freq  

#tabela com codigos dos elementos
def tab_codificacao(arq_tabela):
    dic = {}
    lst_aux = []
    arq = open(arq_tabela, "rt")
    linha = arq.readline()

    while linha != "":
        lst_aux = linha.split()
        dic[lst_aux[0]] = lst_aux[1]
        lst_aux = []
        linha = arq.readline()       

    arq.close()

    return dic

def codifica_texto(arq_codificar, dic):
    texto_cod = ""
    lst_aux = []
    arq = open(arq_codificar, "rt")
    linha = arq.readline()
    while linha != "":
        for i in linha:
            if i in dic:
                lst_aux.append(i)
        linha = arq.readline()
    
    for j in lst_aux:
        texto_cod += dic[j] 

    arq.close()
    print(linha)
    return texto_cod

def multiplo(valor):
    v = 0
    if v // 8 == 0:
        return True
    else: 
        return False

def decodifica(arq_codificado, arq_tabela):
    dic = tab_codificacao(arq_tabela)
 
    lst_final = []
    aux = []
    texto = ""
    arq = open(arq_codificado, "rt")
    linha = arq.readline()

    while (linha != ""):
        for i in range(len(linha)):
            texto += linha[i]

        for n in texto:
            aux.append(n)

        for chave, valor in dic.items():
            if valor == texto:
                lst_final.append(chave)
                texto = ""

        print(lst_final)
        linha = arq.readline()

    return 0

def main():
    #ABERTURA DE ARQUIVOS
    arq_codificado = "arq_codificado.txt" #arquivo codificado 
    arq_tabela = "arquivo.txt" #arquivo contendo a tabela ASC 2
    arq_freq = "texto.txt" #arquivo para verificar frequencia
    arq_codificar = "texto_codificar.txt" #arquivo para codificar

    #FUNÇÕES
    freq = frequencia(arq_freq)
    dic = tab_codificacao(arq_tabela)
    codifica_texto(arq_codificar, dic)
    decodifica(arq_codificado, arq_tabela)

    #print(frequencia(arq_freq))
    #print(codifica_texto(arq_codificar, dic))
    multiplo(freq)

    #print(dic)

if __name__ == "__main__":
        main()