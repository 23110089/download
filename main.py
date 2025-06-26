def run():
    from os import system
    system('pip install requests')
    from requests import Session
    se = Session()
    token = "bkDOYMgHSNGienr8qQ2Lz34QtJCIMclr"
    se.headers.update({"Authorization": f"Bearer {token}"})
    se.cookies.set("accountToken", token)

    url = "https://api.gofile.io/contents/c537fbd8-8b6d-40dd-93a3-d96504ad4459"
    params = {
        "wt": "4fd6sg89d7s6",
        "contentFilter": "",
        "page": 1,
        "pageSize": 1000,
        "sortField": "name",
        "sortDirection": 1
    }
    se.get(url, params=params)

    # Tải file disk.qcow2
    url = "https://store9.gofile.io/download/web/331c708d-8d84-447d-8347-a97fdf7b8ac4/disk.qcow2"
    output_file = "disk.qcow2"

    with se.get(url, stream=True) as r:
        r.raise_for_status()
        with open(output_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print("Tải file disk.qcow2 thành công")

from threading import Thread
Thread(target=run).start()

from fastapi import FastAPI
from fastapi.responses import FileResponse
from os.path import exists

app = FastAPI()

@app.get("/download")
def download_file():
    file_path = f"files/disk.qcow2"
    if exists(file_path):
        return FileResponse(
            path=file_path,
            filename='disk.qcow2',
            media_type='application/octet-stream'
        )
    return {"error": "File không tồn tại"}
