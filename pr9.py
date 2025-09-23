
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Open/Generate', 'Snapshot', 'Fix data', 'Numbers', 'Plot room', 'Stop']

class AirqualityTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def look(self, path):
        if not os.path.exists(path):
            d=pd.date_range("2023-03-01", periods=150, freq="D")
            tmp=pd.DataFrame({
                "date":d,
                "city":np.random.choice(["Alpha","Beta","Gamma","Delta"], len(d)),
                "AQI":np.random.randint(35,320,len(d)),
                "PM25":np.random.uniform(5,180,len(d)),
                "PM10":np.random.uniform(10,230,len(d)),
                "Temp":np.random.uniform(10,40,len(d))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def drawit(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def wash(self):
        if self.df.empty: return
        self.df = self.df.dropna().reset_index(drop=True)

    def loadit(self):
        if self.df.empty: return
        print("AQI std:", round(float(self.df["AQI"].std()),2))

    def quickstats(self):
        if self.df.empty: return
        plt.figure(); self.df["AQI"].plot(kind="kde"); plt.title("KDE view"); plt.tight_layout(); plt.savefig("airquality_01_kde.png"); plt.close()
        plt.figure(); self.df.plot(kind="scatter", x="PM25", y="AQI"); plt.title("SCATTER view 2"); plt.tight_layout(); plt.savefig("airquality_01_scatter.png"); plt.close()

def show_menu():
    print("\n======================================")
    print("Mini Studio :: Welcome!")
    print("======================================")
    for i, it in enumerate(ITEMS, 1): print(f"{i}) {it}")

def main():
    app = AirqualityTool()
    while True:
        show_menu()
        pick = input(">> ").strip()
        if pick == "1":
            p = input("CSV path (blank to auto-generate): ") or "airquality.csv"
            app.look(p); print("loaded ✓")
        elif pick == "2":
            app.drawit()
        elif pick == "3":
            app.wash(); print("cleaned ✓")
        elif pick == "4":
            app.loadit()
        elif pick == "5":
            app.quickstats(); print("plots saved 📊")
        elif pick == "6":
            print("bye!"); break
        else:
            print("??")

if __name__ == "__main__":
    main()
