import os

def bmicalc(wight,hight):
    bmi= wight/hight**2

    print("your bmi is","{:.2f}".format(bmi))
    if bmi <18.5:
        print("your bmi is low")
    elif 18.5 <= bmi <=25:
        print("your bmi is normal")
    elif bmi > 25:
        print("your bmi is high")

def main():
    try:
        wight= float(input("Enter your wight: "))
        hight= float(input("Enter your hight: "))
        bmicalc(wight,hight)
    except:
        os.system('clear')
        print("try again")
        main()
main()
