from setuptools import find_packages, setup

setup(
    name="dlprime",
    packages=find_packages(),
    version="0.1.0",
    description="A library that includes basic machine learning and deep learning tools such as the Perceptron, "
                "LinearRegression, LogisticRegression etc.",
    author="Jiho Lee",
    install_requires=["numpy", "pandas", "matplotlib", "sklearn"],
)