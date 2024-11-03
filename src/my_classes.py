class MyClass:
    def __init__(self):
        pass

    def my_method(self) -> str:
        # 何やら外部と通信したり、ユニットテスト時には実行したくない処理がある
        # ...
        return 'original_value'
