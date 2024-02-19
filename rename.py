import os

def rename(dir, nome_atual, nome_novo):
    # loop para percorrer todas as pastas dentro de dir e criando um array com o resultado do que encontrar
    for file in os.listdir(dir):
        old_path = os.path.join(dir, file) # juntando o dir com o nome da pasta encontrada
        for file in os.listdir(old_path):
            if nome_atual in file:
                pathOld = os.path.join(old_path, file) # criando um novo diretório com o nome do diretório anterior + o nome das pastas encontradas
                new_path = os.path.join(old_path, nome_novo)
                os.rename(pathOld, new_path) # renomeando o diretório antigo para o novo criado
print("Processo finalizado.")
