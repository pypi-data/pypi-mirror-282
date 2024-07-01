import asyncio
from pyppeteer import launch

import win32api, win32gui, win32con  # pip  install     pywin32  可能会出现问题_请看README_后端py.md

from ..fs.fs_find_file import fs_find_file
from ..win.win_find_name import win_find_name
from ..win.win_hide_taskbar import win_hide_taskbar

globals_show = ""


class SPIDER:
    def __init__(self, *args, **kwargs):
        self.show = "max"
        pass

    # 启动浏览器
    async def browser_start(self, show="max", desc="浏览器启动_位置全部隐藏", x=1, y=1):
        message = "启动浏览器了:"
        self.show = show
        executablePath = fs_find_file([r'C:\Program Files\Google\Chrome', r'C:\Users\Administrator\AppData\Local'], ["chrome.exe"])  ## chrome://version
        print("浏览器路径executablePath                 :", executablePath)
        opt_chrome = {
            "devtools": True,
            "userDataDir": r'C:\AAA_userDataDir',
            # "userDataDir": r'C:\Users\Administrator\Desktop\userdir',
            # "executablePath": r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe',  # 浏览器安装路径   chrome://version
            # 'executablePath': r'C:\Program Files\Google\Chrome\Application\chrome.exe',  # 浏览器安装路径   chrome://version
            # 'executablePath': r'C:\Users\Administrator\AppData\Local\360ChromeX\Chrome\Application\360ChromeX.exe',  # 浏览器安装路径   chrome://version
            "executablePath": executablePath,  # 浏览器安装路径   chrome://version
            "headless": False,  # 无头浏览器
            "dumpio": True,  # 减少内存消耗
        }

        opt_chrome["args"] = [
            "--mute-audio",  # 禁音
            '--no-sandbox',  # 关闭沙盒
            '--disable-gpu',  # 禁用 GPU 硬件加速
            # '--log-level=3',  # 日志等级
            '--disable-infobars',  # 禁用提示栏 --开启后页面加载不了
            '--start-maximized',
            '--window-size=1600,900',  # 屏幕大小
            f'--window-position={x},{y}',  # 桌面位置
            # '--blink-settings=imagesEnabled=false'  # 用图片加载
            '--disable-features=BlockingStylesheets'  # 禁用CSS加载
            '--disable-dev-shm-usage'  # 是一个用于解决Chrome/Chromium浏览器在某些特殊环境下启动问题的参数,通常会被添加到 pyppeteer 的启动参数中。
            "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        ]
        self.browser = await launch(opt_chrome)

        self.pages = await self.browser.pages()
        self.page = await self.browser.newPage()  # 初始化页面

        await self.page.setCacheEnabled(False)  # 禁用缓存
        self.web = self.page
        await self.web.setViewport({"width": 1920, "height": 1080})
        if self.show == "no": await self.browser_hide_taskbar()
        await self.web.evaluate('''() => { Object.defineProperty(navigator, 'webdriver', {get: () => undefined})}''')  # evaluateOnNewDocument
        zzz = 1

        message = "成功:" + desc + "      " + message
        print(message)
        return self

    # 隐藏任务栏
    async def browser_hide_taskbar(self):
        win = win_find_name("oog")
        if win:
            result = win_hide_taskbar(win["hwnd"])
            print("隐藏任务栏成功==browser_111hide_taskbar", f"result:{result}         ", win)
            return True
        else:
            raise ValueError(f"browser_hide_taskba111r 发现程序:oog        " + win)

    # 页面设置cookies_str
    async def web_set_cookies(self, desc="默认描述", cookies=""):
        message = "页面设置cookies_str了:"
        for ele in cookies:
            await self.web.setCookie(ele)
        message = "成功:" + desc + "      " + message
        print(message)
        # await asyncio.sleep(1)
        return self

    # 页面跳转
    async def web_goto(self, url="", desc="默认描述"):
        message = "页面跳转了:"
        await self.web.goto(url)
        if self.show == "no": await self.browser_hide_taskbar()
        await self.web.waitForSelector("html", timeout=10 * 1000)
        await self.web.evaluate('''() => { Object.defineProperty(navigator, 'webdriver', {get: () => undefined})}''')  # evaluateOnNewDocument
        await self.web.evaluate(""" document.title = 'web';  """)
        message = "成功:" + desc + "      " + message + url
        print(message)
        return self

    # 等待css元素
    async def web_await_css(self, css="body", desc="默认描述", timeout=10 * 1000):
        message = "等待了css元素:"
        await self.web.waitForSelector(css, timeout=timeout)
        await self.web.querySelector(css)
        message = "成功:" + desc + "      " + message + css
        print(message)
        return self

    # 点击css元素
    async def web_await_click(self, css="body", desc="默认描述", timeout=10 * 1000):
        message = "点击了css元素:"
        await self.web.waitForSelector(css, timeout=timeout)
        await self.web.click(css)
        message = "成功:" + desc + "      " + message + css
        print(message)
        return self

    # input上传文件
    async def web_await_input_files(self, css="body", desc="默认描述", files=[], timeout=10 * 1000):
        message = "input上传文件了:"
        await self.web.waitForSelector(css, timeout=timeout)
        input_element = await self.web.querySelector(css)
        await input_element.uploadFile(*files)
        message = "成功:" + desc + "      " + message + css
        print(message)
        return self

    # input输入文字
    async def web_await_input_text(self, css="body", desc="默认描述", text="hello world", timeout=10 * 1000):
        message = "input输入文字了:"
        await self.web.waitForSelector(css, timeout=timeout)
        await self.web.click(css)
        await self.web.type(css, text)
        await asyncio.sleep(0.1)
        message = "成功:" + desc + "      " + message + css
        print(message)
        return self

    # 出现css元素了关闭浏览器
    async def web_await_css_close_browser(self, desc="默认描述", css="body", timeout=10 * 1000):
        message = "出现css元素了关闭浏览器:"
        await self.web.waitForSelector(css, timeout=timeout)
        await self.browser.close()
        message = "成功:" + desc + "      " + message + css
        print(message)
        return self


# 启动浏览器窗口
async def spider_pyppeteer(show="max", desc="浏览器启动_位置全部隐藏", x=1, y=1):
    """ 启动浏览器窗口
        code
        # spider = await spider_pyppeteer()
        # spider = await __.spider.spider_pyppeteer(desc="全部显示位置",x=0, y=0)
        # spider = await __.spider.spider_pyppeteer(desc="全部隐藏位置",x=0, y=-900 + 2)
        spider = await __.spider.spider_pyppeteer(desc="一点隐藏位置", x=0, y=-900 + 100)
    """
    once = await SPIDER().browser_start(show=show, desc=desc, x=x, y=1)
    return once
