import os
import csv
import random

def generate_random_list(size):
    """Gera uma lista de inteiros aleatórios de um dado tamanho."""
    return [random.randint(0, 1000000) for _ in range(size)]

def save_list_to_csv(data_list, filename, output_dir):
    """Salva uma lista em um arquivo CSV."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        for item in data_list:
            writer.writerow([item])
    print(f"Gerado: {filepath}")

def generate_input_files(sizes, num_files_per_size, output_base_dir="dados/entradas"):
    """
    Gera múltiplos arquivos CSV com listas de inteiros aleatórios
    para diferentes tamanhos de entrada.
    """
    print(f"Iniciando a geração de arquivos de entrada em '{output_base_dir}'...")
    for size in sizes:
        for i in range(num_files_per_size):
            filename = f"entrada_{size}_{i}.csv"
            random_list = generate_random_list(size)
            save_list_to_csv(random_list, filename, output_base_dir)
    print("Geração de arquivos de entrada concluída!")

if __name__ == "__main__":
    # Tamanhos de entrada e número de arquivos por tamanho
    input_sizes = [100, 10000, 100000]
    num_files = 15 # 15 arquivos para cada tamanho

    # Chama a função para gerar os arquivos
    generate_input_files(input_sizes, num_files)