# Trabalho Prático - Gato vs Não-Gato

Reconhecimento de padrões é o processo de treinamento de uma rede neural para atribuir uma classe correta para um conjunto de padrões de entrada. Uma vez treinada, a rede pode ser usada para classificar padrões que não tenha visto antes.

Neste trabalho, um conjunto de dados deve ser usado para treinar e testar uma rede neural, que classifica  imagens em "gatos" e "não gatos".

Os dados para treinamento, validação e teste foram obtidos a partir de uma base fornecida no curso de deep learning do Andrew Ng.

Os parâmetros de entrada para a rede são imagens rgb colocados em uma matriz de 64x64x3 (4096 pixeis coloridos).

E a saída é o valor correto da classificação , sendo que o dígito 0 corresponde a "Não Gato" e 1 corresponde a "Gato".

Este exercício pode ser feito em qualquer linguagem/ambiente.

- Nosso grupo decidiu fazer em Python

Você deve resolver o problema com um perceptron apenas (regressão logistica), uma rede de camada rasa e uma rede convolucional. Além da demonstração das redes funcionando, um Relatório COMPLETO deve ser entregue, contendo informações  de Quantos e Quais experimentos foram feitos até chegar no resultado final; Como foi o treinamento (taxa de aprendizado, arquitetura de rede, uso de regularização, etc.); Qual a taxa de acertos da rede; A matriz de confusão, etc...
