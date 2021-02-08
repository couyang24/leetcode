from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dct ={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = []
        lst = [[j for j in dct[i]] for i in digits]
        return ["".join(i) for i in list(product(*lst))]
