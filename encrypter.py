import os
import pyaes

def encrypt_file(file_name, key):
    try:
        # Verificar o tamanho da chave
        if len(key) not in {16, 24, 32}:
            raise ValueError("A chave deve ter 16, 24 ou 32 bytes para AES.")

        # Abrir o arquivo a ser criptografado
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"O arquivo '{file_name}' não foi encontrado.")

        with open(file_name, "rb") as file:
            file_data = file.read()

        # Criptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        # Remover o arquivo original
        os.remove(file_name)

        # Salvar o arquivo criptografado
        new_file_name = file_name + ".crypto"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo criptografado com sucesso: {new_file_name}")

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Nome do arquivo e chave de criptografia
file_name = "challenge.txt"
key = b"santanderbootcamp"

encrypt_file(file_name, key)
