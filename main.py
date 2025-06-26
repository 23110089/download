def run():
    from os import system
    system('pip install aiofiles')
    system('curl -X GET "https://api.gofile.io/contents/c537fbd8-8b6d-40dd-93a3-d96504ad4459?wt=4fd6sg89d7s6&contentFilter=&page=1&pageSize=1000&sortField=name&sortDirection=1" -H "Authorization: Bearer bkDOYMgHSNGienr8qQ2Lz34QtJCIMclr"')
    system('wget --header="cookie: accountToken=bkDOYMgHSNGienr8qQ2Lz34QtJCIMclr" "https://store9.gofile.io/download/web/331c708d-8d84-447d-8347-a97fdf7b8ac4/disk.qcow2" -O disk.qcow2')
    print("Tải file disk.qcow2 thành công")

from threading import Thread
Thread(target=run).start()

from fastapi import FastAPI
from fastapi.responses import FileResponse
from os.path import exists

app = FastAPI()
@app.get("/")
def home(): return

@app.get("/download")
def download_file():
    file_path = f"./disk.qcow2"
    if exists(file_path):
        return FileResponse(
            path=file_path,
            filename='disk.qcow2',
            media_type='application/octet-stream'
        )
    return {"error": "File không tồn tại"}
