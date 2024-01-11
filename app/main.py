import json
import decimal


def calculate_profit(json_file_name: str) -> None:
    with open(json_file_name) as f:
        data_coins = json.load(f)

        result = {"earned_money": 0, "matecoin_account": 0}

        for data_coin in data_coins:
            dec_matecoin = decimal.Decimal(data_coin["matecoin_price"])
            if data_coin["bought"]:
                dec_bought = decimal.Decimal(data_coin["bought"])
                result["earned_money"] -= dec_bought * dec_matecoin
                result["matecoin_account"] += dec_bought
            if data_coin["sold"]:
                dec_sold = decimal.Decimal(data_coin["sold"])
                result["earned_money"] += dec_sold * dec_matecoin
                result["matecoin_account"] -= dec_sold

        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])

        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)
