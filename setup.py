from setuptools import setup, find_packages
setup(
    name="biomarcadores-neuroinflamacion-depresion-2020-2024",
    version="1.0.0",
    description="Datos globales de biomarcadores de neuroinflamación (IL-6, TNF-alfa, PCR) en depresión y trastorno d",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/biomarcadores-neuroinflamacion-depresion-2020-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="biomarcadores, dataset, depresion, il-6, neuroinflamacion, open-data, salud-mental, tnf-alfa, zenodo, open-data",
)