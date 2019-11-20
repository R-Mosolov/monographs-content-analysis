import sys
import pdfminer.high_level

with open('pdf/fiction_literature/russian/Tolstoy/big_form/Tolstoyi_L_Anna_KareninaI.a6.pdf', 'rb') as file:
    pdfminer.high_level.extract_text_to_fp(file, sys.stdout)