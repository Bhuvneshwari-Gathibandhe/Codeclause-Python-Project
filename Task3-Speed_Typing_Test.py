from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except:
            error=error+1
    return error
        
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__=='__main__':
    while True:
        ck=input("ready to test : yes/no: ")
        if ck=="yes":
            test=["I am very beautiful girl","Soccer is played by me","I am not going to take you out","I am very shy girl"]
            test1=r.choice(test)
            print("******Speed typing test Python Project(Golden Project)******")
            print(test1)
            print()
            print()
            time_1=time()
            testinput=input("Enter : ")
            time_2=time()

            print("Speed :",speed_time(time_1,time_2,testinput),"w/sec")
            print("Error :",mistake(test1,testinput))
      
        elif ck=='no':
            print("thank you")
            break
        else:
            print("wrong input")
