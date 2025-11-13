# Explicação Completa do Código main.py
## Classificação de Imagens: Gatos vs Não-Gatos 🐱

---

## **Parte 1: Visão Geral e Importações** 📚

### Contexto do Projeto
Baseado no README.md, este código resolve um problema de **classificação binária de imagens**: distinguir entre imagens de **"gatos"** (classe 1) e **"não-gatos"** (classe 0). O dataset vem do curso de Deep Learning do Andrew Ng, e as imagens são RGB com dimensões 64x64x3 (4096 pixels coloridos).

O código implementa **três abordagens diferentes**, conforme pedido no trabalho:
1. ✅ **Regressão Logística** (perceptron - modelo mais simples)
2. ✅ **Rede Neural de Camada Rasa** (1 camada oculta)
3. ✅ **Rede Convolucional (CNN)** (arquitetura mais sofisticada)

### As Importações

```python
import h5py
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
```

**O que cada biblioteca faz:**

- **`h5py`**: Lê arquivos HDF5 (`.h5`), formato usado para armazenar os datasets de treino e teste
- **`numpy`**: Biblioteca fundamental para operações matemáticas e manipulação de arrays/matrizes
- **`tensorflow`**: Framework de deep learning do Google
- **`keras`**: API de alto nível (integrada ao TensorFlow) que simplifica a criação de redes neurais
- **`layers`**: Módulo do Keras com as camadas que compõem as redes (Dense, Conv2D, etc.)

---

## **Parte 2: Carregamento e Pré-processamento dos Dados** 📂

Agora vamos entender como os dados são carregados e preparados:

```python
def carregar_dados():
    train_dataset = h5py.File('train_catvnoncat.h5', "r")
    test_dataset = h5py.File('test_catvnoncat.h5', "r")

    X_train = np.array(train_dataset["train_set_x"][:])
    Y_train = np.array(train_dataset["train_set_y"][:])
    X_test = np.array(test_dataset["test_set_x"][:])
    Y_test = np.array(test_dataset["test_set_y"][:])

    # Normalizar para [0,1]
    X_train = X_train / 255.
    X_test = X_test / 255.

    # Para regressão e RN rasa, achatar as imagens
    X_train_flat = X_train.reshape(X_train.shape[0], -1)
    X_test_flat = X_test.reshape(X_test.shape[0], -1)

    return X_train, Y_train, X_train_flat, X_test, Y_test, X_test_flat
```

### **Passo a passo:**

#### **1. Abertura dos arquivos HDF5**
```python
train_dataset = h5py.File('train_catvnoncat.h5', "r")
test_dataset = h5py.File('test_catvnoncat.h5', "r")
```
- Abre os arquivos `.h5` em modo leitura (`"r"`)
- `train_catvnoncat.h5`: imagens para treinar o modelo
- `test_catvnoncat.h5`: imagens para avaliar o modelo (dados nunca vistos)

#### **2. Extração dos dados**
```python
X_train = np.array(train_dataset["train_set_x"][:])
Y_train = np.array(train_dataset["train_set_y"][:])
```
- **`X_train`**: Imagens de treino (shape: `[num_exemplos, 64, 64, 3]`)
- **`Y_train`**: Labels/rótulos de treino (0 = não-gato, 1 = gato)
- **`X_test`** e **`Y_test`**: Mesma coisa, mas para teste

#### **3. Normalização** 🎯
```python
X_train = X_train / 255.
X_test = X_test / 255.
```
**Por que dividir por 255?**
- Pixels RGB têm valores de 0 a 255
- Dividindo por 255, os valores ficam entre 0 e 1
- **Benefício**: Redes neurais convergem melhor com dados normalizados (evita gradientes muito grandes)

#### **4. Achatamento (Flatten)** 🔄
```python
X_train_flat = X_train.reshape(X_train.shape[0], -1)
X_test_flat = X_test.reshape(X_test.shape[0], -1)
```
**O que está acontecendo:**
- Transforma cada imagem `[64, 64, 3]` em um vetor de **12.288 valores** (64×64×3)
- Exemplo: `[209, 64, 64, 3]` → `[209, 12288]` (209 imagens achatadas)

