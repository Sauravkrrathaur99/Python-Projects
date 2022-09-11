from time import *
import random as r


def mistake(para, user):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != user[i]:
                error += 1
        except:
            error += 1

    return error


def speed_time(time_s, time_e, user):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(user) / time_r
    return round(speed)



if __name__=='__main__':
    while True:
        ck = input("Ready to tes : yes / no : ")
        if ck == "yes":

            test = [
                "A computer network is a set of devices connected through links. A node can be computer, printer, or any other device capable of sending or receiving the data. The links connecting the nodes are known as communication channels.",
                "Computer Network uses distributed processing in which task is divided among several computers. Instead, a single computer handles an entire task, each separate computer handles a subset.",
                "The database is a collection of inter-related data which is used to retrieve, insert and delete the data efficiently. It is also used to organize the data in the form of a table, schema, views, and reports, etc."]

            test1 = r.choice(test)
            print("     ***** Typing Speed *****      ")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter : ")
            time_2 = time()

            print("Speed : ",speed_time(time_1,time_2,testinput)," w/sec")
            print("Error : ",mistake(test1,testinput))

        elif ck == "no":
            print(" Thankyou ")
            break
        else:
            print(" Wrong Input ")

