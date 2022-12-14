import requests
import json
from datetime import datetime
from database import DatabaseConnection


URL = "https://www.infomoney.com.br/wp-admin/admin-ajax.php"
data = {
    "action": "tool_altas_e_baixas",
    "pagination": 1,
    "altas_e_baixas_table_nonce": "6d317dd767",
    "perPage": 100,
    "stock": 1,
    "type": 1,
    "market": 4224,
}


def extract_stock_page() -> any:
    page = requests.post(URL, data)
    json_data = json.loads(page.text)
    return json_data


def split_stock_data(json_data: json) -> dict:
    stock_list = list()
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y")
    for company in json_data["aaData"]:
        (
            c_name,
            stock_code,
            time,
            price,
            var_day,
            _,
            _,
            _,
            min_value,
            max_value,
            _,
            volume,
        ) = company
        stock_list.append(
            (
                stock_code,
                c_name,
                f"{current_time} {time}",
                price,
                min_value,
                max_value,
                volume,
            )
        )
    return stock_list


if __name__ == "__main__":
    obj = DatabaseConnection()
    json_data = extract_stock_page()
    stocks = split_stock_data(json_data)
    with DatabaseConnection() as db:
        for s in stocks:
            print(s)
            db.execute(
                "INSERT INTO stock (stock_code, c_name, time, price, min_value, max_value, volume) VALUES (?, ?, ?, ?, ?, ?, ?)",
                s,
            )
