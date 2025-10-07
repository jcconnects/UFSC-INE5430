Prezado assistente de IA,

A seguir, apresento uma diretriz estruturada e detalhada para a execução das tarefas delineadas no documento "Proposta de Trabalho sobre Raciocínio Probabilístico 2018_2.pdf". O trabalho está dividido em duas partes distintas, cada uma com seus próprios objetivos e requisitos. É imperativo que todos os cálculos solicitados sejam explicitamente demonstrados.

### **Estrutura Geral do Documento de Resposta**

O documento de resposta final deve ser segmentado em "PARTE 1" e "PARTE 2", conforme o arquivo original. Cada seção deve conter as respostas para as questões correspondentes, com a demonstração completa do raciocínio matemático e dos cálculos efetuados.

---

### **Instruções Detalhadas para a PARTE 1**

**Objetivo:** Utilizar a Rede Bayesiana fornecida para calcular probabilidades condicionais e conjuntas relacionadas a um sistema de detecção de fraude de cartão de crédito.

**Variáveis do Modelo:**
* [cite_start]**F (Fraude):** {sim, não} [cite: 10]
* [cite_start]**I (Idade):** {<30, 30-50, >50} [cite: 11]
* [cite_start]**S (Sexo):** {masculino, feminino} [cite: 12]
* [cite_start]**G (Gasolina):** {sim, não} (compra nas últimas 24h) [cite: 13]
* [cite_start]**C (Crédito para Celular):** {sim, não} (compra nas últimas 24h) [cite: 14]

**Topologia da Rede Bayesiana:**
[cite_start]A estrutura de dependência, conforme o diagrama[cite: 25, 26, 27, 36, 38], é a seguinte:
* As variáveis `I` (Idade) e `S` (Sexo) são independentes.
* A variável `F` (Fraude) é condicionalmente dependente de `I` e `S`.
* A variável `G` (Gasolina) é condicionalmente dependente de `F`.
* A variável `C` (Crédito para Celular) é condicionalmente dependente de `F`.

**Procedimento para Execução:**

Para cada uma das seis questões a seguir, realize os seguintes passos:
1.  Identifique a probabilidade que precisa ser calculada.
2.  Extraia os valores de probabilidade necessários das tabelas de probabilidade condicional (CPTs) fornecidas no documento.
3.  Aplique as fórmulas fundamentais da teoria da probabilidade e da inferência em Redes Bayesianas (e.g., regra da cadeia, inferência por enumeração, teorema de Bayes).
4.  Apresente todos os cálculos de forma clara e sequencial.
5.  Forneça a resposta numérica final.

**Questões a Serem Resolvidas:**

1.  **Cálculo de $P(G=não \mid F=sim)$:**
    * [cite_start]**Descrição:** Calcular a probabilidade de não ter havido uma compra de gasolina, dado que a transação é uma fraude. [cite: 79]
    * **Metodologia:** Este valor pode ser lido diretamente da tabela de probabilidade condicional da variável `G`, condicionada a `F`. Localize a entrada correspondente a $P(G=não \mid F=sim)$.

2.  **Cálculo da Probabilidade Conjunta $P(F=sim, G=sim, I=>50, S=fem, C=não)$:**
    * [cite_start]**Descrição:** Calcular a probabilidade de o sistema estar no estado específico onde a transação é uma fraude, houve compra de gasolina, o titular tem mais de 50 anos, é do sexo feminino e não houve compra de crédito para celular. [cite: 81]
    * **Metodologia:** Utilize a regra da cadeia para Redes Bayesianas para expandir a probabilidade conjunta:
        $P(I, S, F, G, C) = P(I) \times P(S) \times P(F \mid I, S) \times P(G \mid F) \times P(C \mid F)$
    * Substitua as variáveis pelos seus respectivos estados e extraia cada termo da probabilidade das tabelas fornecidas no documento.

3.  **Cálculo da Probabilidade Marginal $P(G=sim)$:**
    * [cite_start]**Descrição:** Calcular a probabilidade total de haver uma compra de gasolina nas últimas 24 horas. [cite: 82]
    * **Metodologia:** Utilize a inferência por enumeração, marginalizando as outras variáveis. A fórmula a ser aplicada é:
        $P(G=sim) = \sum_{F,I,S} P(G=sim \mid F) \times P(F \mid I, S) \times P(I) \times P(S)$
    * Este cálculo exige a soma sobre todos os estados possíveis das variáveis `F`, `I` e `S`.

4.  **Cálculo da Probabilidade Marginal $P(C=sim)$:**
    * [cite_start]**Descrição:** Calcular a probabilidade total de haver uma compra de créditos para celular nas últimas 24 horas. [cite: 84]
    * **Metodologia:** Semelhante à questão 3, utilize a inferência por enumeração, marginalizando sobre `F`, `I` e `S`:
        $P(C=sim) = \sum_{F,I,S} P(C=sim \mid F) \times P(F \mid I, S) \times P(I) \times P(S)$

