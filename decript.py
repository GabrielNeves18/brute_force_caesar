#!/usr/bin/python3

def cifrado() -> str:
    """ Entrada do arquivo ou frase cifrada """
    
    print('Seja Bem vindo ao nosso programa de brute force César.\nCaso precise de ajuda digite --help')
    escolha= input('Digite o que você deseja (frase) ou (arquivo) ')
    
    if escolha == '--help':
        print('Digite (arq) ou (arquivo) para decifrar um arquivo\nDigite (frase) para decifrar frase')
       
    elif escolha == 'arq' or escolha == 'arquivo':
        arquivo_cifrada= open(input('Digite o nome do arquivo: '))
        decifrar(arquivo_cifrada,  escolha)
    elif escolha == 'frase':
        frase= input('Digite a frase cifrada: ')
        decifrar(frase, escolha)
        
    else:
        opcao= input('Opção invalida, tente novamente, caso tenha duvida, digite --help: ')
        if opcao == '--help':
            print('Digite (arq) ou (arquivo) para decifrar um arquivo\nDigite (frase) para decifrar frase')
        
        else:
            cifrado()
            
def decifrar(arq_ou_frase, escolha_arq_frase) -> str:
    """ Executa o brute force de César """
    
    mensagem_cifrada = []
    
    if escolha_arq_frase == 'arq' or escolha_arq_frase == 'arquivo':
        rota = 1
        while rota <= 26:  #26 pq é o numero de possibilidades num alfabeto
            
            for frase in arq_ou_frase:
                for letra in frase:                
                    if letra in './: ':
                        mensagem_cifrada.append(letra)
                    else:
                        mensagem_cifrada.append(chr(ord(letra) - rota))
                print(''.join(mensagem_cifrada))
        rota += 1
    
    else:
        print(arq_ou_frase,'\n')
            
cifrado()

