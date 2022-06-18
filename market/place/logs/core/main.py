import socket
from urllib import request
from db import DB
import app
from server import Marketplace
import json

IP = None

def start_server():
    global IP
    IP = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[1] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((str(IP), 2000))
    server.listen(10)

    print("-"*20)
    print(f"current IP address: {str(IP)}")
    print("-"*20)

    source_css = ""
    with open("private/css/style.css", "r") as css:
        source_css = css.read()
        source_css = source_css.replace("WHERE_MY_IP", str(IP))
    

    with open("css/style.css", "w") as css:
        css.write(source_css)

    source = ""
    with open("private/index.html", "r") as handle:
        source = handle.read()
        source = source.replace("WHERE_MY_IP",str(IP))
        source = source.replace("WHERE_MY_CSS", source_css)

    with open("index.html", "w") as handle:
        handle.write(source)
    

    
    with open("private/js/script.js", "r") as handle:
        source = handle.read()
        source = source.replace("WHERE_MY_IP",str(IP))

    with open("js/script.js", "w") as handle:
        handle.write(source)

    with open("private/js/loadNFTs.js", "r") as handle:
        source = handle.read()
        source = source.replace("WHERE_MY_IP",str(IP))

    with open("js/loadNFTs.js", "w") as handle:
        handle.write(source)

         
    try:
        while True:
            try:
                client_socket, address = server.accept()

                data = client_socket.recv(1024).decode("utf-8")
                content = load_page(data)

                client_socket.send(content)

                client_socket.shutdown(socket.SHUT_WR)
            except:
                print("server-client error")
    except:
        print("server error")



def loadMarketPlace():
    global IP
    marketplace_data = Marketplace()
    images_link = []
    datas = marketplace_data.load()
    for i in range(len(datas)):
        images_link.append(marketplace_data.image_by_id(datas[i][0]))
    
    cs = "<ul class='market-list'>"
    # Тут заполняем наш список
    for i in images_link:
        cs += "<li>"
        cs += f"<img src='http://WHERE_MY_IP:2000{i}/'>".replace("WHERE_MY_IP", str(IP))
        cs += "<input type='button' class='buer' value='bue'>"
        cs += "</li>"
    cs += "</ul>"
    return cs

def loadMarketPlaceAccount():
    global IP
    marketplace_data = Marketplace()
    images_link = []
    datas = marketplace_data.loadAccount()
    for i in range(len(datas)):
        images_link.append(marketplace_data.image_by_id(datas[i][0]))
    
    cs = "<ul class='market-list'>"
    # Тут заполняем наш список
    for i in images_link:
        cs += "<li>"
        cs += f"<img src='http://WHERE_MY_IP:2000{i}/'>".replace("WHERE_MY_IP", str(IP))
        cs += "<input type='button' class='sole' value='sole'>"
        cs += "</li>"
    cs += "</ul>"
    return cs

def loadLoginIn():
    with open("private/login_in.html", "r") as handle:
        source = handle.read()
    with open("private/js/login.js", "r") as handle:
        source += f"<script>{handle.read()}</script>"
    return source


def load_page(data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n'
    path = data.split("/")[1]
    response = ''
    print(path)
    if path=="main" or path=="":
        with open("index.html", "r") as file:
            response = file.read()
        response = response.replace("MARKET_PLACE", str(loadMarketPlace()))
        response = response.replace("LOGIN_IN", loadLoginIn())
        return HDRS.encode("utf-8") + response.encode("utf-8")

    
    if path=="account":
        with open("private/account.html", "r") as file:
            response = file.read()
        response = response.replace("MY_ACCOUNT", str(loadMarketPlace()))
        with open("private/css/style.css", "r") as css:
            css_ = css.read()
        response = response.replace("WHERE_MY_CSS", css_)
        return HDRS.encode("utf-8") + response.encode("utf-8")


    if path=="send":
        user_name = data.split("/")[2]
        user_id = data.split("/")[3]
        user_message = data.split("/")[4]
        datas = 'hello'
        return HDRS.encode("utf-8") + datas.encode("utf-8")
    
   
    if path=="Market":
        return  HDRS.encode("utf-8") + loadMarketPlace().encode("utf-8")

    if path=="getJS":
        fileName = data.split("/")[2]
        print("js filename: ", fileName)
        with open(f"js/{fileName}.js", "r") as JS:
            return  HDRS.encode("utf-8") + JS.read().encode("utf-8")
    
    if path=="private" and data.split("/")[2]=="nft":
        store = data.split("/")[3]
        print(data.split("/")[3])
        with open(f"private/nft/{store}", "rb") as handle:
            return HDRS.encode("utf-8") + handle.read()

    if path=="bye":
        product_id = data.split("/")[2]
        ac_1 = data.split("/")[3]
        marketplace = Marketplace()
        marketplace.sell(product_id, ac_1)

    if path=="css-main":
        with open("private/css/style.css", "r") as css:
            return  HDRS.encode("utf-8") + css.read().encode("utf-8")

    

if __name__ == '__main__':
    start_server()