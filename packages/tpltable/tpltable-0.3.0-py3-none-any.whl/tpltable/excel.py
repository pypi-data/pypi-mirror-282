import numpy as np
import pandas as pd
from tpltable.table import *
from tpltable.style import *

class ExcelFileIOException(Exception):
    pass

class Excel(dict):
    def __init__(self, fpath:str=None, *, style:bool=True):
        """
        *Create an Excel object from an excel file or empty
        :param fpath: excel file path. If None, will create an empty Excel object.
        *
        :param style: bool. If True, will load the style of the cell(may be cost). Default is True.
        """
        self._path = fpath
        if self._path:
            # try:
                wb = load_workbook(fpath)
                tbls = {sheet.title: self.__table_from_sheet(sheet, only_data=not style) for sheet in wb.worksheets}
                wb.close()
            # except Exception as e:
            #     raise ExcelFileIOException("\n\nFatal to load excel file: \n" + reinsert_indent(str(e), '\t'))
        else:
            tbls = {}

        super().__init__(tbls)

        # 添加数字索引
        self.numbers = {i: tbl for i, (name, tbl) in enumerate(tbls.items())}

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.numbers[item]
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if isinstance(key, int):
            key = list(self.keys())[key]
        super().__setitem__(key, value)

    def __delitem__(self, key):
        if isinstance(key, int):
            key = list(self.keys())[key]
            del self.numbers[key]
        super().__delitem__(key)


    def __table_from_sheet(self, sheet:Worksheet, only_data:bool=False):
        _construct_2d_list = []
        _merges = [_merge.coord for _merge in sheet.merged_cells.ranges]

        if only_data:
            _styles = None
            for row in sheet.iter_rows():
                _construct_2d_list.append([cell.value if cell.value else NaN for cell in row])
        else:
            _styles = []
            for row in sheet.iter_rows():
                _construct_2d_list.append([cell.value if cell.value else NaN for cell in row])
                _styles.append([Style(sheet, cell) for cell in row])


        return Table(_construct_2d_list, _styles, _merges, copy=False)

    @property
    def path(self):
        return self._path

    @property
    def tables(self):
        return list(self.values())

    @staticmethod
    def __simple_str(string, max:int=20):
        _len = len(string)
        assert max > 4, "Max length should be greater than 4."
        if _len > max:
            _half = max // 2 - 1
            return f"{string[:9]}...{string[_len-9:]}"
        return string

    def __repr__(self):
        return f"Excel({self.__simple_str(self._path)}|{len(self)} tables)"

    def __str__(self):
        _txt = f"Excel({self.__simple_str(self._path)}|{len(self)} tables)\t" + '{\n'
        _MAX_SIZE = 16 - 2

        # Max length key
        keys = [k for k in self.keys()]
        max_len_key = max([len(key) for key in keys])
        _MAX_SIZE = min(_MAX_SIZE, max_len_key) + 2
        max_len_key = max(max_len_key, _MAX_SIZE)

        for name, tbl in self.items():
            name = self.__simple_str(name, _MAX_SIZE)
            _left_space = ' ' * (max_len_key - len(name))
            _txt += f"\t'{name}'{_left_space}: {tbl.__repr__()},\n"
        _txt += '}'
        return _txt

    def append(self, tbl:Table, name:str=None):
        if name is None:
            name = f"sheet{len(self)}"
            while name in self:
                name = '_' + name
        self.numbers[len(self)] = tbl
        self[name] = tbl
        return tbl


    def detail(self) -> str:
        _txt = f"Excel({self.__simple_str(self._path)}|{len(self)} tables)\t" + '{\n'
        _MAX_SIZE = 16 - 2

        for name, tbl in self.items():
            _sub_txt = color_string(f"\tTable '{name}'") + " >\n" + reinsert_indent(str(tbl), '\t\t')
            _txt += _sub_txt + '\n\n'

        if len(self) > 0:
            _txt = _txt[:-1]
        _txt += '}'

        return _txt

    def save(self, fpath:str=None, *, style:bool=True):
        """
        *Save the Excel object to an excel file.
        :param fpath:
        *
        :param style: bool. If True, will save the style of the cell. Default is True.
            NOTE: if use, will slower 20X and more
        :return:
        """
        wb = Workbook()
        for name, tbl in self.items():
            ws = wb.create_sheet(name)
            for row in tbl:
                _row = []
                for value in row:
                    # if nan, set to None
                    if isnan(value):
                        _row.append(None)
                    else:
                        _row.append(value)
                ws.append(_row)

            # Merge
            for merge in tbl.merges:
                ws.merge_cells(f"{merge[0].letter}:{merge[1].letter}")

            # Style
            if style and tbl.styles is not None:
                style_tbl = tbl.styles
                for i, row in enumerate(ws.iter_rows()):
                    for j, cell in enumerate(row):
                        style_tbl[i][j].apply(ws, cell)

        # remove the default sheet
        wb.remove(wb.active)

        if not fpath:
            fpath = self._path
        if not fpath:
            raise ExcelFileIOException("\n\nNo file path defined: " + str(self))

        try:
            wb.save(fpath)
        except Exception as e:
            raise ExcelFileIOException("\n\nFatal to save excel file: \n" + reinsert_indent(str(e), '\t'))
        wb.close()


if __name__ == '__main__':
    from ffre import FileFinder
    fdir = r"C:\Users\22290\Desktop\20240504整理\tpltable 数据"
    ff = FileFinder(fdir)
    fpaths = list(ff.find(".xlsx"))

    if not fpaths:
        print("No excel file found.")
        exit(0)

    fp = fpaths[1]
    _t = TimeRecorder()
    for i in range(1):
        excel = Excel(fp, style=False)
    print("Load excel without style cost:", _t.dms(1), "ms")
    _t.tick()
    for i in range(1):
        excel = Excel(fp, style=True)
    print("Load excel with style cost:", _t.dms(1), "ms")

    excel[0].styles['A1'][TYPE_COL_WIDTH] = 200

    print(excel)
    _t.tick()
    excel.save("test.xlsx", style=False)
    print("Save excel without style cost:", _t.dms(1), "ms")
    _t.tick()
    excel.save("test_style.xlsx", style=True)
    print("Save excel with style cost:", _t.dms(1), "ms")




