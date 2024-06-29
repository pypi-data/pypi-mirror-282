from setuptools import setup, find_packages

setup(
    name='MassWalletETH',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[

    ],
    author='lunairefine',
    author_email='teamcyber2809@gmail.com',
    description='MassWalletETH is a powerful tool for generating multiple Ethereum wallets and checking their balances.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lunairefine/MassWalletETH',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
