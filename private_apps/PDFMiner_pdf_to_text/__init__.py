import sys
import pdfminer.high_level

with open('../../../texts-datasets/PDFMiner_pdf_to_text/pdf/examples/RU_Kant_I._Sochineniya_V_6_Tomah_T._1.pdf', 'rb') as file:
    pdfminer.high_level.extract_text_to_fp(file, sys.stdout)
