import os
import os


def show_files(path, _type):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    file_list.sort()
    length = file_list.__len__()

    for i in range(length):
        if i == 0:continue
        if file_list[i][-_type.__len__():] != _type:
            file_list.insert(0, file_list[i])
            del file_list[i+1]
    for i in range(length):
        if file_list[i] == "index.html":
            file_list.insert(0, file_list[i])
            del file_list[i+1]
            break


    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        index = open("{}/index.html".format(path), "a")

        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            insert = "<a href= {}> {} </a>".format(file, file)
            index.write(insert)
            index.write("<br>\n")
            show_files(cur_path, _type)
        else:
            insert = "<a href= {}> {} </a>".format(file, file)
            index.write(insert)
            index.write("<br>\n")

def clean(path):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    open("{}/index.html".format(path), "w")

    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)

        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            clean(cur_path)


if __name__ == '__main__':

    papers = "./papers"
    clean(papers)
    show_files(papers, ".html")

    algorithm = "./papers/html"
    clean(algorithm)
    show_files(algorithm, ".html")

    papers = "./papers/pdf"
    clean(papers)
    show_files(papers, ".pdf")

    print("end")