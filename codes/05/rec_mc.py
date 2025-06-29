def rec_mc(coin_value_list, change):
    min_coins = change
    # 检查是否为基本情况: 尝试使用1枚硬币找零。
    if change in coin_value_list:
        return 1
    # 如果没有一个硬币面值与找零金额相等，就对每一个小于找零金额的硬币面值进行递归调用。
    else:
        # 使用列表循环来筛选出小于当前找零金额的硬币面值
        for i in [c for c in coin_value_list if c <= change]:
            # 递归调用将找零金额减去所选的硬币面值，并将所需的硬币数加1，以表示使用了1枚硬币。
            num_coins = 1 + rec_mc(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


if __name__ == "__main__":
    print(rec_mc([1, 5, 10, 25], 519))
