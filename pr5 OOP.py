
class Citizen:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        cls = "Citizen"
        return cls + "(" + "name=" + str(self.name) + ", age=" + str(self.age) + ")"

class Associate(Citizen):
    def __init__(self, name, age, code="", pay=0.0):
        super().__init__(name, age)
        self.__eid = str(code)
        self.__wage = float(pay)

    # encapsulation
    def id_of(self): return self.__eid
    def set_code(self, new_code): self.__eid = str(new_code)
    def salary_of(self): return self.__wage
    def set_salary(self, value):
        value = float(value)
        if value < 0: print("Invalid pay")
        else: self.__wage = value

    # 'overloading' via alternative constructors
    @classmethod
    def starter(cls, name, age, code):
        return cls(name, age, code, 0.0)
    @classmethod
    def from_dict(cls, d):
        return cls(d.get("name",""), d.get("age",0), d.get("employee_id",""), d.get("salary",0))

    def __str__(self):
        return "Associate(name=" + str(self.name) + ", age=" + str(self.age) + ", code=" + str(self.__eid) + ", pay=$" + str(self.__wage) + ")"
    # comparison operators -> pay based
    def __eq__(self, other): return isinstance(other, Associate) and self.salary_of() == other.salary_of()
    def __lt__(self, other): return isinstance(other, Associate) and self.salary_of() < other.salary_of()
    def __gt__(self, other): return isinstance(other, Associate) and self.salary_of() > other.salary_of()

    def display(self): print(self)

class Head(Associate):
    def __init__(self, name, age, code, pay, dept):
        super().__init__(name, age, code, pay)
        self.dept = dept
    def display(self):
        print(super().__str__() + " | squad: " + str(self.dept))

class Coder(Associate):
    def __init__(self, name, age, code, pay, lang):
        super().__init__(name, age, code, pay)
        self.lang = lang
    def display(self):
        print(super().__str__() + " | tech: " + str(self.lang))

print("check:", issubclass(Head, Associate), issubclass(Coder, Associate))

people_bin = []
staff_map = {}

def banner():
    print("\n--- Role Manager ---")
    print("1) New Citizen")
    print("2) New Associate")
    print("3) New Head")
    print("4) New Coder")
    print("5) Show")
    print("6) Compare Pay")
    print("7) Exit")

while True:
    banner()
    pick = input("Choose: ").strip()
    if pick == "1":
        nm = input("Name: "); ag = int(input("Age: "))
        people_bin.append(Citizen(nm, ag))
        print("saved")
    elif pick == "2":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("Badge: "); py = float(input("Wage: "))
        e = Associate(nm, ag, cd, py); staff_map[e.id_of()] = e; print("ok")
    elif pick == "3":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("Badge: "); py = float(input("Wage: ")); dp = input("Squad: ")
        m = Head(nm, ag, cd, py, dp); staff_map[m.id_of()] = m; print("ok")
    elif pick == "4":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("Badge: "); py = float(input("Wage: ")); lg = input("Tech: ")
        d = Coder(nm, ag, cd, py, lg); staff_map[d.id_of()] = d; print("ok")
    elif pick == "5":
        print("a) Citizens  b) Associate by id  c) all Associate")
        sub = input("-> ").strip().lower()
        if sub == "a":
            if not people_bin: print("none")
            for i, p in enumerate(people_bin, 1): print(i, p)
        elif sub == "b":
            key = input("id: "); obj = staff_map.get(key)
            if obj: obj.display()
            else: print("not found")
        else:
            if not staff_map: print("empty")
            for v in staff_map.values(): v.display()
    elif pick == "6":
        a = input("id1: "); b = input("id2: ")
        x = staff_map.get(a); y = staff_map.get(b)
        if not x or not y: print("missing")
        else:
            if x == y: print("same pay")
            elif x > y: print(a, "earns more than", b)
            else: print(a, "earns less than", b)
    elif pick == "7":
        print("bye"); break
    else:
        print("wrong")
