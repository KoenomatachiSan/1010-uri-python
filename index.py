COD_PEÇA_1 = int(input("Código da peca 1:"))
QTD_PEÇA_1 = int(input("Quantidade de peças 1:"))
VALUE_PECA_1 = float(input("Valor da peca 1:"))
TOTAL_1 = (QTD_PEÇA_1 * VALUE_PECA_1)

COD_PEÇA_2 = int(input("Código da peca 2:"))
QTD_PEÇA_2 = int(input("Quantidade de peças 2:"))
VALUE_PECA_2 = float(input("Valor da peca 2:"))
TOTAL_2 = (QTD_PEÇA_2 * VALUE_PECA_2)

TOTAL = TOTAL_1 + TOTAL_2
print("VALOR A PAGAR: R$:", TOTAL)
