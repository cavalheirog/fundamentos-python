# Programa simples de login em Python com limite de tentativas de senha
# O usuário tem até 3 tentativas para acertar a senha correta


Usuario = input('Digite o nome de usuario:')
Senha = input('Digite a senha:')
Tentativas = 0 

while (not Senha == '1234' and Tentativas < 2):
    Senha = input('Digite a senha:')
    Tentativas += 1

if Senha == '1234':
    print ('Acesso Permitido')
else:
    print('Acesso Negado')
 