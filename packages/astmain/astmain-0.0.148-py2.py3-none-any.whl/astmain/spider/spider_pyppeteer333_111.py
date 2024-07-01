import asyncio
import datetime
from multiprocessing import freeze_support

from pyppeteer import launch

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
        opt = dict(
            title="title333小许" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            content="content333",
            files=[r"C:\Users\Administrator\Desktop\111.png", r"C:\Users\Administrator\Desktop\222.png"],
            cookies_str="""[
    {
        "name": "abRequestId",
        "value": "8c000796-7b13-5489-b50a-323172dea808",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1750573302.787641,
        "sameSite": "unspecified"
    },
    {
        "name": "a1",
        "value": "1903e9b9990f0a0g9zdck8w46x6qxkhtwbuxh7vhd50000162929",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1750573303,
        "sameSite": "unspecified"
    },
    {
        "name": "webId",
        "value": "6e5373c836a5fafd6ebec9da5931c12d",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1750573303,
        "sameSite": "unspecified"
    },
    {
        "name": "gid",
        "value": "yj8qdjD0qYEJyj8qdjDjjDWhj8i808kjufST7xfYE4KCKC28ACTx9x888yKJjJj8dKWfyiK8",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1754124806.455951,
        "sameSite": "unspecified"
    },
    {
        "name": "acw_tc",
        "value": "3e6c448464d52b812766be662eb810c66f346f0190814a4164de89721b4fa235",
        "domain": "www.xiaohongshu.com",
        "hostOnly": true,
        "path": "/",
        "secure": false,
        "httpOnly": true,
        "session": false,
        "expirationDate": 1719566551.747954,
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
        "name": "web_session",
        "value": "0400698e30a4ad561bd286314b344b5739cce4",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": true,
        "httpOnly": true,
        "session": false,
        "expirationDate": 1751100783.717251,
        "sameSite": "unspecified"
    },
    {
        "name": "unread",
        "value": "{%22ub%22:%226676f2e3000000001d01b468%22%2C%22ue%22:%226679108c000000001f007ed8%22%2C%22uc%22:30}",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": true,
        "sameSite": "unspecified"
    },
    {
        "name": "websectiga",
        "value": "7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1719823990,
        "sameSite": "unspecified"
    },
    {
        "name": "sec_poison_id",
        "value": "37025440-4d43-4a20-a7cd-b4a0d2a3348e",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1719565395,
        "sameSite": "unspecified"
    },
    {
        "name": "galaxy_creator_session_id",
        "value": "qhvQEnEHXSJ8QXXyzWlcIwkieFxxviFTXcv3",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1720169604.780629,
        "sameSite": "unspecified"
    },
    {
        "name": "galaxy.creator.beaker.session.id",
        "value": "1719564804173011837940",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1720169604.780666,
        "sameSite": "unspecified"
    },
    {
        "name": "xsecappid",
        "value": "creator-creator",
        "domain": ".xiaohongshu.com",
        "hostOnly": false,
        "path": "/",
        "secure": false,
        "httpOnly": false,
        "session": false,
        "expirationDate": 1751100805,
        "sameSite": "unspecified"
    }
]""",
        )

        opt["cookies"] = __.to_json(opt["cookies_str"])
        spider = await __.spider.spider_pyppeteer(desc="全部显示位置", x=0, y=0)
        # spider = await __.spider.spider_pyppeteer(desc="全部隐藏位置",x=0, y=-900 + 2)
        # spider = await __.spider.spider_pyppeteer(desc="一点隐藏位置", x=0, y=-900 + 100)
        # await spider.web_set_cookies(desc="小红书设置cookies", cookies=opt["cookies"])
        await spider.web_set_cookies(desc="小红书设置cookies", cookies=opt["cookies"])
        await spider.web_goto(desc="小红书首页home", url="https://creator.xiaohongshu.com")
        await spider.web_goto(desc="小红书发布页面", url="https://creator.xiaohongshu.com/publish/publish")
        await spider.web_await_click(desc="上传按钮", css=".tab:nth-child(2)")
        await spider.web_await_input_files(desc="上传完图片", css=".upload-input", files=opt["files"])
        await spider.web_await_input_text(desc="输入标题", css=".titleInput .el-input__wrapper .el-input__inner", text=opt["title"])
        await spider.web_await_input_text(desc="输入描述", css=".topic-container", text=opt["content"])
        await spider.web_await_click(desc="权限设置_私密", css=".el-radio__label")
        await spider.web_await_click(desc="点击发布按钮", css=".publishBtn")
        # await __.tool_await(0.1)
        # await __.tool_await(9999)
        await spider.web_await_css_close_browser(desc="完美!!!发布成功", css=".btn-content")


    asyncio.get_event_loop().run_until_complete(aaa())
