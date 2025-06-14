from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_invoice(order_items, total_amount, filename='invoice.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "E-Commerce Invoice")

    c.setFont("Helvetica", 12)
    c.drawString(30, height - 80, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(30, height - 100, "Customer: Guest User")

    y = height - 140
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y, "Product")
    c.drawString(300, y, "Price")
    c.setFont("Helvetica", 12)
    y -= 20

    for item in order_items:
        c.drawString(30, y, item['name'])
        c.drawString(300, y, f"₹ {item['price']}")
        y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y - 10, f"Total Amount: ₹ {total_amount}")

    c.showPage()
    c.save()
