import os

def rename(dir, nome_atual, nome_novo):
    # loop para percorrer todas as pastas dentro de dir e criando um array com o resultado do que encontrar
    for file in os.listdir(dir):
        old_path = os.path.join(dir, file) # juntando o dir com o nome da pasta encontrada

        for file in os.listdir(old_path):
            pathOld = os.path.join(old_path, file) # criando um novo diretório com o nome do diretório anterior + o nome das pastas encontradas
            if file == nome_atual:
                new_path = os.path.join(old_path, nome_novo)
                os.rename(pathOld, new_path) # renomeando o diretório antigo para o novo criado
            else:
                print("Pasta não encontrada.")
    print("Processo finalizado.")
