from fpdf import FPDF
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.normpath(os.path.join(CURRENT_DIR, "DejaVuSans.ttf"))

class SkeletonKeyReport(FPDF):
    def header(self):
        self.set_text_color(182, 112, 50)
        self.set_font("DejaVu", "B", 16)
        self.cell(0, 10, "SKELETON KEY - SECURITY AUDIT REPORT", ln=True, align="C")
        
        self.set_draw_color(182, 112, 50)
        self.line(10, 22, 200, 22)
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Confidential Report - Page {self.page_no()}", align="C")

def export_to_pdf(filename, db_id, date, mode, algorithm, key, input_text, output_text):
    pdf = SkeletonKeyReport()
    

    pdf.add_font("DejaVu", "", FONT_PATH)
    pdf.add_font("DejaVu", "B", FONT_PATH)
    pdf.add_font("DejaVu", "I", FONT_PATH)
    
    pdf.add_page()
    
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(95, 8, f"Transaction ID: {db_id}", border="B")
    pdf.cell(95, 8, f"Timestamp: {date}", border="B", ln=True, align="R")
    pdf.ln(10)

    pdf.set_text_color(182, 112, 50)
    pdf.set_font("DejaVu", "B", 12)
    pdf.cell(0, 10, "1. CONFIGURATION DETAILS", ln=True)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("DejaVu", "", 11)
    

    data_points = [
        ("Algorithm:", algorithm),
        ("Mode:", mode),
        ("Security Key:", key)
    ]
    
    for label, value in data_points:
        pdf.set_font("DejaVu", "B", 11)
        pdf.cell(40, 8, label)
        pdf.set_font("DejaVu", "", 11)
        pdf.cell(0, 8, str(value), ln=True)

    pdf.ln(10)

    sections = [
        ("2. INPUT DATA", input_text),
        ("3. PROCESSED OUTPUT", output_text)
    ]

    for title, content in sections:
        pdf.set_text_color(182, 112, 50)
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 10, title, ln=True)
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("DejaVu", "", 10)
        
        pdf.set_fill_color(248, 248, 248)
        clean_content = str(content).strip().replace('\n\n', '\n')
        pdf.multi_cell(0, 5, clean_content, border=1, fill=True)
        pdf.ln(10)

    pdf.output(filename)