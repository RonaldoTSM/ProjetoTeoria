# Análise de Complexidade do QuickSort: Comparativo entre Python e C

## Projeto Acadêmico

Este projeto foi desenvolvido para a disciplina de **Teoria da Computação**, ministrada pelos Profs. Pâmela e Daniel, como parte dos requisitos avaliativos. O objetivo principal é realizar uma análise detalhada da complexidade de tempo do algoritmo QuickSort, comparando sua performance teórica com medições práticas obtidas através de implementações em Python e C.

**Período:** 1º Semestre de 2025

**Grupo:**
* Eduardo Roma
* Luís Melo
* Ronaldo Souto Maior

---

## 1. Descrição do Projeto

Este estudo foca no algoritmo de ordenação QuickSort. Foram desenvolvidas implementações em C e Python, que são submetidas a uma série de testes com diferentes volumes de dados de entrada. A análise compreende:

* **Descrição detalhada do algoritmo QuickSort:** Incluindo sua lógica "dividir para conquistar" e pseudocódigo.
* **Classificação Assintótica:** Análise das notações Big-O (Pior Caso), Big-Ω (Melhor Caso) e Big-Θ (Caso Médio).
* **Discussão sobre Aplicabilidade Prática:** Contextos onde o QuickSort é eficiente ou não.
* **Simulação com Dados Sintéticos:** Execução dos algoritmos com entradas de tamanhos pequeno (100), médio (10.000) e grande (100.000), com 15 repetições para cada.
* **Coleta e Análise de Tempos de Execução:** Registro dos tempos, cálculo de média e desvio padrão.
* **Comparação de Desempenho:** Geração de gráficos e tabelas para comparar os tempos medidos, a complexidade teórica e a velocidade de execução entre C e Python.
* **Análise de Casos:** Discussão sobre o melhor, pior e caso médio do QuickSort.
* **Reflexão Final:** Considerações sobre a classe de complexidade do problema (P, NP) e problemas relacionados NP-Completos.

O relatório completo com todas as análises, discussões teóricas, gráficos e conclusões pode ser encontrado em `relatorio/relatorio.pdf` (gerado a partir do Jupyter Notebook `relatorio/relatorio.ipynb`).

---

## 2. Estrutura de Pastas

O projeto está organizado da seguinte forma:

```text
PROJETOTEORIA/
├── c/                             # Implementação e scripts em C
│   ├── src/
│   │   └── quicksort.c            # Código fonte do QuickSort em C
│   └── scripts/
│       └── benchmark.sh           # Script para compilar e executar os testes em C
├── python/                        # Implementação e scripts em Python
│   ├── src/
│   │   └── quicksort.py           # Código fonte do QuickSort em Python
│   └── scripts/
│       ├── gerar_entradas.py      # Script para gerar arquivos de entrada CSV
│       ├── testar_quicksort.py    # Script para testar o QuickSort Python em uma entrada
│       └── coletar_dados.py       # Script para executar todos os testes em Python e salvar resultados
├── dados/                         # Dados de entrada e resultados dos testes
│   ├── entradas/                  # Arquivos CSV com as listas de entrada geradas
│   └── resultados/                # Arquivos CSV com os tempos de execução coletados (Python e C)
├── relatorio/                     # Relatório do projeto
│   └── relatorio.ipynb            # Jupyter Notebook com a análise, gráficos e conclusões
│   └── relatorio.pdf              # Versão em PDF do relatório
├── README.md                      # Este arquivo
└── requirements.txt               # Dependências Python 
```
---

## 3. Pré-requisitos

Para executar este projeto, você precisará de:

* **Para a parte em C:**
    * Um compilador C (como GCC)
    * Um ambiente shell (como Bash) para executar o script `benchmark.sh`
* **Para a parte em Python:**
    * Python 3.x
    * Bibliotecas Python listadas em `requirements.txt`. Para instalá-las, execute:
        ```bash
        pip install -r requirements.txt
        ```
        As principais bibliotecas utilizadas no relatório (`relatorio.ipynb`) são `pandas`, `matplotlib` e `seaborn`.

---

## 4. Como Executar

Siga os passos abaixo para reproduzir os experimentos:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/RonaldoTSM/ProjetoTeoria.git
    cd PROJETOTEORIA/
    ```

2.  **Gere os Arquivos de Entrada:**
    Os arquivos de entrada são gerados pelo script `gerar_entradas.py`. Ele criará 15 arquivos CSV para cada um dos tamanhos definidos (100, 10.000, 100.000) na pasta `dados/entradas/`.
    ```bash
    python python/scripts/gerar_entradas.py
    ```

3.  **Execute os Testes da Implementação em C:**
    O script `benchmark.sh` compila o `quicksort.c` e executa o programa para cada arquivo de entrada gerado, salvando os tempos em `dados/resultados/tempos_c.csv`.
    ```bash
    bash c/scripts/benchmark.sh
    ```

4.  **Execute os Testes da Implementação em Python:**
    O script `coletar_dados.py` executa o `quicksort.py` para cada arquivo de entrada, coleta os tempos e salva os resultados brutos e estatísticas em `dados/resultados/tempos_python.csv`.
    ```bash
    python python/scripts/coletar_dados.py
    ```

5.  **Visualize o Relatório:**
    Após a coleta de dados, o Jupyter Notebook `relatorio/relatorio.ipynb` pode ser executado para carregar os dados, gerar as tabelas, gráficos comparativos e visualizar toda a análise[cite: 64]. Uma versão em PDF (`relatorio/relatorio.pdf`) também está disponível para consulta direta.

---

## 5. Linguagens e Ferramentas

* **Linguagens de Programação:** C, Python
* **Ferramentas de Análise e Relatório:** Jupyter Notebook, Pandas, Matplotlib, Seaborn
* **Shell:** Bash (para o script de benchmark em C)

---