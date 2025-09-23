
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Fetch data', 'Show head/tail', 'Wash data', 'Lite metrics', 'Paint graphs', 'Bye']

class CovidTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def drawit(self, path):
        if not os.path.exists(path):
            days=pd.date_range("2020-04-01", periods=120, freq="D")
            tmp=pd.DataFrame({
                "date":days,
                "country":np.random.choice(list("ABCD"), len(days)),
                "cases":np.random.randint(30,3000,len(days)),
                "deaths":np.random.randint(0,120,len(days)),
                "recovered":np.random.randint(10,2500,len(days))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def quickstats(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def wash(self):
        if self.df.empty: return
        self.df = self.df.dropna().reset_index(drop=True)

    def look(self):
        if self.df.empty: return
        print("peak cases:", int(self.df["cases"].max())); print("mean deaths:", round(float(self.df["deaths"].mean()),2))

    def loadit(self):
        if self.df.empty: return
        plt.figure(); self.df.plot(kind="scatter", x="cases", y="deaths"); plt.title("SCATTER view"); plt.tight_layout(); plt.savefig("covid_01_scatter.png"); plt.close()
        plt.figure(); self.df.groupby("country")[["cases","deaths"]].sum().plot(kind="bar"); plt.title("BAR view 2"); plt.tight_layout(); plt.savefig("covid_01_bar.png"); plt.close()

def show_menu():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Pocket Suite :: Hola!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i, it in enumerate(ITEMS, 1): print(f"{i}) {it}")

def main():
    app = CovidTool()
    while True:
        show_menu()
        pick = input(">> ").strip()
        if pick == "1":
            p = input("CSV path (blank to auto-generate): ") or "covid.csv"
            app.drawit(p); print("loaded ✓")
        elif pick == "2":
            app.quickstats()
        elif pick == "3":
            app.wash(); print("cleaned ✓")
        elif pick == "4":
            app.look()
        elif pick == "5":
            app.loadit(); print("plots saved 📊")
        elif pick == "6":
            print("bye!"); break
        else:
            print("??")

if __name__ == "__main__":
    main()
