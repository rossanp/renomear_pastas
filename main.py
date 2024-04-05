import rename, criar, os, time

print("Opções:")
print("#1 - Renomear pastas")
print("#2 - Criar pastas")
print("#3 - Sair")

opcao = int(input("O que gostaria de fazer? Digite somente o número!"))
dir = r'L:\\'
""" dir = r'M:\\25-CONTROLE GERAL\05-TI\testando' """

if opcao == 1:
    nome_atual = input("Qual é o nome atual do cliente?")
    nome_novo = input("Para qual nome será renomeado?")

    change = rename.rename(dir, nome_atual, nome_novo) #chamando o método
elif opcao == 2:
    nome = input("Qual é o nome da empresa?")

    change = criar.criar(dir, nome)
else:
    print("Escolhido sair")
    os.system("exit")
    time.sleep(3)