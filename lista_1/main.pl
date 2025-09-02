%% Base de Conhecimento sobre Variedades de Café
%% Autor: André Thiago Pfleger, Gustavo Girotto, João Pedro Schmidt Cordeiro
%% Data: 24/07/2024
%%
%% Este arquivo contém fatos e regras em Prolog para representar o conhecimento
%% sobre diferentes variedades de café, suas características e métodos de preparo,
%% com base no texto de referência.

% --- Fatos ---

% -- Relações hierárquicas e de origem --
familia(robusta, canephora).
familia(arabica, arabica).
variante(conilon, canephora).
subgrupo(bourbon, arabica).
mutacao(caturra, bourbon).
mutacao(acaia, mundo_novo).
mutacao(maragogipe, typica).
cruzamento(mundo_novo, typica, bourbon).
hibrido(pacamara, pacas, maragogipe).

% -- Variedades de Café --
variedade(robusta).
variedade(conilon).
variedade(arabica).
variedade(bourbon).
variedade(catuai).
variedade(mundo_novo).
variedade(caturra).
variedade(acaia).
variedade(typica).
variedade(geisha).
variedade(maragogipe).
variedade(pacamara).

% -- Descrição de cada variedade --
descricao(robusta, 'Sabor acentuado e rústico, corpo pesado, maior resistência a doenças e teor de cafeína elevado; frequentemente utilizado em blends e produtos solúveis.').
descricao(conilon, 'Variante de canephora muito explorada no Brasil; grãos tipicamente menores, amargor pronunciado e alto teor de cafeína; uso comum em commodity e blends.').
descricao(arabica, 'A variedade mais consumida globalmente; perfis sensoriais complexos com acidez, doçura e notas frutadas/ florais, fortemente dependentes de terroir e altitude.').
descricao(bourbon, 'Subgrupo de Arábica com doçura pronunciada e aroma intenso; bebida tipicamente suave.').
descricao(catuai, 'Cultivar brasileira resultante de cruzamentos; planta compacta, produtividade e doçura natural; amplamente plantado.').
descricao(mundo_novo, 'Cruzamento natural (Typica × Bourbon); vigoroso, produtivo; tende a oferecer corpo mais pronunciado e doçura.').
descricao(caturra, 'Mutação do Bourbon com planta de porte compacto; boa produtividade inicial; produz cafés de boa qualidade e doçura.').
descricao(acaia, 'Mutação do Mundo Novo; variedade rara, com bom desempenho em altitudes acima de 800m; xícara com notas frutadas e lembranças de chocolate.').
descricao(typica, 'Variedade histórica e clássica; perfil doce e floral/complexo; menor produtividade e maior sensibilidade a pragas.').
descricao(geisha, 'Variedade muito expressiva aromaticamente (jasmim, flores, frutas de caroço); extremamente valorizada no mercado specialty.').
descricao(maragogipe, 'Mutação de Typica com sementes excepcionalmente grandes ("grão-elefante"); perfil muitas vezes suave e frutado; baixa produtividade.').
descricao(pacamara, 'Híbrido que produz grãos grandes e perfil complexo (floral, frutado e corpo médio).').

% -- Torra Recomendada --
torra_recomendada(robusta, media_a_escura).
torra_recomendada(conilon, media_a_escura).
torra_recomendada(arabica, clara_a_media).
torra_recomendada(bourbon, clara_a_media).
torra_recomendada(catuai, media).
torra_recomendada(mundo_novo, media_a_media_escura).
torra_recomendada(caturra, clara_a_media).
torra_recomendada(acaia, clara_a_media).
torra_recomendada(typica, clara).
torra_recomendada(geisha, clara).
torra_recomendada(maragogipe, clara_a_media).
torra_recomendada(pacamara, clara_a_media).

% -- Moagem Sugerida --
moagem_sugerida(robusta, fina_a_media).
moagem_sugerida(conilon, fina_a_media).
moagem_sugerida(arabica, media_a_fina).
moagem_sugerida(bourbon, media_a_fina).
moagem_sugerida(catuai, media).
moagem_sugerida(mundo_novo, media_a_media_grosseira).
moagem_sugerida(caturra, media).
moagem_sugerida(acaia, media_fina_a_media).
moagem_sugerida(typica, media_fina).
moagem_sugerida(geisha, media_fina_a_media).
moagem_sugerida(maragogipe, media).
moagem_sugerida(pacamara, media_fina_a_media).

