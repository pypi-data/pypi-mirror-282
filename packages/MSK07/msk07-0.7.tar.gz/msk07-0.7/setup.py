from setuptools import setup, find_packages

setup(
    name='MSK07',
    version='0.7',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    description='Pacote teste do Massaki',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Seu Nome',
    author_email='prof.massaki@gmail.com',
    url='https://github.com/massakiigarashi2/',  # URL do repositório se houver
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)