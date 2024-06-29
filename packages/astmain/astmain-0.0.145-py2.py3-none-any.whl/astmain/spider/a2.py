import asyncio
from pyppeteer import launch


async def start_browser():
    browser = await launch(
        headless=False,  # 设置为 False 可以看到浏览器界面
        args=["--no-sandbox", "--disable-gpu"]
    )
    return browser


from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get("/test1", response_class=HTMLResponse)
async def index():
    browser = await start_browser()
    page = await browser.newPage()
    await page.goto("https://www.example.com")
    html = await page.content()
    await browser.close()
    return html


if __name__ == '__main__':
    # 该方法作用是阻止子进程运行其后面的代码 ----
    import uvicorn
    print("url             http://127.0.0.1:9999/docs          ")
    print("url             http://127.0.0.1:9999/static/logo.png            ")
    print("url             http://127.0.0.1:9999/main?num=1              ")
    print("url             http://127.0.0.1:9999/xiaohongshu?num=1              ")

    # ------------------------------------
    # uvicorn.run("main:app", host='0.0.0.0', port=9999, reload=True, workers=1)
    # uvicorn.run(app, host='0.0.0.0', port=9999, reload=True, workers=1)
    uvicorn.run(app, host='0.0.0.0',  port=9999, reload=True, workers=1)
    # thread.join()
    # uvicorn.run("p1:app", host='0.0.0.0', port=9999, reload=False)

