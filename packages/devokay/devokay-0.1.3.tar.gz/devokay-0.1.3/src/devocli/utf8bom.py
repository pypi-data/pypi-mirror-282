# -*- coding: UTF-8 -*-
# python3

import os
import chardet # /opt/anaconda3/envs/py312/lib/python3.12/site-packages
import codecs

'''
utf8bom

@brief 扫描指定/当前目录，将 .h, .c, .cc, .cpp 文件转为 UFT8 with BOM
'''

def __detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            confidence = result['confidence']

            print(f"文件 '{file_path}' 的编码是 '{encoding}'，置信度为 {confidence}")

            if confidence >= 0.99:
                # 文件编码转换为 UTF-8 with BOM
                try:
                    content = raw_data.decode(encoding)
                    with codecs.open(file_path, 'w', 'utf-8-sig') as f_out:
                        f_out.write(content)
                    print(f"文件 '{file_path}' 已转换为 UTF-8 with BOM 编码")
                except Exception as e:
                    print(f"文件 '{file_path}' 转换时出现错误: {str(e)}")
    except Exception as ex:
        print(f"检测文件编码时出现异常: {str(ex)}")

def __scan_files(target_dir, file_suffixes): # 遍历文件夹
    file_cnt = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file) # 获取文件的完整路径
            for suffix in suffixes: # 检查文件后缀是否在指定的后缀数组中
                if file.endswith(suffix):
                    file_cnt += 1

                    print(f'[{file_cnt} ]path: {file_path}')

                    __detect_encoding(file_path)

class Utf8bomCmd:
    def __init__(self):
        pass

    def regist(self, subparsers):
        parser = subparsers.add_parser('utf8bom', help='文件编码转存UTF8-BOM')
        parser.add_argument('-d', '--dir', type=str, default='.', help='文件夹路径')
        parser.add_argument('-s', '--suffix', type=str, default='h,hpp,c,cc,cpp', help='文件后缀')
        parser.set_defaults(handle=Utf8bomCmd.handle)

    @classmethod
    def handle(cls, args):
        __scan_files(args.dir)

    
if __name__ == '__main__':
    folder_path = '/Users/fallenink/Desktop/Developer/pc-launcher'  # 替换为实际的文件夹路径
    suffixes = ['.h', '.hpp', '.c', '.cc', '.cpp']   # 后缀数组，可以添加需要匹配的后缀

    __scan_files(folder_path, suffixes)