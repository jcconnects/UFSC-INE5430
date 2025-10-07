"""
Cálculos de Probabilidades para Redes Bayesianas
Trabalho 3 - Raciocínio Probabilístico
INE5430 - Inteligência Artificial - UFSC
"""

import itertools

# ================================================
# PARTE 1: Detecção de Fraude em Cartão de Crédito
# ================================================

# Probabilidades marginais
P_F = {
    'sim': 0.001,
    'nao': 0.999
}

P_I = {
    '<30': 0.25,
    '30-50': 0.40,
    '>50': 0.35
}

P_S = {
    'masc': 0.50,
    'fem': 0.50
}

# P(G|F) - Probabilidade de compra de gasolina dado fraude
P_G_dado_F = {
    ('sim', 'sim'): 0.20,
    ('nao', 'sim'): 0.80,
    ('sim', 'nao'): 0.01,
    ('nao', 'nao'): 0.99
}

# P(C|F,I,S) - Probabilidade de compra de crédito celular dado F, I, S
P_C_dado_FIS = {
    # F=sim
    ('sim', 'sim', '<30', 'masc'): 0.95,
    ('nao', 'sim', '<30', 'masc'): 0.05,
    ('sim', 'sim', '<30', 'fem'): 0.95,
    ('nao', 'sim', '<30', 'fem'): 0.05,
    ('sim', 'sim', '30-50', 'masc'): 0.95,
    ('nao', 'sim', '30-50', 'masc'): 0.05,
    ('sim', 'sim', '30-50', 'fem'): 0.95,
    ('nao', 'sim', '30-50', 'fem'): 0.05,
    ('sim', 'sim', '>50', 'masc'): 0.95,
    ('nao', 'sim', '>50', 'masc'): 0.05,
    ('sim', 'sim', '>50', 'fem'): 0.95,
    ('nao', 'sim', '>50', 'fem'): 0.05,
    # F=nao
    ('sim', 'nao', '<30', 'masc'): 0.80,
    ('nao', 'nao', '<30', 'masc'): 0.20,
    ('sim', 'nao', '<30', 'fem'): 0.75,
    ('nao', 'nao', '<30', 'fem'): 0.25,
    ('sim', 'nao', '30-50', 'masc'): 0.75,
    ('nao', 'nao', '30-50', 'masc'): 0.25,
    ('sim', 'nao', '30-50', 'fem'): 0.75,
    ('nao', 'nao', '30-50', 'fem'): 0.25,
    ('sim', 'nao', '>50', 'masc'): 0.50,
    ('nao', 'nao', '>50', 'masc'): 0.50,
    ('sim', 'nao', '>50', 'fem'): 0.60,
    ('nao', 'nao', '>50', 'fem'): 0.40
}


def questao_3():
    """
    Questão 3: Calcular P(G=sim)
    Marginalizando sobre F, I, S
    """
    print("=" * 70)
    print("QUESTÃO 3: P(G=sim)")
    print("=" * 70)
    
    p_g_sim = 0.0
    
    print("\nCálculo por enumeração:")
    print("P(G=sim) = Σ_F,I,S P(G=sim|F) × P(F) × P(I) × P(S)")
    print()
    
    for f in ['sim', 'nao']:
        for i in ['<30', '30-50', '>50']:
            for s in ['masc', 'fem']:
                prob = P_G_dado_F[('sim', f)] * P_F[f] * P_I[i] * P_S[s]
                p_g_sim += prob
                print(f"  F={f:3s}, I={i:5s}, S={s:4s}: "
                      f"{P_G_dado_F[('sim', f)]:.3f} × {P_F[f]:.3f} × "
                      f"{P_I[i]:.2f} × {P_S[s]:.2f} = {prob:.8f}")
    
    print(f"\nP(G=sim) = {p_g_sim:.8f} = {p_g_sim*100:.6f}%")
    print()
    return p_g_sim


