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

# numero de rainhas
numero_rainhas = 8

# Parâmetros do AG
ga_instance = pygad.GA(
    num_generations=1000,
    num_parents_mating=20,
    fitness_func=funcao_fitness,
    sol_per_pop=50,
    num_genes=numero_rainhas,
    gene_type=int,
    gene_space=list(range(8)),  # cada rainha pode estar em uma das 8 linhas
    parent_selection_type="rank",
    keep_parents=10,
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=15
)

# executa o AG com base nos parametros
ga_instance.run()

solution, solution_fitness, _ = ga_instance.best_solution()
print("Melhor solução encontrada:", solution)
print("Fitness da melhor solução:", solution_fitness)

# função para mostrar o tabuleiro
def print_tabuleiro(solution):
    board = np.full((8, 8), ".")
    for col, row in enumerate(solution):
        board[row][col] = "Q" # ha uma rainha nesta posicao
    for row in board:
        print(" ".join(row))

print("\nTabuleiro gerado:")
print_tabuleiro(solution)

# plot da evolução do fitness
ga_instance.plot_fitness()