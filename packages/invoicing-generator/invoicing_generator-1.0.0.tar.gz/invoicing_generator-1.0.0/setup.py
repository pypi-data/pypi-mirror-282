from setuptools import setup

setup(
    name='invoicing-generator',
    packages=['invoicing'],
    version='1.0.0',
    license='MIT',
    description='This package is used to convert Excel files to PDF format.',
    author='Nancy Chaudhry',
    author_email='chaudhrynancyann@gmail.com',
    url='https://nancychaudhry.com/',
    keywords=['invoice', 'excel', 'pdf', 'generator'],
    install_requires=['pandas', 'fpdf', 'openpyxl'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
)
