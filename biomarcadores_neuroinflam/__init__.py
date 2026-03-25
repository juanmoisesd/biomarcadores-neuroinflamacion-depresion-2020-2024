"""Datos globales de biomarcadores de neuroinflamación (IL-6, TNF-alfa, PCR) en depresión y trastorno d
DOI: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OCXEK7 | GitHub: https://github.com/juanmoisesd/biomarcadores-neuroinflamacion-depresion-2020-2024"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OCXEK7".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). Datos globales de biomarcadores de neuroinflamación (IL-6, TNF-alfa, PCR) en dep. Zenodo. https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OCXEK7'
def info(): print(f"Dataset: Datos globales de biomarcadores de neuroinflamación (IL-6, TNF-alfa, PCR) en dep\nDOI: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OCXEK7\nGitHub: https://github.com/juanmoisesd/biomarcadores-neuroinflamacion-depresion-2020-2024")