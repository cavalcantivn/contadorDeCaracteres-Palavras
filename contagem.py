def contar_caracteres(texto):
    return len(texto)


def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)


continuar_execucao = True

while continuar_execucao:
    print("=== Contador de Caracteres/Palavras ===")
    entrada_usuario = input("Digite um texto (ou 'sair' para encerrar): ")

    if entrada_usuario.lower() == 'sair':
        print("Programa encerrado. Até logo!")
        continuar_execucao = False
    else:
        opcao = input("Escolha a opção (C para caracteres, P para palavras): ")

        if opcao.upper() == 'C':
            resultado = contar_caracteres(entrada_usuario)
            print(f"O texto tem {resultado} caracteres.")
        elif opcao.upper() == 'P':
            resultado = contar_palavras(entrada_usuario)
            print(f"O texto tem {resultado} palavras.")
        else:
            print("Opção inválida. Tente novamente.")
