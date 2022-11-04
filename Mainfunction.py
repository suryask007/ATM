import withdraw as p1
import check_balance as p2
import change_pin as p3
def fun():
    print("1=Withdraw")
    print("2=Checkbalance")
    print("3=change pin")
    for i  in range(1,4):
        
        number=int(input("enter the option:"))
        if number==1:
            p1.fun1()
        elif number==2:
            p2.fun2()
        elif number==3:
            p3.fun3()
        else:
            print("enter the correct option:")
        option=str(input("Do you want continue: \n yes or no:"))
        if option=="yes":
            print("1=Withdraw")
            print("2=Checkbalance")
            print("3=change pin")
            continue
        elif option=="no":
            print("Thankyou!")
            break
fun()
