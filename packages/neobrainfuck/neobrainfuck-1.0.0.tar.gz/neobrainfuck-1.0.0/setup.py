from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='neobrainfuck',
    version='1.0.0',
    author='kusrabyzarc',
    author_email='crazybarsuk@mail.ru',
    description='Just another rethink of the BrainFuck language',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/kusrabyzarc/NeoBrainF--k',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',  # Уровень готовности проекта: Beta, например
        'Intended Audience :: Developers',  # Основная аудитория
        'License :: OSI Approved :: MIT License',  # Лицензия вашего пакета
        'Programming Language :: Python :: 3',  # Версия Python, совместимая с вашим пакетом
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',  # Для совместимости с PyPy
        'Topic :: Software Development :: Interpreters',  # Тема вашего пакета
        'Topic :: Software Development :: Libraries :: Python Modules',  # Другая тема вашего пакета
    ],
    keywords='BrainFuck interpreter extended programming language esolang development python library brainfuck-interpreter esoteric extended-brainfuck',
    project_urls={},
    python_requires='>=3.6'
)