% -- Métodos de Preparo Indicados --
metodo_preparo(robusta, espresso).
metodo_preparo(robusta, moka).
metodo_preparo(robusta, blends_industriais).
metodo_preparo(robusta, cafes_instantaneos).
metodo_preparo(conilon, espresso).
metodo_preparo(conilon, blends).
metodo_preparo(conilon, soluvel).
metodo_preparo(arabica, pour_over).
metodo_preparo(arabica, chemex).
metodo_preparo(arabica, aeropress).
metodo_preparo(arabica, filtros).
metodo_preparo(arabica, espresso_specialty).
metodo_preparo(bourbon, pour_over).
metodo_preparo(bourbon, chemex).
metodo_preparo(bourbon, aeropress).
metodo_preparo(bourbon, prensa_francesa).
metodo_preparo(catuai, pour_over).
metodo_preparo(catuai, coador).
metodo_preparo(catuai, blends).
metodo_preparo(catuai, prensa_francesa).
metodo_preparo(mundo_novo, pour_over).
metodo_preparo(mundo_novo, prensa_francesa).
metodo_preparo(mundo_novo, blends).
metodo_preparo(caturra, filtrados).
metodo_preparo(caturra, chemex).
metodo_preparo(caturra, aeropress).
metodo_preparo(caturra, single_origin).
metodo_preparo(acaia, pour_over).
metodo_preparo(acaia, aeropress).
metodo_preparo(acaia, cupping).
metodo_preparo(typica, pour_over).
metodo_preparo(typica, cupping).
metodo_preparo(geisha, pour_over).
metodo_preparo(geisha, kalita_wave).
metodo_preparo(maragogipe, filtrados_especiais).
metodo_preparo(maragogipe, single_origin).
metodo_preparo(pacamara, pour_over).
metodo_preparo(pacamara, aeropress).
metodo_preparo(pacamara, extracoes_experimentais).

% -- Fatos sobre moagem por método --
moagem_por_metodo(espresso, fina).
moagem_por_metodo(aeropress, media_fina).
moagem_por_metodo(pour_over, media_fina).
moagem_por_metodo(chemex, media_grosseira).
moagem_por_metodo(prensa_francesa, grossa).
moagem_por_metodo(cold_brew, extra_grossa).


% --- Regras ---

% Regra para recomendar uma variedade com base no método de preparo desejado.
% Exemplo de consulta: recomenda_por_metodo(espresso, Variedade).
recomenda_por_metodo(Metodo, Variedade) :-
    metodo_preparo(Variedade, Metodo).

% Regra para encontrar variedades que são adequadas para uma determinada torra.
% Exemplo de consulta: recomenda_por_torra(clara, Variedade).
recomenda_por_torra(Torra, Variedade) :-
    torra_recomendada(Variedade, Torra).

% Regra para encontrar variedades que são adequadas para uma determinada moagem.
% Exemplo de consulta: recomenda_por_moagem(media, Variedade).
recomenda_por_moagem(Moagem, Variedade) :-
    moagem_sugerida(Variedade, Moagem).

% Regra para verificar se uma variedade pertence à família Arábica (diretamente ou por herança).
% Exemplo de consulta: e_arabica(bourbon).
e_arabica(Variedade) :- subgrupo(Variedade, arabica).
e_arabica(Variedade) :- mutacao(Variedade, Parente), e_arabica(Parente).
e_arabica(Variedade) :- cruzamento(Variedade, P1, P2), (e_arabica(P1) ; e_arabica(P2)).
e_arabica(arabica).

% Regra para listar todas as informações sobre uma variedade.
% Exemplo de consulta: info_variedade(robusta).
info_variedade(Variedade) :-
    variedade(Variedade),
    write('--- Informações sobre a variedade: '), writeln(Variedade),
    descricao(Variedade, Desc), write('Descrição: '), writeln(Desc),
    torra_recomendada(Variedade, Torra), write('Torra Recomendada: '), writeln(Torra),
    moagem_sugerida(Variedade, Moagem), write('Moagem Sugerida: '), writeln(Moagem),
    findall(Metodo, metodo_preparo(Variedade, Metodo), Metodos),
    write('Métodos de Preparo: '), writeln(Metodos).

% Regra para recomendar uma combinação completa (variedade, torra, moagem) para um método.
% Exemplo de consulta: recomendacao_completa(pour_over, Variedade, Torra, Moagem).
recomendacao_completa(Metodo, Variedade, Torra, Moagem) :-
    recomenda_por_metodo(Metodo, Variedade),
    torra_recomendada(Variedade, Torra),
    moagem_sugerida(Variedade, Moagem).

% Fim da base de conhecimento.
