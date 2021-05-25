#!/usr/bin/python3

def cifrado() -> str:
    """ Entrada do arquivo ou frase cifrada """
    
    print('Seja Bem vindo ao nosso programa de brute force César.\nCaso precise de ajuda digite --help')
    escolha= input('Digite o que você deseja (frase) ou (arquivo) ')
    
    if escolha == '--help':
        print('Digite (arq) ou (arquivo) para decifrar um arquivo\nDigite (frase) para decifrar frase')
       
    elif escolha == 'arq' or escolha == 'arquivo':
        arquivo_cifrada= open(input('Digite o nome do arquivo: '))
        entrada_decifra(arquivo_cifrada,  escolha)
    elif escolha == 'frase':
        frase= input('Digite a frase cifrada: ')
        entrada_decifra(frase, escolha)
        
    else:
        opcao= input('Opção invalida, tente novamente, caso tenha duvida, digite --help: ')
        if opcao == '--help':
            print('Digite (arq) ou (arquivo) para decifrar um arquivo\nDigite (frase) para decifrar frase')
        
        else:
            cifrado()
            
def entrada_decifra(arq_ou_frase, escolha_arq_frase) -> str:
    """ Executa o brute force de César """

    if escolha_arq_frase == 'arq' or escolha_arq_frase == 'arquivo':
        frase_cifra = arq_ou_frase.readline()
        mensagem_decifrada = []
        rota= 1
        arq_limpo = open('Brute_force.txt', 'a+')
        while rota <= 26:  #26 pq é o numero de possibilidades num alfabeto
            for letra in frase_cifra:                
                if letra in './: ':
                    mensagem_decifrada.append(letra)
                else:
                    mensagem_decifrada.append(chr(ord(letra) - rota))
            mensagem_decifrada.append('\n')
            rota += 1
        mensagem_limpa= ''.join(mensagem_decifrada)
        arq_limpo.writelines(mensagem_limpa)
        
        arq_limpo.close()
        arq_ou_frase.close()

    
    else:
        mensagem_decifrada= []
        rota= 1
        while rota <= 26:  #26 pq é o numero de possibilidades num alfabeto
            for letra in arq_ou_frase:                
                if letra in './: ':
                    mensagem_decifrada.append(letra)
                else:
                    mensagem_decifrada.append(chr(ord(letra) - rota))
            mensagem_decifrada.append('\n')
            rota += 1
        mensagem_limpa= ''.join(mensagem_decifrada)
        print(mensagem_limpa)
            

cifrado()

