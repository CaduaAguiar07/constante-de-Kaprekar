# ============================================================
# ALGORITMO: ROTINA DE KAPREKAR (CONSTANTE 6174)
# REQUISITOS: APENAS MATEMÁTICA, SEM STRINGS, SEM LISTAS
# ============================================================

def main():
    # 1. Leitura do número inicial
    print("--- Simulador da Rotina de Kaprekar ---")
    n_inicial = int(input("Digite um número de 4 dígitos (diferentes): "))
    
    # 2. Validação rigorosa
    if n_inicial < 0 or n_inicial > 9999:
        print("Erro: O número deve ter entre 1 e 4 dígitos.")
        return
    
    if n_inicial != 0 and n_inicial % 1111 == 0:
        print("Erro: Os dígitos não podem ser todos iguais (ex: 1111).")
        return

    # Definimos a variável de trabalho e o contador de iterações
    num = n_inicial
    iteracao = 0
    
    print(f"\nIniciando processo para o número: {num:04d}")
    print("-" * 30)

    # 3. Laço Principal: Repete até chegar na constante 6174
    # Se o número já for 6174, o edital geralmente pede para mostrar ao menos 1 execução
    # ou parar imediatamente. Aqui, faremos o processo padrão.
    
    primeira_execucao = True

    while num != 6174 or primeira_execucao:
        # Se o número for 6174 logo de cara, ele executa uma vez e para.
        # Se não, ele segue até encontrar o 6174.
        if num == 6174 and not primeira_execucao:
            break
            
        iteracao += 1
        
        # A. EXTRAÇÃO DOS DÍGITOS (Decomposição Matemática)
        # Ex: Se num = 3412
        milhar  = num // 1000            # 3
        centena = (num // 100) % 10      # 4
        dezena  = (num // 10) % 10       # 1
        unidade = num % 10               # 2

        # B. ORDENAÇÃO MANUAL (Algoritmo de Troca Simples)
        # Vamos organizar do maior para o menor: d1, d2, d3, d4
        d1, d2, d3, d4 = milhar, centena, dezena, unidade
        
        # Bubble Sort manual para 4 variáveis
        for i in range(4):
            if d1 < d2: d1, d2 = d2, d1
            if d2 < d3: d2, d3 = d3, d2
            if d3 < d4: d3, d4 = d4, d3

        # C. MONTAGEM DOS VALORES (Composição Matemática)
        valor_maior = (d1 * 1000) + (d2 * 100) + (d3 * 10) + d4
        valor_menor = (d4 * 1000) + (d3 * 100) + (d2 * 10) + d1
        
        # D. CÁLCULO DO NOVO NÚMERO
        resultado = valor_maior - valor_menor
        
        # E. EXIBIÇÃO FORMATADA
        # O :04d preenche com zeros à esquerda se o número tiver menos de 4 dígitos
        print(f"Passo {iteracao}: {valor_maior:04d} - {valor_menor:04d} = {resultado:04d}")
        
        # Atualização para a próxima rodada
        num = resultado
        primeira_execucao = False
        
        # Prevenção contra o zero (caso os dígitos sejam iguais por erro)
        if num == 0:
            print("Resultado zero atingido. Digitos iguais?")
            break

    print("-" * 30)
    print(f"Rotina finalizada. Constante 6174 encontrada em {iteracao} passos.")

# Iniciar o programa
if __name__ == "__main__":
    main()