# canvas_form.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
def form(path):
    my_canvas = canvas.Canvas(path, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)
    my_canvas.drawString(30, 750, "FUCK JORDAN 1'S")
    my_canvas.drawString(30, 735, 'BOCHU ROBIN && BRAVARD THIBAULT')
    my_canvas.drawString(500, 750, "12/12/2010")
    my_canvas.line(120, 700, 580, 700)
    my_canvas.save()

if __name__ == '__main__':
    form('canvas_form.pdf')