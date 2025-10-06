# importação de bibliotecas utilizadas
import pygad
import numpy as np
import matplotlib.pyplot as plt

# Função de avaliação (fitness)
def funcao_fitness(ga_instance, solution, solution_idx):
    # fitness: número de pares de rainhas que não se atacam
    fitness = 28

    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            # conflito na mesma linha/coluna
            if solution[i] == solution[j]:
                fitness -= 1

            # conflito na mesma diagonal
            elif abs(solution[i] - solution[j]) == abs(i - j):
                fitness -= 1

    return fitness

# Função de callback para parar quando fitness = 28
def on_generation(ga_instance):
    best_fitness = ga_instance.best_solution()[1]
    if best_fitness == 28:
        return "stop"

# função para mostrar o tabuleiro
def print_tabuleiro(solution):
    board = np.full((8, 8), ".")
    for col, row in enumerate(solution):
        board[row][col] = "Q" # ha uma rainha nesta posicao
    for row in board:
        print(" ".join(row))

# Função para criar e executar uma instância do AG
def criar_ga_instance(num_generations=3000):
    """Cria uma nova instância do algoritmo genético com os parâmetros configurados"""
    return pygad.GA(
        num_generations=num_generations,
        num_parents_mating=70,
        fitness_func=funcao_fitness,
        sol_per_pop=120,
        num_genes=8,
        gene_type=int,
        gene_space=list(range(8)),  # cada rainha pode estar em uma das 8 linhas
        parent_selection_type="rank",
        keep_parents=30,
        crossover_type="two_points",
        mutation_type="random",
        mutation_num_genes=3,
        on_generation=on_generation
    )

# Executa apenas se for o script principal
if __name__ == "__main__":
    # Parâmetros do AG
    ga_instance = criar_ga_instance()

    # executa o AG com base nos parametros
    ga_instance.run()

    solution, solution_fitness, _ = ga_instance.best_solution()
    print("Melhor solução encontrada:", solution)
    print("Fitness da melhor solução:", solution_fitness)

    print("\nTabuleiro gerado:")
    print_tabuleiro(solution)

    # plot da evolução do fitness
    ga_instance.plot_fitness()