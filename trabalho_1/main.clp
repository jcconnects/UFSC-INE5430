;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; main.clp - Sistema Especialista (Variedades de Café)
;; - abordagem: frames via deftemplate + regras para inferência
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Templates (frames)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(deftemplate variety
  "Fatos de entrada: uma variedade de café (somente nome)"
  (slot name))

(deftemplate recommendation
  "Recomendação inferida: torra, moagem, métodos e harmonizações"
  (slot name)
  (slot torra)
  (slot moagem)
  (multislot metodo)
  (multislot harmonizacao))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Fatos iniciais: variedades 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(deffacts variedades-iniciais
  "Variedades listadas na tabela."
  (variety (name Robusta))
  (variety (name Conilon))
  (variety (name Arabica))
  (variety (name Bourbon))
  (variety (name Catuaí))
  (variety (name MundoNovo))
  (variety (name Caturra))
  (variety (name Acaia))
  (variety (name Typica))
  (variety (name Geisha))
  (variety (name Maragogipe))
  (variety (name Pacamara))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Regras para gerar recomendações primárias (torra, moagem, método)
;; Cada regra insere um fato (recommendation ...) para a variedade,
;; caso ainda não exista.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule rec-robusta
  (variety (name Robusta))
  (not (recommendation (name Robusta)))
  =>
  (assert (recommendation
            (name Robusta)
            (torra "Média a Escura")
            (moagem "Fina a média")
            (metodo "Pressão" "Comercial")
            (harmonizacao) )))

(defrule rec-conilon
  (variety (name Conilon))
  (not (recommendation (name Conilon)))
  =>
  (assert (recommendation
            (name Conilon)
            (torra "Média a Escura")
            (moagem "Fina a média")
            (metodo "Comercial" "Pressão")
            (harmonizacao) )))

(defrule rec-arabica
  (variety (name Arabica))
  (not (recommendation (name Arabica)))
  =>
  (assert (recommendation
            (name Arabica)
            (torra "Clara a média")
            (moagem "Média a fina")
            (metodo "Filtragem" "Pressão")
            (harmonizacao) )))

(defrule rec-bourbon
  (variety (name Bourbon))
  (not (recommendation (name Bourbon)))
  =>
  (assert (recommendation
            (name Bourbon)
            (torra "Clara a média")
            (moagem "Média a fina")
            (metodo "Filtragem" "Imersão")
            (harmonizacao) )))

(defrule rec-catuai
  (variety (name Catuaí))
  (not (recommendation (name Catuaí)))
  =>
  (assert (recommendation
            (name Catuaí)
            (torra "Média")
            (moagem "Média")
            (metodo "Imersão" "Comercial")
            (harmonizacao) )))

(defrule rec-mundonovo
  (variety (name MundoNovo))
  (not (recommendation (name MundoNovo)))
  =>
  (assert (recommendation
            (name MundoNovo)
            (torra "Média a Média Escura")
            (moagem "Média a Média-Grosseira")
            (metodo "Imersão" "Filtragem" "Comercial")
            (harmonizacao) )))

(defrule rec-caturra
  (variety (name Caturra))
  (not (recommendation (name Caturra)))
  =>
  (assert (recommendation
            (name Caturra)
            (torra "Clara a média")
            (moagem "Média")
            (metodo "Pressão" "Filtragem")
            (harmonizacao) )))

(defrule rec-acaia
  (variety (name Acaia))
  (not (recommendation (name Acaia)))
  =>
  (assert (recommendation
            (name Acaia)
            (torra "Clara a Média")
            (moagem "Média a Fina")
            (metodo "Filtragem" "Imersão")
            (harmonizacao) )))

(defrule rec-typica
  (variety (name Typica))
  (not (recommendation (name Typica)))
  =>
  (assert (recommendation
            (name Typica)
            (torra "Clara")
            (moagem "Média a fina")
            (metodo "Imersão")
            (harmonizacao) )))

(defrule rec-geisha
  (variety (name Geisha))
  (not (recommendation (name Geisha)))
  =>
  (assert (recommendation
            (name Geisha)
            (torra "Clara")
            (moagem "Média a fina")
            (metodo "Filtragem")
            (harmonizacao) )))

(defrule rec-maragogipe
  (variety (name Maragogipe))
  (not (recommendation (name Maragogipe)))
  =>
  (assert (recommendation
            (name Maragogipe)
            (torra "Clara a Média")
            (moagem "Média")
            (metodo "Filtragem")
            (harmonizacao) )))

