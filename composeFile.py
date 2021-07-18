import codecs
import os

import chardet as chardet

path=r'D:\Code\getShengYanCollection\newfiles'

def read_files_name(path):
    files_name_list=[]
    for _,_,files in os.walk(path):
        files_name_list=files
    return files_name_list


files_name_list=read_files_name(path)
# print(chardet.detect(open(path+'/'+'印顺长老著述中的真常唯心论以《大乘起信论讲记》为主.txt', 'rb').read())['encoding'])

# for file_name in files_name_list:
#     encoding = chardet.detect(open(path+'/'+file_name, 'rb').read())['encoding']
#     print(file_name)
#     if encoding=='utf-8':
#         with open(path+'/'+file_name,'r',encoding='utf8') as f_read:
#             article=f_read.read()+'\n'
#             with open('圣严法师文集1.txt','a',encoding='utf8') as f_write:
#                 f_write.write('○○○'+file_name.split('.')[0]+'\n\n\n')
#                 f_write.write(article)
#     elif encoding == 'ANSI':
#         with open(path + '/' + file_name, 'r', encoding='ANSI') as f_read:
#             article = f_read.read()+'\n'
#             with open('圣严法师文集1.txt', 'a',encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0]+'\n\n\n')
#                 f_write.write(article)
#     elif encoding == 'UTF-16':
#         with open(path + '/' + file_name, 'r', encoding='UTF-16') as f_read:
#             article = f_read.read()
#             with open('圣严法师文集1.txt', 'a', encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0] + '\n\n\n')
#                 f_write.write(article)
#     elif encoding == 'UTF-8-SIG':
#         with open(path + '/' + file_name, 'r', encoding='UTF-8-SIG') as f_read:
#             article = f_read.read()
#             with open('圣严法师文集1.txt', 'a', encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0] + '\n\n\n')
#                 f_write.write(article)
#     elif encoding == 'GB2312':
#         with open(path + '/' + file_name, 'r', encoding='GB2312') as f_read:
#             article = f_read.read()
#             with open('圣严法师文集1.txt', 'a', encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0] + '\n\n\n')
#                 f_write.write(article)
#     elif encoding == 'ASCII':
#         with open(path + '/' + file_name, 'r', encoding='ASCII') as f_read:
#             article = f_read.read()
#             with open('圣严法师文集1.txt', 'a', encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0] + '\n\n\n')
#                 f_write.write(article)
#     elif encoding == 'ISO-8859-1':
#         with open(path + '/' + file_name, 'r', encoding='ISO-8859-1') as f_read:
#             article = f_read.read()
#             with open('圣严法师文集1.txt', 'a', encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0] + '\n\n\n')
#                 f_write.write(article)
#
#
#     elif encoding == 'GB18030':
#         with open(path + '/' + file_name, 'r', encoding='gbk') as f_read:
#             article = f_read.read()
#             with open('圣严法师文集1.txt', 'a', encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0] + '\n\n\n')
#                 f_write.write(article)
#     elif encoding == 'UNICODE':
#         with open(path + '/' + file_name, 'r', encoding='UNICODE') as f_read:
#             article = f_read.read()
#             with open('圣严法师文集1.txt', 'a', encoding='ANSI') as f_write:
#                 f_write.write('○○○' + file_name.split('.')[0] + '\n\n\n')
#                 f_write.write(article)
#     else:
#         with open(path+'/'+file_name,'r','ignore') as f_read:
#             article=f_read.read()+'\n'
#             with open('圣严法师文集1.txt','a',encoding='utf8') as f_write:
#                 f_write.write('○○○'+file_name.split('.')[0]+'\n\n\n')
#                 f_write.write(article)



for file_name in files_name_list:
    encoding = chardet.detect(open(path+'/'+file_name, 'rb').read())['encoding']
    file= codecs.open(path + '/' + file_name, 'r',encoding)
    content=file.read()
    file.close()
    print(file_name)
    try:
        with open('圣严法师文集_全.txt', 'a', encoding="utf-8") as f_write:
            f_write.write('\n\n\n○○○' + file_name.split('.')[0]+'\n\n\n')
            f_write.write(content)
    except Exception as e:
        print(e)
