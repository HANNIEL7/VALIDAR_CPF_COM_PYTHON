from typing import Set

# Conjunto de CPFs inválidos conhecidos
CPFS_INVALIDOS: Set[str] = {
    "12345678909", "11111111111", "00000000000", "22222222222",
    "33333333333", "44444444444", "55555555555", "66666666666",
    "77777777777", "88888888888", "99999999999"
}

def calcular_digito(cpf: str, peso_inicial: int) -> int:
    """
    Calcula um dos dígitos verificadores do CPF.

    Args:
        cpf (str): Parte do CPF usada no cálculo.
        peso_inicial (int): Peso inicial a ser usado na multiplicação.

    Returns:
        int: Dígito verificador calculado.
    """
    soma = sum(int(cpf[i]) * (peso_inicial - i) for i in range(len(cpf)))
    return (soma * 10 % 11) % 10

def validar_cpf(cpf: str) -> bool:
    """
    Valida um número de CPF.

    Args:
        cpf (str): CPF em formato com ou sem máscara (ex: '123.456.789-09').

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    if not cpf:
        return False

    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf in CPFS_INVALIDOS or cpf == cpf[0] * 11:
        return False

    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:9] + str(digito1), 11)

    return cpf[-2:] == f"{digito1}{digito2}"

if __name__ == "__main__":
    cpf_teste = "529.982.247-25"
    if validar_cpf(cpf_teste):
        print(f"O CPF {cpf_teste} é válido.")
    else:
        print(f"O CPF {cpf_teste} é inválido.")