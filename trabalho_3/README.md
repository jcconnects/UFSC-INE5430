# Trabalho 3 - Raciocínio Probabilístico

## Descrição

Este trabalho aborda a aplicação de Redes Bayesianas para modelagem e inferência probabilística em dois cenários distintos:

### PARTE 1: Detecção de Fraude em Cartão de Crédito
- **Variáveis:** Fraude, Idade, Sexo, Gasolina, Crédito para Celular
- **6 Questões:** Cálculos de probabilidades condicionais, conjuntas e marginais
- **Técnicas:** Regra da cadeia, inferência por enumeração, Teorema de Bayes

### PARTE 2: Desonestidade Acadêmica
- **Variáveis:** Nível de Ensino, Cola, Viu Colega Colando, Estuda, Sente-se Penalizado
- **2 Questões:** Construção da rede e cálculos probabilísticos
- **Foco:** Modelagem da rede a partir de descrições textuais

## Arquivos

- **`main.tex`**: Documento LaTeX principal com todo o conteúdo do trabalho
- **`main.pdf`**: Documento final compilado
- **`calculations.py`**: Script Python com cálculos das questões complexas (3-6 Parte 1, Questão 2 Parte 2)
- **`ref.bib`**: Referências bibliográficas (se necessário)
- **`desc_raciocinio_probabilistico.md`**: Descrição detalhada das diretrizes do trabalho

## Como Compilar

O documento requer LuaLaTeX para compilação:

```bash
lualatex main.tex
```

Ou usando o caminho completo:

```bash
/Library/TeX/texbin/lualatex main.tex
```

## Como Executar os Cálculos

Para ver os cálculos detalhados das questões complexas:

```bash
python3 calculations.py
```

Isso exibirá:
- Todos os cálculos passo a passo
- Probabilidades intermediárias
- Resultados finais com interpretações

## Estrutura do Documento

1. **Introdução**: Contextualização sobre Redes Bayesianas
2. **PARTE 1**: 
   - Descrição do problema de detecção de fraude
   - Variáveis e estrutura da rede
   - Tabelas de probabilidade condicional (CPTs)
   - 6 questões com cálculos completos e interpretações
3. **PARTE 2**:
   - Descrição do problema de desonestidade acadêmica
   - Modelagem da rede (variáveis, topologia, CPTs)
   - 2 questões com cálculos completos e interpretações
4. **Conclusão**: Principais resultados e aprendizados
5. **Apêndice**: Código Python dos cálculos computacionais

## Principais Resultados

### PARTE 1
- P(G=sim) = 1,02%
- P(C=sim) = 68,65%
- P(C=sim | G=sim) = 69,14%
- P(F=sim | C=sim, G=não) = 0,112%

### PARTE 2
- P(Cola=Sim) = 33%
- P(N=Secundário | V=Sim, P=Sim) = 55%

## Autores

- André Thiago Pfleger
- Gustavo Girotto
- João Pedro Schmidt Cordeiro

## Disciplina

INE5430 - Inteligência Artificial  
Universidade Federal de Santa Catarina (UFSC)

