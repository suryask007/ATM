import random
pin=2001
def fun3():
    pin1=int(input("enter the pin:"))
    if pin1==pin:
        m=random.randrange(1000,10000)
        print("Your OTP is :",m)
        user=int(input("enter the number:"))
        if user==m:
            print("OTP is Correct:::")
            print("please Enter the new pin:")
            pin2=int(input("enter the new pin:"))
            print("enter the pin new again:")
            pin3=int(input("enter the new pin again:"))
            if pin3==pin2:
                print("Succesfully changed")
            else:
                print("your pin not match")
        else:
            print("!!!!!enter the correct OTP!!!!!!!")
    else:
        print("enter the correct pin!!")
