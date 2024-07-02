from setuptools import setup, find_packages

dependencies = []

# 打开requirements.txt文件并读取内容
with open('requirements.txt', 'r') as file:
    for line in file:
        dependencies.append(line.strip())

print(dependencies)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='zjbbintest',
    version='3.0',
    author="zhangjiabin01",
    author_email="zhangjiabin01@baidu.com",
    description="bintest自动化框架",
    packages=find_packages(),
    package_data={
            'zjbbintest': ['Template/*'],  # 包含my_package中的templates文件夹下的所有文件
        },
    install_requires=dependencies,
    long_description=long_description,
    long_description_content_type="text/markdown",
)