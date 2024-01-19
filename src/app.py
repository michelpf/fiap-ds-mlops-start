"""Module responsible to get data from produts API"""
import requests


def get_product(product_id):
    """Get a product by id"""
    results = requests.get("https://dummyjson.com/products/"+str(product_id), timeout=10)
    return results


get_product(1)
