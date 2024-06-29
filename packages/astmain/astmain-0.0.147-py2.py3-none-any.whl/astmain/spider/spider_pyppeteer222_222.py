import asyncio
import datetime
from multiprocessing import freeze_support

from pyppeteer import launch

import win32api, win32gui, win32con  # pip  install     pywin32  可能会出现问题_请看README_后端py.md

__ = None

import astmain_py777.astmain as __  # 本地包


def my_set_win_taskbar_hide():
    exe1 = __.win_find_name("oog")
    if exe1:
        print("有找到程序 exe1                 :", exe1)
        hwnd = exe1["hwnd"]
        result = __.win_hide_taskbar(hwnd)
        print("result                 :", result)
        result if print("成功:隐藏了程序_任务栏") else print("失败:未隐藏程序_任务栏")
    else:
        print("没找到程序 exe1                 :", exe1)


if __name__ == '__main__':
    async def aaa():
        pass
        opt = dict(
            title="title222小许" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            text="text2222",
            files=[r"C:\Users\Administrator\Desktop\111.png", r"C:\Users\Administrator\Desktop\222.png"],
            cookies_str="""[
    {
        "name": "abRequestId",
        "value": "a376129c-d49b-5bbc-a8f4-170cc4bfe129",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1751043092.862638,
        "sameSite": "unspecified"
    },
    {
        "name": "a1",
        "value": "1905a9c0831wg416b0zniax0jqghkn390f4cocqpf50000243666",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1751043093,
        "sameSite": "unspecified"
    },
    {
        "name": "webId",
        "value": "6e110199fae6482d9b9f8ba843732d83",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1751043093,
        "sameSite": "unspecified"
    },
    {
        "name": "websectiga",
        "value": "984412fef754c018e472127b8effd174be8a5d51061c991aadd200c69a2801d6",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1719771432,
        "sameSite": "unspecified"
    },
    {
        "name": "gid",
        "value": "yj820jSJyW8Dyj820jS8YiSAqyEk4yKD8uI34Ui0C8VAkS28xTIqjl888J4qKKK8yKqfJWW8",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1754072239.355501,
        "sameSite": "unspecified"
    },
    {
        "name": "xsecappid",
        "value": "xhs-pc-web",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1751048236,
        "sameSite": "unspecified"
    },
    {
        "name": "acw_tc",
        "value": "34c2c09702979dbc55eba1576545febc0fddd0a0fc0f0b928dd2a4fd5803e004",
        "domain": "www.xiaohongshu.com",
        "hostOnly": true,
        "path": "/",
        "secure": false,
        "httpOnly": true,
        "session": false,
        "expirationDate": 1719514031.519517,
        "sameSite": "unspecified"
    },
    {
        "name": "webBuild",
        "value": "4.23.1",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": true,
        "sameSite": "unspecified"
    },
    {
        "name": "sec_poison_id",
        "value": "3116f21d-6593-4b6a-a780-3ff76159bc1f",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1719512837,
        "sameSite": "unspecified"
    },
    {
        "name": "web_session",
        "value": "0400698e30a4ad561bd2d4e448344b3da94447",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": true,
        "httpOnly": true,
        "session": false,
        "expirationDate": 1751048248.987734,
        "sameSite": "unspecified"
    },
    {
        "name": "unread",
        "value": "{%22ub%22:%2266798188000000001e013457%22%2C%22ue%22:%22667d734b000000001c02806a%22%2C%22uc%22:25}",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": true,
        "sameSite": "unspecified"
    }
]""",
        )

        num = 0
        opt = __.to_obj_dict(opt)

        # spider = await spider_pyppeteer()
        # spider = await __.spider.spider_pyppeteer(**dict( x=300, y=1))
        # spider = await __.spider.spider_pyppeteer(**dict(x=0, y=-900 + 2))
        spider = await __.spider.spider_pyppeteer(**dict(x=-10, y=-900 + 999))
        page = spider.page
        # cookies登陆
        # await spider.web_goto_set_cookie("https://creator.xiaohongshu.com/publish/publish", __.to.JSON(opt.cookies_str))
        await spider.web_goto_set_cookie("https://creator.xiaohongshu.com", __.to.JSON(opt.cookies_str))
        await asyncio.sleep(0.5)
        await spider.web_goto("https://creator.xiaohongshu.com/publish/publish")
        for ele in range(10):
            await asyncio.sleep(1)
            print("循环ele                 :", ele + 1)

        my_set_win_taskbar_hide()
        print( "cookies登陆url                 :", 111)
        await __.tool_await(1)

        # 点击发布图文_上传图片
        await spider.web_await_click(css=".tab:nth-child(2)")
        await spider.web_await_input_files(css=".upload-input", files=opt.files)

        print( "点击发布图文_上传图片                 :")

        # 输入标题
        await spider.web_await_input_text(css=".titleInput .el-input__wrapper .el-input__inner", text=opt.title)

        print("输入标题                 :")

        # 输入描述
        await spider.web_await_input_text(css=".topic-container", text=opt.text)
        print( "输入描述                 :")

        # 添加地点
        pass

        # 权限设置_私密
        await spider.web_await_click(css=".el-radio__label",desc="111")

        print( "权限设置_私密                 :")

        # 发布_按钮点击
        await spider.web_await_click(css=".publishBtn")
        num += 1
        print(num, "发布_按钮点击                 :")

        # 判断_是否_成功
        await spider.web_await_css(css=".btn-content")
        html = await page.content()
        num += 1
        print(num, "成功:发布内容---xiaohongshu")

        await __.tool_await(0.1)
        await __.tool_await(9999)
        await spider.browser.close()
        print("成功:关闭浏览器---xiaohongshu")


    asyncio.get_event_loop().run_until_complete(aaa())
