# 01 - Introdução

Motor de Inferência
Base de Regras
### Memória de Trabalho
Contêm símbolos terminais e não terminais (Do mesmo jeito que formais)
## Três linhas da IA
- Simbólica
- Conexionista
- Evolutiva
## Dissociação entre IA
- IA fraca
- IA forte
## Áreas da IA
- Criar modelos
- Criar/desenvolver frameworks
- Criar uma aplicação
# 02 - Exemplo
Técnicas de IA são gerais e dissociadas ao conhecimento que leva à solução do problema. Precisa ter essa característica de estar desacoplada do problema em si.

A cada jogada, cada step, de tomada de decisão, é necessário criar uma nova árvore de decisão. No exemplo do jogo Tic Tac Toe uma árvore é criada a cada jogada.

Para diminuir o processamento nas árvores, **podemos utilizar cortes alpha e beta**. 
![[Anotações de aula - Exemplo de cortes min e max.png]]

# 03 - Knowledge Representation
> [!PDF|yellow] [[03-KR.pdf#page=2&selection=17,0,18,65&color=yellow|03-KR, p.2]]
> > Representação de Conhecimento e Raciocínio é a parte da IA que diz respeito a como um agente usa o que sabe para decidir o que fazer

"Não reinventamos nada na IA"

---
## Definição de conhecimento para a área da IA
> [!PDF|yellow] [[03-KR.pdf#page=2&selection=17,0,18,65&color=yellow|03-KR, p.2]]
> > Representação de Conhecimento e Raciocínio é a parte da IA que diz respeito a como um agente usa o que sabe para decidir o que fazer

## Definição de representação
> [!PDF|yellow] [[03-KR.pdf#page=5&selection=2,0,2,67&color=yellow|03-KR, p.5]]
> > relação entre dois domínios: o real e o da representação (símbolos)

Existem alguns métodos de representação diferentes:
[[03-KR.pdf#page=6&selection=5,0,6,64&color=yellow|03-KR, p.6]]
## Definição de raciocínio
> [!PDF|yellow] [[03-KR.pdf#page=6&selection=5,0,6,64&color=yellow|03-KR, p.6]]
> > Manipulação formal de símbolos que representam uma coleção de proposições para produzir outras proposições (inferência lógica)


## Extra
Preciso fazer algumas restrições de complexidade para aplicar a IA no mundo real, no problema que se quer solucionar:
- Limitar o domínio de atuação
- Restringir a informação perceptiva do agente
- Simplificar a descrição do conhecimento para adequá-la à aplicação
- Utilizar definições precisas

Um formalismo matemático para expressar e manipular conhecimento declarativo de forma tratável e computacionalmente eficiente deve ter:
- Linguagem de representação de conhecimento
- Um mecanismo de inferência
- Estratégias de controle da inferência

## Formas de representação de conhecimento para conhecimento lógico declarativo:
### Base para o prolog 
[[03-KR.pdf#page=20&selection=0,0,0,6&color=important|03-KR, p.20]]
- Conjunto de fórmulas que podem assumir valores verdadeiro ou falso "Hipótese do terceiro excluído"
- Conjunto de regras de inferência
### Redes semânticas (Ontologias)
[[03-KR.pdf#page=27&selection=0,0,0,16&color=yellow|03-KR, p.27]]
Usa nodos e arcos para representar a informação e sua correlação:
- nodos: representam objetos e conceitos 
- arcos: representam relações binárias entre objetos
Define um caminho como sequência de 1 ou mais arcos e as conclusões são baseadas nos caminhos.
Conhecimento é procedural
### Quadros (Frames)
Precursor das linguagens orientadas a objeto
Conhecimento é procedural

# Sistemas de Produção e Sistemas Especialistas
[[04-se_pos.pdf]]

Sempre posso usar um mecanismo de prova de teoremas para montar um motor de inferência lógica do framework de um sistema especialista.

## Sistemas de produção
Sistemas de produção são os `Sistemas de Post` 
É um método de processamento de dados
[No que ele consiste?](04-se_pos.pdf#page=3&selection=2,0,2,11&color=yellow|04-se_pos, p.3)
- Conjunto de regras de produção
- Memória de trabalho
- Interpretador - escolhe qual regra aplicar
## Arquitetura de um sistema especialista
> [!PDF|yellow] [[04-se_pos.pdf#page=12&selection=2,0,2,38&color=yellow|04-se_pos, p.12]]
> > Arquitetura de um Sistema Especialista

## Ciclo do Motor de Inferência
### Estratégia para resolução de conflitos
> [!PDF|yellow] [[04-se_pos.pdf#page=12&selection=2,0,2,38&color=yellow|04-se_pos, p.12]]
> > Arquitetura de um Sistema Especialista

### Ação: modos de raciocínio
- [Raciocínio guiado por objetivos (encadeamento para trás)](04-se_pos.pdf#page=18&selection=4,0,5,11&color=yellow|04-se_pos, p.18 )
- [Raciocínio guiado por dados (encadeamento para frente) (*modus ponens*)](04-se_pos.pdf#page=18&selection=12,0,13,12&color=yellow|04-se_pos, p.18)

## Aplicações de Sistemas Especialistas
[[04-se_pos.pdf#page=24&selection=0,0,0,10&color=yellow|04-se_pos, p.24]]
## Arcabouço
[[04-se_pos.pdf#page=32&selection=0,0,0,15&color=yellow|04-se_pos, p.32]]