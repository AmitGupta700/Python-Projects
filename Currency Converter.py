from forex_python.converter import CurrencyRates

c= CurrencyRates()   #creating instance

r= c.convert("USD","INR",1)

print(r)



