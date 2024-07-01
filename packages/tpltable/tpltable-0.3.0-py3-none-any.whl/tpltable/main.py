from ffre import FileFinder, FCollect
from tpltable.excel import Excel, Table
from tpltable.style import *
DIR_PATH = r"C:\Users\22290\Desktop\20240504整理\tpltable 数据"

xlsx_paths:FCollect = FileFinder(DIR_PATH).find("xlsx", pattern=".+线$", exclude="^~")


# e = Excel()
#
# t = e.append(Table(
#     [[0],
#     [4, 5, 6, 7],
#     [8, 9, 10, 11],
#     [12, 13, 14, 15]])
# )
#
# t.styles.set(TYPE_HALIGN, 'center')  # 设置水平居中
# t.styles['A2', 'D3'].set(TYPE_COLOR, 'FF0000')  # 设置红色前景色
# t.styles['A:D'].set(TYPE_FONT_TYPE, 'Arial')  # 设置字体
# t.styles['A1:D4'].set(TYPE_FONT_SIZE, 20)  # 设置字号
# t.styles['A1'].set(TYPE_COL_WIDTH, 40)  # 设置列宽
# t.styles[:, 1].set(TYPE_BCOLOR, COLOR_LIGHTGRAY)  # 设置浅灰色背景色
# t.merge("A1:D1")  # 合并单元格

e = Excel('test.xlsx')
t = e[0]

del t['A']

del t['B1', 'C2']

e.save()






