import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


sns.set_theme(style="ticks")

x = np.array(range(0, 50))

y = np.array([1] * len(x))
y2 = np.log2(x)
y3 = x
y4 = x * np.log2(x)
y5 = x**2
y6 = x**3
y7 = np.power(2, x)
y8 = np.array(map(factorial, x))
df = pd.DataFrame({"n": x, "f(n)": y})
df2 = pd.DataFrame({"n": x, "f(n)": y2})
df3 = pd.DataFrame({"n": x, "f(n)": y3})
df4 = pd.DataFrame({"n": x, "f(n)": y4})
df5 = pd.DataFrame({"n": x, "f(n)": y5})
df6 = pd.DataFrame({"n": x, "f(n)": y6})
df7 = pd.DataFrame({"n": x, "f(n)": y7})
df8 = pd.DataFrame({"n": x, "f(n)": y8})
sns.lineplot(df, x="n", y="f(n)", label="f(n)=1")
sns.lineplot(df2, x="n", y="f(n)", label="f(n)=logn")
sns.lineplot(df3, x="n", y="f(n)", label="f(n)=n")
sns.lineplot(df4, x="n", y="f(n)", label="f(n)=nlogn")
sns.lineplot(df5, x="n", y="f(n)", label="f(n)=n^2")
sns.lineplot(df6, x="n", y="f(n)", label="f(n)=n^3")
sns.lineplot(df7, x="n", y="f(n)", label="f(n)=2^n")
sns.lineplot(df8, x="n", y="f(n)", label="f(n)=n!")
plt.ylim(bottom=0, top=1500)
# plt.ylim(bottom=0)
plt.savefig("../imgs/imgs/func_plot.pdf", format="pdf", bbox_inches="tight")
plt.show()
