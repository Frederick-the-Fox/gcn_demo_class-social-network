import xlrd

excel_path = "./data.xlsx"
 
file = 'class.cites'

#打开文件，获取excel文件的workbook（工作簿）对象
excel = xlrd.open_workbook(excel_path,encoding_override="utf-8")

#获取sheet对象
sheet = excel.sheets()[0]
 
sheet_row_mount = sheet.nrows
sheet_col_mount = sheet.ncols
 
print("row number: {0} ; col number: {1}".format(sheet_row_mount, sheet_col_mount))

#每一行数据写一行content
with open (file,'a') as file_object:
    for x in range(1, sheet_row_mount):
        print('-----------x is', x)
        y = 8
        while y < sheet_col_mount:
            print ('y is', y)
            if (sheet.cell_value(x,y) == ''): break
            else:
                file_object.write(str(int(sheet.cell_value(x,0))))
                file_object.write('\t')
                file_object.write(str(int(sheet.cell_value(x,y))))
                file_object.write('\n')
                y += 1
    print('finished')