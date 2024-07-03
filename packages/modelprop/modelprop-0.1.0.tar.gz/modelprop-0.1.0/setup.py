from setuptools import setup, find_packages




with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="modelprop",  
    version="0.1.0",  
    author="Aniket Jagtap",
    author_email="aniketjagtap18@gmail.com",
    description="A package for evaluating machine learning supervised model and its performance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ashura0Sage/modeldetect-lib",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Development Status :: 4 - Beta",
    ],
    keywords="machine learning supervised model overfitting machine learning target seperability optimum threshold to classify data science data analysis modelprop decile analysis information value decile gain capture weight of evidence",
    python_requires='>=3.6',
    install_requires=[
        "pandas",  
        "numpy",
        "scikit-learn",
        "datetime"
    ]
)