from django.conf import settings
from django.shortcuts import render
from .core.app import App, Auth
from .core.server import Marketplace
from .core.db import DB



def marketplace_(request):
    marketplace = Marketplace("demo3.db")
    # Тут нужен id пользователя
    coins = marketplace.info_account_coins(0)

    data = loadMarketPlace()
    products = marketplace.load()
    users = marketplace.load_product_users(products)
    print(data)
    print(products)
    
    
    context = {
		'products' : data,
        'prod': products,
        'users' : users
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
        marketplace = Marketplace("demo3.db")

        coins = marketplace.info_account_coins(data["user_id"][0])
        
        data_pr = marketplace.loadCurrent(int(data["id"][0]))

        print(data_pr)

        context = {
		    'products': marketplace.image_by_id(data_pr[0][0]),
            'product_id' : data['id'][0],
            'coins': coins,
            'data': data_pr,
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
        print(data)
        marketplace = Marketplace("demo3.db")
        hash = marketplace.sell(data['product_id'][0], data[id][0])
        return render(request, {"product":data['product_id'][0], "user":data[id][0], "hash": hash})
    else:
        return render(request, "logs/404.html")


def loadMarketPlace():
    marketplace_data = Marketplace("demo3.db")
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

    return (str(i) for i in range(size))

def to_dict(array_1: list, array_2: list):
    result = {}
    for i in range(len(array_1)):
        result[array_1[i]] = array_2[i]
    return result
    