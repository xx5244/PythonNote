import unittest
from unittest.main import main  # 要導入此module
from DEMO.math import add    # 語法1


class TestAdd(unittest.TestCase):   # 要建立測試類別
    # 建立測試項目
    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # 預測是否參數兩值相等，參數1填測試的function後面填預想的結果
        self.assertEqual(add(4, 2), 6)

    def test_add2(self):
        self.assertEqual(add(10, 20), 30)

    def test_add3(self):
        self.assertNotEqual(add(1, 4), 3)

    def test_add4(self):
        self.assertRaises(ValueError, add, 1, 1.2)  # 為了觸發條件


if __name__ == '__main__':
    unittest.main()


"""
在測試文件裡，通常命名以test_為開頭
如果預測結果跟實際運行結果不符則會顯示FAILED
測試的項目是以多少以test_開頭的方法去區分，所以，一個測試方法如寫多個測試，只要其中有個測試失敗整塊就會算失敗
assertRaises裡面，第一個參數放斷言結果，第二個參數放該函數，第三個以後的參數放該函數輸入的參數
"""
