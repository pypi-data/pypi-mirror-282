from setuptools import setup, find_packages

setup(
    name='jmeter_compare',
    version='1.0',
    entry_points={
        'console_scripts': [
            'jmeter_compare=jmeter_compare.main:main',
        ],
    },
    author='Me',
    description='This runs my script which is great.',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'matplotlib >= 3.9.0',
        'pandas >= 0.22.0',
        'numpy >= 1.16.0'
    ],
    python_requires='>=3.5'
)
