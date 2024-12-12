import os
import pyaes

def decrypt_file(file_name, key):
    try:
        # Verificar o tamanho da chave
        if len(key) not in {16, 24, 32}:
            raise ValueError("A chave deve ter 16, 24 ou 32 bytes para AES.")

        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Descriptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        new_file_name = file_name.replace(".crypto", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado com sucesso: {new_file_name}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    except ValueError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Nome do arquivo e chave de descriptografia
file_name = "challenge.txt.crypto"
key = b"santanderbootcamp"

decrypt_file(file_name, key)
