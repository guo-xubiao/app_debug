# 从测试报告中获取测试结果
import re

class TestResultsHandler:
    def __init__(self, report_file):
        self.report_file = report_file

    def get_results(self):
        # 读取测试报告内容
        with open(self.report_file, 'r') as file:
            content = file.read()

        # 使用正则表达式找到所有的测试用例和结果
        test_cases = re.findall(r'Test Case:\s+(.+)', content)
        results = re.findall(r'Result:\s+(.+)', content)

        # 将测试结果保存到字典中
        test_results = {test_case: result for test_case, result in zip(test_cases, results)}

        return test_results

    def calculate_pass_rate(self):
        # 获取测试结果字典
        test_results = self.get_results()

        # 计算通过率
        passed_count = sum(1 for result in test_results.values() if result == 'Pass')
        total_count = len(test_results)
        pass_rate = passed_count / total_count if total_count > 0 else 0

        return pass_rate

    def generate_report(self, output_file):
        # 获取测试结果字典
        test_results = self.get_results()

        # 计算通过率
        pass_rate = self.calculate_pass_rate()

        # 生成测试报告
        with open(output_file, 'w') as file:
            file.write(f"Pass Rate: {pass_rate}\n")

            for test_case, result in test_results.items():
                file.write(f"Test Case: {test_case}, Result: {result}\n")

        return "Test allure-results generated successfully."