def questao_4():
    """
    Questão 4: Calcular P(C=sim)
    Marginalizando sobre F, I, S
    """
    print("=" * 70)
    print("QUESTÃO 4: P(C=sim)")
    print("=" * 70)
    
    p_c_sim = 0.0
    
    print("\nCálculo por enumeração:")
    print("P(C=sim) = Σ_F,I,S P(C=sim|F,I,S) × P(F) × P(I) × P(S)")
    print()
    
    for f in ['sim', 'nao']:
        for i in ['<30', '30-50', '>50']:
            for s in ['masc', 'fem']:
                prob = P_C_dado_FIS[('sim', f, i, s)] * P_F[f] * P_I[i] * P_S[s]
                p_c_sim += prob
                print(f"  F={f:3s}, I={i:5s}, S={s:4s}: "
                      f"{P_C_dado_FIS[('sim', f, i, s)]:.2f} × {P_F[f]:.3f} × "
                      f"{P_I[i]:.2f} × {P_S[s]:.2f} = {prob:.8f}")
    
    print(f"\nP(C=sim) = {p_c_sim:.8f} = {p_c_sim*100:.6f}%")
    print()
    return p_c_sim


def questao_5():
    """
    Questão 5: Calcular P(C=sim | G=sim)
    """
    print("=" * 70)
    print("QUESTÃO 5: P(C=sim | G=sim)")
    print("=" * 70)
    
    # Precisamos calcular P(C=sim, G=sim) e P(G=sim)
    # P(C=sim, G=sim) = Σ_F,I,S P(C=sim|F,I,S) × P(G=sim|F) × P(F) × P(I) × P(S)
    
    print("\nPasso 1: Calcular P(C=sim, G=sim)")
    print("P(C=sim, G=sim) = Σ_F,I,S P(C=sim|F,I,S) × P(G=sim|F) × P(F) × P(I) × P(S)")
    print("\nNote que C e G são condicionalmente independentes dado F:")
    print()
    
    p_c_sim_g_sim = 0.0
    
    for f in ['sim', 'nao']:
        for i in ['<30', '30-50', '>50']:
            for s in ['masc', 'fem']:
                prob = (P_C_dado_FIS[('sim', f, i, s)] * 
                       P_G_dado_F[('sim', f)] * 
                       P_F[f] * P_I[i] * P_S[s])
                p_c_sim_g_sim += prob
                print(f"  F={f:3s}, I={i:5s}, S={s:4s}: "
                      f"{P_C_dado_FIS[('sim', f, i, s)]:.2f} × "
                      f"{P_G_dado_F[('sim', f)]:.2f} × {P_F[f]:.3f} × "
                      f"{P_I[i]:.2f} × {P_S[s]:.2f} = {prob:.10f}")
    
    print(f"\nP(C=sim, G=sim) = {p_c_sim_g_sim:.10f}")
    
    # Calcular P(G=sim) (já calculado na questão 3)
    p_g_sim = 0.0
    for f in ['sim', 'nao']:
        for i in ['<30', '30-50', '>50']:
            for s in ['masc', 'fem']:
                p_g_sim += P_G_dado_F[('sim', f)] * P_F[f] * P_I[i] * P_S[s]
    
    print(f"\nPasso 2: Usar P(G=sim) calculado na Questão 3")
    print(f"P(G=sim) = {p_g_sim:.10f}")
    
    print(f"\nPasso 3: Aplicar a definição de probabilidade condicional")
    print(f"P(C=sim | G=sim) = P(C=sim, G=sim) / P(G=sim)")
    
    p_c_sim_dado_g_sim = p_c_sim_g_sim / p_g_sim
    
    print(f"P(C=sim | G=sim) = {p_c_sim_g_sim:.10f} / {p_g_sim:.10f}")
    print(f"P(C=sim | G=sim) = {p_c_sim_dado_g_sim:.8f} = {p_c_sim_dado_g_sim*100:.6f}%")
    print()
    return p_c_sim_dado_g_sim


