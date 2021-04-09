from forex_python.converter import CurrencyRates

currencies = {"EUR":"Euro-Member-Countries","IDR":"Indonesia-Rupiah","BGN":"Bulgaria-Lev","ILS":"Israel-Shekel","GBP":"United-Kingdom Pound","DKK":"Denmark-Krone","CAD":"Canada-Dollar","JPY":"Japan-Yen","HUF":"Hungary-Forint","RON":"Romania-New-Leu","MYR":"Malaysia-Ringgit","SEK":"Sweden-Krona","SGD":"Singapore-Dollar","HKD":"Hong-Kong-Dollar","AUD":"Australia Dollar","CHF":"Switzerland-Franc","KRW":"Korea-(South)-Won","CNY":"China-Yuan-Renminbi","TRY":"Turkey-Lira","HRK":"Croatia-Kuna","NZD":"New-Zealand-Dollar","THB":"Thailand-Baht","USD":"United-States-Dollar","NOK":"Norway-Krone","RUB":"Russia-Ruble","INR":"India-Rupee","MXN":"Mexico-Peso","CZK":"Czech-Republic-Koruna","BRL":"Brazil-Real","PLN":"Poland-Zloty","PHP":"Philippines-Peso","ZAR":"South-Africa-Rand"}

rate = CurrencyRates()

def is_valid_currency(cur):
    test_cur = [val for val in currencies.keys()]

    if cur.upper() in test_cur:
        return True
    else:
        return False

def convert_currency(from_cur,to_cur,ammt):
    try:
        float(ammt)
    except ValueError:
        return "Not Valid Ammount"
    if is_valid_currency(from_cur) and is_valid_currency(to_cur):
        
        return rate.convert(from_cur.upper(),to_cur.upper(),float(ammt))
    else:
        return "Not Valid Code"