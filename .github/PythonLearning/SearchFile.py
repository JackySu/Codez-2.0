import os


def main():
    str = input('输入查询字符串：')
    path_name = input('输入查询路径（默认为工作路径）:')
    if path_name == '':
        path_name = '.'  # 给懒癌患者一个交代
    minus = len(path_name)

    def list_file(str, path):
        list_all = os.listdir(path)
        for name_f in list_all:
            path_c = os.path.join(path, name_f)
            if os.path.isfile(path_c) and str in os.path.splitext(name_f)[0]:
                print(path_c[minus:])  # 把路径前缀去掉
            elif os.path.isdir(path_c):
                list_file(str, path_c)

    list_file(str, path_name)


if __name__ == '__main__':
    main()
