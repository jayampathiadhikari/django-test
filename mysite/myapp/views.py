from django.http import HttpResponse
import json
import os
from django.views.decorators.csrf import csrf_exempt


def index(request):
    #f = open('/product_list.txt')
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'product_list.txt')
    f = open(file_path, 'r')
    post = []
    for sentence in f:
        word_array = sentence.split(',')
        dictionary = {
            "id": word_array[0], "name": word_array[1], "price": word_array[-1][:-2]}
        post.append(dictionary)
    y = json.dumps(post)
    response = HttpResponse(y)
    response["Access-Control-Allow-Origin"] = "*"
    return response


def delete(request, id):
    result = ''
    try:
        if(len(id) == 4):
            module_dir = os.path.dirname(__file__)  # get current directory
            file_path = os.path.join(module_dir, 'product_list.txt')
            input_f = open(file_path, 'r')
            output = ''
            for sentence in input_f:
                if (str(id) not in sentence):
                    output += sentence
                else:
                    result = 'delete successfull'
            input_f.close()
            output_f = open(file_path, 'w')
            output_f.write(output)
            output_f.close()
        if result == '':
            result = 'id doesnot match any entries'
    except:
        result = 'delete unsuccessfull'

    x = {"result": result, "array": json.loads(get_all())}
    y = json.dumps(x)
    response = HttpResponse(y)
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_all():
    #f = open('/product_list.txt')
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'product_list.txt')
    f = open(file_path, 'r')
    post = []
    for sentence in f:
        word_array = sentence.split(',')
        dictionary = {
            "id": word_array[0], "name": word_array[1], "price": word_array[-1][:-2]}
        post.append(dictionary)
    y = json.dumps(post)
    return y


def search(request, name):
    try:
        all_products = get_all()
        all_products_dic = json.loads(all_products)
        output_dict = [x for x in all_products_dic if (
            str(name).capitalize() in x['name'])]  # check if str
        output_json = json.dumps(output_dict)
        response = HttpResponse(output_json)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except:
        response = HttpResponse(json.dumps({"response": "error"}))
        response["Access-Control-Allow-Origin"] = "*"
        return response

@csrf_exempt
def add_product(request):  
    if request.method == "POST": 
        try:
            result = 'success'
            prod_id = request.GET["id"]
            name = request.GET['name']
            price = '$'+request.GET["price"]
            new_product = prod_id+','+name+','+price+'\n'
            module_dir = os.path.dirname(__file__)  # get current directory
            file_path = os.path.join(module_dir, 'product_list.txt')
            f = open(file_path, 'r')
            for sentence in f:
                if prod_id in sentence:
                    result = 'id already exists'
                    break
            f.close()
            f = open(file_path, 'a')
            if(result == 'success'):
                f.write(str(new_product))
            f.close()
            x = {"result": result, "array": json.loads(get_all())}
            y = json.dumps(x)
            response = HttpResponse(y)
            response["Access-Control-Allow-Origin"] = "*"
            
            return response
        except :

            response = HttpResponse(json.dumps({"result": "error occured"}))
            response["Access-Control-Allow-Origin"] = "*"
            return response
