import tkinter as tk
from tkinter import filedialog, messagebox
from pipeline import pipeline  # Importa o pipeline

class OntologyConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Conversor de Dados Estruturados para Ontologias")

        # Título do projeto
        self.label = tk.Label(master, text="Conversor de Dados Estruturados para Ontologias", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Botão para upload de arquivo CSV
        self.upload_button = tk.Button(master, text="Fazer Upload de Arquivo CSV", command=self.upload_file)
        self.upload_button.pack(pady=10)

        # Label para mostrar o arquivo selecionado
        self.file_label = tk.Label(master, text="")
        self.file_label.pack(pady=10)

        # Botão para gerar OWL
        self.generate_button = tk.Button(master, text="Gerar Ontologia OWL", command=self.generate_owl, state=tk.DISABLED)
        self.generate_button.pack(pady=10)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            self.file_label.config(text=f"Arquivo selecionado: {self.file_path}")
            self.generate_button.config(state=tk.NORMAL)

    def generate_owl(self):
        try:
            # Chamar a função de pipeline com o arquivo carregado
            pipeline(self.file_path)  # Chama o pipeline com o caminho do arquivo
            messagebox.showinfo("Sucesso", "Ontologia OWL gerada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
