from setuptools import setup,find_packages

setup(
    name='sc_mc_interface',
    version='1.0.9',
    description='mc/Wa模版相关接口',
    author='dyy',
    packages=find_packages(),
    install_requires=["requests>=2.0.0"]
)