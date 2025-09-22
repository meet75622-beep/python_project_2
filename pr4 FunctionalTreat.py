
DATA = {"kind":"1D","vals":[]}

def enter_data():
    """Input 1D/2D data; 2D stored as list of lists."""
    global DATA
    print("\n1) 1D  2) 2D")
    z = input("Pick: ").strip()
    if z == "2":
        r = int(input("Rows? "))
        g = []
        for i in range(r):
            g.append([int(p) for p in input(f"Row {i+1}: ").split()])
        DATA = {"kind":"2D","vals":g}
    else:
        DATA = {"kind":"1D","vals":[int(x) for x in input("Numbers: ").split()]}
    print("Saved.")

def summary():
    """len/sum/min/max demo with printing."""
    if DATA["kind"] == "1D":
        a = DATA["vals"]
        if not a: print("Empty."); return
        print("count:", len(a), "min:", min(a), "max:", max(a), "sum:", sum(a), "avg:", round(sum(a)/len(a),2))
    else:
        g = DATA["vals"]
        flat = [n for row in g for n in row]
        if not flat: print("Empty."); return
        print("rows:", len(g), "total:", len(flat), "min:", min(flat), "max:", max(flat), "sum:", sum(flat), "avg:", round(sum(flat)/len(flat),2))
        for row in g: print(" ".join(map(str,row)))

def f(n): 
    """factorial recursive"""
    return 1 if n<=1 else n*f(n-1)

def do_rec():
    """ask user and show factorial"""
    k = int(input("n: ")); print("fact =", f(k))

def do_lambda():
    """lambda with filter/map threshold"""
    if DATA["kind"] != "1D": print("Use 1D for this demo."); return
    a = DATA["vals"]; 
    if not a: print("Empty."); return
    t = int(input("threshold: "))
    kept = list(filter(lambda v: v>=t, a))
    print("kept:", kept)
    print("tripled:", list(map(lambda v:v*3, kept)))

def many(*args, **kwargs):
    """show *args and **kwargs at once"""
    print("args ->", args)
    print("kwargs ->", kwargs)

def pack_stats():
    """return multiple values from dataset"""
    seq = DATA["vals"] if DATA["kind"]=="1D" else [n for r in DATA["vals"] for n in r]
    if not seq: return None
    return min(seq), max(seq), sum(seq), sum(seq)/len(seq)

def sorter():
    """sort 1D in place; 2D per row with sorted()"""
    if DATA["kind"]=="1D":
        a = DATA["vals"]
        if not a: print("Empty."); return
        mode = input("1=asc 2=desc: ")
        a.sort(reverse=(mode=="2"))
        print("sorted:", a)
    else:
        newg = [sorted(r) for r in DATA["vals"]]
        print("sorted rows:")
        for r in newg: print(r)


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

def docs():
    """print the __doc__ of key functions"""
    for fx in [enter_data, summary, do_rec, do_lambda, sorter, pack_stats, many]:
        print(fx.__name__, "->", (fx.__doc__ or "").strip())

while True:
    show_menu()
    c = input("choice: ").strip()
    if c=="1": enter_data()
    elif c=="2": summary()
    elif c=="3": do_rec()
    elif c=="4": do_lambda()
    elif c=="5": sorter()
    elif c=="6":
        res = pack_stats()
        if res:
            mn,mx,sm,av = res
            many(mn,mx,sm,round(av,2), minimum=mn, maximum=mx, total=sm, average=round(av,2))
        else: print("Empty.")
    elif c=="7": docs()
    elif c=="8": print("Goodbye!"); break
    else: print("bad input")
