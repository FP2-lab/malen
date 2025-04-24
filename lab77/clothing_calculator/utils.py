from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime

def save_to_excel(data, filename="clothing_report.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Clothing Report"
    
    headers = ["Дата", "Тип", "Размер", "Ткань (м)", "Стоимость", "Детали"]
    ws.append(headers)
    
    for cell in ws[1]:
        cell.font = Font(bold=True)
    
    for item in data:
        ws.append([
            item.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            item.get("type", ""),
            item.get("size", ""),
            item.get("fabric", ""),
            item.get("cost", ""),
            item.get("details", "")
        ])
    
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column_letter].width = adjusted_width
    
    wb.save(filename)
    return filename