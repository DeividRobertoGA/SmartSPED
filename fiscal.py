from tkinter import messagebox
import locale

def calValueTypeDocument(array):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    calc65 = 0.00
    calc55 = 0.00
    for sub_array in array:
        if len(sub_array) >= 2 and sub_array[0] == "C100" and sub_array[4] == "65":
            valor_str = sub_array[11]
            try:
                valor_float = float(valor_str.replace(",", "."))
            except (ValueError, AttributeError):
                valor_float = 0.00

            calc65 = calc65 + valor_float
        
        if len(sub_array) >= 2 and sub_array[0] == "C100" and sub_array[4] == "55":
            valor_str = sub_array[11]
            try:
                valor_float = float(valor_str.replace(",", "."))
            except (ValueError, AttributeError):
                valor_float = 0.00

            calc55 = calc55 + valor_float

    calc65 = locale.format_string('%.2f', calc65, grouping=True)
    calc55 = locale.format_string('%.2f', calc55, grouping=True)

    messagebox.showinfo("Finalizado", f"Valor total do arquivo NFC-e igual á\n{calc65} Reais")
    messagebox.showinfo("Finalizado", f"Valor total do arquivo NFe igual á\n{calc55} Reais")