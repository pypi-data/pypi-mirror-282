from setuptools import setup, find_packages

setup(
    name="combo-llm",
    version="0.1.0",
    author="Jared Hao",
    author_email="9190632@qq.com",
    description="combo Chinese llms",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
