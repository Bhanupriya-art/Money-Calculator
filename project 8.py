print("WELCOME TO MONEY CONVERTOR CALCULATOR")
print()
print("Indian ruppes = INR, US dollar = USD, Chinese Yuan = CNY, Russian Ruble = RUB, Canadian Dollae = CAD, EURO, POUNDS")

print()

a=input("convert From:- ")
b=input("convert to:- ")
c=float(input("Enter Amount: "))

print()
if (a=="INR" and b=="USD") or (a=="inr" and b=="usd") or (a=="USD" and b=="INR") or (a=="usd" and b=="inr"):
    if (a=="INR" or a=="inr"):
        d=c/82.20
        print(f"your amount in {b} is {round(d,5)}")
    else:
        d=c*82.20
        print(f"your amount in {b} is {round(d,5)}")
        
elif (a=="INR" and b=="POUND") or (a=="inr" and b=="pound") or (a=="POUND" and b=="INR") or (a=="pound" and b=="inr"):
    if (a=="INR" or a=="inr"):
        d=c/100.32
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*100.32
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="INR" and b=="EURO") or (a=="inr" and b=="euro") or (a=="EURO" and b=="INR") or (a=="euro" and b=="inr"):
    if (a=="INR" or a=="inr"):                      
        d=c/86.37
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*86.37
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="INR" and b=="CAD") or (a=="inr" and b=="cad") or (a=="CAD" and b=="INR") or (a=="cad" and b=="inr"):
    if (a=="INR" or a=="inr"):                      
        d=c/60.21
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*60.21
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="INR" and b=="CNY") or (a=="inr" and b=="cny") or (a=="CNY" and b=="INR") or (a=="cny" and b=="inr"):
    if (a=="INR" or a=="inr"):                      
        d=c/11.79
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*11.79
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="INR" and b=="RUB") or (a=="inr" and b=="rub") or (a=="RUB" and b=="INR") or (a=="rub" and b=="inr"):
    if (a=="INR" or a=="inr"):                      
        d=c/1.33
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*1.33
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="USD" and b=="RUB") or (a=="usd" and b=="rub") or (a=="RUB" and b=="USD") or (a=="rub" and b=="usd"):
    if (a=="USD" or a=="usd"):                      
        d=c*63.02
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/63.02
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="USD" and b=="POUND") or (a=="usd" and b=="pound") or (a=="POUND" and b=="USD") or (a=="pound" and b=="usd"):
    if (a=="USD" or a=="usd"):                      
        d=c/1.22
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*1.22
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="USD" and b=="EURO") or (a=="usd" and b=="euro") or (a=="EURO" and b=="USD") or (a=="euro" and b=="usd"):
    if (a=="USD" or a=="usd"):                      
        d=c/1.05
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*1.05
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="USD" and b=="CAD") or (a=="usd" and b=="cad") or (a=="CAD" and b=="USD") or (a=="cad" and b=="usd"):
    if (a=="USD" or a=="usd"):                      
        d=c*1.37
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/1.37
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="USD" and b=="CNY") or (a=="usd" and b=="cny") or (a=="CNY" and b=="USD") or (a=="cny" and b=="usd"):
    if (a=="USD" or a=="usd"):                      
        d=c*6.97
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/6.97
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="POUND" and b=="CAD") or (a=="pound" and b=="cad") or (a=="CAD" and b=="POUND") or (a=="cad" and b=="pound"):
    if (a=="POUND" or a=="pound"):
        d=c*1.67
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/1.67
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="POUND" and b=="EURO") or (a=="pound" and b=="euro") or (a=="EURO" and b=="POUND") or (a=="euro" and b=="pound"):
    if (a=="POUND" or a=="pound"):
        d=c*1.16
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/1.16
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="POUND" and b=="RUB") or (a=="pound" and b=="rub") or (a=="RUB" and b=="POUND") or (a=="rub" and b=="pound"):
    if (a=="POUND" or a=="pound"):
        d=c*76.77
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/76.77
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="POUND" and b=="CNY") or (a=="pound" and b=="cny") or (a=="CNY" and b=="POUND") or (a=="cny" and b=="pound"):
    if (a=="POUND" or a=="pound"):
        d=c*8.50
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/8.50
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="EURO" and b=="CAD") or (a=="euro" and b=="cad") or (a=="CAD" and b=="EURO") or (a=="cad" and b=="euro"):
    if (a=="EURO" or a=="euro"):
        d=c*1.44
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/1.44
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="EURO" and b=="RUB") or (a=="euro" and b=="rub") or (a=="RUB" and b=="EURO") or (a=="rub" and b=="euro"):
    if (a=="EURO" or a=="euro"):
        d=c*66.09
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/66.09
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="EURO" and b=="CNY") or (a=="euro" and b=="cny") or (a=="CNY" and b=="EURO") or (a=="cny" and b=="euro"):
    if (a=="EURO" or a=="euro"):
        d=c*7.33
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/7.33
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="RUB" and b=="CNY") or (a=="rub" and b=="cny") or (a=="CNY" and b=="RUB") or (a=="cny" and b=="rub"):
    if (a=="RUB" or a=="rub"):
        d=c/9.03
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*9.03
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="RUB" and b=="CAD") or (a=="rub" and b=="cad") or (a=="CAD" and b=="RUB") or (a=="cad" and b=="rub"):
    if (a=="RUB" or a=="rub"):
        d=c/46.08
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c*46.08
        print(f"Your amount in {b} is {round(d,5)}")
elif (a=="CAD" and b=="CNY") or (a=="cad" and b=="cny") or (a=="CNY" and b=="CAD") or (a=="cny" and b=="cad"):
    if (a=="CAD" or a=="cad"):
        d=c*5.10
        print(f"Your amount in {b} is {round(d,5)}")
    else:
        d=c/5.10
        print(f"Your amount in {b} is {round(d,5)}")

        

    

    
