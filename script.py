import customtkinter as ctk
from tkinter import filedialog, messagebox
from utils import gerar_array, salvar_array
from contribuicao import correcao17COD_CTA
from fiscal import calValueTypeDocument

ctk.set_appearance_mode("light")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SPEED")
        self.geometry("400x250")

        self.current_page = 0  # 0 = Fiscal, 1 = Contribuição

        # Topo comum
        self.top_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.top_frame.pack(fill="x", padx=15, pady=15)

        self.file_path_var = ctk.StringVar()
        self.file_entry = ctk.CTkEntry(self.top_frame, textvariable=self.file_path_var, width=230, height=32, border_color="#757575", border_width=0.8)
        self.file_entry.pack(side="left")

        self.select_button = ctk.CTkButton(self.top_frame, text="Selecionar arquivo", command=self.select_file, fg_color="#FFA000", text_color="white", width=128, height=32)
        self.select_button.pack(side="left", padx=(15,0))

        self.line = ctk.CTkFrame(self, height=2, width=370, fg_color="#757575")
        self.line.pack(fill="x", padx=15)

        # Área de conteúdo variável
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=15, pady=(15,0))

        # Botões de navegação
        self.nav_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.nav_frame.pack(fill="x", padx=15, pady=15)

        self.fiscal_button = ctk.CTkButton(self.nav_frame, text="SPEED Fiscal", command=self.fiscal_page, height=24, width=86, fg_color="#FFA000", text_color="white")
        self.fiscal_button.pack(side="left", padx=(0,15))

        self.contrib_button = ctk.CTkButton(self.nav_frame, text="SPEED Contribuição", command=self.contrib_page, height=24, width=119, fg_color="#FFA000", text_color="white")
        self.contrib_button.pack(side="left")

        self.arrow_button = ctk.CTkButton(self.nav_frame, text="→", command=self.init_script, height=24, width=24, fg_color="transparent", text_color="#757575", font=("Arial", 24))
        self.arrow_button.pack(side="right")

        # Inicializa páginas
        self.pages = [self.create_fiscal_page(), self.create_contrib_page()]
        self.show_page(0)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos TXT", "*.txt")])
        if file_path:
            self.file_path_var.set(file_path)

    def create_fiscal_page(self):
        frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        title = ctk.CTkLabel(frame, text="Fiscal", font=("Arial", 18, "bold"))
        title.pack(anchor="w")

        self.fiscal_checkbox = ctk.CTkCheckBox(frame, text="Calcular valor por tipo documento", border_color="#757575", font=("Arial", 12), checkbox_width=20, checkbox_height=20, border_width=0.8, corner_radius=5)
        self.fiscal_checkbox.pack(anchor="w")

        return frame

    def create_contrib_page(self):
        frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        title = ctk.CTkLabel(frame, text="Contribuição", font=("Arial", 18, "bold"))
        title.pack(anchor="w")

        self.contrib_checkbox = ctk.CTkCheckBox(frame, text="Correção 17 COD_CTA",  border_color="#757575", font=("Arial", 12), checkbox_width=20, checkbox_height=20, border_width=0.8, corner_radius=5)
        self.contrib_checkbox.pack(anchor="w")

        return frame

    def show_page(self, index):
        for page in self.pages:
            page.pack_forget()
        self.pages[index].pack(fill="both", expand=True)
        self.current_page = index

        # Controle de visibilidade do botão "Próxima Página"
        if self.current_page == len(self.pages) - 1:
            self.contrib_button.pack_forget()
        else:
            self.contrib_button.pack(side="left")

        # Controle do botão "Voltar Página"
        if self.current_page == 0:
            self.fiscal_button.pack_forget()
        else:
            self.fiscal_button.pack(side="left")

    def contrib_page(self):
        if self.current_page < len(self.pages) - 1:
            self.show_page(self.current_page + 1)

    def fiscal_page(self):
        if self.current_page > 0:
            self.show_page(self.current_page - 1)

    def init_script(self):

        caminho = self.file_path_var.get();

        if self.current_page == 0:
            if not self.fiscal_checkbox.get():
                messagebox.showinfo("Aviso", "Nenhuma opção marcada na página Fiscal.")

            if self.fiscal_checkbox.get():
                array_final = gerar_array(caminho)
                calValueTypeDocument(array_final)


        elif self.current_page == 1:
            if not self.contrib_checkbox.get():
                messagebox.showinfo("Aviso", "Nenhuma opção marcada na página Contribuição.")

            if self.contrib_checkbox.get():
                array_final = gerar_array(caminho)
                correcao17COD_CTA(array_final)
                salvar_array(array_final, caminho)

if __name__ == "__main__":
    app = App()
    app.mainloop()