def questao_6():
    """
    Questão 6: Calcular P(F=sim | C=sim, G=não)
    Usando Teorema de Bayes
    """
    print("=" * 70)
    print("QUESTÃO 6: P(F=sim | C=sim, G=não)")
    print("=" * 70)
    
    print("\nUsando o Teorema de Bayes:")
    print("P(F=sim | C=sim, G=não) = P(C=sim, G=não | F=sim) × P(F=sim) / P(C=sim, G=não)")
    
    # Calcular P(C=sim, G=não | F=sim)
    # Como C e G são condicionalmente independentes dado F:
    # P(C=sim, G=não | F=sim) = Σ_I,S P(C=sim|F=sim,I,S) × P(G=não|F=sim) × P(I) × P(S)
    
    print("\nPasso 1: Calcular P(C=sim, G=não | F=sim)")
    print("Como C e G são condicionalmente independentes dado F:")
    print("P(C=sim, G=não | F=sim) = Σ_I,S P(C=sim|F=sim,I,S) × P(G=não|F=sim) × P(I) × P(S)")
    print()
    
    p_cg_dado_f_sim = 0.0
    for i in ['<30', '30-50', '>50']:
        for s in ['masc', 'fem']:
            prob = (P_C_dado_FIS[('sim', 'sim', i, s)] * 
                   P_G_dado_F[('nao', 'sim')] * 
                   P_I[i] * P_S[s])
            p_cg_dado_f_sim += prob
            print(f"  I={i:5s}, S={s:4s}: "
                  f"{P_C_dado_FIS[('sim', 'sim', i, s)]:.2f} × "
                  f"{P_G_dado_F[('nao', 'sim')]:.2f} × "
                  f"{P_I[i]:.2f} × {P_S[s]:.2f} = {prob:.6f}")
    
    print(f"\nP(C=sim, G=não | F=sim) = {p_cg_dado_f_sim:.6f}")
    
    # Calcular P(C=sim, G=não | F=não)
    print("\nPasso 2: Calcular P(C=sim, G=não | F=não)")
    print("P(C=sim, G=não | F=não) = Σ_I,S P(C=sim|F=não,I,S) × P(G=não|F=não) × P(I) × P(S)")
    print()
    
    p_cg_dado_f_nao = 0.0
    for i in ['<30', '30-50', '>50']:
        for s in ['masc', 'fem']:
            prob = (P_C_dado_FIS[('sim', 'nao', i, s)] * 
                   P_G_dado_F[('nao', 'nao')] * 
                   P_I[i] * P_S[s])
            p_cg_dado_f_nao += prob
            print(f"  I={i:5s}, S={s:4s}: "
                  f"{P_C_dado_FIS[('sim', 'nao', i, s)]:.2f} × "
                  f"{P_G_dado_F[('nao', 'nao')]:.2f} × "
                  f"{P_I[i]:.2f} × {P_S[s]:.2f} = {prob:.6f}")
    
    print(f"\nP(C=sim, G=não | F=não) = {p_cg_dado_f_nao:.6f}")
    
    # Calcular o numerador
    numerador = p_cg_dado_f_sim * P_F['sim']
    print(f"\nPasso 3: Calcular o numerador")
    print(f"Numerador = P(C=sim, G=não | F=sim) × P(F=sim)")
    print(f"Numerador = {p_cg_dado_f_sim:.6f} × {P_F['sim']:.3f} = {numerador:.10f}")
    
    # Calcular o denominador
    denominador = (p_cg_dado_f_sim * P_F['sim'] + 
                  p_cg_dado_f_nao * P_F['nao'])
    print(f"\nPasso 4: Calcular o denominador")
    print(f"P(C=sim, G=não) = P(C=sim, G=não | F=sim)×P(F=sim) + P(C=sim, G=não | F=não)×P(F=não)")
    print(f"P(C=sim, G=não) = {p_cg_dado_f_sim:.6f}×{P_F['sim']:.3f} + {p_cg_dado_f_nao:.6f}×{P_F['nao']:.3f}")
    print(f"P(C=sim, G=não) = {numerador:.10f} + {p_cg_dado_f_nao * P_F['nao']:.10f}")
    print(f"P(C=sim, G=não) = {denominador:.10f}")
    
    # Calcular P(F=sim | C=sim, G=não)
    resultado = numerador / denominador
    
    print(f"\nPasso 5: Calcular a probabilidade final")
    print(f"P(F=sim | C=sim, G=não) = {numerador:.10f} / {denominador:.10f}")
    print(f"P(F=sim | C=sim, G=não) = {resultado:.10f} = {resultado*100:.8f}%")
    print()
    
    return resultado


# ================================================
# PARTE 2: Desonestidade Acadêmica
# ================================================

# Probabilidades para Parte 2 (baseado no enunciado)
P_N = {
    'Universitario': 0.1,
    'Secundario': 0.3,
    'Fundamental': 0.6
}

