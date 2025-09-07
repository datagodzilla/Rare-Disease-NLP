from setuptools import setup, find_packages

setup(
    name='rare-disease-nlp',
    version='0.1.0',
    description='NLP tools for rare disease research',
    author='Your Name',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'streamlit',
        'jupyter',
        'pytest',
    ],
    python_requires='>=3.7',
)
