"""
Script simplificado para executar experimentos com modelos de classificação.
Resultados são salvos em resultados_experimentos.json (append mode).
"""

import time
import json
import os
from datetime import datetime
from pathlib import Path

from main import (
    carregar_dados,
    regressao_logistica_keras,
    rn_camada_rasa_keras,
    cnn_keras
)

RESULTS_FILE = 'resultados_experimentos.json'
NUM_EXECUCOES = 10


def carregar_resultados_existentes():
    """Carrega resultados anteriores do JSON se existir."""
    if Path(RESULTS_FILE).exists():
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'execucoes': []}


def salvar_resultados(nova_execucao):
    """Adiciona nova execução ao JSON sem sobrescrever anteriores."""
    dados = carregar_resultados_existentes()
    dados['execucoes'].append(nova_execucao)

    with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Resultados salvos em: {RESULTS_FILE}")
    print(f"  Total de execuções no arquivo: {len(dados['execucoes'])}")


def executar_experimento(nome, model_fn, X_train, Y_train, X_test, Y_test,
                         epochs, batch_size=32, config=None):
    """Executa um experimento e retorna métricas."""
    print(f"▶ {nome} (epochs={epochs})")

    start_time = time.time()
    model = model_fn()

    history = model.fit(
        X_train, Y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        verbose=0
    )

    loss_test, acc_test = model.evaluate(X_test, Y_test, verbose=0)
    tempo = time.time() - start_time

    resultado = {
        'nome': nome,
        'epochs': epochs,
        'batch_size': batch_size,
        'config': config or {},
        'num_parametros': int(model.count_params()),
        'tempo_segundos': round(tempo, 2),
        'acc_train': round(history.history['accuracy'][-1] * 100, 2),
        'acc_val': round(history.history['val_accuracy'][-1] * 100, 2),
        'acc_test': round(acc_test * 100, 2),
        'loss_test': round(loss_test, 4)
    }

    print(f"  ✓ {tempo:.1f}s | Acc Teste: {resultado['acc_test']:.2f}%\n")
    return resultado


class ExperimentRunner:
    """Gerencia execução de experimentos."""

    def __init__(self):
        print("Carregando dados...")
        self.X_train, self.Y_train, self.X_train_flat, \
        self.X_test, self.Y_test, self.X_test_flat = carregar_dados()
        print(f"✓ Dados carregados\n")
        self.resultados = []

    def regressao_logistica(self, epochs_list=[30, 50, 70]):
        """Experimentos com Regressão Logística."""
        print("=" * 50)
        print("REGRESSÃO LOGÍSTICA")
        print("=" * 50)

        for epochs in epochs_list:
            resultado = executar_experimento(
                nome="Regressão Logística",
                model_fn=regressao_logistica_keras,
                X_train=self.X_train_flat,
                Y_train=self.Y_train,
                X_test=self.X_test_flat,
                Y_test=self.Y_test,
                epochs=epochs
            )
            self.resultados.append(resultado)

    def rede_rasa(self, neurons_list=[5, 7, 10, 20], epochs=50):
        """Experimentos com Rede Rasa."""
        print("=" * 50)
        print("REDE NEURAL RASA")
        print("=" * 50)

        for neurons in neurons_list:
            resultado = executar_experimento(
                nome="Rede Rasa",
                model_fn=lambda: rn_camada_rasa_keras(neurons=neurons),
                X_train=self.X_train_flat,
                Y_train=self.Y_train,
                X_test=self.X_test_flat,
                Y_test=self.Y_test,
                epochs=epochs,
                config={'neurons': neurons}
            )
            self.resultados.append(resultado)

    def cnn(self, epochs_list=[10, 20, 30]):
        """Experimentos com CNN."""
        print("=" * 50)
        print("CNN")
        print("=" * 50)

        for epochs in epochs_list:
            resultado = executar_experimento(
                nome="CNN",
                model_fn=cnn_keras,
                X_train=self.X_train,
                Y_train=self.Y_train,
                X_test=self.X_test,
                Y_test=self.Y_test,
                epochs=epochs
            )
            self.resultados.append(resultado)

    def executar_todos(self):
        """Executa todos os grupos de experimentos."""
        self.regressao_logistica()
        self.rede_rasa()
        self.cnn()
        return self.resultados


def main(num_execucoes=1):
    """
    Executa experimentos múltiplas vezes.

    Args:
        num_execucoes: Número de vezes para rodar todos os experimentos
    """
    print("\n" + "=" * 50)
    print("EXPERIMENTOS - TRABALHO 4")
    print("=" * 50)
    print(f"Número de execuções: {num_execucoes}\n")

    for i in range(num_execucoes):
        if num_execucoes > 1:
            print(f"\n{'#' * 50}")
            print(f"EXECUÇÃO {i + 1}/{num_execucoes}")
            print(f"{'#' * 50}\n")

        inicio = time.time()
        runner = ExperimentRunner()
        resultados = runner.executar_todos()
        tempo_total = time.time() - inicio

        execucao = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'tempo_total_segundos': round(tempo_total, 2),
            'num_experimentos': len(resultados),
            'experimentos': resultados
        }

        salvar_resultados(execucao)

        print(f"\n✓ Execução {i + 1} concluída em {tempo_total/60:.1f} min")
        print(f"  Total de experimentos: {len(resultados)}")

    print(f"\n{'=' * 50}")
    print(f"✓ CONCLUÍDO: {num_execucoes} execução(ões)")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    # Altere o número abaixo para rodar múltiplas vezes
    main(num_execucoes=NUM_EXECUCOES)
