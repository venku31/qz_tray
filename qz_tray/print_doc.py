import frappe
import io
from frappe.utils.print_format import download_pdf

@frappe.whitelist()
def print_sales_invoice(docname):
    pdf = download_pdf('Sales Invoice', docname)
    return io.BytesIO(pdf)