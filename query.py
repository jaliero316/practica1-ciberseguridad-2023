import requests


def get_company_information(symbol: str) -> dict:
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    r = requests.get(url, headers=user_agent)

    print(r.json())
    my_data_selection = {
        "nombre": r.json()["quoteSummary"]["result"][0]["price"]["shortName"],
        "ticker": r.json()["quoteSummary"]["result"][0]["price"]["symbol"],
        "precio": r.json()["quoteSummary"]["result"][0]["summaryDetail"]["previousClose"]["raw"]
    }

    print(my_data_selection)
    return my_data_selection


get_company_information("KO")
