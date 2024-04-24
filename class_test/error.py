# raise TypeError("This is a type error")
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import pandas as pd

# 事务集
transactions = [
    ['a', 'c', 'f', 'm', 'p'],
    ['a', 'b', 'c', 'f', 'l', 'o'],
    ['b', 'f', 'm', 'p'],
    ['b', 'c', 'm', 'o'],
    ['a', 'c', 'f', 'l', 'o', 'p']
]

# 将事务集转换成适合Apriori算法的形式
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 计算频繁项集
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# 输出频繁项集
print(frequent_itemsets)
