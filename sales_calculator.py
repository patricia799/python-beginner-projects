import csv
import tkinter as tk
from tkinter import filedialog, messagebox


def process_csv_sales(filepath):
    """Reads a CSV file and calculates total items and revenue."""
    total_revenue = 0.0
    total_items = 0
    row_count = 0

    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            
            qty = int(row["Quantity"])
            price = float(row["Unit_Price"])

            if qty < 0 or price < 0:
                raise ValueError("Negative values are not allowed.")

            total_items += qty
            total_revenue += qty * price
            row_count += 1

    return {
        "transactions": row_count,
        "total_items": total_items,
        "total_revenue": total_revenue,
    }


def calculate_single_sale(qty_str, price_str):
    """Calculates a single manual transaction from GUI entry boxes."""
    qty = int(qty_str)
    price = float(price_str)
    if qty <= 0 or price < 0:
        raise ValueError("Quantity must be > 0 and price cannot be negative.")
    return qty * price


# TKINTER GUI APPLICATION
class SalesCalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Graphical Sales Calculator")
        self.root.geometry("450x420")
        self.root.padx = 20
        self.root.pady = 20

        self.selected_file = "transactions.csv"  # Default sample file
        self.last_report_text = ""

        # Title Label
        tk.Label(
            root, text="Sales & Revenue Calculator", font=("Times New Roman", 14, "bold"), bg="#ffe4ec", fg="#4a0e2e"
        ).pack(pady=10)

        # Manual Entry Section
        manual_frame = tk.LabelFrame(
            root, text="Quick Single Sale Calculation", padx=10, pady=10, bg="#ffd6e5", fg="#4a0e2e"
        )
        manual_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(manual_frame, text="Quantity:").grid(
            row=0, column=0, sticky="w"
        )
        self.qty_entry = tk.Entry(manual_frame, width=15)
        self.qty_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(manual_frame, text="Unit Price (R):").grid(
            row=1, column=0, sticky="w"
        )
        self.price_entry = tk.Entry(manual_frame, width=15)
        self.price_entry.grid(row=1, column=1, padx=5, pady=2)

        tk.Button(
            manual_frame,
            text="Calculate Single Sale",
            command=self.handle_manual_calc,
            bg="#da8ee7",
            fg="white",
        ).grid(row=0, column=2, rowspan=2, padx=10)

        # CSV Batch Processing Section
        csv_frame = tk.LabelFrame(
            root, text="CSV File Processing", padx=10, pady=10
        )
        csv_frame.pack(fill="x", padx=20, pady=10)

        self.file_label = tk.Label(
            csv_frame, text=f"Target File: {self.selected_file}", fg="gray"
        )
        self.file_label.pack(anchor="w", pady=(0, 5))

        btn_row = tk.Frame(csv_frame)
        btn_row.pack(fill="x")

        tk.Button(btn_row, text="Select CSV", command=self.select_file).pack(
            side="left", padx=5
        
        )
        tk.Button(
            btn_row,
            text="Calculate CSV Totals",
            command=self.handle_csv_calc,
            bg="#a000c8",
            fg="#de73ff",
        ).pack(side="left", padx=5)
        tk.Button(
            btn_row, text="Save Summary", command=self.save_summary
        ).pack(side="left", padx=5)

        # Results Display Window
        result_frame = tk.LabelFrame(
            root, text="Calculated Results", padx=10, pady=10
        )
        result_frame.pack(fill="both", expand=True, padx=20, pady=5)

        self.result_display = tk.Label(
            result_frame,
            text="Load a CSV or enter values above to view results.",
            justify="left",
            font=("Consolas", 10),
        )
        self.result_display.pack(anchor="w")

    def select_file(self):
        filepath = filedialog.askopenfilename(
            title="Select Transaction CSV",
            filetypes=[("CSV Files", ".csv"), ("All Files", ".*")],
        )
        if filepath:
            self.selected_file = filepath
            # Display only the filename for neatness
            short_name = filepath.split("/")[-1]
            self.file_label.config(
                text=f"Target File: {short_name}", fg="black"
            )

    def handle_manual_calc(self):
        try:
            total = calculate_single_sale(
                self.qty_entry.get(), self.price_entry.get()
            )
            self.last_report_text = (
                f"*** SINGLE SALE RECEIPT ***\n"
                f"Quantity:    {self.qty_entry.get()}\n"
                f"Unit Price:  R {float(self.price_entry.get()):.2f}\n"
                f"Total Due:   R {total:.2f}"
            )
            self.result_display.config(text=self.last_report_text, fg="black")
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid whole number for Quantity and a valid number for Price.",
            )

    def handle_csv_calc(self):
        try:
            summary = process_csv_sales(self.selected_file)
            self.last_report_text = (
                f"*** CSV SALES REPORT ***\n"
                f"Transactions Processed: {summary['transactions']}\n"
                f"Total Units Sold:       {summary['total_items']}\n"
                f"Total Revenue:          R {summary['total_revenue']:,.2f}"
            )
            self.result_display.config(text=self.last_report_text, fg="black")
        except FileNotFoundError:
            messagebox.showerror(
                "Missing File",
                f"Could not find '{self.selected_file}'.\nPlease select a valid CSV file.",
            )
        except (ValueError, KeyError) as e:
            messagebox.showerror(
                "CSV Data Error",
                f"Invalid numeric data or missing columns in CSV.\nDetails: {e}",
            )

    def save_summary(self):
        if not self.last_report_text:
            messagebox.showwarning(
                "Nothing to Save", "Please calculate a result first."
            )
            return

        try:
            with open("sales_summary.txt", "w", encoding="utf-8") as f:
                f.write(self.last_report_text + "\n")
            messagebox.showinfo(
                "Saved",
                "Report successfully saved to 'sales_summary.txt'!",
            )
        except IOError as e:
            messagebox.showerror("Save Error", f"Could not write file: {e}")


# RUN APPLICATION
if __name__ == "__main__":
   root = tk.Tk()
   app = SalesCalculatorApp(root)
   root.mainloop()