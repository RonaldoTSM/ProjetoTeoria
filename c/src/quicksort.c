#include <stdio.h>   
#include <stdlib.h> 
#include <string.h>  
#include <time.h>   

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high]; 
    int i = (low - 1);     

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int* read_csv_to_array(const char* filename, int* size) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Erro ao abrir o arquivo CSV: %s\n", filename);
        *size = 0;
        return NULL;
    }

    int count = 0;
    char line[1024]; 

    while (fgets(line, sizeof(line), file) != NULL) {
        if (strlen(line) > 1 || (strlen(line) == 1 && line[0] != '\n')) {
            count++;
        }
    }
    
    *size = count; 

    fseek(file, 0, SEEK_SET);

    int* arr = (int*)malloc(count * sizeof(int));
    if (arr == NULL) {
        fprintf(stderr, "Erro de alocação de memória.\n");
        fclose(file);
        *size = 0;
        return NULL;
    }

    int i = 0;
    while (fgets(line, sizeof(line), file) != NULL && i < count) {
        line[strcspn(line, "\n")] = 0; 
        if (strlen(line) > 0) { 
            arr[i++] = atoi(line); 
        }
    }

    fclose(file);
    return arr;
}

// --- Função Principal (main) ---
int main(int argc, char *argv[]) {
    // Verifica se o caminho do arquivo CSV foi fornecido como argumento
    if (argc < 2) {
        // Usa fprintf(stderr) para mensagens de uso para o canal de erro padrão
        fprintf(stderr, "Uso: %s <caminho_para_o_arquivo.csv>\n", argv[0]);
        return 1; // Sai do programa com código de erro
    }

    const char* filename = argv[1]; 
    int size = 0;
    int* arr = read_csv_to_array(filename, &size); 

    if (arr == NULL || size == 0) {
        fprintf(stderr, "Não foi possível ler os dados do arquivo ou o arquivo está vazio.\n");
        return 1; // Sai com erro
    }

    clock_t start_time = clock();
    
    quickSort(arr, 0, size - 1);
    
    clock_t end_time = clock();

    double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("%.9f\n", cpu_time_used);

    free(arr);

    return 0;
}