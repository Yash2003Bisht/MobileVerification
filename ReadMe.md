# Verify Mobile Number
## Programme to verify mobile number. Using [apilayer](https://apilayer.com/) API we can verify if mobile number is validate or not. You just have to type a number with country code for ex: 911234567890, here first two digits are my country code and then a number.

## Download repository and get ready to run
### 1) Clone repository
#### To clone repository run `git clone https://github.com/Yash2003Bisht/MobileVerificaton`

### 2) Make a virtual environment
#### For linux `python3 virtualenv venv`, for windows `python virtualenv venv` you can change the folder name of your choice

### 3) Activate your virtual environment
#### For linux `source bin/activte`, for windows `venv/scripts/activate`

### 4) Installing requirements
#### After activating your virtual environment run `pip install -r requirements.txt`

### 5) Now you are ready to run the programme. Just run `python main.py` enter a number you want to verify, and you will see a output like this,
#### Enter your number with country code, for ex 91123456789: 91123456789
#### valid: True
#### number: 91123456789
#### local_format: 0123456789
#### international_format: +91123456789
#### country_prefix: +91
#### country_code: IN
#### country_name: India (Republic of)
#### location: Delhi
#### carrier: Vodafone Idea Ltd (formerly Vodafone India Ltd)
#### line_type: mobile


## **Note**: Don't forget to create an account on [apilayer](https://apilayer.com/) and get you API it's free.