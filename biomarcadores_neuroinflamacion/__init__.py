"""
biomarcadores-neuroinflamacion-depresion
=========================================
Accede al conjunto de datos de Harvard Dataverse DVN/OCXEK7.
DOI: https://doi.org/10.7910/DVN/OCXEK7
Autor: Juan Moises de la Serna (ORCID: 0000-0002-8401-8018)

Uso:
    from biomarcadores_neuroinflamacion import cargar_datos, resumen_biomarcadores
    df = cargar_datos()
    resumen = resumen_biomarcadores()
"""
from .cargador import cargar_datos, listar_archivos, resumen_biomarcadores, obtener_doi
__version__ = "1.0.0"
__doi__ = "10.7910/DVN/OCXEK7"
__autor__ = "Juan Moises de la Serna"
__all__ = ["cargar_datos","listar_archivos","resumen_biomarcadores","obtener_doi"]
