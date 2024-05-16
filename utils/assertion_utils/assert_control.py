class AssertionControl:
    def __init__(self, enable_assertions=True):
        """
        初始化 AssertionControl 类。

        参数:
        - enable_assertions: 是否启用断言，默认为 True。
        """
        self.enable_assertions = enable_assertions

    def assert_equal(self, expected, actual, message=""):
        """
        断言两个值相等。

        参数:
        - expected: 期望的值。
        - actual: 实际的值。
        - message: 断言失败时显示的额外信息，默认为空字符串。
        """
        if self.enable_assertions:
            assert expected == actual, f"Assertion failed: Expected '{expected}', but got '{actual}'. {message}"

    def assert_not_equal(self, expected, actual, message=""):
        """
        断言两个值不相等。

        参数:
        - expected: 期望的值。
        - actual: 实际的值。
        - message: 断言失败时显示的额外信息，默认为空字符串。
        """
        if self.enable_assertions:
            assert expected != actual, f"Assertion failed: Expected value to be different from '{expected}', but got '{actual}'. {message}"

    def assert_true(self, condition, message=""):
        """
        断言条件为真。

        参数:
        - condition: 要断言的条件。
        - message: 断言失败时显示的额外信息，默认为空字符串。
        """
        if self.enable_assertions:
            assert condition, f"Assertion failed: Condition is not True. {message}"

    def assert_false(self, condition, message=""):
        """
        断言条件为假。

        参数:
        - condition: 要断言的条件。
        - message: 断言失败时显示的额外信息，默认为空字符串。
        """
        if self.enable_assertions:
            assert not condition, f"Assertion failed: Condition is not False. {message}"
