from setuptools import setup, find_packages

setup(
    name='hcv_genotypes',
    version='0.0.1',
    author='Irfan Hussain',
    author_email='ir_hussain@hotmail.com',
    description='hcv genotypes Dataset',
    long_description=open('README.md').read(),  # Ensure you have a README.md file in your project
    long_description_content_type='text/markdown',
    url='https://github.com/irfan112/HCV-subgenotypes',  # Update with your actual URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)