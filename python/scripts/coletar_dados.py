import os
import csv
import re
import pandas as pd
import sys 

sys.path.append(os.path.join(os.path.dirname(__file__)))

from testar_quicksort import ler_lista_csv, executar_e_medir_tempo

def coletar_tempos_python(entradas_dir="dados/entradas", resultados_dir="dados/resultados"):

    tempos_coletados = [] 
    
   
    if not os.path.exists(resultados_dir):
        os.makedirs(resultados_dir)
            
    arquivos_csv = [f for f in os.listdir(entradas_dir) if f.endswith('.csv')]
    arquivos_csv.sort()
    print("Iniciando a coleta de dados para QuickSort em Python (versão direta)...")

    for arquivo_csv in arquivos_csv:
        caminho_completo_entrada = os.path.join(entradas_dir, arquivo_csv)
        
        match = re.search(r'entrada_(\d+)_', arquivo_csv)
        tamanho_entrada = int(match.group(1)) if match else 'N/A'

        print(f"  Testando {arquivo_csv} (Tamanho: {tamanho_entrada})...")

        try:
            lista_original = ler_lista_csv(caminho_completo_entrada)
            
            tempo = executar_e_medir_tempo(lista_original)

            if tempo is not None:
                tempos_coletados.append({
                    "arquivo": arquivo_csv,
                    "tamanho": tamanho_entrada,
                    "tempo": tempo
                })
            else:
                print(f"    AVISO: Tempo não foi medido para {arquivo_csv}.")

        except Exception as e:
            print(f"    Ocorreu um erro inesperado para {arquivo_csv}: {e}")

    df_tempos = pd.DataFrame(tempos_coletados)

    if df_tempos.empty:
        print("Nenhum dado de tempo coletado. Verifique os arquivos de entrada e os scripts.")
        return 

    
    df_estatisticas = df_tempos.groupby('tamanho')['tempo'].agg(['mean', 'std']).reset_index()
    df_estatisticas.rename(columns={'mean': 'tempo_medio', 'std': 'desvio_padrao'}, inplace=True)
    
    print("\n--- Estatísticas por Tamanho ---")
    print(df_estatisticas.to_string(index=False)) 

    
    caminho_saida_csv = os.path.join(resultados_dir, "tempos_python.csv")
    df_tempos.to_csv(caminho_saida_csv, index=False) 
    print(f"\nResultados brutos (todos os tempos) salvos em: {caminho_saida_csv}")
    print("Coleta de dados em Python concluída com sucesso!")

if __name__ == "__main__":
    coletar_tempos_python()