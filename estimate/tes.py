class MyClass:
    def __init__(self, value):
        self._const_value = value  # プライベート変数として定義

    @property
    def const_value(self):
        return self._const_value  # 読み取り専用

obj = MyClass(42)
print(obj.const_value)  # 42
obj._const_value = 100  # AttributeError: can't set attribute
print(obj._const_value)  # 42
obj.const_value = 100  # AttributeError: can't set attribute
