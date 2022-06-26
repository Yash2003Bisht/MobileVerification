import requests

def print_data(data: dict):
    for key, value in data.items():
        print(f"{key}: {value}")

def main():
    url = "https://api.apilayer.com/number_verification/validate?number={}"
    headers = {
        "apikey": "Add you API key here"
    }
    number = input("Enter your number with country code, for ex 91123456789: ")
    response = requests.request("GET", url.format(number), headers=headers)

    if response.ok:
        print_data(response.json())
    else:
        print("Error! please check if you add your api or not?")


if __name__ == '__main__':
    main()
