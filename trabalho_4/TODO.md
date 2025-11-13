# Lista de Tarefas Pendentes - Trabalho Gato vs Não-Gato

## 📋 Status Geral

Este documento lista todas as informações e implementações necessárias para completar o relatório do trabalho, conforme especificado no README.md.

**Progresso atual:**
- ✅ Matriz de Confusão implementada (1/6 tarefas críticas)
- 📊 3 imagens PNG geradas para o relatório
- 📦 requirements.txt criado

---

## 🔴 **TAREFAS CRÍTICAS (Obrigatórias para o Relatório)** - 1/6 Concluída

### 1. **Implementar Matriz de Confusão**
**Status:** ✅ CONCLUÍDO
**Prioridade:** 🔴 ALTA
**Requisito do trabalho:** Sim (mencionado explicitamente no README)

**O que foi feito:**
- ✅ Adicionado código para gerar predições no conjunto de teste
- ✅ Calculada matriz de confusão usando `sklearn.metrics.confusion_matrix`
- ✅ Gerada visualização da matriz (heatmap com seaborn)
- ✅ Salva imagem para incluir no relatório (3 arquivos PNG)
- ✅ Interpretação dos resultados (VP, VN, FP, FN) exibida no console

**Implementação:**
- Função `plotar_matriz_confusao()` criada (linhas 30-45 do main.py)
- Integrada com os 3 modelos (Regressão Logística, Rede Rasa, CNN)
- Gera arquivos: `confusion_matrix_regressão_logística.png`, `confusion_matrix_rede_rasa.png`, `confusion_matrix_cnn.png`
- Exibe VP, VN, FP, FN no console para cada modelo

---

### 2. **Documentar Experimentos Realizados**
**Status:** ❌ NÃO DOCUMENTADO
**Prioridade:** 🔴 ALTA
**Requisito do trabalho:** Sim ("Quantos e Quais experimentos foram feitos até chegar no resultado final")

**O que fazer:**
- Documentar todas as tentativas e variações testadas
- Registrar quais hiperparâmetros foram experimentados:
  - Diferentes números de epochs
  - Diferentes learning rates
  - Diferentes arquiteturas (quantos neurônios, camadas, etc.)
  - Diferentes batch sizes
- Explicar por que a configuração final foi escolhida
- Criar tabela comparativa dos experimentos

**Formato sugerido:**
```
Experimento 1: Regressão Logística com 30 epochs → Acurácia: X%
Experimento 2: Regressão Logística com 50 epochs → Acurácia: Y%
Experimento 3: Rede Rasa com 5 neurônios → Acurácia: Z%
...
```

---

### 3. **Documentar Taxa de Aprendizado (Learning Rate)**
**Status:** ⚠️ IMPLÍCITO (não explícito no código)
**Prioridade:** 🔴 ALTA
**Requisito do trabalho:** Sim ("taxa de aprendizado")

**O que fazer:**
- Tornar explícito o learning rate no código
- Atualmente usa Adam com learning rate padrão (0.001)
- Modificar código para:
```python
from tensorflow.keras.optimizers import Adam
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, ...)
```
- Documentar no relatório o valor utilizado
- Explicar por que essa taxa foi escolhida

---

### 4. **Gerar Histórico de Treinamento**
**Status:** ❌ NÃO SALVO
**Prioridade:** 🟡 MÉDIA
**Requisito do trabalho:** Sim (para mostrar "como foi o treinamento")

**O que fazer:**
- Salvar o objeto `history` retornado por `model.fit()`
- Gerar gráficos de:
  - Loss vs Epochs (treino e validação)
  - Accuracy vs Epochs (treino e validação)
- Adicionar conjunto de validação (validation_split=0.2)
- Salvar gráficos para o relatório

**Código necessário:**
```python
history = model.fit(..., validation_split=0.2)
# Plotar history.history['loss'], history.history['val_loss']
```

---

### 5. **Implementar Métricas Adicionais**
**Status:** ❌ NÃO IMPLEMENTADO
**Prioridade:** 🟡 MÉDIA
**Requisito do trabalho:** Implícito (para análise completa)

**O que fazer:**
- Calcular e reportar:
  - **Precision** (Precisão)
  - **Recall** (Revocação/Sensibilidade)
  - **F1-Score**
  - **Especificidade**
- Usar `sklearn.metrics.classification_report` para relatório completo

**Bibliotecas necessárias:**
```python
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
```

---

### 6. **Documentar Uso de Regularização**
**Status:** ❌ NÃO UTILIZADA
**Prioridade:** 🟡 MÉDIA
**Requisito do trabalho:** Sim ("uso de regularização, etc.")

**O que fazer:**
- Atualmente NENHUMA regularização é usada
- Opções para experimentar:
  - **Dropout** (camadas de dropout entre Dense layers)
  - **L2 Regularization** (kernel_regularizer em Dense/Conv2D)
  - **Early Stopping** (parar quando validação piorar)
- Documentar no relatório:
  - Se foi usado ou não
  - Por que foi ou não foi necessário
  - Resultados com e sem regularização (se testado)

---

## 🟢 **TAREFAS COMPLEMENTARES (Recomendadas)**

### 7. **Mostrar Quantidade de Dados**
**Status:** ❌ NÃO MOSTRADO
**Prioridade:** 🟢 BAIXA

**O que fazer:**
- Imprimir quantidade de exemplos:
```python
print(f"Exemplos de treino: {len(X_train)}")
print(f"Exemplos de teste: {len(X_test)}")
print(f"Distribuição de classes: {np.bincount(Y_train)}")
```

---

