C_SRC_DIR="c/src"
C_EXECUTABLE="c/quicksort_c" 
INPUTS_DIR="dados/entradas"
RESULTS_DIR="dados/resultados"
OUTPUT_CSV="${RESULTS_DIR}/tempos_c.csv"

echo "Iniciando o benchmark do QuickSort em C..."


echo "Compilando quicksort.c..."

gcc "${C_SRC_DIR}/quicksort.c" -o "${C_EXECUTABLE}" -Wall -O3

if [ $? -ne 0 ]; then
    echo "Erro na compilação do quicksort.c. Abortando."
    exit 1
fi
echo "Compilação concluída com sucesso. Executável em: ${C_EXECUTABLE}"

mkdir -p "${RESULTS_DIR}"

echo "arquivo,tamanho,tempo" > "${OUTPUT_CSV}"
echo "Criado arquivo de resultados: ${OUTPUT_CSV}"

find "${INPUTS_DIR}" -name "entrada_*.csv" | sort | while read -r input_file; do
    
    filename=$(basename "${input_file}")

    if [[ "${filename}" =~ entrada_([0-9]+)_ ]]; then
        size="${BASH_REMATCH[1]}"
    else
        size="N/A" 
    fi

    echo "  Testando ${filename} (Tamanho: ${size})..."

    time_output=$( "${C_EXECUTABLE}" "${input_file}" 2>/dev/null )

    if echo "${time_output}" | grep -Eq '^[0-9]+([.][0-9]+)?$'; then
        # Adiciona o resultado ao CSV
        echo "${filename},${size},${time_output}" >> "${OUTPUT_CSV}"
    else
        echo "    AVISO: Nao foi possivel obter o tempo para ${filename}. Saida: ${time_output}"
    fi

done

echo "Benchmark do QuickSort em C concluído! Resultados em: ${OUTPUT_CSV}"