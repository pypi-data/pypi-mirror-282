import pathlib
import setuptools

setuptools.setup(
    name='HitoAI_SusNet',
    version='0.1.0',
    description='A project to predict temperature using an Artificial Neural Network.',
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author='Shenal Elekuttige',
    author_email='shenaal.h@hitoai.ai',
    packages=setuptools.find_packages(),
    install_requires=[
        'tensorflow>=2.0.0',
        'keras>=2.3.0',
        'numpy>=1.18.0',
        'pandas>=1.0.0',
        'scikit-learn>=0.22.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    include_package_data=True,
)