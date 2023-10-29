import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": "false",
}

response = requests.get(url, params=params)
data = response.json()

html_table = "<table><tr><th>Иконка</th><th>Криптовалюта</th><th>Цена в USD</th><th>Рыночная капитализация</th></tr>"
for crypto_data in data:
    crypto_name = crypto_data.get("name", "N/A")
    price_usd = crypto_data.get("current_price", "N/A")
    market_cap = crypto_data.get("market_cap", "N/A")
    icon_url = crypto_data.get("image", "N/A")
    crypto_url = f"https://coingecko.com/en/coins/{crypto_data['id']}"
    html_table += f"<tr><td><img src='{icon_url}' width='20' height='20'></td>"
    html_table += f"<td><a href='{crypto_url}' target='_blank'>{crypto_name}</a></td>"
    html_table += f"<td>${price_usd}</td>"
    html_table += f"<td>${market_cap}</td></tr>"

html_table += "</table>"

with open("result_6.html", "w") as file:
    file.write(html_table)




