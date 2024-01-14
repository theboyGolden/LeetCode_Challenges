class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        min_leftover = money  # Initialize min_leftover with the initial amount of money

        # Iterate through the prices array
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                # Calculate the total cost of buying the current pair of chocolates
                total_cost = prices[i] + prices[j]

                # Check if buying the chocolates leaves non-negative leftover money
                if total_cost <= money:
                    leftover_money = money - total_cost

                    # Update min_leftover if the current leftover_money is smaller
                    min_leftover = min(min_leftover, leftover_money)

        return min_leftover
