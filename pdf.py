import tabula as tb
import os
import re


from PyPDF2 import PdfFileReader, PdfFileWriter
#pdf = PdfFileReader("Victor_Caballero_College_Transcript_10_25_2022.pdf")
myfile = open("C:\Users\ps4vi\Downloads\Victor_Caballero_College_Transcript_10_25_2022.pdf")
pdf = myfile.read()
myfile.close()
#(top, left, bottom, right)

fall2018 = tb.read_pdf(pdf, area = (175, 5, 225, 250), pages = '1', silent = True,)
fall2019 = tb.read_pdf(pdf, area = (145, 400, 225, 600), pages = '1', silent = True,)
spring2019 = tb.read_pdf(pdf, area = (365, 5, 445, 240), pages = '1', silent = True,)
print("                    Fall 2018")
print(fall2018)
print("\n")
print("                    Spring 2019")
print(spring2019)
print("\n")
print("                    Fall 2019")
print(fall2019)

#(top, left, bottom, right)
spring2020 = tb.read_pdf(pdf, area = (120, 5, 225, 250), pages = '2', silent = True,)
spring2021 = tb.read_pdf(pdf, area = (145, 400, 225, 600), pages = '2', silent = True,)
fall2020 = tb.read_pdf(pdf, area = (355, 5, 445, 240), pages = '2', silent = True,)
summer2021 = tb.read_pdf(pdf, area = (355, 400, 430, 600), pages = '2', silent = True,)
print("                    Spring 2020")
print(spring2020)
print("\n")
print("                    Fall 2020")
print(fall2020)
print("\n")
print("                    Spring 2021")
print(spring2021)
print("\n")
print("                    Summer 2021")
print(summer2021)

#(top, left, bottom, right)
fall2021 = tb.read_pdf(pdf, area = (140, 5, 225, 250), pages = '3', silent = True,)
spring2022= tb.read_pdf(pdf, area = (355, 5, 445, 240), pages = '3', silent = True,)
fall2022 = tb.read_pdf(pdf, area = (160, 400, 220, 600), pages = '3', silent = True,)
print("                    Fall 2021")
print(fall2021)
print("\n")
print("                    Spring 2022")
print(spring2022)
print("\n")
print("                    Fall 2022")
print(fall2022)
