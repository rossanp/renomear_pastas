import rename

nome_atual = input("Qual é o nome atual da pasta?")
nome_novo = input("Para qual nome será renomeado?")

dir = r'L:\\'

change = rename.rename(dir, nome_atual, nome_novo) #chamando o método