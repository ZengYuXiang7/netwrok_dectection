from setuptools import setup, find_packages

setup(
    name="LSTC",
    version="0.1.0",
    author="Yuxiang Zeng",
    author_email="zengyuxiang@hnu.edu.cn",
    description="Tensor Comletion",
    long_description_content_type="text/markdown",
    # url="https://github.com/Zengyuxiang7/LLGAT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "openpyxl",
        "node2vec",
        "pysnooper",
        "loguru",
        "einops",
        "nbformat",
        "numexpr",
        "yagmail",
        "faiss-cpu",
        "openai",
        "netron",
        "thop",
    ],
    entry_points={
        "console_scripts": [
            "run=run_demo:main",  # 将 `run` 函数注册为命令行工具
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.rst", "*.md"],
        "your_package": ["data/*.dat"],
    },
)