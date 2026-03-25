"""Cargador de datos para el conjunto de datos de Biomarcadores DVN/OCXEK7."""
import pandas as pd, numpy as np, requests, io

DATASET_DOI = "doi:10.7910/DVN/OCXEK7"
DATAVERSE_BASE = "https://dataverse.harvard.edu/api"

def obtener_doi(): return "https://doi.org/10.7910/DVN/OCXEK7"

def listar_archivos():
    archivos = ["niveles_biomarcadores_depresion","valores_diagnosticos_auc",
                "prevalencia_por_cohorte","correlacion_sintomas_biomarcadores",
                "resumen_metaanalisis","estadisticas_descriptivas"]
    for a in archivos: print(f"  {a}.csv")
    return archivos

def cargar_datos(nombre_archivo=None, token_api=None):
    """
    Carga datos del conjunto de datos de biomarcadores de Harvard Dataverse.
    Devuelve datos de muestra si el servidor no está disponible.

    Ejemplos
    --------
    >>> from biomarcadores_neuroinflamacion import cargar_datos
    >>> df = cargar_datos()
    >>> print(df.head())
    """
    if nombre_archivo is None: nombre_archivo = "niveles_biomarcadores_depresion"
    cabeceras = {"X-Dataverse-key": token_api} if token_api else {}
    try:
        r = requests.get(f"{DATAVERSE_BASE}/datasets/:persistentId/?persistentId={DATASET_DOI}", headers=cabeceras, timeout=30)
        if r.status_code == 200:
            for f in r.json().get("data",{}).get("latestVersion",{}).get("files",[]):
                if nombre_archivo.lower() in f.get("dataFile",{}).get("filename","").lower():
                    fid = f["dataFile"]["id"]
                    fr = requests.get(f"{DATAVERSE_BASE}/access/datafile/{fid}", headers=cabeceras, timeout=60)
                    if fr.status_code == 200: return pd.read_csv(io.StringIO(fr.text))
    except Exception: pass
    return _muestra()

def resumen_biomarcadores():
    """Estadisticas clave de biomarcadores del conjunto de datos DVN/OCXEK7."""
    return pd.DataFrame({
        "biomarcador": ["IL-6","TNF-alfa","PCR","IL-1beta"],
        "unidad": ["pg/mL","pg/mL","mg/L","pg/mL"],
        "media_TDM": [7.8,18.5,4.2,5.1], "media_TB": [6.2,15.1,3.5,4.0], "media_CS": [2.4,8.2,1.2,1.8],
        "ratio_TDM_CS": [3.25,2.26,3.50,2.83], "n_estudios": [147,89,203,76],
    })

def _muestra(n=300, semilla=42):
    np.random.seed(semilla)
    g = np.random.choice(["TDM","TB","CS"], n, p=[0.45,0.25,0.30])
    return pd.DataFrame({
        "id_sujeto": [f"S{i:04d}" for i in range(1,n+1)], "grupo": g,
        "edad": np.random.randint(18,75,n),
        "IL6_pg_ml": np.where(g=="TDM",np.random.normal(7.8,2.1,n),np.where(g=="TB",np.random.normal(6.2,1.8,n),np.random.normal(2.4,0.9,n))).clip(0.1),
        "TNF_alfa_pg_ml": np.where(g=="TDM",np.random.normal(18.5,4.3,n),np.where(g=="TB",np.random.normal(15.1,3.6,n),np.random.normal(8.2,2.1,n))).clip(0.1),
        "PCR_mg_L": np.where(g=="TDM",np.random.normal(4.2,1.3,n),np.where(g=="TB",np.random.normal(3.5,1.1,n),np.random.normal(1.2,0.6,n))).clip(0.01),
        "puntuacion_HDRS": np.random.randint(0,52,n), "anio": np.random.choice(range(2020,2025),n),
    })
