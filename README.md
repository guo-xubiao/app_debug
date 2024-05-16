#-一个小作业项目，持续完善中
#-各个文件的作用
app_debug
├────allure-results/ allure测试报告
├────output/ 测试报告，日志，图片保存的目录
│ ├────image/
│ ├────log/
│ │ └────app.log
|
├────test_case/ 测试用例目录
│ ├────__init__.py
│ ├────conftest.py pytest框架中一个特殊且重要的组件，它允许你定义和重用测试fixture
│ ├────test_01sjfd.py 测试用例
│ ├────test_02txws.py 测试用例
│ ├────test_03rigi.py 测试用例
│ ├────test_04sjsd.py 测试用例
│ ├────test_05hcql.py 测试用例
│ ├────test_06jcgl.py 测试用例
│ ├────test_07lltj.py 测试用例
│ ├────test_08gjgj.py 测试用例
│ ├────test_09szzx.py 测试用例
|
utils/ 工具类
|
data_utils/ 数据处理
├────__init__.py
└────faker_handle.py 封装的faker包的一些方法
|
files_utils/ 文件处理
├────__init__.py
└────yaml_handle.py 读写yaml文件
|
logger_utils/ 日志处理
├────__init__.py
└────loguru_log.py 封装的loguru日志处理
|
report_utils/ 报告处理
├────__init__.py
├────allure_handle.py 封装的allure的一些操作
├────get_results_handle.py 从测试报告中获取测试结果
|
ui_utils/ UI工具类
├────__init__.py
├────base_page.py 封装的selenium的一些基础浏览器操作方法
|
|
├────config/ 配置文件目录
├────conftest.py pytest框架中一个特殊且重要的组件，它允许你定义和重用测试fixture
├────pytest.ini pytest的配置文件
├────README.md
├────requirements.txt 项目包管理
├────run.py 框架主入口文件

#打开allure报告：allure serve allure-results