**Por que fazer isso?**
- Regressão Logística e Redes Rasas trabalham com **vetores**, não com imagens 3D
- CNNs preservam a estrutura espacial, então usam `X_train` original

#### **5. Retorno**
A função retorna **6 variáveis**:
- `X_train`: Imagens originais (para CNN)
- `Y_train`: Labels de treino
- `X_train_flat`: Imagens achatadas (para modelos lineares)
- `X_test`, `Y_test`, `X_test_flat`: Versões de teste

---

## **Parte 3: Modelo 1 - Regressão Logística** 🎯

A regressão logística é o modelo **mais simples** - essencialmente um **perceptron** (neurônio único).

```python
def regressao_logistica_keras():
    model = keras.Sequential([
        layers.Input(shape=(12288,)),  # 64x64x3
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
```

### **Anatomia do Modelo:**

#### **1. Arquitetura Sequential**
```python
model = keras.Sequential([...])
```
- `Sequential`: Modelo em que as camadas são empilhadas **linearmente** (uma após a outra)

#### **2. Camada de Entrada**
```python
layers.Input(shape=(12288,))
```
- Define que cada imagem entra como um vetor de **12.288 valores**
- Lembre-se: 64 × 64 × 3 = 12.288 pixels

#### **3. Camada Dense (Densa)**
```python
layers.Dense(1, activation='sigmoid')
```
**O que é uma camada Dense?**
- Camada totalmente conectada: cada entrada se conecta à saída
- **1**: Apenas **1 neurônio** de saída (classificação binária: gato ou não-gato)
- **sigmoid**: Função de ativação que transforma o resultado em probabilidade [0, 1]

**Matematicamente:**

\[ y = \sigma(w^T x + b) \]

Onde:
- \(x\): vetor de entrada (12.288 valores)
- \(w\): pesos aprendidos
- \(b\): bias
- \(\sigma\): função sigmoid

#### **4. Compilação**
```python
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```
**Parâmetros importantes:**
- **`optimizer='adam'`**: Algoritmo que ajusta os pesos (Adam é eficiente e adaptativo)
- **`loss='binary_crossentropy'`**: Função de perda para classificação binária
- **`metrics=['accuracy']`**: Durante o treino, também mostra a acurácia (% de acertos)

---

**Visualização do Modelo:**
```
Entrada (12.288) → [1 neurônio + sigmoid] → Saída (0 ou 1)
```

Este é o modelo **mais básico** possível - apenas uma transformação linear seguida de sigmoid.

---

## **Parte 4: Modelo 2 - Rede Neural de Camada Rasa** 🧠

Agora temos uma rede **um pouco mais complexa** com uma camada oculta intermediária.

```python
def rn_camada_rasa_keras():
    model = keras.Sequential([
        layers.Input(shape=(12288,)),
        layers.Dense(7, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
```

### **Anatomia do Modelo:**

#### **1. Camada de Entrada**
```python
layers.Input(shape=(12288,))
```
- Mesma entrada da regressão logística: vetor achatado de 12.288 valores

#### **2. Camada Oculta** ⭐
```python
layers.Dense(7, activation='relu')
```
**Novidades importantes:**
- **7 neurônios**: A rede pode aprender 7 "características" diferentes das imagens
- **`relu`** (Rectified Linear Unit): Função de ativação não-linear
  - ReLU: \(f(x) = \max(0, x)\)
  - Se valor negativo → 0
  - Se valor positivo → mantém o valor

**Por que ReLU é importante?**
- Adiciona **não-linearidade** ao modelo
- Permite que a rede aprenda padrões mais complexos que a regressão logística não consegue