# P(C|N) - Cola dado Nível
P_Cola_dado_N = {
    ('Sim', 'Universitario'): 0.6,
    ('Nao', 'Universitario'): 0.4,
    ('Sim', 'Secundario'): 0.5,
    ('Nao', 'Secundario'): 0.5,
    ('Sim', 'Fundamental'): 0.2,
    ('Nao', 'Fundamental'): 0.8
}

# P(V|N) - Viu colega colar dado Nível
P_Viu_dado_N = {
    ('Sim', 'Universitario'): 0.7,
    ('Nao', 'Universitario'): 0.3,
    ('Sim', 'Secundario'): 0.5,
    ('Nao', 'Secundario'): 0.5,
    ('Sim', 'Fundamental'): 0.1,
    ('Nao', 'Fundamental'): 0.9
}

# P(E|N) - Estuda dado Nível
P_Estuda_dado_N = {
    ('Sim', 'Universitario'): 0.5,
    ('Nao', 'Universitario'): 0.5,
    ('Sim', 'Secundario'): 0.3,
    ('Nao', 'Secundario'): 0.7,
    ('Sim', 'Fundamental'): 0.2,
    ('Nao', 'Fundamental'): 0.8
}

# P(P|C,E) - Sente-se penalizado dado Cola e Estuda
P_Penalizado_dado_CE = {
    ('Sim', 'Sim', 'Sim'): 0.1,    # Cola=Sim, Estuda=Sim
    ('Nao', 'Sim', 'Sim'): 0.9,
    ('Sim', 'Sim', 'Nao'): 0.8,    # Cola=Sim, Estuda=Não
    ('Nao', 'Sim', 'Nao'): 0.2,
    ('Sim', 'Nao', 'Sim'): 0.9,    # Cola=Não, Estuda=Sim
    ('Nao', 'Nao', 'Sim'): 0.1,
    ('Sim', 'Nao', 'Nao'): 0.5,    # Cola=Não, Estuda=Não
    ('Nao', 'Nao', 'Nao'): 0.5
}


def parte2_questao_1():
    """
    PARTE 2 - Questão 1: Calcular P(Cola=Sim)
    """
    print("=" * 70)
    print("PARTE 2 - QUESTÃO 1: P(Cola=Sim)")
    print("=" * 70)
    
    print("\nCálculo por marginalização sobre Nível:")
    print("P(Cola=Sim) = Σ_n P(Cola=Sim | N=n) × P(N=n)")
    print()
    
    p_cola_sim = 0.0
    
    for n in ['Universitario', 'Secundario', 'Fundamental']:
        prob = P_Cola_dado_N[('Sim', n)] * P_N[n]
        p_cola_sim += prob
        print(f"  N={n:13s}: {P_Cola_dado_N[('Sim', n)]:.1f} × {P_N[n]:.1f} = {prob:.3f}")
    
    print(f"\nP(Cola=Sim) = {p_cola_sim:.3f} = {p_cola_sim*100:.1f}%")
    print()
    return p_cola_sim


