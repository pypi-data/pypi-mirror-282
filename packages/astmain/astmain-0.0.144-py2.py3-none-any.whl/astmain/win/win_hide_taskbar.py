import ctypes


def win_hide_taskbar(hwnd: int) -> None:
    """
    设置隐藏程序的任务栏


    code
    print("result                 :", wind_set_taskbar_hide("Goog"))
    """
    # 隐藏任务栏
    window_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)  # -16 代表 GWL_STYLE
    window_style &= ~0x10000000  # 清除 WS_VISIBLE 标志位
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, window_style)
    result = ctypes.windll.user32.SetWindowPos(hwnd, None, 100, -880, 0, 0, 0x0001)
    return result
    """
    好博客 https://blog.csdn.net/weixin_30314631/article/details/97574375
    hwnd 是要移动的窗口的句柄。
    hWndInsertAfter 设为 None 表示不改变窗口的插入顺序。
    x 和 y 设置为 100,表示将窗口的左上角移动到屏幕坐标 (100, 100)。
    cx 和 cy 设为 0 表示不改变窗口的大小。
    uFlags 设为 0x0001 表示只修改窗口的位置,不修改大小。
    """


if __name__ == '__main__':
    print("result                 :", win_hide_taskbar("Goog"))
