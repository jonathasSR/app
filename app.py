import os

print("""Sabor Express
      """)

print('1. Cadastrar restaurante')
print('2.Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair')


opcao_escolhida = int(input('Escolha uma opção: '))



def Finaliza_app():
    os.system('clear')
    print('Encerrando o programa\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes') 
elif opcao_escolhida == 3:
    print('Ativar restaurantes')
else:
    Finaliza_app()














