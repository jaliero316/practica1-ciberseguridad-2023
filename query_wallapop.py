
import urllib.parse
import requests


def get_wallapop(search_text: str):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    keywords = search_text
    keywords = urllib.parse.quote(keywords)
    url = f"https://api.wallapop.com/api/v3/general/search?filters_source=search_box&keywords={keywords}&longitude=-3.69196&latitude=40.41956"

    r = requests.get(url, headers=user_agent)

    print(r.json())
    search_results = r.json()['search_objects']
    price_sum = 0
    num_elements = len(search_results)

    if num_elements == 0:
        return {
            "num_results": num_elements,
            "price_avg": None,
            "results": [],
        }

    results = []
    for r in search_results:
        articulo = {
            "price": r["price"],
            "title": r["title"],
            "description": r["description"]
        }

        results.append(articulo)
        print("-----------------------------------")

        price_sum = price_sum + r["price"]

    price_avg = price_sum / num_elements

    return {
        "num_results": num_elements,
        "price_avg": price_avg,
        "results": results,
    }











