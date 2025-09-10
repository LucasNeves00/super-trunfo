def comparar(cartax, cartay, atributo):
    """
    Compara o valor de um atributo entre duas cartas.
    :param cartax: Carta
    :param cartay: Carta
    :param atributo: str -> nome do atributo a ser comparado
    :return: str -> resultado da comparação
    """
    valor_x = cartax.atributos.get(atributo)
    valor_y = cartay.atributos.get(atributo)

    if valor_x is None or valor_y is None:
        return f"Atributo '{atributo}' inválido para comparação."

    if valor_x > valor_y:
        return f"{cartax.nome} venceu com {atributo} ({valor_x} vs {valor_y})!"
    elif valor_x < valor_y:
        return f"{cartay.nome} venceu com {atributo} ({valor_y} vs {valor_x})!"
    else:
        return f"Empate no atributo {atributo}! ({valor_x} vs {valor_y})"
