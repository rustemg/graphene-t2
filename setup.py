import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='graphene-metafora',
    version='0.0.1',
    author='Röstäm Gaziz',
    # author_email='author@example.com',
    description='An extension for graphene',
    long_description=long_description,
    license='MIT',
    long_description_content_type='text/markdown',
    # url='https://github.com/pypa/sampleproject',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords='api graphql graphene',
    install_requires=[
        'graphene>=2.1.7,<3',
    ],
)
