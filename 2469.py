# 2469. Convert the Temperature

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        def k(x):
            return x+273.15
        def f(x):
            return (x*1.8)+32
        return[k(celsius),f(celsius)]
