from odslib import ODS
def report():
    ods = ODS()

    # sheet title
    sheet = ods.content.getSheet(0)
    sheet.setSheetName('Totals')

    # title
    sheet.getCell(0,0).stringValue("Nice cool report").setFontSize('14pt')
    sheet.getRow(0).setHeight('18pt')
    sheet.getColumn(0).setWidth('10cm')

    # Cell1
    sheet.getCell(0,1).stringValue("Foo")
    sheet.getCell(1,1).floatValue(2)

    # Cell2
    sheet.getCell(0,2).stringValue("Bar")
    sheet.getCell(1,2).floatValue(3)

    # Cell3 with formula
    sheet.getCell(0,3).stringValue("Total").setBold(True)
    sheet.getCell(1,3).floatFormula(0,'=SUM(B2:B3)').setBold(True)

    # generando el archivo y guardando
    ods.save("archivo.ods")
report()
