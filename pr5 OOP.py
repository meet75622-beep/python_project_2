
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        cls = "Human"
        return f"{cls}(name={self.name}, age={self.age})"

class Worker(Human):
    def __init__(self, name, age, code="", pay=0.0):
        super().__init__(name, age)
        self.__tag = str(code)
        self.__salary = float(pay)

    # encapsulation
    def get_id(self): return self.__tag
    def set_id(self, new_code): self.__tag = str(new_code)
    def get_pay(self): return self.__salary
    def set_pay(self, value):
        value = float(value)
        if value < 0: print("Invalid pay")
        else: self.__salary = value

    # 'overloading' via alternative constructors
    @classmethod
    def from_min(cls, name, age, code):
        return cls(name, age, code, 0.0)
    @classmethod
    def from_record(cls, d):
        return cls(d.get("name",""), d.get("age",0), d.get("employee_id",""), d.get("salary",0))

    def __str__(self):
        return f"Worker(name={self.name}, age={self.age}, code={self.__tag}, pay=${self.__salary})"
    # comparison operators -> pay based
    def __eq__(self, other): return isinstance(other, Worker) and self.get_pay() == other.get_pay()
    def __lt__(self, other): return isinstance(other, Worker) and self.get_pay() < other.get_pay()
    def __gt__(self, other): return isinstance(other, Worker) and self.get_pay() > other.get_pay()

    def reveal(self): print(self)

class TeamLead(Worker):
    def __init__(self, name, age, code, pay, dept):
        super().__init__(name, age, code, pay)
        self.dept = dept
    def reveal(self):
        print(super().__str__() + " | department: " + str(self.dept))

class SoftwareMaker(Worker):
    def __init__(self, name, age, code, pay, lang):
        super().__init__(name, age, code, pay)
        self.lang = lang
    def reveal(self):
        print(super().__str__() + " | programming language: " + str(self.lang))

print("check:", issubclass(TeamLead, Worker), issubclass(SoftwareMaker, Worker))

rollcall = []
ledger = {}

def banner():
    print("\n--- Staff Console ---")
    print("1) New Human")
    print("2) New Worker")
    print("3) New TeamLead")
    print("4) New SoftwareMaker")
    print("5) Show")
    print("6) Compare Pay")
    print("7) Exit")

while True:
    banner()
    pick = input("Choose: ").strip()
    if pick == "1":
        nm = input("Name: "); ag = int(input("Age: "))
        rollcall.append(Human(nm, ag))
        print("saved")
    elif pick == "2":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("Employee ID: "); py = float(input("Salary: "))
        e = Worker(nm, ag, cd, py); ledger[e.get_id()] = e; print("ok")
    elif pick == "3":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("Employee ID: "); py = float(input("Salary: ")); dp = input("Department: ")
        m = TeamLead(nm, ag, cd, py, dp); ledger[m.get_id()] = m; print("ok")
    elif pick == "4":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("Employee ID: "); py = float(input("Salary: ")); lg = input("Programming Language: ")
        d = SoftwareMaker(nm, ag, cd, py, lg); ledger[d.get_id()] = d; print("ok")
    elif pick == "5":
        print("a) Humans  b) Worker by id  c) all Worker")
        sub = input("-> ").strip().lower()
        if sub == "a":
            if not rollcall: print("none")
            for i, p in enumerate(rollcall, 1): print(i, p)
        elif sub == "b":
            key = input("id: "); obj = ledger.get(key)
            if obj: obj.reveal()
            else: print("not found")
        else:
            if not ledger: print("empty")
            for v in ledger.values(): v.reveal()
    elif pick == "6":
        a = input("id1: "); b = input("id2: ")
        x = ledger.get(a); y = ledger.get(b)
        if not x or not y: print("missing")
        else:
            if x == y: print("same pay")
            elif x > y: print(a, "earns more than", b)
            else: print(a, "earns less than", b)
    elif pick == "7":
        print("bye"); break
    else:
        print("wrong")