def parte2_questao_2():
    """
    PARTE 2 - Questão 2: Calcular P(N=Secundário | V=Sim, P=Sim)
    """
    print("=" * 70)
    print("PARTE 2 - QUESTÃO 2: P(N=Secundário | V=Sim, P=Sim)")
    print("=" * 70)
    
    print("\nUsando o Teorema de Bayes:")
    print("P(N=Sec | V=Sim, P=Sim) = P(V=Sim, P=Sim | N=Sec) × P(N=Sec) / P(V=Sim, P=Sim)")
    
    # Para cada nível, calcular P(V=Sim, P=Sim | N)
    print("\nPasso 1: Calcular P(V=Sim, P=Sim | N) para cada nível")
    print("P(V=Sim, P=Sim | N) = Σ_C,E P(V=Sim|N) × P(P=Sim|C,E) × P(C|N) × P(E|N)")
    print()
    
    p_vp_dado_n = {}
    
    for n in ['Universitario', 'Secundario', 'Fundamental']:
        print(f"\nPara N={n}:")
        prob_total = 0.0
        
        for c in ['Sim', 'Nao']:
            for e in ['Sim', 'Nao']:
                prob = (P_Viu_dado_N[('Sim', n)] * 
                       P_Penalizado_dado_CE[('Sim', c, e)] * 
                       P_Cola_dado_N[(c, n)] * 
                       P_Estuda_dado_N[(e, n)])
                prob_total += prob
                print(f"  C={c:3s}, E={e:3s}: "
                      f"{P_Viu_dado_N[('Sim', n)]:.1f} × "
                      f"{P_Penalizado_dado_CE[('Sim', c, e)]:.1f} × "
                      f"{P_Cola_dado_N[(c, n)]:.1f} × "
                      f"{P_Estuda_dado_N[(e, n)]:.1f} = {prob:.4f}")
        
        p_vp_dado_n[n] = prob_total
        print(f"  P(V=Sim, P=Sim | N={n}) = {prob_total:.4f}")
    
    # Calcular o numerador para N=Secundário
    print(f"\nPasso 2: Calcular numerador para N=Secundário")
    numerador = p_vp_dado_n['Secundario'] * P_N['Secundario']
    print(f"Numerador = P(V=Sim, P=Sim | N=Sec) × P(N=Sec)")
    print(f"Numerador = {p_vp_dado_n['Secundario']:.4f} × {P_N['Secundario']:.1f} = {numerador:.6f}")
    
    # Calcular o denominador
    print(f"\nPasso 3: Calcular denominador P(V=Sim, P=Sim)")
    denominador = 0.0
    for n in ['Universitario', 'Secundario', 'Fundamental']:
        termo = p_vp_dado_n[n] * P_N[n]
        denominador += termo
        print(f"  N={n:13s}: {p_vp_dado_n[n]:.4f} × {P_N[n]:.1f} = {termo:.6f}")
    
    print(f"\nP(V=Sim, P=Sim) = {denominador:.6f}")
    
    # Calcular resultado final
    resultado = numerador / denominador
    
    print(f"\nPasso 4: Calcular probabilidade final")
    print(f"P(N=Secundário | V=Sim, P=Sim) = {numerador:.6f} / {denominador:.6f}")
    print(f"P(N=Secundário | V=Sim, P=Sim) = {resultado:.6f} = {resultado*100:.4f}%")
    print()
    
    return resultado


if __name__ == "__main__":
    print("\n")
    print("*" * 70)
    print("TRABALHO 3 - RACIOCÍNIO PROBABILÍSTICO")
    print("Cálculos de Probabilidades para Redes Bayesianas")
    print("*" * 70)
    print("\n")
    
    # PARTE 1
    print("\n")
    print("#" * 70)
    print("# PARTE 1: DETECÇÃO DE FRAUDE EM CARTÃO DE CRÉDITO")
    print("#" * 70)
    print("\n")
    
    q3 = questao_3()
    print("\n")
    
    q4 = questao_4()
    print("\n")
    
    q5 = questao_5()
    print("\n")
    
    q6 = questao_6()
    print("\n")
    
    # PARTE 2
    print("\n")
    print("#" * 70)
    print("# PARTE 2: DESONESTIDADE ACADÊMICA")
    print("#" * 70)
    print("\n")
    
    p2q1 = parte2_questao_1()
    print("\n")
    
    p2q2 = parte2_questao_2()
    print("\n")
    
    # Resumo dos resultados
    print("\n")
    print("*" * 70)
    print("RESUMO DOS RESULTADOS")
    print("*" * 70)
    print(f"\nPARTE 1:")
    print(f"  Questão 3 - P(G=sim): {q3:.8f} ({q3*100:.6f}%)")
    print(f"  Questão 4 - P(C=sim): {q4:.8f} ({q4*100:.6f}%)")
    print(f"  Questão 5 - P(C=sim|G=sim): {q5:.8f} ({q5*100:.6f}%)")
    print(f"  Questão 6 - P(F=sim|C=sim,G=não): {q6:.10f} ({q6*100:.8f}%)")
    print(f"\nPARTE 2:")
    print(f"  Questão 1 - P(Cola=Sim): {p2q1:.3f} ({p2q1*100:.1f}%)")
    print(f"  Questão 2 - P(N=Sec|V=Sim,P=Sim): {p2q2:.6f} ({p2q2*100:.4f}%)")
    print("\n")

