import tkinter as tk

# Sample static conversion rates (USD base)
conversion_rates = {
    'USD': 1.0,
    'INR': 86.72,
    'EUR': 0.87,
    'GBP': 0.75,
    'JPY': 147.46
}

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = from_var.get()
    to_currency = to_var.get()
    
    converted_amount = amount * conversion_rates[to_currency] / conversion_rates[from_currency]
    result_label.config(text=f'{converted_amount:.2f} {to_currency}')

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x200")

# Widgets
tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="From:").pack()
from_var = tk.StringVar(root)
from_var.set("USD")
tk.OptionMenu(root, from_var, *conversion_rates.keys()).pack()

tk.Label(root, text="To:").pack()
to_var = tk.StringVar(root)
to_var.set("INR")
tk.OptionMenu(root, to_var, *conversion_rates.keys()).pack()

tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack()

root.mainloop()
