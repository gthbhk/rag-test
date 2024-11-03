from unittest.mock import patch


def test_my_class_my_method():
    with patch('src.my_classes.MyClass.my_method') as m:
        m.return_value = 'mocked'
        from src.my_classes import MyClass
        my_class = MyClass()
        assert my_class.my_method() == 'mocked'
