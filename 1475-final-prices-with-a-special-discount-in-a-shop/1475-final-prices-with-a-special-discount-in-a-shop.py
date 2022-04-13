class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if j == len(prices)-1 and prices[j] > prices[i]:
                    output.append(prices[i])
                elif j == len(prices)-1 and prices[j] == prices[i]:
                    output.append(prices[i]-prices[j])
                elif prices[j] <= prices[i]:
                    output.append(prices[i]-prices[j])
                    break
        output.append(prices[-1])
        return output
        