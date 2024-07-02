from setuptools import setup, find_packages

setup(
    name='dyno_dino',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        
    ],
    author='João Victor Godoi Bernardino',
    author_email='joaogodoi1010@gmail.com',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JoaoGodoi/dyno-dino',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)