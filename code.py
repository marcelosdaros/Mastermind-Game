import random

#Verifica se input do usuário é um inteiro
def validaInput():
    validacao = False
    while not validacao:
        try: 
            numeroTentativas = int(input("Digite quantas tentativas você deseja ter: "))
            validacao = True
        except:
            print("Número inválido, digite um inteiro")
    return numeroTentativas

#Verificação da formatação 
def validaFormatacao(tentativa):
    virgulas = tentativa.count(",")
    while (virgulas != 3):
        tentativa = input("Senha inválida: formatação incorreta, tente novamente separando as cores por vírgula (exemplo: amarelo,verde,azul,roxo): ")
        virgulas = tentativa.count(",")
    tentativa = tentativa.replace(" ", "").lower().split(",")
    for cor in tentativa:
        if cor.isalpha() == False:
            return validaCores(validaFormatacao(input("Senha inválida: apenas letras devem ser inseridas, tente novamente (cores possíveis: amarelo, verde, azul, roxo, vermelho, laranja): ")))
    return tentativa
    
#Verificação de repetição de cores e cores válidas, os indexes de contadorCores considera os mesmos indexes da lista cores, ex.: contadorCores[0] = amarelo, contadorCores[1] = verde, etc
def validaCores(tentativa):
    contadorCores = [0, 0, 0, 0, 0, 0]
    for cor in tentativa:
        if cor == "amarelo":
            contadorCores[0] += 1
        elif cor == "verde":
            contadorCores[1] += 1
        elif cor == "azul":
            contadorCores[2] += 1
        elif cor == "roxo":
            contadorCores[3] += 1
        elif cor == "vermelho":
            contadorCores[4] += 1
        elif cor == "laranja":
            contadorCores[5] += 1
        else:
            tentativa = validaCores(validaFormatacao(input("Senha inválida: cor inválida foi encontrada, tente novamente (cores possíveis: amarelo, verde, azul, roxo, vermelho, laranja): ")))
    return validaRepeticao(tentativa, contadorCores)

def validaRepeticao(tentativa, contadorCores):
    for contador in contadorCores:
        if contador > 1:
            tentativa = input("Senha inválida: não é permitido repetir cores, tente novamente (exemplo: amarelo,verde,azul,roxo): ")
            return validaCores(validaFormatacao(tentativa))
    return tentativa

#Retorna o pino referente à resposta da cor na tentativa
def verificaCorNaSenha(index, cor, senha):
    if senha[index] == cor:
        return "branco"
    elif cor in senha:
        return "preto"
    else:
        return "vazio"

#Verifica se existem pinos restantes de determinada cor antes do incremento
def verificaContagemMaximaAtingidaAntes(index, cor, contagemCoresPartida):
    if contagemCoresPartida[index] == 0:
        print(f"Você não possui nenhum pino {cor} restante, tente novamente sem usar essa cor.")
        return True
    return False

#Verifica se existem pinos restantes de determinada cor após o incremento
def verificaContagemMaximaAtingidaDepois(index, contagemCoresPartida):
    if contagemCoresPartida[index] == 0:
        return True
    return False

#Verifica se um pino de determinada cor está contida na senha
def corNaSenha(cor, senha):
    if cor in senha:
        return True
    return False

#Início
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nBem vindo ao jogo Mastermind!\nO jogo consiste em adivinhar uma senha que será gerada a cada partida, composta por quatro cores dentre as citadas: amarelo, verde, azul, roxo, vermelho, laranja.\nInicialmente será necessário inserir quantas tentativas você deseja ter para acertar a senha.\nExistem 10 pinos de cada cor no total para serem usados, não podendo exceder esse número por pino na partida.\nA cada tentativa será informado por pinos brancos se a cor está na posição certa, por pinos pretos se a cor está na presente na senha porém na posição errada e pela palavra 'vazio' se a cor não está contida na senha.\nNas suas tentativas insira 4 das cores citadas separadas por vírgula para tentar adivinhar a senha, sem repetir cor na mesma tentativa (exemplo: amarelo,verde,azul,roxo).\nBoa sorte!\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
cores = ["amarelo", "verde", "azul", "roxo", "vermelho", "laranja"]
senha = random.sample(cores, 4)
senha = ["amarelo", "verde", "azul", "roxo"]
contagemCoresPartida = [10, 10, 10, 10, 10, 10]
corFaltanteEstaNaSenha = False
corFaltante = ''
numeroTentativas = validaInput()

