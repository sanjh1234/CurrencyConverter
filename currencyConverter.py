with open ('currencyData.txt') as f:
    lines = f.readlines()

currency_dict = {}

for line in lines:
    element = line.split("\t")
    currency_dict[element[0]] = element[1]

print(f"""
    HELLO! WELCOME TO CURRENCY CONVERTER
    Here Is A Currency Converter For You

    Available Options For Currencies are
""")
[print(f"#  {cur}") for cur in currency_dict.keys()]



while True:
    try:

        ask = input("""
    Type q To Quit
    Do You Wanna Convert Foreign Currency To INR(into INR)
    Or INR To Foreign Currency(INR into) """)

        if ask.lower() == "q":
            print("""
THANK YOU For Using Our Converter""")
            break


        currency = input("""
    Enter Your Currency : """)

        amount = int(input("""
    Enter The Amount : """))

        if ask.lower() == "inr into":
            convert = amount * float(currency_dict.get(currency,"SORRY! Currency Is Not In The List"))
            print(f"""
        {amount} INR = {convert} {currency}""")

        if ask.lower() == "into inr":
            convert = amount / float(currency_dict.get(currency,"SORRY! Currency Is Not In The List"))
            print(f"""
        {amount} {currency} = {convert} INR """)
        

    except ValueError :
        print("SORRY! Please Enter A Valid Value")