### 8. **Medir Tempo de Treinamento**
**Status:** ❌ NÃO MEDIDO
**Prioridade:** 🟢 BAIXA

**O que fazer:**
- Adicionar medição de tempo:
```python
import time
start = time.time()
model.fit(...)
end = time.time()
print(f"Tempo de treino: {end - start:.2f}s")
```

---

### 9. **Mostrar Exemplos de Predições**
**Status:** ❌ NÃO IMPLEMENTADO
**Prioridade:** 🟢 BAIXA

**O que fazer:**
- Selecionar algumas imagens do conjunto de teste
- Mostrar imagem + predição + label real
- Incluir no relatório exemplos de:
  - Acertos (VP e VN)
  - Erros (FP e FN)

---

### 10. **Visualizar Arquitetura das Redes**
**Status:** ❌ NÃO IMPLEMENTADO
**Prioridade:** 🟢 BAIXA

**O que fazer:**
- Usar `model.summary()` para mostrar detalhes
- Gerar diagrama visual com `keras.utils.plot_model()`
- Incluir no relatório

---

### 11. **Análise de Overfitting/Underfitting**
**Status:** ❌ NÃO ANALISADO
**Prioridade:** 🟡 MÉDIA

**O que fazer:**
- Comparar loss de treino vs validação
- Comparar accuracy de treino vs teste
- Identificar se há overfitting (treino >> teste)
- Documentar conclusões no relatório

---

## 📊 **INFORMAÇÕES JÁ DISPONÍVEIS NO CÓDIGO ATUAL**

### ✅ **Informações Completas:**
- [x] Arquitetura das 3 redes (linhas 49-89)
- [x] Função de perda: binary_crossentropy
- [x] Otimizador: Adam
- [x] Batch size: 32
- [x] Epochs: 50 (logística/rasa) e 20 (CNN)
- [x] Acurácia final no teste
- [x] Normalização dos dados (divisão por 255)
- [x] Pré-processamento (flatten para modelos não-convolucionais)
- [x] Matriz de Confusão implementada e visualizada
- [x] Métricas VP, VN, FP, FN calculadas

### ⚠️ **Informações Parciais:**
- [~] Taxa de aprendizado (usa padrão 0.001, mas não explícito)
- [~] Loss final (capturado mas não reportado)

---

## 🎯 **PRIORIZAÇÃO SUGERIDA**

### **Fase 1 - Crítico (Fazer PRIMEIRO):**
1. ✅ ~~Implementar Matriz de Confusão~~ **CONCLUÍDO**
2. Documentar experimentos realizados
3. Tornar learning rate explícito
4. Documentar uso (ou não-uso) de regularização

### **Fase 2 - Importante (Fazer DEPOIS):**
5. Gerar histórico de treinamento com gráficos
6. Calcular métricas adicionais (Precision, Recall, F1)
7. Análise de overfitting/underfitting

### **Fase 3 - Complementar (Se houver tempo):**
8. Mostrar quantidade de dados
9. Medir tempo de treinamento
10. Exemplos de predições
11. Visualizar arquitetura

---

## 📝 **CHECKLIST PARA O RELATÓRIO**

Use este checklist ao escrever o relatório:

### Seção: Experimentos
- [ ] Tabela com todos os experimentos realizados
- [ ] Justificativa para escolha de hiperparâmetros
- [ ] Comparação entre diferentes configurações

### Seção: Treinamento
- [ ] Taxa de aprendizado documentada
- [ ] Arquitetura de cada rede descrita
- [ ] Uso de regularização (ou justificativa de não-uso)
- [ ] Gráficos de loss e accuracy por epoch
- [ ] Quantidade de epochs e batch size justificada

### Seção: Resultados
- [x] Taxa de acertos de cada modelo
- [x] Matriz de confusão de cada modelo
- [ ] Precision, Recall e F1-Score
- [ ] Comparação entre os 3 modelos
- [x] Análise de erros (FP e FN) - valores exibidos

### Seção: Análise
- [ ] Discussão sobre qual modelo performou melhor
- [ ] Por que a CNN é superior (ou não)?
- [ ] Limitações observadas
- [ ] Possíveis melhorias

---

## 🔧 **MODIFICAÇÕES NECESSÁRIAS NO CÓDIGO**

### Arquivo: `main.py`

**Adicionar:**
1. ✅ Import de bibliotecas de métricas e visualização
2. ✅ Função para gerar matriz de confusão
3. Função para plotar histórico de treinamento
4. Função para calcular métricas adicionais
5. Salvar modelos treinados (opcional)
6. Logging detalhado dos experimentos

**Arquivos criados:**
- ✅ `requirements.txt` - Dependências do projeto

**Criar novo arquivo:**
- `analise_resultados.py` - Script separado para análise detalhada

---

## 📚 **REFERÊNCIAS ÚTEIS**

- Matriz de Confusão: `sklearn.metrics.confusion_matrix`
- Métricas: `sklearn.metrics.classification_report`
- Plots: `matplotlib.pyplot` e `seaborn`
- Keras Callbacks: `tensorflow.keras.callbacks.History`

---

## ✅ **QUANDO CONSIDERAR COMPLETO**

O trabalho estará completo quando:

1. ✅ Todos os itens da Fase 1 estiverem implementados
2. ✅ Relatório contiver todas as informações da checklist
3. ✅ Código gerar todas as figuras/tabelas necessárias
4. ✅ Experimentos estiverem documentados
5. ✅ Análise crítica dos resultados estiver escrita

---

**Última atualização:** 2025-11-13
**Status geral:** 🟡 EM ANDAMENTO - Matriz de Confusão ✅ CONCLUÍDA
