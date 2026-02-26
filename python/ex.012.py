preco = float(input('Qual o valor do produto? R$'))
desc = int(input('Quanto de desconto? '))
#que bagunça do kct tmnc
desc_produto = preco - (preco * desc / 100 )
5
print(f'O Produto com Desconto é R${desc_produto:.2F}')
 