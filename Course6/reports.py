#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])

def generate_reports(filename, title, para):
  elements = []
  i=0

  # Open the model report
  file=open(para)
  infile   = file.read()
  report_paragraphs = infile.split("\n")
  
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  elements.append(report_title)
  empty_line = Spacer(1, 0)
  elements.append(Spacer(1,2))
  for param in report_paragraphs:
    elements.append(Paragraph(param, styles["BodyText"]))
    i=i+1
    if i%2 ==0 :
      elements.append(empty_line)
      elements.append(empty_line)

  print(elements)
  #report_info = Paragraph(para, styles["BodyText"])

  report.build(elements)