#### **3. Camada de Saída**
```python
layers.Dense(1, activation='sigmoid')
```
- Igual à regressão logística: 1 neurônio com sigmoid
- Converte os 7 valores da camada oculta em 1 probabilidade final

#### **4. Compilação**
- Idêntica ao modelo anterior (adam, binary_crossentropy, accuracy)

---

### **Visualização da Arquitetura:**

```
Entrada (12.288 valores)
         ↓
[7 neurônios + ReLU] ← Camada Oculta (aprende features)
         ↓
[1 neurônio + sigmoid] ← Saída (probabilidade: gato?)
         ↓
    0.0 a 1.0
```

### **Diferença da Regressão Logística:**

| Aspecto | Regressão Logística | Rede Rasa |
|---------|-------------------|-----------|
| Camadas ocultas | 0 | 1 (com 7 neurônios) |
| Capacidade | Apenas linear | Pode aprender padrões não-lineares |
| Parâmetros | ~12.289 | ~86.000 (mais pesos) |

**Por que 7 neurônios?**
- Escolha do desenvolvedor (hiperparâmetro)
- Pequeno o suficiente para ser "raso" mas já adiciona capacidade de aprendizado

---

## **Parte 5: Modelo 3 - Rede Convolucional (CNN)** 🖼️

A CNN é o modelo **mais sofisticado** e adequado para imagens, pois preserva a **estrutura espacial** dos pixels.

```python
def cnn_keras():
    model = keras.Sequential([
        layers.Input(shape=(64, 64, 3)),
        layers.Conv2D(16, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
```

### **Anatomia do Modelo:**

#### **1. Camada de Entrada**
```python
layers.Input(shape=(64, 64, 3))
```
- **DIFERENÇA CRUCIAL**: Recebe a imagem **original** (não achatada!)
- `64, 64, 3`: altura × largura × canais RGB
- Preserva a **relação espacial** entre pixels vizinhos

#### **2. Primeira Camada Convolucional** 🔍
```python
layers.Conv2D(16, (3, 3), activation='relu')
```
**O que é convolução?**
- Aplica **16 filtros** de tamanho 3×3 que "varrem" a imagem
- Cada filtro detecta um padrão específico (bordas, texturas, cores, etc.)
- **Saída**: `[62, 62, 16]` (16 "mapas de características")

**Como funciona:**
```
Imagem original → [filtro 3×3] desliza → detecta padrões locais
```

#### **3. Primeira Camada de Pooling** 📉
```python
layers.MaxPooling2D((2, 2))
```
**O que é MaxPooling?**
- Reduz o tamanho das imagens pela **metade** (2×2)
- Pega o valor **máximo** de cada região 2×2
- **Saída**: `[31, 31, 16]`

**Benefícios:**
- Reduz a quantidade de parâmetros (mais eficiente)
- Mantém as características mais importantes
- Adiciona invariância à posição

#### **4. Segunda Camada Convolucional** 🔍🔍
```python
layers.Conv2D(32, (3, 3), activation='relu')
```
- Agora com **32 filtros** (mais capacidade de aprendizado)
- Detecta padrões mais complexos a partir dos 16 mapas anteriores
- **Saída**: `[29, 29, 32]`

#### **5. Segunda Camada de Pooling** 📉📉
```python
layers.MaxPooling2D((2, 2))
```
- Reduz novamente pela metade
- **Saída**: `[14, 14, 32]` = 6.272 valores

#### **6. Achatamento (Flatten)** 🔄
```python
layers.Flatten()
```
- Transforma `[14, 14, 32]` em vetor de **6.272 valores**
- Prepara os dados para as camadas densas finais

#### **7. Camadas Densas Finais**
```python
layers.Dense(64, activation='relu')
layers.Dense(1, activation='sigmoid')
```
- **64 neurônios**: Combinam as características aprendidas
- **1 neurônio final**: Decisão final (gato ou não-gato)

---

### **Visualização da Arquitetura Completa:**

