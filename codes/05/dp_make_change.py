def dp_make_change(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]

def print_coins(coin_used, change):
    coin = change
    while coin > 0:
        this_coin = coin_used[coin]
        print(this_coin)
        coin = coin - this_coin


if __name__ == '__main__':
    c1 = [1, 5, 10, 21, 25]
    coins_used = [0] * 64
    coin_count = [0] * 64
    # print(dp_make_change(c1, 63, coin_count, coins_used))
    print(print_coins(coins_used, 63))