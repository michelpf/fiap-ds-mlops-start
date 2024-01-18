import requets


def get_product(id):
    results = requets.get("https://dummyjson.com/products/"+str(id))
    print(results.status_code)
    print(results.json())


get_product(1)