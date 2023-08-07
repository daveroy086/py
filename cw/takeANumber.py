# takeANumber.py

def sum_dig_pow(a, b):
    outputList =[]
    
    for num in range(a, b + 1):
        savedNum = num        
        digitList =[]

        for digit in str(num):
            digitList.append(int(digit))
        
        for i, digit in enumerate(digitList):
            num -= digit ** (i + 1)
            if num == 0:
                outputList.append(savedNum)

    return outputList


# contents of test_takeANumber.py
# import unittest
# from takeANumber import sum_dig_pow

# class Test_sDP(unittest.TestCase):
#     def test_sDP(self):
#         self.assertEquals( sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
#         self.assertEqual(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
#         self.assertEqual(sum_dig_pow(10, 89),  [89])
#         self.assertEqual(sum_dig_pow(10, 100),  [89])
#         self.assertEqual(sum_dig_pow(90, 100), [])
#         self.assertEqual(sum_dig_pow(89, 135), [89, 135])
        
# if __name__ == '__main__':
#     unittest.main()