(defrule rec-pacamara
  (variety (name Pacamara))
  (not (recommendation (name Pacamara)))
  =>
  (assert (recommendation
            (name Pacamara)
            (torra "Clara a Média")
            (moagem "Média a fina")
            (metodo "Pressão" "Filtragem")
            (harmonizacao) )))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Regras de harmonização (comidas) baseadas em torra, moagem e método
;; — adicionam itens à lista 'harmonizacao' (multislot) evitando duplicações
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Torra -> Pães integrais
(defrule harm-torra-clara
  ?r <- (recommendation (name ?n) (torra ?t&:(or (eq ?t "Clara") (eq ?t "Clara a média"))) (harmonizacao $?h))
  (test (not (member$ "Pães integrais de fermentação natural" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Pães integrais de fermentação natural")))

(defrule harm-torra-media
  ?r <- (recommendation (name ?n) (torra "Média") (harmonizacao $?h))
  (test (not (member$ "Pães integrais com castanhas e frutas secas" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Pães integrais com castanhas e frutas secas")))

(defrule harm-torra-media-escura
  ?r <- (recommendation (name ?n) (torra ?t&:(or (eq ?t "Média a Escura") (eq ?t "Média a Média Escura"))) (harmonizacao $?h))
  (test (not (member$ "Pães integrais com sementes" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Pães integrais com sementes")))

;; Moagem -> Queijos semicurados
(defrule harm-moagem-fina-media
  ?r <- (recommendation (name ?n) (moagem "Fina a média") (harmonizacao $?h))
  (test (not (member$ "Queijo semicurado parmesão jovem" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Queijo semicurado parmesão jovem")))

(defrule harm-moagem-media-fina
  ?r <- (recommendation (name ?n) (moagem "Média a fina") (harmonizacao $?h))
  (test (not (member$ "Queijo semicurado gouda" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Queijo semicurado gouda")))

(defrule harm-moagem-media
  ?r <- (recommendation (name ?n) (moagem "Média") (harmonizacao $?h))
  (test (not (member$ "Queijo semicurado canastra meia cura" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Queijo semicurado canastra meia cura")))

(defrule harm-moagem-media-media-grosseira
  ?r <- (recommendation (name ?n) (moagem "Média a Média-Grosseira") (harmonizacao $?h))
  (test (not (member$ "Queijo semicurado gouda" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Queijo semicurado gouda")))

;; Método -> Bolos cítricos
(defrule harm-metodo-pressao
  ?r <- (recommendation (name ?n) (metodo $?m) (harmonizacao $?h))
  (test (member$ "Pressão" $?m))
  (test (not (member$ "Bolo cítrico de limão" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Bolo cítrico de limão")))

(defrule harm-metodo-filtragem
  ?r <- (recommendation (name ?n) (metodo $?m) (harmonizacao $?h))
  (test (member$ "Filtragem" $?m))
  (test (not (member$ "Bolo cítrico de laranja com calda" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Bolo cítrico de laranja com calda")))

(defrule harm-metodo-imersao
  ?r <- (recommendation (name ?n) (metodo $?m) (harmonizacao $?h))
  (test (member$ "Imersão" $?m))
  (test (not (member$ "Bolo cítrico de tangerina com cobertura leve" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Bolo cítrico de tangerina com cobertura leve")))

(defrule harm-metodo-comercial
  ?r <- (recommendation (name ?n) (metodo $?m) (harmonizacao $?h))
  (test (member$ "Comercial" $?m))
  (test (not (member$ "Bolo cítrico de limão" $?h)))
  =>
  (modify ?r (harmonizacao $?h "Bolo cítrico de limão")))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Regra utilitária para imprimir recomendações após inferência
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule imprimir-recommendations
  (declare (salience -10)) ;; roda ao final
  ?r <- (recommendation (name ?n) (torra ?t) (moagem ?mo) (metodo $?mt) (harmonizacao $?hz))
  =>
  (printout t "=== Recomendação para: " ?n crlf)
  (printout t "  Torra: " ?t crlf)
  (printout t "  Moagem: " ?mo crlf)
  (printout t "  Métodos: " ?mt crlf)
  (printout t "  Harmonizações: " ?hz crlf crlf)
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Exemplo de casos de teste (podemos considerar estes como "casos")
;; Execute: (load "main.clp") (reset) (run)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
