# CREATED: 6 Sep 2019
# AUTHOR: The Software Guy
# PURPOSE: Fun with Python statements

def main():
    for i in range(1,13):
        if i==3:
            continue
        if i==11:
            break
        if i % 2 == 0:
            print("%x" % i)
        else:
            print("%d" % i)
            

if __name__=="__main__":
    main()
