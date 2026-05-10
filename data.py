import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data={
     "Month":["Jan","Feb","Mar","Apr","May","Jun"],
     "Sales":[200,350,300,400,500,450],
     "Profit":[50,80,70,100,120,110]
     }
df=pd.DataFrame(data)
sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
plt.plot(df["Month"], df["Sales"],
         marker='o',label="Sales")
plt.plot(df["Month"],df["Profit"],
         marker='s',label="Profit")
plt.title("Sales and Profit Analysis",
          fontsize=16,
          fontweight='bold')
plt.xlabel("Months")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8,5))
sns.barplot(x="Month",y="Sales",data=df)
plt.title("Monthly Sales Visualization",
          fontsize=15)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
plt.figure(figsize=(7,7))
plt.pie(df["Sales"],
       labels=df["Month"],
       autopct="%1.1f%%",
       startangle=90)
plt.title("Sales Distribution by Month")
plt.show()
print("Data Visualization Completed Successfully!")
