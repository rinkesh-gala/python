def usd_to_inr(amount,rates=83.37):
    return (amount*rates)

a= int(input("enter a USD amount which you want to convert to INR: "))
print("INR value is",usd_to_inr(a))
