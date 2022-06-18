from django.conf import settings
from django.shortcuts import render
from .core.app import App, Auth
from .core.server import Marketplace
from .core.db import DB



def marketplace_(request):
    marketplace = Marketplace("demo2.db")
    # Тут нужен id пользователя
    coins = marketplace.info_account_coins(0)

    data = loadMarketPlace()
    products = marketplace.load()
    products_date = get_index(products, 5)
    print(data)
    print(products)
    context = {
		'products_link_image': data,
        'products_date': products_date,
        'loadNFT': "/logs/js/loadNFT.js",
        'coins': coins,
        'range' : get_range(len(products_date))
	}
    return render(request,
		'logs/index.html', context)

def auth(request):
    return render(request, 'logs/auth.html')

def oauth(request, id):
    oauth = Auth(id)
    print(oauth.oauth())
    return render(request, oauth.oauth())


def currentNFT(request):
    if request.method=="POST":
        data = request.POST
        data = dict(data.lists())
        marketplace = Marketplace("demo2.db")

        coins = marketplace.info_account_coins(data["user_id"][0])
        
        data_pr = marketplace.loadCurrent(int(data["id"][0]))
        context = {
		    'products': marketplace.image_by_id(data_pr[0][0]),
            'product_id' : data['id'][0],
            'coins': coins
	    }
        return render(request, 'logs/currentNFT.html', context)


def bye(request):
    if request.method == "POST":
        return render(request, 'POST IS GET IT')
    return render(request, 'logs/404.html')


def sole(request):
    if request.method == "POST":
        data = request.POST
        data = dict(data.lists())

        marketplace = Marketplace("demo2.db")
        hash = marketplace.sell(data['product_id'][0], data[id][0])
        return render(request, {"product":data['product_id'][0], "user":data[id][0], "hash": hash})
    else:
        return render(request, "logs/404.html")


def loadMarketPlace():
    marketplace_data = Marketplace("demo2.db")
    images_link = []
    datas = marketplace_data.load()
    for i in range(len(datas)):
        images_link.append(marketplace_data.image_by_id(datas[i][0]))
    return images_link


def get_index(array: list, index: int):
    result = []
    for i in array:
        result.append(i[index])
    return result

def get_range(size: int):
    # result = ""
    # for i in range(size):
    #     result+=str(i)
    # return result

    return [str(i) for i in range(size)]
