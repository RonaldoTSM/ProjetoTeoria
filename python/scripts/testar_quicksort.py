import sys
import os
import csv
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from quicksort import quicksort 

def ler_lista_csv(caminho_arquivo):

    lista = []
    try:
        with open(caminho_arquivo, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row: 
                    lista.append(int(row[0])) 
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
        sys.exit(1) 
    except ValueError:
        print(f"Erro: Conteúdo inválido no arquivo {caminho_arquivo}. Esperado números inteiros.")
        sys.exit(1) 
    return lista

def executar_e_medir_tempo(lista):
   
    lista_para_ordenar = lista[:] 

    inicio = time.perf_counter()

    quicksort(lista_para_ordenar, 0, len(lista_para_ordenar) - 1)

    fim = time.perf_counter()

    return fim - inicio

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 testar_quicksort.py <caminho_para_o_arquivo.csv>")
        sys.exit(1)

    arquivo_csv = sys.argv[1] 

    print(f"Testando QuickSort com o arquivo: {arquivo_csv}")


    lista_original = ler_lista_csv(arquivo_csv)

    tempo_execucao = executar_e_medir_tempo(lista_original)

    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")