def calcular_multa_com_carencia(dias_atraso, dias_carencia, valor_por_dia):
    dias_cobrados = max(0, dias_atraso - dias_carencia)
    return dias_cobrados * valor_por_dia