# 001 - Introdução

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
# 002 - Exemplo
Técnicas de IA são gerais e dissociadas ao conhecimento que leva à solução do problema. Precisa ter essa característica de estar desacoplada do problema em si.

A cada jogada, cada step, de tomada de decisão, é necessário criar uma nova árvore de decisão. No exemplo do jogo Tic Tac Toe uma árvore é criada a cada jogada.

Para diminuir o processamento nas árvores, **podemos utilizar cortes alpha e beta**. 
![[Anotações de aula - Exemplo de cortes min e max.png]]

# 003 - Knowledge Representation
> [!PDF|yellow] [[003-KR.pdf#page=2&selection=17,0,18,65&color=yellow|003-KR, p.2]]
> > Representação de Conhecimento e Raciocínio é a parte da IA que diz respeito a como um agente usa o que sabe para decidir o que fazer

"Não reinventamos nada na IA"

---
## Definição de conhecimento para a área da IA
> [!PDF|yellow] [[003-KR.pdf#page=2&selection=17,0,18,65&color=yellow|003-KR, p.2]]
> > Representação de Conhecimento e Raciocínio é a parte da IA que diz respeito a como um agente usa o que sabe para decidir o que fazer

## Definição de representação
> [!PDF|yellow] [[003-KR.pdf#page=5&selection=2,0,2,67&color=yellow|003-KR, p.5]]
> > relação entre dois domínios: o real e o da representação (símbolos)

Existem alguns métodos de representação diferentes:
[[003-KR.pdf#page=6&selection=5,0,6,64&color=yellow|003-KR, p.6]]
## Definição de raciocínio
> [!PDF|yellow] [[003-KR.pdf#page=6&selection=5,0,6,64&color=yellow|003-KR, p.6]]
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
[[003-KR.pdf#page=20&selection=0,0,0,6&color=important|003-KR, p.20]]
- Conjunto de fórmulas que podem assumir valores verdadeiro ou falso "Hipótese do terceiro excluído"
- Conjunto de regras de inferência
### Redes semânticas (Ontologias)
[[003-KR.pdf#page=27&selection=0,0,0,16&color=yellow|003-KR, p.27]]
Usa nodos e arcos para representar a informação e sua correlação:
- nodos: representam objetos e conceitos 
- arcos: representam relações binárias entre objetos
Define um caminho como sequência de 1 ou mais arcos e as conclusões são baseadas nos caminhos.
Conhecimento é procedural
### Quadros (Frames)
Precursor das linguagens orientadas a objeto
Conhecimento é procedural

# 004 - Sistemas de Produção e Sistemas Especialistas
[[004-se_pos.pdf]]

Sempre posso usar um mecanismo de prova de teoremas para montar um motor de inferência lógica do framework de um sistema especialista.

## Sistemas de produção
Sistemas de produção são os `Sistemas de Post` 
É um método de processamento de dados
[No que ele consiste?](004-se_pos.pdf#page=3&selection=2,0,2,11&color=yellow|004-se_pos, p.3)
- Conjunto de regras de produção
- Memória de trabalho
- Interpretador - escolhe qual regra aplicar
## Arquitetura de um sistema especialista
> [!PDF|yellow] [[004-se_pos.pdf#page=12&selection=2,0,2,38&color=yellow|004-se_pos, p.12]]
> > Arquitetura de um Sistema Especialista

## Ciclo do Motor de Inferência
### Estratégia para resolução de conflitos
> [!PDF|yellow] [[004-se_pos.pdf#page=12&selection=2,0,2,38&color=yellow|004-se_pos, p.12]]
> > Arquitetura de um Sistema Especialista

### Ação: modos de raciocínio
- [Raciocínio guiado por objetivos (encadeamento para trás)](004-se_pos.pdf#page=18&selection=4,0,5,11&color=yellow|004-se_pos, p.18 )
- [Raciocínio guiado por dados (encadeamento para frente) (*modus ponens*)](004-se_pos.pdf#page=18&selection=12,0,13,12&color=yellow|004-se_pos, p.18)

## Aplicações de Sistemas Especialistas
[[004-se_pos.pdf#page=24&selection=0,0,0,10&color=yellow|004-se_pos, p.24]]
## Arcabouço
[[004-se_pos.pdf#page=32&selection=0,0,0,15&color=yellow|004-se_pos, p.32]]

# 005 - Lógica RC
[[005-LogicaRC.pdf]]

## [Sintaxe](005-LogicaRC.pdf#page=3&selection=0,0,0,7&color=yellow|005-LogicaRC, p.3)
Constante -> Início do alfabeto
Variável -> Final do alfabeto
Função -> Meio do alfabeto
Predicado -> Maiúsculas
![[005-LogicaRC.pdf#page=5&rect=104,18,237,303&color=yellow|005-LogicaRC, p.5]]
## [Semântica](005-LogicaRC.pdf#page=6&selection=0,0,0,9&color=yellow|005-LogicaRC, p.6)
![[005-LogicaRC.pdf#page=6&rect=349,66,557,702&color=yellow|005-LogicaRC, p.6]]

## [Representação de Conhecimento em Lógica](005-LogicaRC.pdf#page=14&selection=0,0,0,12&color=yellow|005-LogicaRC, p.14)
Como podemos inferir algo, baseado em uma determinada premissa?
### [Raciocínio em Lógica](005-LogicaRC.pdf#page=17&selection=0,0,0,20&color=yellow|005-LogicaRC, p.17)
Dado um conjunto de fatos e regras, podemos inferir novos conhecimentos que sejam verdadeiros.

Precisamos de um método para aplicar a prova automática. Os que vamos estudar são os seguintes:
- Método da Resolução
- Método de Tableaux

## Formas normais
[[005-LogicaRC.pdf#page=22&selection=0,0,0,24&color=yellow|005-LogicaRC, p.22]]
[[005-LogicaRC.pdf#page=22&selection=2,0,2,42&color=yellow|Forma normal conjuntiva (ou forma clausal)]]
[[005-LogicaRC.pdf#page=23&selection=2,0,2,47&color=yellow|Forma normal disjuntiva (ou forma clausal dual)]]

### Algoritmo FNC
[[005-LogicaRC.pdf#page=25&selection=0,0,0,13&color=yellow|Algoritmo FNC]]
## [Método da Resolução](005-LogicaRC.pdf#page=32&selection=0,0,0,19&color=yellow|Método da Resolução)
1. Coloco na CNF
2. 

### Algoritmo de Unificação
[[005-LogicaRC.pdf#page=33&selection=0,0,0,22&color=yellow|Algoritmo de Unificação]]


# 006 - Busca
[[006-busca.pdf]]

Exploration vs Exploitation

## Busca em Largura
## Busca em Profundidade
## Busca Bidirecional
## Busca heurística
[[006-busca.pdf#page=22&selection=0,0,0,16&color=yellow|006-busca, p.22]]

Algoritmo A* assegura a melhor solução, tendo em vista a admissibilidade da heurística.
## Subida de Encosta
[[006-busca.pdf#page=28&selection=0,0,0,17&color=yellow|006-busca, p.28]]

## Subida de Encosta pela Trilha mais Íngreme
[[006-busca.pdf#page=32&selection=0,10,0,37&color=yellow|006-busca, p.32]]

## Têmpera Simulada
[[006-busca.pdf#page=34&selection=0,0,0,16&color=yellow|006-busca, p.34]]

# 007 - Jogos

# 008 - Agent Oriented Programming with Jason
[[008-aop.pdf]]
## Definição de sistemas multiagentes
[[008-aop.pdf#page=3&selection=6,0,7,20&color=yellow|008-aop, p.3]]
Existe uma estrutura de organização entre os agentes autônomos, na qual cada um tem uma função e eles se complementam.

![[008-aop.pdf#page=9&rect=5,5,342,267&color=yellow|008-aop, p.4]]
### Agentes
- software/hardware
- coarse-grain/small-grain
- heterogeneous/homogeneous
- reactive/pro-active entities
### Ambiente
- virtual/physical
- passive/active
- deterministic/non deterministic
- ...
### Interação
É o motor da dinâmica dos sistemas multiagentes
- direct/indirect between agents
- interaction between agent and environment
### Organização
 - pre-defined/emergent
 - static/adaptive
 - open/closed (relacionada a entrada e saída de agentes)
 - ...
## Abstração em sistemas multiagentes
### Individual level 
- autonomy, situatedness
- beliefs, desires, goals, intentions, plans 
- sense/reason/act, reactive/pro-active behaviour 
### Environment level 
- resources and services that agents can access and control 
- sense/act 
### Social level 
- cooperation, competition, parasite, symbiosys, comensalism
- languages
- protocols 
### Organisation level 
- coordination, regulation patterns, norms, obligations, rights
## Agentes Jason
[[008-agentes_jason.pdf]]
![[008-agentes_jason.pdf#page=6&rect=4,56,360,255&color=yellow|09-agentes_jason, p.6]]
## Arquitetura BDI
  ![[008-aop.pdf#page=17&rect=6,62,331,266&color=yellow|008-aop, p.12]]


