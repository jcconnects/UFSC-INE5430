# Análise dos Resultados - Trabalho 4: Gato vs Não-Gato

**Data da Análise:** 2025-11-13 11:08:04
**Total de Execuções:** 10
**Total de Experimentos:** 100

---

## 1. Configurações Testadas

### CNN 10e

- **10 epochs**

### CNN 20e

- **20 epochs**

### CNN 30e

- **30 epochs**

### Rede Rasa 10n

- **10 neurônios**, 50 epochs

### Rede Rasa 20n

- **20 neurônios**, 50 epochs

### Rede Rasa 5n

- **5 neurônios**, 50 epochs

### Rede Rasa 7n

- **7 neurônios**, 50 epochs

### Regressão Logística 30e

- **30 epochs**

### Regressão Logística 50e

- **50 epochs**

### Regressão Logística 70e

- **70 epochs**

## 2. Estatísticas Consolidadas

Média ± Desvio Padrão de múltiplas execuções:

| Modelo | Config | N | Acc Treino | Acc Val | Acc Teste | Loss Teste | Tempo (s) | Params | Status |
|--------|--------|---|------------|---------|-----------|------------|-----------|--------|--------|
| CNN | 10e | 10 | 89.6±3.6 | 76.0±4.4 | 61.8±16.7 | 0.738±0.350 | 1.7 | 406,625 | 🔴 Overfitting Severo |
| CNN | 20e | 10 | 93.5±3.7 | 77.4±4.5 | 78.0±9.5 | 0.558±0.290 | 2.7 | 406,625 | 🔴 Overfitting Severo |
| CNN | 30e | 10 | 99.0±0.9 | 74.8±3.8 | 79.0±6.1 | 0.602±0.224 | 3.9 | 406,625 | 🔴 Overfitting Severo |
| Rede Rasa | 10n, 50e | 10 | 78.5±14.0 | 60.7±10.4 | 53.4±19.0 | 0.784±0.150 | 2.2 | 122,901 | 🔴 Overfitting Severo |
| Rede Rasa | 20n, 50e | 10 | 83.9±17.1 | 61.2±9.8 | 54.8±17.0 | 0.893±0.177 | 2.3 | 245,801 | 🔴 Overfitting Severo |
| Rede Rasa | 5n, 50e | 10 | 66.0±6.2 | 69.8±5.3 | 36.8±8.9 | 0.740±0.032 | 2.1 | 61,451 | 🔴 Overfitting Severo |
| Rede Rasa | 7n, 50e | 10 | 66.2±6.6 | 69.5±6.0 | 38.4±13.9 | 0.743±0.046 | 2.1 | 86,031 | 🔴 Overfitting Severo |
| Regressão Logística | 30e | 10 | 88.0±4.8 | 54.8±7.8 | 66.8±19.7 | 0.766±0.359 | 1.2 | 12,289 | 🔴 Overfitting Severo |
| Regressão Logística | 50e | 10 | 94.3±1.5 | 52.4±3.9 | 73.4±5.7 | 0.724±0.095 | 1.9 | 12,289 | 🔴 Overfitting Severo |
| Regressão Logística | 70e | 10 | 96.8±1.3 | 52.9±6.6 | 71.2±5.6 | 0.816±0.100 | 2.5 | 12,289 | 🔴 Overfitting Severo |

**Legenda:**
- `N`: Número de execuções
- `Config`: n=neurônios, e=epochs
- Valores mostrados como Média±Desvio

## 3. Melhores Configurações por Modelo

### CNN

**Melhor:** 30 epochs
- Acurácia Teste: **79.00% ± 6.13%**
- Acurácia Treino: 99.04%
- Acurácia Validação: 74.76%
- Loss Teste: 0.6021
- Status: 🔴 Overfitting Severo
- Tempo Médio: 3.91s

**Ranking:**
1. 30e: 79.00% ± 6.13%
2. 20e: 78.00% ± 9.48%
3. 10e: 61.80% ± 16.72%

### Rede Rasa

**Melhor:** 20 neurônios, 50 epochs
- Acurácia Teste: **54.80% ± 16.98%**
- Acurácia Treino: 83.89%
- Acurácia Validação: 61.19%
- Loss Teste: 0.8927
- Status: 🔴 Overfitting Severo
- Tempo Médio: 2.32s

**Ranking:**
1. 20n, 50e: 54.80% ± 16.98%
2. 10n, 50e: 53.40% ± 19.00%
3. 7n, 50e: 38.40% ± 13.91%

### Regressão Logística

**Melhor:** 50 epochs
- Acurácia Teste: **73.40% ± 5.74%**
- Acurácia Treino: 94.25%
- Acurácia Validação: 52.38%
- Loss Teste: 0.7240
- Status: 🔴 Overfitting Severo
- Tempo Médio: 1.85s

