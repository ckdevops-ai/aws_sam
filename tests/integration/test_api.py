import requests
import time
import subprocess
import sys

def test_local_api():
    # 启动 sam local api（后台）
    proc = subprocess.Popen([
        "sam", "local", "start-api", "--port", "3001"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(5)  # 等待启动

    try:
        resp = requests.get("http://127.0.0.1:3001/hello")
        assert resp.status_code == 200
        assert "hello world" in resp.text
    finally:
        proc.terminate()
        proc.wait()
