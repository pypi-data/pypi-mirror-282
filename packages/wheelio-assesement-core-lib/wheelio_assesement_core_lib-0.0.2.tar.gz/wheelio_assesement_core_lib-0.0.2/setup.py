from setuptools import setup, find_packages

setup(
    name="wheelio-assesement-core-lib",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["pydantic", "pyjwt", "fastapi", "motor"],
    author='Ashwin Singh',
    author_email='ashwinsinghgr8@gmail.com',
    description='A common package for shared utilities and models for wheel.io technical challenge',
    long_description='Do not use this, this will go off in some time',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/common_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
