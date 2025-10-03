import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count
from main import criar_ga_instance

# Função para executar uma única rodada do AG
def run_single_ga(run_number):
    ga_instance = criar_ga_instance(num_generations=1500)
    ga_instance.run()
    _, best_fitness, _ = ga_instance.best_solution()
    
    print(f"Run {run_number+1} concluído: fitness = {best_fitness}")
    return best_fitness

# Número de execuções para testar
num_runs = 50
num_processes = cpu_count()  # Usa todos os cores disponíveis

print(f"Executando {num_runs} vezes usando {num_processes} processos paralelos...")
print("="*50)

# Executa em paralelo
if __name__ == '__main__':
    with Pool(processes=num_processes) as pool:
        fitness_results = pool.map(run_single_ga, range(num_runs))
    
    # Estatísticas
    count_28 = fitness_results.count(28)
    percentage = (count_28 / num_runs) * 100
    
    print("\n" + "="*50)
    print(f"Resultados após {num_runs} execuções:")
    print(f"Soluções ótimas (fitness = 28): {count_28}/{num_runs} ({percentage:.1f}%)")
    print(f"Fitness médio: {np.mean(fitness_results):.2f}")
    print(f"Fitness mínimo: {min(fitness_results)}")
    print(f"Fitness máximo: {max(fitness_results)}")
    print("="*50)
    
    # Criar gráfico de barras mostrando a distribuição dos fitness
    plt.figure(figsize=(10, 6))
    
    # Contar a frequência de cada fitness
    unique_fitness = sorted(set(fitness_results))
    fitness_counts = [fitness_results.count(f) for f in unique_fitness]
    
    # Criar gráfico de barras
    bars = plt.bar(unique_fitness, fitness_counts, color='steelblue', edgecolor='black')
    
    # Destacar a barra do fitness 28 em verde
    if 28 in unique_fitness:
        idx_28 = unique_fitness.index(28)
        bars[idx_28].set_color('green')
    
    plt.xlabel('Fitness Score', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.title(f'Distribuição de Fitness em {num_runs} Execuções do AG\n({count_28} soluções ótimas, {percentage:.1f}%)', fontsize=14)
    plt.xticks(unique_fitness)
    plt.grid(axis='y', alpha=0.3)
    
    # Adicionar valores no topo das barras
    for bar, count in zip(bars, fitness_counts):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{count}',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('convergence_test.png', dpi=150)
    print("\nGráfico salvo como 'convergence_test.png'")
    plt.show()

