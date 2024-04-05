import os

def criar(dir, nome):
    for file in os.listdir(dir):
        old_path = os.path.join(dir, file)
        if file == "10-OUTROS":
            print("Está pasta não será criada a nova!", old_path)
        else:
            for file in os.listdir(old_path):
                new_pasta = os.path.join(old_path, nome)
                if not os.path.exists(new_pasta):
                    # Se não existe, criar a pasta
                    os.mkdir(new_pasta)
                    print(f'A pasta {nome} foi criada em {dir}.')
                else:
                    print(f'A pasta {nome} já existe em {dir}.')