```
Entrada [64×64×3]
       ↓
Conv2D (16 filtros) → [62×62×16] + ReLU
       ↓
MaxPooling → [31×31×16]
       ↓
Conv2D (32 filtros) → [29×29×32] + ReLU
       ↓
MaxPooling → [14×14×32]
       ↓
Flatten → [6.272 valores]
       ↓
Dense (64) + ReLU
       ↓
Dense (1) + sigmoid → Probabilidade [0, 1]
```

### **Por que CNNs são melhores para imagens?**

| Vantagem | Explicação |
|----------|------------|
| **Preserva estrutura espacial** | Pixels vizinhos têm relação (orelha de gato, bigodes, etc.) |
| **Detecta padrões locais** | Não precisa ver a imagem inteira de uma vez |
| **Invariância à posição** | Detecta gatos independente de onde estão na foto |
| **Hierarquia de features** | Camada 1: bordas → Camada 2: formas → Final: gato |

---

## **Parte 6: Execução Principal - Treinamento e Avaliação** 🚀

Esta é a parte onde **tudo acontece**: os modelos são treinados e testados.

```python
# Execução principal
if __name__ == "__main__":
    X_train, Y_train, X_train_flat, X_test, Y_test, X_test_flat = carregar_dados()

    # epochs : Quantas vezes o modelo "vê" todo o conjunto de treino
    # batch_size : Quantos exemplos o modelo usa de cada vez antes de atualizar os pesos
    # verbose : Controla o nível de mensagens mostradas durante o treino

    # Regressão Logística
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("          Regressão Logística         ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    model = regressao_logistica_keras()
    model.fit(X_train_flat, Y_train, epochs=50, batch_size=32, verbose=2)
    loss, acc = model.evaluate(X_test_flat, Y_test, verbose=0)
    print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%\n\n")

    # Rede Neural de Camada Rasa
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("     Rede Neural de Camada Rasa      ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    model = rn_camada_rasa_keras()
    model.fit(X_train_flat, Y_train, epochs=50, batch_size=32, verbose=2)
    loss, acc = model.evaluate(X_test_flat, Y_test, verbose=0)
    print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%\n\n")

    # Rede Convolucional (CNN)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("       Rede Convolucional (CNN)       ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    model = cnn_keras()
    model.fit(X_train, Y_train, epochs=20, batch_size=32, verbose=2)
    loss, acc = model.evaluate(X_test, Y_test, verbose=0)
    print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%")
```

### **Estrutura Geral:**

#### **1. Bloco `if __name__ == "__main__":`**
```python
if __name__ == "__main__":
```
- Garante que o código só execute quando o arquivo é rodado diretamente
- Se importado como módulo, esse bloco não executa

#### **2. Carregamento dos Dados**
```python
X_train, Y_train, X_train_flat, X_test, Y_test, X_test_flat = carregar_dados()
```
- Chama a função explicada na Parte 2
- Obtém dados normalizados, tanto originais quanto achatados

#### **3. Comentários Explicativos**
```python
# epochs : Quantas vezes o modelo "vê" todo o conjunto de treino
# batch_size : Quantos exemplos o modelo usa de cada vez antes de atualizar os pesos
# verbose : Controla o nível de mensagens mostradas durante o treino
```

**Conceitos importantes:**
- **Epochs**: Se há 200 imagens e você treina por 50 epochs, o modelo verá essas 200 imagens **50 vezes**
- **Batch size**: Atualiza os pesos a cada 32 imagens processadas (não espera ver todas)
- **Verbose**: `2` = progresso resumido, `1` = barra de progresso, `0` = silencioso

---

### **Treinamento dos Modelos:**

#### **MODELO 1: Regressão Logística**

```python
model = regressao_logistica_keras()
model.fit(X_train_flat, Y_train, epochs=50, batch_size=32, verbose=2)
loss, acc = model.evaluate(X_test_flat, Y_test, verbose=0)
print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%\n\n")
```

**Passo a passo:**

