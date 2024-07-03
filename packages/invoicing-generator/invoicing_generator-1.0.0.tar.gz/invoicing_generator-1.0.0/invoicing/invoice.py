import os

import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, image_path, product_id,
             product_name, amount_purchased, price_per_unit, total_price):
    """
    This function converts invoice Excel files into invoices in PDF format.
    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        filename = Path(filepath).stem
        invoice_nr, invoice_date = filename.split("-")

        pdf.set_font("Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Date {invoice_date}", ln=1)

        # Add a table header
        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        columns = df.columns
        columns = [item.replace("_", " ").title() for item in columns]

        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=22, h=10, border=1, txt=columns[0])
        pdf.cell(w=70, h=10, border=1, txt=columns[1])
        pdf.cell(w=37, h=10, border=1, txt=columns[2])
        pdf.cell(w=30, h=10, border=1, txt=columns[3])
        pdf.cell(w=30, h=10, border=1, txt=columns[4], ln=1)

        # Add table rows
        for index, row in df.iterrows():
            pdf.set_font(family="Times", size=12)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=22, h=10, border=1, txt=str(row[product_id]))
            pdf.cell(w=70, h=10, border=1, txt=row[product_name])
            pdf.cell(w=37, h=10, border=1, txt=str(row[amount_purchased]))
            pdf.cell(w=30, h=10, border=1, txt=str(row[price_per_unit]))
            pdf.cell(w=30, h=10, border=1, txt=str(row[total_price]), ln=1)

        total = df[total_price].sum()

        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=22, h=10, txt="", border=1)
        pdf.cell(w=70, h=10, txt="", border=1)
        pdf.cell(w=37, h=10, txt="", border=1)
        pdf.cell(w=30, h=10, txt="", border=1)
        pdf.cell(w=30, h=10, border=1, txt=f"{total}", ln=1)

        # Add total sum sentence
        pdf.cell(w=30, h=10, txt=f"The total price is {total}", ln=1)

        # Add company name and logo
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=30, h=10, txt=f"PythonHow")
        pdf.image(image_path, w=10)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")
