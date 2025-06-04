import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0)
        
        #title h1
        self.labelTitle = tk.Label(self, text="CALCULADORA DE JUROS SIMPLES", font=('Helvetica', 20, 'bold'))
        self.labelTitle.grid(row=0, column=1, columnspan=3, pady=50)
        
        # Labels and entrys for  M C F I T

        self.labelCapital = tk.Label(self, text="Capital(C): ", font=('Arial', 15, 'bold'))
        self.labelCapital.grid(row= 2, column=0, sticky='e') 
        self.entryCapital = tk.Entry(self, width=25, font=('Arial', 15, 'bold'))
        self.entryCapital.grid(row=2, column=1, sticky='w')

        self.labelTaxa = tk.Label(self, text="Taxa(I): ", font=('Arial', 15, 'bold'))
        self.labelTaxa.grid(row= 3, column=0, sticky='e') 
        self.entryTaxa = tk.Entry(self, width=25, font=('Arial', 15, 'bold'))
        self.entryTaxa.grid(row=3, column=1,sticky='w')
        
        self.labelTempo = tk.Label(self, text="Tempo(T): ", font=('Arial', 15, 'bold'))
        self.labelTempo.grid(row= 4, column=0, sticky='e') 
        self.entryTempo = tk.Entry(self, width=25, font=('Arial', 15, 'bold'))
        self.entryTempo.grid(row=4, column=1, sticky='w')

        #Label for RespostalabelResposta
        self.labelResposta = tk.Label(self, text='', font=('Arial', 15, 'bold'))
        self.labelResposta.grid(row=8, column=1, pady=40)

        #Button for calc
        self.buttonCalculo = tk.Button(self, width=40, height=2, text="Calcular", font=('Arial', 15, 'bold'), command=self.funcaoCalcular)
        self.buttonCalculo.grid(row=10, column=1, pady=50)

    def funcaoCalcular(self):
        entradaTaxa = self.entryTaxa.get()
        entradaCapital = self.entryCapital.get()
        entradaTempo = self.entryTempo.get()
        
        respostaJuros = 0
        textoResposta = ''

        if self.isNumber(entradaCapital) and self.isNumber(entradaTaxa) and self.isNumber(entradaTempo):
            respostaJuros = self.calculoJuros(float(entradaCapital), float(entradaTaxa)/100, float(entradaTempo))
            textoResposta = f"Juros(J) = {respostaJuros}"
            textoResposta = f'{textoResposta}\nMontante(M) = {self.calculoMontante(float(entradaCapital), respostaJuros)}'
            self.labelResposta.config(text=textoResposta)
        else:
            self.labelResposta.config(text="Digite Valores validos")
        
    def calculoMontante(self, capital, juros):
        return capital + juros

    def calculoJuros(self, capital, taxa, tempo):
        return capital * taxa * tempo

    #implementar futuramente
    def calculoCapital(self, juros, taxa, tempo):
        return juros/(taxa*tempo)
    
    def calculoTaxa(self, capital, juros, tempo):
        return juros/(capital * tempo)

    def calculoTempo(self, capital, juros, taxa):
        return juros/(capital * taxa)

    def isNumber(self, string):
        try:
            float(string)
        except ValueError:
            return False
        return True

root = tk.Tk()
root.title("Juros")
root.geometry("750x500")
root.resizable(False, False)
myapp = App(root)
myapp.mainloop()