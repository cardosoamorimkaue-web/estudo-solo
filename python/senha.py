#senha = []

s = input('Digite uma senha: ')

while True:    
    T = input('Digite a Senha novamente: ')
    if T == s:
        print('senha correta')
        break
    else:
        print('senha incorreta tente novamente')
        
   