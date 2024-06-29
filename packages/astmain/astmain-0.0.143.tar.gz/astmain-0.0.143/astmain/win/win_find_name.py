import win32gui
import win32con


def win_find_name(name) -> dict:
    """ 通过标题名称获取程序窗口数据 nane
        code  :
        print("win                 :", win_find_name("Postman111"))

    """
    windows = []

    def callback(hwnd, param):
        title = win32gui.GetWindowText(hwnd)
        name_class = win32gui.GetClassName(hwnd)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        if (name in title):
            obj1 = dict(title=title, name_class=name_class, hwnd=hwnd, left=left, right=right, top=top, bottom=bottom, style=style)
            windows.append(obj1)
        return True

    win32gui.EnumWindows(callback, None)

    if len(windows) >= 1:
        return windows[0]
    else:
        return None


if __name__ == '__main__':
    print("win                 :", win_find_name("Postman"))
