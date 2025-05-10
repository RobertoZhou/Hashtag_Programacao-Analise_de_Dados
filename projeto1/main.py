#   Importando bibliotecas
import pandas as pd

#   Trazendo a base de dados
tabela = pd.read_excel("Vendas.xlsx")
#print(tabela)

faturamento_total = tabela["Valor Final"].sum()
#print(f"Faturamento Total: {faturamento_total}")

#   Faturamento por Loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
#print(faturamento_por_loja)

#   Detalhes da Loja para entender Melhor
faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)