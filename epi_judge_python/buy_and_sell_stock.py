from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if len(prices)<2:
        return 0
    min_so_far = prices[0]
    max_gain = 0 if prices[1] - prices[0]<0 else prices[1] - prices[0]
    for i in range(1, len(prices)):
        if prices[i]-min_so_far>max_gain:
            max_gain = prices[i] - min_so_far
        if prices[i] < min_so_far:
            min_so_far = prices[i]
    return max_gain


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
