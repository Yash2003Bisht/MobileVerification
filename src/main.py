import requests
import pandas as pd

def print_data(data: dict):
    for key, value in data.items():
        print(f"{key}: {value}")

def get_data_as_csv(json_data):
    data = pd.DataFrame(
        {
            "Valid": [json_data["valid"]],
            "Number": [json_data["number"]],
            "Local Format": [json_data["local_format"]],
            "International Formate": [json_data["international_format"]],
            "Country Prefix": [json_data["country_prefix"]],
            "Country Code": [json_data["country_code"]],
            "Country Name": [json_data["country_name"]],
            "Location": [json_data["location"]],
            "Carrier": [json_data["carrier"]],
            "Line Type": [json_data["line_type"]],
        }
    )
    data.to_csv("data.csv")
    print("data saved in data.csv file.")

def main():
    url = "https://api.apilayer.com/number_verification/validate?number={}"
    headers = {
        "apikey": "Add you API key here"
    }
    number = input("Enter your number with country code, for ex 91123456789: ")
    response = requests.request("GET", url.format(number), headers=headers)

    if response.ok:
        data = response.json()
        print_data(data)
        get_data_as_csv(data)
    else:
        print("Error! please check if you add your api or not?")


if __name__ == '__main__':
    main()