1. Cria o modelo (perceptron simples)
2. `model.fit()` - **TREINA** o modelo
   - `X_train_flat`: Imagens achatadas (12.288 valores)
   - `Y_train`: Labels (0 ou 1)
   - `epochs=50`: 50 passadas completas pelos dados
   - `batch_size=32`: Atualiza pesos a cada 32 imagens
   - `verbose=2`: Mostra progresso por epoch

3. `model.evaluate()` - **TESTA** o modelo
   - Usa `X_test_flat` e `Y_test` (dados nunca vistos!)
   - Retorna a perda (loss) e acurácia
   - `verbose=0`: Não mostra progresso

4. Imprime a acurácia em porcentagem

---

#### **MODELO 2: Rede Neural Rasa**

```python
model = rn_camada_rasa_keras()
model.fit(X_train_flat, Y_train, epochs=50, batch_size=32, verbose=2)
loss, acc = model.evaluate(X_test_flat, Y_test, verbose=0)
print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%\n\n")
```

**Exatamente o mesmo processo:**
- Cria modelo com 1 camada oculta (7 neurônios)
- Treina por 50 epochs
- Avalia no conjunto de teste
- Usa dados **achatados** (`X_train_flat`)

---

#### **MODELO 3: CNN**

```python
model = cnn_keras()
model.fit(X_train, Y_train, epochs=20, batch_size=32, verbose=2)
loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print(f"Acurácia no conjunto de teste: {acc * 100:.2f}%")
```

**Diferenças importantes:**

1. **Menos epochs** (20 vs 50):
   - CNNs são mais complexas, aprendem mais rápido
   - Evita overfitting (memorizar os dados de treino)

2. **Usa `X_train` (não achatado!)**:
   - Imagens originais `[64, 64, 3]`
   - Preserva estrutura espacial para convolução

3. **Mesmo processo**: treinar → avaliar → mostrar resultado

---

### **Resumo da Execução:**

```
1. Carrega dados (treino + teste)
           ↓
2. Treina Regressão Logística (50 epochs)
   → Testa e mostra acurácia
           ↓
3. Treina Rede Rasa (50 epochs)
   → Testa e mostra acurácia
           ↓
4. Treina CNN (20 epochs)
   → Testa e mostra acurácia
```

### **O que esperar nos resultados:**

| Modelo | Acurácia Esperada | Por quê? |
|--------|-------------------|----------|
| Regressão Logística | ~60-70% | Muito simples, apenas linear |
| Rede Rasa | ~65-75% | Um pouco melhor, tem não-linearidade |
| CNN | ~75-85%+ | **Melhor!** Aproveita estrutura espacial |

---

## **🎓 Conclusão**

O código implementa uma **comparação justa** entre três arquiteturas:

1. ✅ **Perceptron** (regressão logística) - baseline simples
2. ✅ **Rede rasa** - adiciona capacidade de aprendizado
3. ✅ **CNN** - estado da arte para visão computacional

Todos usam:
- Mesmo otimizador (Adam)
- Mesma função de perda (binary crossentropy)
- Mesmos dados (do Andrew Ng)

Isso permite **comparar diretamente** qual arquitetura funciona melhor para classificar gatos vs não-gatos! 🐱

---

## **Glossário de Termos**

- **Epoch**: Uma passagem completa por todos os dados de treinamento
- **Batch Size**: Quantidade de exemplos processados antes de atualizar os pesos
- **Loss (Perda)**: Medida de quão errado o modelo está
- **Accuracy (Acurácia)**: Porcentagem de acertos
- **Overfitting**: Quando o modelo memoriza os dados de treino mas não generaliza bem
- **Sigmoid**: Função que transforma valores em probabilidades [0, 1]
- **ReLU**: Função de ativação não-linear (max(0, x))
- **Flatten**: Achatar/transformar matriz em vetor
- **Dense**: Camada totalmente conectada
- **Conv2D**: Camada convolucional 2D para processamento de imagens
- **MaxPooling**: Redução de dimensionalidade mantendo características importantes
