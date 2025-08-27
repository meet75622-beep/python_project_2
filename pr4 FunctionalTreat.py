
global_box = {"shape":"1D","data":[]}

def get_data():
    """Input numbers; keep in global_box."""
    global global_box
    t = input("Type 1D or 2D? (1/2): ")
    if t=="2":
        r = int(input("rows: ")); g=[]
        for i in range(r):
            g.append([int(x) for x in input(f"row {i+1}: ").split()])
        global_box={"shape":"2D","data":g}
    else:
        global_box={"shape":"1D","data":[int(x) for x in input("values: ").split()]}
    print("ok")

def builtins_view():
    """Print stats using built-ins; also grid view for 2D."""
    if global_box["shape"]=="1D":
        a=global_box["data"]; 
        if not a: print("none"); return
        print("count",len(a),"min",min(a),"max",max(a),"sum",sum(a),"avg",round(sum(a)/len(a),2))
    else:
        g=global_box["data"]; flat=[n for r in g for n in r]
        if not flat: print("none"); return
        print("total",len(flat),"min",min(flat),"max",max(flat),"sum",sum(flat))
        for r in g: print(" ".join(map(str,r)))

def rec(n):
    """recursion factorial"""
    return 1 if n<=1 else n*rec(n-1)

def rec_demo():
    """Ask n and print rec(n)."""
    n=int(input("n: ")); print("fact:",rec(n))

def lam_demo():
    """filter >= threshold and then +1 using map"""
    if global_box["shape"]!="1D": print("1D only"); return
    a=global_box["data"]; 
    if not a: print("none"); return
    t=int(input("threshold: "))
    after=list(filter(lambda x:x>=t,a))
    print("filtered:",after)
    print("plus one:",list(map(lambda x:x+1,after)))

def multi():
    """return min,max,sum,avg"""
    seq=global_box["data"] if global_box["shape"]=="1D" else [n for r in global_box["data"] for n in r]
    if not seq: return None
    return min(seq),max(seq),sum(seq),sum(seq)/len(seq)

def sortit():
    """sorter"""
    if global_box["shape"]=="1D":
        a=global_box["data"]; 
        if not a: print("none"); return
        rev=input("desc? y/n: ")=="y"
        a.sort(reverse=rev); print("sorted:",a)
    else:
        g=global_box["data"]; print("sorted rows:"); 
        for r in [sorted(r) for r in g]: print(r)

def star(*a,**k):
    """*args/**kwargs demo"""
    print("args:",a); print("kwargs:",k)


def show_menu():
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Help: Function Docs")
    print("8. Exit Program")

def docs_show():
    """docs viewer"""
    for f in [get_data,builtins_view,rec_demo,lam_demo,sortit,multi,star]:
        print(f.__name__,":",(f.__doc__ or "").strip())

while True:
    show_menu()
    ch=input("choice: ")
    if ch=="1": get_data()
    elif ch=="2": builtins_view()
    elif ch=="3": rec_demo()
    elif ch=="4": lam_demo()
    elif ch=="5": sortit()
    elif ch=="6":
        r=multi()
        if r:
            mn,mx,sm,av=r; star(mn,mx,sm,round(av,2),minimum=mn,maximum=mx,total=sm,average=round(av,2))
        else: print("none")
    elif ch=="7": docs_show()
    elif ch=="8": print("bye"); break
    else: print("??")
