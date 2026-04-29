def main():
    print("--- Simulador da Rotina de Kaprekar ---")
    n_inicial = int(input("Digite um número de 4 dígitos (não todos iguais): "))

    # Rejeita números fora do intervalo válido de 4 dígitos (1 a 9999)
    if n_inicial < 1 or n_inicial > 9999:
        print("Erro: O número deve ter entre 1 e 4 dígitos.")
        return

    # Rejeita números com todos os dígitos iguais (1111, 2222 ... 9999)
    # pois a subtração resultaria em zero — a rotina nunca convergiria
    if n_inicial % 1111 == 0:
        print("Erro: Os dígitos não podem ser todos iguais (ex: 1111).")
        return

    num = n_inicial
    iteracao = 0

    print(f"\nIniciando processo para o número: {num:04d}")
    print("-" * 30)

    # Loop principal: a rotina de Kaprekar sempre converge para 6174
    # em no máximo 7 iterações para qualquer entrada válida de 4 dígitos
    while True:
        iteracao += 1

        # Decompõe o número atual em seus 4 dígitos usando divisão inteira e módulo
        # Isso evita o uso de strings — requisito do algoritmo
        milhar  = num // 1000
        centena = (num // 100) % 10
        dezena  = (num // 10) % 10
        unidade = num % 10

        # Bubble sort manual em 4 variáveis — 3 passadas são suficientes
        # para garantir a ordenação completa de 4 elementos em qualquer caso
        d1, d2, d3, d4 = milhar, centena, dezena, unidade

        for _ in range(3):
            if d1 < d2: d1, d2 = d2, d1
            if d2 < d3: d2, d3 = d3, d2
            if d3 < d4: d3, d4 = d4, d3

        # Reconstrói o maior número (dígitos em ordem decrescente)
        # e o menor (dígitos em ordem crescente, ou seja, d4..d1)
        valor_maior = d1 * 1000 + d2 * 100 + d3 * 10 + d4
        valor_menor = d4 * 1000 + d3 * 100 + d2 * 10 + d1

        # O coração da rotina: a diferença entre o maior e o menor arranjo
        resultado = valor_maior - valor_menor

        # :04d formata com zeros à esquerda — garante exibição sempre com 4 dígitos
        # Ex: 495 é exibido como 0495, não como 495
        print(f"Passo {iteracao}: {valor_maior:04d} - {valor_menor:04d} = {resultado:04d}")

        num = resultado

        # Guarda de segurança: resultado zero indica dígitos todos iguais
        # que passaram pela validação inicial (ex: entrada 0 não capturada)
        if num == 0:
            print("Resultado zero atingido. Dígitos iguais detectados tardiamente.")
            break

        # Condição de parada: chegamos à constante de Kaprekar
        # A prova matemática garante que todo número válido chega aqui
        if num == 6174:
            break

    print("-" * 30)
    print(f"Rotina finalizada. Constante 6174 encontrada em {iteracao} passos.")


# Ponto de entrada padrão do Python — impede execução automática ao importar
# este arquivo como módulo em outro script
if __name__ == "__main__":
    main()
