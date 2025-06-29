import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="ticks")

scale = [10000] * 5 + [100000] * 5 + [1000000] * 5
time = [
    0.0005231,
    0.0004969,
    0.0007591,
    0.0005000,
    0.0005682,
    0.0052481,
    0.0050349,
    0.0052311,
    0.0052531,
    0.0051970,
    0.0502801,
    0.0507140,
    0.0509501,
    0.0515950,
    0.0506890,
]
df = pd.DataFrame({"scale": scale, "time": time})
sns.scatterplot(df, x="scale", y="time")
plt.savefig("../imgs/imgs/sum_of_n_1.pdf", format="pdf", bbox_inches="tight")
plt.show()


# scale = [10000, 100000, 1000000, 10000000, 100000000]
# time = [0.0000009537, 0.0000009537, 0.0000007153, 0.0000009537, 0.0000011921]
# df = pd.DataFrame({'scale': scale, 'time': time})
# sns.scatterplot(df, x='scale', y='time')
# plt.ylim(0, 0.00001)
# plt.savefig("../imgs/imgs/sum_of_n_2.pdf", format="pdf", bbox_inches="tight")
# plt.show()