**Ranking:**
1. 50e: 73.40% ± 5.74%
2. 70e: 71.20% ± 5.59%
3. 30e: 66.80% ± 19.67%

## 4. Comparação Geral: Melhor de Cada Tipo

| Rank | Modelo | Configuração | Acc Teste | Loss Teste | Parâmetros | Tempo |
|------|--------|--------------|-----------|------------|------------|-------|
| 🥇 1 | CNN | 30e | **79.00%** ± 6.13% | 0.6021 | 406,625 | 3.9s |
| 🥈 2 | Regressão Logística | 50e | **73.40%** ± 5.74% | 0.7240 | 12,289 | 1.9s |
| 🥉 3 | Rede Rasa | 20n, 50e | **54.80%** ± 16.98% | 0.8927 | 245,801 | 2.3s |

### 🏆 Modelo Vencedor

**CNN** é o modelo com melhor desempenho no teste!

- **Configuração:** 30 epochs
- **Acurácia Teste:** 79.00% ± 6.13%
- **Parâmetros:** 406,625
- **Tempo Médio:** 3.91s

## 5. Insights e Observações

### 5.1 Análise de Overfitting

**Configurações com Overfitting:**
- Rede Rasa (5n, 50e): diferença de 29.2% (Teste: 36.8%)
- Rede Rasa (20n, 50e): diferença de 29.1% (Teste: 54.8%)
- CNN (10e): diferença de 27.8% (Teste: 61.8%)
- Rede Rasa (7n, 50e): diferença de 27.8% (Teste: 38.4%)
- Regressão Logística (70e): diferença de 25.6% (Teste: 71.2%)
- Rede Rasa (10n, 50e): diferença de 25.1% (Teste: 53.4%)
- Regressão Logística (30e): diferença de 21.2% (Teste: 66.8%)
- Regressão Logística (50e): diferença de 20.9% (Teste: 73.4%)
- CNN (30e): diferença de 20.0% (Teste: 79.0%)
- CNN (20e): diferença de 15.5% (Teste: 78.0%)

### 5.2 Impacto do Número de Epochs

**CNN:**
- 10 epochs → 30 epochs: 61.8% → 79.0% (↑ 17.2%)

**Rede Rasa:**
- 50 epochs → 50 epochs: 36.8% → 54.8% (↑ 18.0%)

**Regressão Logística:**
- 30 epochs → 70 epochs: 66.8% → 71.2% (↑ 4.4%)

### 5.3 Estabilidade dos Modelos

Configurações com menor variabilidade (mais estáveis):

- Regressão Logística (70e): 71.2% ± 5.59%
- Regressão Logística (50e): 73.4% ± 5.74%
- CNN (30e): 79.0% ± 6.13%
- Rede Rasa (5n, 50e): 36.8% ± 8.85%
- CNN (20e): 78.0% ± 9.48%

## 6. Metodologia

### Configuração dos Experimentos

- **Otimizador:** Adam (learning rate: 0.001)
- **Função de Perda:** Binary Crossentropy
- **Batch Size:** 32
- **Validação:** 20% dos dados de treino
- **Normalização:** Pixels divididos por 255 (range [0, 1])
- **Múltiplas Execuções:** Cada configuração foi executada múltiplas vezes

### Arquiteturas

**1. Regressão Logística:**
- Input: 12288 features (64×64×3 flatten)
- Dense(1, sigmoid)
- Parâmetros: 12,289

**2. Rede Neural Rasa:**
- Input: 12288 features
- Dense(n, relu) + Dense(1, sigmoid)
- Parâmetros: varia conforme n (neurônios)

**3. CNN:**
- Input: 64×64×3
- Conv2D(16) → MaxPool → Conv2D(32) → MaxPool → Flatten → Dense(64, relu) → Dense(1, sigmoid)
- Parâmetros: 406,625

## 7. Conclusões

1. **Melhor Modelo:** CNN alcançou a melhor acurácia média de teste (79.00%)

2. **Complexidade vs Desempenho:**
   - Modelos mais complexos (CNN) tendem a ter melhor desempenho
   - Regressão Logística é mais rápida mas menos precisa
   - Rede Rasa oferece meio-termo entre velocidade e precisão

3. **Recomendações:**
   - Para este dataset, use CNN com 30 epochs
   - Considere usar regularização (Dropout) se overfitting for problema
   - Dataset pequeno (50 imagens teste) causa alta variabilidade

---

**Observações:**
- Este relatório foi gerado automaticamente a partir dos dados experimentais
- Estatísticas calculadas: Média ± Desvio Padrão
- Dataset: 209 treino (167 após split 80/20), 50 teste

*Gerado em: 2025-11-13 11:08:04*