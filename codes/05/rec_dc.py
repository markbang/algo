def rec_dc(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    # 检查查询字典中是否已经有某个找零金额对应的最少硬币数
    elif known_results[change] > 0:
        return known_results[change]
    # 如果没有，就递归地计算并且把得到的最少硬币数结果存在表中
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_dc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


if __name__ == '__main__':
    change = 519
    print(rec_dc([1, 5, 10, 25], change, {i + 1: 0 for i in range(change)}))