for i in range (numeroTentativas):
    tentativa = validaCores(validaFormatacao(input("Digite sua tentativa: ")))
    maximoAtingido = False
    resultado = []

    if tentativa == senha:
        print("\nParabéns! Você acertou a senha!")
        break
    else:
        for index, cor in enumerate(tentativa):
            if cor == "amarelo":
                if verificaContagemMaximaAtingidaAntes(0, cor, contagemCoresPartida):
                    break
                contagemCoresPartida[0] -= 1
                if verificaContagemMaximaAtingidaDepois(0, contagemCoresPartida):
                    corFaltanteEstaNaSenha = corNaSenha(cor, senha)
                    if corFaltanteEstaNaSenha:
                        corFaltante = cor
                        break
            elif cor == "verde":
                if verificaContagemMaximaAtingidaAntes(1, cor, contagemCoresPartida):
                    break
                contagemCoresPartida[1] -= 1
                if verificaContagemMaximaAtingidaDepois(1, contagemCoresPartida):
                    corFaltanteEstaNaSenha = corNaSenha(cor, senha)
                    if corFaltanteEstaNaSenha:
                        corFaltante = cor
                        break
            elif cor == "azul":
                if verificaContagemMaximaAtingidaAntes(2, cor, contagemCoresPartida):
                    break
                contagemCoresPartida[2] -= 1
                if verificaContagemMaximaAtingidaDepois(2, contagemCoresPartida):
                    corFaltanteEstaNaSenha = corNaSenha(cor, senha)
                    if corFaltanteEstaNaSenha:
                        corFaltante = cor
                        break
            elif cor == "roxo":
                if verificaContagemMaximaAtingidaAntes(3, cor, contagemCoresPartida):
                    break
                contagemCoresPartida[3] -= 1
                if verificaContagemMaximaAtingidaDepois(3, contagemCoresPartida):
                    corFaltanteEstaNaSenha = corNaSenha(cor, senha)
                    if corFaltanteEstaNaSenha:
                        corFaltante = cor
                        break
            elif cor == "vermelho":
                if verificaContagemMaximaAtingidaAntes(4, cor, contagemCoresPartida):
                    break
                contagemCoresPartida[4] -= 1
                if verificaContagemMaximaAtingidaDepois(4, contagemCoresPartida):
                    corFaltanteEstaNaSenha = corNaSenha(cor, senha)
                    if corFaltanteEstaNaSenha:
                        corFaltante = cor
                        break
            elif cor == "laranja":
                if verificaContagemMaximaAtingidaAntes(5, cor, contagemCoresPartida):
                    break
                contagemCoresPartida[5] -= 1
                if verificaContagemMaximaAtingidaDepois(5, contagemCoresPartida):
                    corFaltanteEstaNaSenha = corNaSenha(cor, senha)
                    if corFaltanteEstaNaSenha:
                        corFaltante = cor
                        break
            resultado.append(verificaCorNaSenha(index, cor, senha))

        if i == numeroTentativas-1:
            print(f"Senha incorreta e suas tentativas acabaram, portanto você perdeu nesta rodada.")
            break
        elif corFaltanteEstaNaSenha:
            print(f"Você não possui mais nenhum pino {corFaltante} restante e essa cor está contida na senha, portanto você perdeu nesta rodada.")
            break
        else:
            print(f"\nSenha incorreta, confira abaixo o resultado e os pinos restantes:\n{resultado}\n" +
            f"Você tem {numeroTentativas-1-i} chutes restantes\n" + 
            f"Você tem {contagemCoresPartida[0]} pinos amarelos disponíveis\n" +
            f"Você tem {contagemCoresPartida[1]} pinos verdes disponíveis\n" +
            f"Você tem {contagemCoresPartida[2]} pinos azuis disponíveis\n" +
            f"Você tem {contagemCoresPartida[3]} pinos roxos disponíveis\n" +
            f"Você tem {contagemCoresPartida[4]} pinos vermelhos disponíveis\n" +
            f"Você tem {contagemCoresPartida[5]} pinos laranjas disponíveis\n"
            )