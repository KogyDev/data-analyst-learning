# Sistema de Gerenciamento de Estoque de uma Loja de Eletrônicos

class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class GerenciadorEstoque:
    def __init__(self):
        self.produtos = []
        self.historico_vendas = []
        self.historico_compras = []
    
    def adicionar_produto(self, produto):
        """Adiciona um novo produto ao estoque"""
        # Verifica se já existe um produto com o mesmo código
        for p in self.produtos:
            if p.codigo == produto.codigo:
                print(f"Produto com código {produto.codigo} já existe. Use atualizar estoque.")
                return False
        
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado com sucesso!")
        return True
    
    def atualizar_estoque(self, codigo, quantidade):
        """Atualiza a quantidade de um produto no estoque"""
        for produto in self.produtos:
            if produto.codigo == codigo:
                produto.quantidade += quantidade
                
                # Registra no histórico de compras/vendas
                if quantidade > 0:
                    self.historico_compras.append({
                        "codigo": codigo,
                        "nome": produto.nome,
                        "quantidade": quantidade,
                        "preco_total": quantidade * produto.preco
                    })
                    print(f"Estoque de {produto.nome} atualizado. Nova quantidade: {produto.quantidade}")
                else:
                    self.historico_vendas.append({
                        "codigo": codigo,
                        "nome": produto.nome,
                        "quantidade": abs(quantidade),
                        "preco_total": abs(quantidade) * produto.preco
                    })
                    print(f"Venda de {produto.nome} registrada. Nova quantidade: {produto.quantidade}")
                
                return True
        
        print(f"Produto com código {codigo} não encontrado.")
        return False
    
    def remover_produto(self, codigo):
        """Remove um produto do estoque"""
        for i, produto in enumerate(self.produtos):
            if produto.codigo == codigo:
                removido = self.produtos.pop(i)
                print(f"Produto {removido.nome} removido do estoque.")
                return True
        
        print(f"Produto com código {codigo} não encontrado.")
        return False
    
    def buscar_produto(self, codigo):
        """Busca um produto pelo código"""
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None
    
    def listar_produtos(self):
        """Lista todos os produtos em estoque"""
        if not self.produtos:
            print("Estoque vazio.")
            return []
        
        print("\n===== ESTOQUE ATUAL =====")
        for produto in self.produtos:
            print(f"Código: {produto.codigo}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")
            print("---")
        
        return self.produtos
    
    def produtos_em_falta(self):
        """Encontra produtos com estoque baixo"""
        produtos_baixo_estoque = [
            produto for produto in self.produtos 
            if produto.quantidade < 5
        ]
        
        if produtos_baixo_estoque:
            print("\n===== PRODUTOS COM ESTOQUE BAIXO =====")
            for produto in produtos_baixo_estoque:
                print(f"Código: {produto.codigo}")
                print(f"Nome: {produto.nome}")
                print(f"Quantidade atual: {produto.quantidade}")
                print("---")
        else:
            print("Todos os produtos estão com estoque adequado.")
        
        return produtos_baixo_estoque
    
    def valor_total_estoque(self):
        """Calcula o valor total do estoque"""
        valor_total = sum(
            produto.preco * produto.quantidade 
            for produto in self.produtos
        )
        print(f"\nValor total do estoque: R$ {valor_total:.2f}")
        return valor_total
    
    def relatorio_vendas(self):
        """Gera relatório de vendas"""
        if not self.historico_vendas:
            print("Nenhuma venda realizada.")
            return []
        
        print("\n===== RELATÓRIO DE VENDAS =====")
        valor_total_vendas = 0
        for venda in self.historico_vendas:
            print(f"Produto: {venda['nome']}")
            print(f"Quantidade vendida: {venda['quantidade']}")
            print(f"Valor total: R$ {venda['preco_total']:.2f}")
            print("---")
            valor_total_vendas += venda['preco_total']
        
        print(f"Valor total de vendas: R$ {valor_total_vendas:.2f}")
        return self.historico_vendas

# Demonstração do uso do sistema
def main():
    # Cria o gerenciador de estoque
    estoque = GerenciadorEstoque()
    
    # Adiciona alguns produtos
    estoque.adicionar_produto(Produto("P001", "Smartphone", 1500.00, 10))
    estoque.adicionar_produto(Produto("P002", "Notebook", 3500.00, 5))
    estoque.adicionar_produto(Produto("P003", "Fone de Ouvido", 250.00, 20))
    
    # Lista produtos
    estoque.listar_produtos()
    
    # Atualiza estoque (compra)
    estoque.atualizar_estoque("P001", 5)
    
    # Atualiza estoque (venda)
    estoque.atualizar_estoque("P002", -2)
    
    # Verifica produtos em falta
    estoque.produtos_em_falta()
    
    # Calcula valor total do estoque
    estoque.valor_total_estoque()
    
    # Gera relatório de vendas
    estoque.relatorio_vendas()

# Executa o programa
if __name__ == "__main__":
    main()