5.  **Cálculo da Probabilidade Condicional $P(C=sim \mid G=sim)$:**
    * [cite_start]**Descrição:** Calcular a probabilidade de haver compra de créditos para celular, dado que houve compra de gasolina. [cite: 86]
    * **Metodologia:** Aplique a definição de probabilidade condicional:
        $P(C=sim \mid G=sim) = \frac{P(C=sim, G=sim)}{P(G=sim)}$
    * O denominador $P(G=sim)$ já foi calculado na questão 3. O numerador $P(C=sim, G=sim)$ deve ser calculado por enumeração. Note que `C` e `G` são condicionalmente independentes dado `F`.

6.  **Cálculo da Probabilidade Condicional $P(F=sim \mid C=sim, G=não)$:**
    * [cite_start]**Descrição:** Calcular a probabilidade de a transação ser uma fraude, dado que houve compra de créditos para celular, mas não de gasolina. [cite: 88]
    * **Metodologia:** Utilize o Teorema de Bayes:
        $P(F=sim \mid C=sim, G=não) = \frac{P(C=sim, G=não \mid F=sim) \times P(F=sim)}{P(C=sim, G=não)}$
    * Expanda cada termo, lembrando que `C` e `G` são condicionalmente independentes dado `F`. O termo no denominador deve ser calculado por marginalização.

---

### **Instruções Detalhadas para a PARTE 2**

**Objetivo:** Modelar um novo cenário sobre desonestidade acadêmica usando uma Rede Bayesiana e, em seguida, usar o modelo para calcular probabilidades específicas.

**Procedimento para Execução:**

**Etapa 1: Modelagem da Rede Bayesiana**

1.  **Definição das Variáveis Aleatórias e seus Domínios:**
    * [cite_start]Analise o texto [cite: 91-98] e identifique as variáveis relevantes. Proponha um conjunto de variáveis como:
        * **Nível (N):** {Universitário, Secundário, Fundamental}
        * **Cola (C):** {Sim, Não}
        * **ViuColegaColar (V):** {Sim, Não}
        * **Estuda (E):** {Sim, Não}
        * **SentePenalizado (P):** {Sim, Não}

2.  **Definição da Topologia da Rede (Estrutura de Dependências):**
    * Com base no texto, determine as relações de causa e efeito entre as variáveis. Por exemplo:
        * [cite_start]A probabilidade de "Colar" depende do "Nível" de ensino. [cite: 93, 94]
        * [cite_start]A probabilidade de "Ver Colega Colar" depende do "Nível". [cite: 94, 95]
        * [cite_start]A probabilidade de "Estudar" depende do "Nível". [cite: 96]
        * [cite_start]A probabilidade de "Sentir-se Penalizado" depende de "Colar" e "Estudar". [cite: 97, 98]
    * Desenhe o grafo acíclico dirigido que representa essas dependências.

3.  **Construção das Tabelas de Probabilidade Condicional (CPTs):**
    * Quantifique as dependências extraindo as probabilidades do texto para preencher as CPTs de cada variável.
        * [cite_start]$P(N)$: {Universitário: 0.1, Secundário: 0.3, Fundamental: 0.6} [cite: 92]
        * [cite_start]$P(E \mid N)$: Ex: $P(E=Sim \mid N=Universitário) = 0.5$ [cite: 96]
        * [cite_start]$P(C \mid N)$: Ex: $P(C=Sim \mid N=Universitário) = 0.6$ [cite: 93]
        * [cite_start]$P(V \mid N)$: Ex: $P(V=Sim \mid N=Fundamental) = 0.1$ [cite: 95]
        * [cite_start]$P(P \mid C, E)$: Ex: $P(P=Sim \mid C=Sim, E=Sim) = 0.1$ [cite: 97]
    * Preencha todas as CPTs com os valores fornecidos e seus complementares.

**Etapa 2: Cálculos de Probabilidade com o Modelo Criado**

1.  [cite_start]**Calcular a probabilidade de um aluno colar, $P(C=Sim)$:** [cite: 100]
    * **Metodologia:** Utilize a inferência por enumeração, marginalizando a variável "Nível":
        $P(C=Sim) = \sum_{n \in N} P(C=Sim \mid N=n) \times P(N=n)$
    * Use os valores das CPTs criadas na Etapa 1.

2.  [cite_start]**Calcular $P(N=Secundário \mid V=Sim, P=Sim)$:** [cite: 101]
    * **Metodologia:** Calcular a probabilidade de um aluno ser do ensino secundário, dado que viu um colega colar e se sentiu penalizado na nota. Aplique o Teorema de Bayes e a inferência por enumeração. A resolução desta consulta é mais complexa e exigirá a expansão completa da probabilidade conjunta e a posterior normalização.