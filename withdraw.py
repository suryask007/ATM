import datetime
Amount=5000
pin=2001

def fun1():
    pin1=int(input("enter the pin:"))
    if pin1==pin:
        print("Enter the withdraw Amount:")
        withdraw_Amount=int(input("enter the amounnt:"))
        if withdraw_Amount<Amount:
            s=Amount-withdraw_Amount
            date_time=datetime.datetime.now()
            print("you are Successfully withdraw the amount:",withdraw_Amount,"\nDate Time is:",date_time)
    else:
        Print(" pin is wrong!!")
