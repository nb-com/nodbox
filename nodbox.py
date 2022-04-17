import os
import sys
import time
from threading import Thread
import webview

port=8889

def start_webview():
    window = webview.create_window('Nodbox', f'http://localhost:{port}/', confirm_close=True, width=900, height=600)
    webview.start()
    window.closed = os._exit(0)


def startApp():
    if sys.platform in ['win32', 'win64']:
        os.system("python manage.py runserver {}:{}".format('127.0.0.1', port))
        
    else:
        os.system("python3 manage.py runserver {}:{}".format('127.0.0.1', port))
       


if __name__ == '__main__':
    Thread(target=startApp).start()
    start_webview() 