import xlrd

excel_path = "./data.xlsx"
 
file = 'class.content'

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
        num_count = 0
        print('---------------x is ', x)
        file_object.write(str(int(sheet.cell_value(x, 0))))
        file_object.write('\t')
        y = 1
        while y < 7:
            print('y is ', y)
            n = int(sheet.cell_value(x,y))
            print('n is ', n)
            b = []  # 存储余数
            while True:  # 一直循环，商为0时利用break退出循环
                s = n // 2  # 商
                z = n % 2  # 余数
                b = b + [z]  # 每一个余数存储到b中
                if s == 0:
                    break  # 余数为0时结束循环
                n = s
            b.reverse()  # 使b中的元素反向排列
            b = [ str(i) for i in b ]
            for each in b:
                file_object.write(str(each))
                num_count += 1
                file_object.write('\t')
            y += 1
        print ('num_count is', num_count)
        for i in range(66 - num_count):
            file_object.write(str(0))
            file_object.write('\t')
        file_object.write(str(int(sheet.cell_value(x, 5))))
        file_object.write('\n')
    print('finished')