import os



def find_file(root_dir, filename):
    """在给定的根目录中搜索指定的文件名,并返回文件的绝对路径。 如果找到文件,返回文件路径;否则返回 None。 """
    file_path = os.path.join(root_dir, filename)
    if os.path.exists(file_path):
        return file_path
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.lower() == filename.lower():
                return os.path.join(dirpath, file)
    return None


def fs_find_file(dirs, filenames):
    """
    根据给定的目录列表和文件名列表,搜索并返回找到的第一个文件的绝对路径。
    如果找到任何文件,则返回文件的绝对路径,否则返回 None。

    示例:
    dirs = ['C:\\Program Files (x86)', 'C:\\Program Files', 'C:\\']
    filenames = ['chrome.exe', 'notepad.exe']
    file_path = fs_find_file(dirs, filenames)
    """
    for root_dir in dirs:
        for filename in filenames:
            file_path = find_file(root_dir, filename)
            if file_path is not None:
                # return file_path
                return file_path.replace('\\', '/')
    return None


def main():
    dirs = ['C:\\Program Files (x86)', 'C:/Program Files', 'C:/']
    filenames = ['chrome.exe']
    file_path = fs_find_file(dirs, filenames)
    if file_path:
        print(f'Found file at: {file_path}')
    else:
        print(f'Files not found.')


if __name__ == '__main__':
    main()

    # 不要使用列表推导式#不要使用lambda表达式#运行速度在快一点,我写好正文注释
    # 不要使用multiprocessing    进程的方式
    # 不要使用 async await       的方式
    # 帮我封装一下

    """






"""
