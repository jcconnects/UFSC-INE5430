"""
Script para análise dos resultados dos experimentos.

Gera um relatório detalhado em Markdown com estatísticas e insights
sobre os modelos de classificação Gato vs Não-Gato.
"""

import json
from pathlib import Path
from typing import List, Dict, Any
from statistics import mean, stdev
from datetime import datetime


# ============================================================================
# CONSTANTES
# ============================================================================

ARQUIVO_RESULTADOS = 'resultados_experimentos.json'
ARQUIVO_SAIDA = 'analise_resultados.md'


# ============================================================================
# FUNÇÕES DE LEITURA DE DADOS
# ============================================================================

def carregar_resultados() -> Dict[str, Any]:
    """Carrega o arquivo JSON com os resultados dos experimentos."""
    arquivo = Path(ARQUIVO_RESULTADOS)

    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo {ARQUIVO_RESULTADOS} não encontrado!")

    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def extrair_todos_experimentos(dados: Dict) -> List[Dict]:
    """
    Extrai todos os experimentos de todas as execuções em uma lista única.

    Args:
        dados: Dicionário com estrutura {execucoes: [{experimentos: [...]}]}

    Returns:
        Lista com todos os experimentos individuais
    """
    todos_experimentos = []

    for execucao in dados['execucoes']:
        todos_experimentos.extend(execucao['experimentos'])

    return todos_experimentos


# ============================================================================
# FUNÇÕES DE AGRUPAMENTO
# ============================================================================

