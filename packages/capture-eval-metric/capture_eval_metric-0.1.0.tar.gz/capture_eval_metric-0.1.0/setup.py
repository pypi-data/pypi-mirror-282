from setuptools import setup, find_packages

setup(
    name='capture_eval_metric',
    version='0.1.0',
    author='Hongyuan Dong',
    author_email='d_ousia@icloud.com',
    description='A package for detail image caption evaluation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/foundation-multimodal-models/CAPTURE',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'stop_words': ['stop_words.txt'],
    },
    install_requires=[
        'torch',
        'transformers',
        'tqdm',
        'nltk',
        'spacy',
        'scipy',
        'sentence-transformers',
        'pandas',
        'numpy',
        'tabulate',
        'FactualSceneGraph'
        # Add other dependencies needed for your package
    ],
    license="Apache-2.0",
)
