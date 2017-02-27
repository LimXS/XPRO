#global k

def t():
    global k
    k+=1
    #print k

def main():
    global k
    k+=1
    print k
    t()
    #return k

if __name__ == '__main__':
   global k
   k=100
   main()

f=open(r"D:\tag\tagconfig\flag",'a')
f.write("12")

f.close()