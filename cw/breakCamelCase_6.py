# breakCamelCase_6.py

def solution(s):

    spaces = 0    
    for i, char in enumerate(s):
        if(ord(char) > 64 and ord(char) < 91):
            s = s[:i + spaces] + " " + s[i + spaces:]
            spaces += 1
    return s

# Test file contents:
# # breakCamelCase_6_test.py
# # at CMD run: python -m unittest breakCamelCase_6_test.py

# import unittest 
# from breakCamelCase_6 import solution 

# class TestBreakCamelCase_5(unittest.TestCase):
#     def test_bCC(self):
#         self.assertEqual(solution("helloWorld"), "hello World")
#         self.assertEqual(solution("camelCase"), "camel Case")
#         self.assertEqual(solution("breakCamelCase"), "break Camel Case")