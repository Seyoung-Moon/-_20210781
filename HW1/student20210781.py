#!/usr/bin/python3
from openpyxl import load_workbook

wb = load_workbook('student.xlsx')
ws = wb.active

for row in ws.iter_rows(min_row=2, values_only=True):
    int total_score = row[6]
    if total_score < 40:
        grade = 'F'
    else:
        if total_score >= 90:
            grade = 'A+'
        elif total_score >= 80:
            grade = 'A'
        elif total_score >= 70:
            grade = 'B+'
        elif total_score >= 60:
            grade = 'B'
        elif total_score >= 50:
            grade = 'C+'
        else:
            grade = 'C'

    ws.cell(row=row[0], column=8, value=grade)

wb.save('student.xlsx')

