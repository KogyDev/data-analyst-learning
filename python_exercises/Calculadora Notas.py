class CalculadoraMedia:
    def __init__(self):
        self.notas = []
        self.media_aprovacao = 6.0
        self.limite_provas = 5

    def validar_nota(self, nota):
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                return True, nota
            else:
                print("\nErro: A nota deve estar entre 0 e 10!")
                return False, None
        except ValueError:
            print("\nErro: Digite um número válido!")
            return False, None

    def coletar_notas(self):
        print("\n=== Calculadora de Média Escolar ===")
        print(f"Digite até {self.limite_provas} notas (pressione Enter sem digitar nada para calcular)")
        print("Obs: Use ponto (.) para decimais - Exemplo: 7.5")
        
        contador = 1
        while contador <= self.limite_provas:
            entrada = input(f"\nDigite a nota da {contador}ª prova (ou Enter para finalizar): ")
            
            if entrada == "":
                break
                
            valido, nota = self.validar_nota(entrada)
            if valido:
                self.notas.append(nota)
                contador += 1

    def calcular_media(self):
        if not self.notas:
            print("\nNenhuma nota foi registrada!")
            return
        
        media = sum(self.notas) / len(self.notas)
        
        print("\n=== Resultado ===")
        print(f"Notas registradas: {', '.join(str(nota) for nota in self.notas)}")
        print(f"Quantidade de provas: {len(self.notas)}")
        print(f"Média final: {media:.1f}")
        
        if media >= self.media_aprovacao:
            print("\n🎉 APROVADO! Parabéns! 🎉")
            if media >= 9:
                print("Excelente desempenho!")
            elif media >= 7.5:
                print("Ótimo desempenho!")
        else:
            print("\n❌ REPROVADO")
            print(f"Faltou {self.media_aprovacao - media:.1f} pontos para atingir a média.")
        
        self.mostrar_estatisticas()

    def mostrar_estatisticas(self):
        if self.notas:
            print("\n=== Estatísticas ===")
            print(f"Maior nota: {max(self.notas):.1f}")
            print(f"Menor nota: {min(self.notas):.1f}")
            print(f"Nota necessária para aprovação: {self.media_aprovacao:.1f}")

def main():
    while True:
        calculadora = CalculadoraMedia()
        calculadora.coletar_notas()
        calculadora.calcular_media()
        
        continuar = input("\nDeseja calcular outra média? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nObrigado por usar a Calculadora de Média!")
            break

if __name__ == "__main__":
    main()