def agrupar_por_modelo(experimentos: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Agrupa experimentos por tipo de modelo.

    Returns:
        Dict com chave=nome_modelo e valor=lista de experimentos
    """
    grupos = {}

    for exp in experimentos:
        nome = exp['nome']
        if nome not in grupos:
            grupos[nome] = []
        grupos[nome].append(exp)

    return grupos


def agrupar_por_configuracao(experimentos: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Agrupa experimentos pela mesma configuração (para calcular médias).

    Para Regressão Logística: agrupa por epochs
    Para Rede Rasa: agrupa por (neurons, epochs)
    Para CNN: agrupa por epochs
    """
    grupos = {}

    for exp in experimentos:
        nome = exp['nome']
        epochs = exp['epochs']

        # Criar chave única baseada na configuração
        if nome == "Rede Rasa":
            neurons = exp['config'].get('neurons', 0)
            chave = f"{nome}_{neurons}n_{epochs}e"
        else:
            chave = f"{nome}_{epochs}e"

        if chave not in grupos:
            grupos[chave] = []
        grupos[chave].append(exp)

    return grupos


# ============================================================================
# FUNÇÕES DE ESTATÍSTICAS
# ============================================================================

def calcular_estatisticas(experimentos: List[Dict]) -> Dict[str, float]:
    """
    Calcula estatísticas para um grupo de experimentos com mesma config.

    Returns:
        Dict com médias e desvios padrão das métricas
    """
    if not experimentos:
        return {}

    acc_train = [exp['acc_train'] for exp in experimentos]
    acc_val = [exp['acc_val'] for exp in experimentos]
    acc_test = [exp['acc_test'] for exp in experimentos]
    loss_test = [exp['loss_test'] for exp in experimentos]
    tempo = [exp['tempo_segundos'] for exp in experimentos]

    stats = {
        'n_execucoes': len(experimentos),
        'acc_train_media': mean(acc_train),
        'acc_train_std': stdev(acc_train) if len(acc_train) > 1 else 0,
        'acc_val_media': mean(acc_val),
        'acc_val_std': stdev(acc_val) if len(acc_val) > 1 else 0,
        'acc_test_media': mean(acc_test),
        'acc_test_std': stdev(acc_test) if len(acc_test) > 1 else 0,
        'loss_test_media': mean(loss_test),
        'loss_test_std': stdev(loss_test) if len(loss_test) > 1 else 0,
        'tempo_medio': mean(tempo),
        'num_parametros': experimentos[0]['num_parametros'],
        'epochs': experimentos[0]['epochs'],
        'batch_size': experimentos[0]['batch_size']
    }

    # Adicionar configuração específica
    if 'neurons' in experimentos[0]['config']:
        stats['neurons'] = experimentos[0]['config']['neurons']

    return stats


def identificar_overfitting(stats: Dict) -> str:
    """
    Identifica se há overfitting baseado na diferença treino vs teste.

    Returns:
        String descritiva do status
    """
    diff = stats['acc_train_media'] - stats['acc_test_media']

    if diff > 15:
        return "🔴 Overfitting Severo"
    elif diff > 10:
        return "🟡 Overfitting Moderado"
    elif diff > 5:
        return "🟢 Overfitting Leve"
    elif diff < -5:
        return "🔵 Possível Underfitting"
    else:
        return "✅ Boa Generalização"


# ============================================================================
# FUNÇÕES DE GERAÇÃO DE RELATÓRIO
# ============================================================================

def gerar_cabecalho(dados: Dict) -> List[str]:
    """Gera o cabeçalho do relatório."""
    linhas = []
    linhas.append("# Análise dos Resultados - Trabalho 4: Gato vs Não-Gato")
    linhas.append("")
    linhas.append(f"**Data da Análise:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    linhas.append(f"**Total de Execuções:** {len(dados['execucoes'])}")

    # Contar total de experimentos
    total_exp = sum(len(exec['experimentos']) for exec in dados['execucoes'])
    linhas.append(f"**Total de Experimentos:** {total_exp}")
    linhas.append("")
    linhas.append("---")
    linhas.append("")

    return linhas


def gerar_secao_configuracoes(grupos_config: Dict) -> List[str]:
    """Gera seção com todas as configurações testadas."""
    linhas = []
    linhas.append("## 1. Configurações Testadas")
    linhas.append("")

    # Separar por tipo de modelo
    config_por_modelo = {}
    for chave in grupos_config.keys():
        modelo = chave.split('_')[0] + " " + chave.split('_')[1]  # Ex: "Regressão Logística"
        if modelo not in config_por_modelo:
            config_por_modelo[modelo] = []
        config_por_modelo[modelo].append(chave)

    for modelo, configs in sorted(config_por_modelo.items()):
        linhas.append(f"### {modelo}")
        linhas.append("")
        for config in sorted(configs):
            exp = grupos_config[config][0]
            if 'neurons' in exp['config']:
                linhas.append(f"- **{exp['config']['neurons']} neurônios**, {exp['epochs']} epochs")
            else:
                linhas.append(f"- **{exp['epochs']} epochs**")
        linhas.append("")

    return linhas


def gerar_tabela_estatisticas(grupos_config: Dict) -> List[str]:
    """Gera tabela consolidada com estatísticas de todas as configurações."""
    linhas = []
    linhas.append("## 2. Estatísticas Consolidadas")
    linhas.append("")
    linhas.append("Média ± Desvio Padrão de múltiplas execuções:")
    linhas.append("")

    # Cabeçalho da tabela
    linhas.append("| Modelo | Config | N | Acc Treino | Acc Val | Acc Teste | Loss Teste | Tempo (s) | Params | Status |")
    linhas.append("|--------|--------|---|------------|---------|-----------|------------|-----------|--------|--------|")

    # Processar cada configuração
    for chave in sorted(grupos_config.keys()):
        exps = grupos_config[chave]
        stats = calcular_estatisticas(exps)
        status = identificar_overfitting(stats)

        # Nome e config
        nome = exps[0]['nome']
        if 'neurons' in stats:
            config = f"{stats['neurons']}n, {stats['epochs']}e"
        else:
            config = f"{stats['epochs']}e"

        # Linha da tabela
        linha = (
            f"| {nome} | {config} | {stats['n_execucoes']} | "
            f"{stats['acc_train_media']:.1f}±{stats['acc_train_std']:.1f} | "
            f"{stats['acc_val_media']:.1f}±{stats['acc_val_std']:.1f} | "
            f"{stats['acc_test_media']:.1f}±{stats['acc_test_std']:.1f} | "
            f"{stats['loss_test_media']:.3f}±{stats['loss_test_std']:.3f} | "
            f"{stats['tempo_medio']:.1f} | "
            f"{stats['num_parametros']:,} | "
            f"{status} |"
        )
        linhas.append(linha)

    linhas.append("")
    linhas.append("**Legenda:**")
    linhas.append("- `N`: Número de execuções")
    linhas.append("- `Config`: n=neurônios, e=epochs")
    linhas.append("- Valores mostrados como Média±Desvio")
    linhas.append("")

    return linhas


def gerar_melhores_modelos(grupos_config: Dict) -> List[str]:
    """Identifica e reporta os melhores modelos de cada tipo."""
    linhas = []
    linhas.append("## 3. Melhores Configurações por Modelo")
    linhas.append("")

    # Agrupar por tipo de modelo
    por_tipo = {}
    for chave, exps in grupos_config.items():
        tipo = exps[0]['nome']
        if tipo not in por_tipo:
            por_tipo[tipo] = {}
        por_tipo[tipo][chave] = exps

    # Para cada tipo, encontrar o melhor
    for tipo in sorted(por_tipo.keys()):
        linhas.append(f"### {tipo}")
        linhas.append("")

        # Calcular estatísticas de todas as configs desse tipo
        configs_stats = []
        for chave, exps in por_tipo[tipo].items():
            stats = calcular_estatisticas(exps)
            stats['chave'] = chave
            configs_stats.append(stats)

        # Ordenar por acurácia de teste
        configs_stats.sort(key=lambda x: x['acc_test_media'], reverse=True)

        # Melhor configuração
        melhor = configs_stats[0]
        if 'neurons' in melhor:
            config_str = f"{melhor['neurons']} neurônios, {melhor['epochs']} epochs"
        else:
            config_str = f"{melhor['epochs']} epochs"

        linhas.append(f"**Melhor:** {config_str}")
        linhas.append(f"- Acurácia Teste: **{melhor['acc_test_media']:.2f}% ± {melhor['acc_test_std']:.2f}%**")
        linhas.append(f"- Acurácia Treino: {melhor['acc_train_media']:.2f}%")
        linhas.append(f"- Acurácia Validação: {melhor['acc_val_media']:.2f}%")
        linhas.append(f"- Loss Teste: {melhor['loss_test_media']:.4f}")
        linhas.append(f"- Status: {identificar_overfitting(melhor)}")
        linhas.append(f"- Tempo Médio: {melhor['tempo_medio']:.2f}s")
        linhas.append("")

        # Top 3
        if len(configs_stats) > 1:
            linhas.append("**Ranking:**")
            for i, stats in enumerate(configs_stats[:3], 1):
                if 'neurons' in stats:
                    cfg = f"{stats['neurons']}n, {stats['epochs']}e"
                else:
                    cfg = f"{stats['epochs']}e"
                linhas.append(f"{i}. {cfg}: {stats['acc_test_media']:.2f}% ± {stats['acc_test_std']:.2f}%")
            linhas.append("")

    return linhas


def gerar_comparacao_geral(grupos_config: Dict) -> List[str]:
    """Compara os melhores de cada tipo de modelo."""
    linhas = []
    linhas.append("## 4. Comparação Geral: Melhor de Cada Tipo")
    linhas.append("")

    # Encontrar melhor de cada tipo
    por_tipo = {}
    for chave, exps in grupos_config.items():
        tipo = exps[0]['nome']
        if tipo not in por_tipo:
            por_tipo[tipo] = {}
        por_tipo[tipo][chave] = exps

    melhores = []
    for tipo, configs in por_tipo.items():
        melhor_chave = max(configs.keys(),
                          key=lambda k: calcular_estatisticas(configs[k])['acc_test_media'])
        stats = calcular_estatisticas(configs[melhor_chave])
        stats['tipo'] = tipo
        melhores.append(stats)

    # Ordenar por acurácia
    melhores.sort(key=lambda x: x['acc_test_media'], reverse=True)

    # Tabela
    linhas.append("| Rank | Modelo | Configuração | Acc Teste | Loss Teste | Parâmetros | Tempo |")
    linhas.append("|------|--------|--------------|-----------|------------|------------|-------|")

    for i, stats in enumerate(melhores, 1):
        if 'neurons' in stats:
            config = f"{stats['neurons']}n, {stats['epochs']}e"
        else:
            config = f"{stats['epochs']}e"

        emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else ""

        linhas.append(
            f"| {emoji} {i} | {stats['tipo']} | {config} | "
            f"**{stats['acc_test_media']:.2f}%** ± {stats['acc_test_std']:.2f}% | "
            f"{stats['loss_test_media']:.4f} | "
            f"{stats['num_parametros']:,} | "
            f"{stats['tempo_medio']:.1f}s |"
        )

    linhas.append("")

    # Vencedor
    vencedor = melhores[0]
    linhas.append("### 🏆 Modelo Vencedor")
    linhas.append("")
    linhas.append(f"**{vencedor['tipo']}** é o modelo com melhor desempenho no teste!")
    linhas.append("")
    if 'neurons' in vencedor:
        linhas.append(f"- **Configuração:** {vencedor['neurons']} neurônios, {vencedor['epochs']} epochs")
    else:
        linhas.append(f"- **Configuração:** {vencedor['epochs']} epochs")
    linhas.append(f"- **Acurácia Teste:** {vencedor['acc_test_media']:.2f}% ± {vencedor['acc_test_std']:.2f}%")
    linhas.append(f"- **Parâmetros:** {vencedor['num_parametros']:,}")
    linhas.append(f"- **Tempo Médio:** {vencedor['tempo_medio']:.2f}s")
    linhas.append("")

    return linhas


def gerar_insights(grupos_config: Dict) -> List[str]:
    """Gera insights e observações sobre os resultados."""
    linhas = []
    linhas.append("## 5. Insights e Observações")
    linhas.append("")

    # Análise de overfitting
    linhas.append("### 5.1 Análise de Overfitting")
    linhas.append("")

    problemas_overfitting = []
    boas_generalizacoes = []

    for chave, exps in grupos_config.items():
        stats = calcular_estatisticas(exps)
        status = identificar_overfitting(stats)
        diff = stats['acc_train_media'] - stats['acc_test_media']

        if 'neurons' in stats:
            nome_config = f"{exps[0]['nome']} ({stats['neurons']}n, {stats['epochs']}e)"
        else:
            nome_config = f"{exps[0]['nome']} ({stats['epochs']}e)"

        if diff > 10:
            problemas_overfitting.append((nome_config, diff, stats['acc_test_media']))
        elif abs(diff) <= 5:
            boas_generalizacoes.append((nome_config, diff, stats['acc_test_media']))

    if problemas_overfitting:
        linhas.append("**Configurações com Overfitting:**")
        for nome, diff, acc in sorted(problemas_overfitting, key=lambda x: x[1], reverse=True):
            linhas.append(f"- {nome}: diferença de {diff:.1f}% (Teste: {acc:.1f}%)")
        linhas.append("")

    if boas_generalizacoes:
        linhas.append("**Configurações com Boa Generalização:**")
        for nome, diff, acc in sorted(boas_generalizacoes, key=lambda x: x[2], reverse=True):
            linhas.append(f"- {nome}: diferença de {diff:.1f}% (Teste: {acc:.1f}%)")
        linhas.append("")

    # Impacto de epochs
    linhas.append("### 5.2 Impacto do Número de Epochs")
    linhas.append("")

    # Agrupar por modelo e analisar tendência
    por_modelo = {}
    for chave, exps in grupos_config.items():
        modelo = exps[0]['nome']
        stats = calcular_estatisticas(exps)
        if modelo not in por_modelo:
            por_modelo[modelo] = []
        por_modelo[modelo].append(stats)

    for modelo in sorted(por_modelo.keys()):
        configs = sorted(por_modelo[modelo], key=lambda x: x['epochs'])
        linhas.append(f"**{modelo}:**")

        # Comparar primeira vs última configuração (em epochs)
        if len(configs) >= 2:
            primeira = configs[0]
            ultima = configs[-1]
            melhoria = ultima['acc_test_media'] - primeira['acc_test_media']

            linhas.append(f"- {primeira['epochs']} epochs → {ultima['epochs']} epochs: "
                         f"{primeira['acc_test_media']:.1f}% → {ultima['acc_test_media']:.1f}% "
                         f"({'↑' if melhoria > 0 else '↓'} {abs(melhoria):.1f}%)")
        linhas.append("")

    # Variabilidade
    linhas.append("### 5.3 Estabilidade dos Modelos")
    linhas.append("")
    linhas.append("Configurações com menor variabilidade (mais estáveis):")
    linhas.append("")

    configs_com_std = []
    for chave, exps in grupos_config.items():
        stats = calcular_estatisticas(exps)
        if stats['n_execucoes'] > 1:
            if 'neurons' in stats:
                nome = f"{exps[0]['nome']} ({stats['neurons']}n, {stats['epochs']}e)"
            else:
                nome = f"{exps[0]['nome']} ({stats['epochs']}e)"
            configs_com_std.append((nome, stats['acc_test_std'], stats['acc_test_media']))

    # Top 5 mais estáveis
    configs_com_std.sort(key=lambda x: x[1])
    for nome, std, media in configs_com_std[:5]:
        linhas.append(f"- {nome}: {media:.1f}% ± {std:.2f}%")

    linhas.append("")

    return linhas


def gerar_metodologia() -> List[str]:
    """Documenta a metodologia utilizada."""
    linhas = []
    linhas.append("## 6. Metodologia")
    linhas.append("")
    linhas.append("### Configuração dos Experimentos")
    linhas.append("")
    linhas.append("- **Otimizador:** Adam (learning rate: 0.001)")
    linhas.append("- **Função de Perda:** Binary Crossentropy")
    linhas.append("- **Batch Size:** 32")
    linhas.append("- **Validação:** 20% dos dados de treino")
    linhas.append("- **Normalização:** Pixels divididos por 255 (range [0, 1])")
    linhas.append("- **Múltiplas Execuções:** Cada configuração foi executada múltiplas vezes")
    linhas.append("")
    linhas.append("### Arquiteturas")
    linhas.append("")
    linhas.append("**1. Regressão Logística:**")
    linhas.append("- Input: 12288 features (64×64×3 flatten)")
    linhas.append("- Dense(1, sigmoid)")
    linhas.append("- Parâmetros: 12,289")
    linhas.append("")
    linhas.append("**2. Rede Neural Rasa:**")
    linhas.append("- Input: 12288 features")
    linhas.append("- Dense(n, relu) + Dense(1, sigmoid)")
    linhas.append("- Parâmetros: varia conforme n (neurônios)")
    linhas.append("")
    linhas.append("**3. CNN:**")
    linhas.append("- Input: 64×64×3")
    linhas.append("- Conv2D(16) → MaxPool → Conv2D(32) → MaxPool → Flatten → Dense(64, relu) → Dense(1, sigmoid)")
    linhas.append("- Parâmetros: 406,625")
    linhas.append("")

    return linhas


def gerar_conclusao(grupos_config: Dict) -> List[str]:
    """Gera conclusão com base nos resultados."""
    linhas = []
    linhas.append("## 7. Conclusões")
    linhas.append("")

    # Encontrar melhor geral
    melhor_chave = max(grupos_config.keys(),
                       key=lambda k: calcular_estatisticas(grupos_config[k])['acc_test_media'])
    melhor_stats = calcular_estatisticas(grupos_config[melhor_chave])
    melhor_tipo = grupos_config[melhor_chave][0]['nome']

    linhas.append(f"1. **Melhor Modelo:** {melhor_tipo} alcançou a melhor acurácia média de teste "
                  f"({melhor_stats['acc_test_media']:.2f}%)")
    linhas.append("")

    # Comparar complexidade
    linhas.append("2. **Complexidade vs Desempenho:**")
    linhas.append("   - Modelos mais complexos (CNN) tendem a ter melhor desempenho")
    linhas.append("   - Regressão Logística é mais rápida mas menos precisa")
    linhas.append("   - Rede Rasa oferece meio-termo entre velocidade e precisão")
    linhas.append("")

    linhas.append("3. **Recomendações:**")
    if 'neurons' in melhor_stats:
        linhas.append(f"   - Para este dataset, use {melhor_tipo} com {melhor_stats['neurons']} neurônios "
                     f"e {melhor_stats['epochs']} epochs")
    else:
        linhas.append(f"   - Para este dataset, use {melhor_tipo} com {melhor_stats['epochs']} epochs")
    linhas.append("   - Considere usar regularização (Dropout) se overfitting for problema")
    linhas.append("   - Dataset pequeno (50 imagens teste) causa alta variabilidade")
    linhas.append("")

    return linhas


def gerar_rodape() -> List[str]:
    """Gera rodapé do relatório."""
    linhas = []
    linhas.append("---")
    linhas.append("")
    linhas.append("**Observações:**")
    linhas.append("- Este relatório foi gerado automaticamente a partir dos dados experimentais")
    linhas.append("- Estatísticas calculadas: Média ± Desvio Padrão")
    linhas.append("- Dataset: 209 treino (167 após split 80/20), 50 teste")
    linhas.append("")
    linhas.append(f"*Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    return linhas


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """Função principal que orquestra a análise."""
    print("=" * 70)
    print("ANÁLISE DE RESULTADOS - Trabalho 4")
    print("=" * 70)
    print()

    # 1. Carregar dados
    print("1. Carregando dados...")
    dados = carregar_resultados()
    print(f"   ✓ {len(dados['execucoes'])} execuções carregadas")

    # 2. Extrair e agrupar experimentos
    print("2. Processando experimentos...")
    todos_exp = extrair_todos_experimentos(dados)
    grupos_config = agrupar_por_configuracao(todos_exp)
    print(f"   ✓ {len(todos_exp)} experimentos encontrados")
    print(f"   ✓ {len(grupos_config)} configurações únicas")

    # 3. Gerar relatório
    print("3. Gerando relatório...")
    relatorio = []

    relatorio.extend(gerar_cabecalho(dados))
    relatorio.extend(gerar_secao_configuracoes(grupos_config))
    relatorio.extend(gerar_tabela_estatisticas(grupos_config))
    relatorio.extend(gerar_melhores_modelos(grupos_config))
    relatorio.extend(gerar_comparacao_geral(grupos_config))
    relatorio.extend(gerar_insights(grupos_config))
    relatorio.extend(gerar_metodologia())
    relatorio.extend(gerar_conclusao(grupos_config))
    relatorio.extend(gerar_rodape())

    # 4. Salvar arquivo
    print("4. Salvando arquivo...")
    arquivo_saida = Path(ARQUIVO_SAIDA)
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write('\n'.join(relatorio))

    print(f"   ✓ Relatório salvo em: {ARQUIVO_SAIDA}")
    print()
    print("=" * 70)
    print("✓ ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("=" * 70)
    print()
    print(f"Arquivo gerado: {arquivo_saida.absolute()}")
    print(f"Linhas: {len(relatorio)}")
    print()


if __name__ == "__main__":
    main()
