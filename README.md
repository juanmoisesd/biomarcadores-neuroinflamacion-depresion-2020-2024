# Biomarcadores de Neuroinflamación en Depresión y Trastornos Mentales: Datos Globales 2020-2024

[![DOI](https://img.shields.io/badge/DOI-10.7910%2FDVN%2FOCXEK7-blue)](https://doi.org/10.7910/DVN/OCXEK7)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Harvard Dataverse](https://img.shields.io/badge/Harvard-Dataverse-red)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OCXEK7)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--8401--8018-green)](https://orcid.org/0000-0002-8401-8018)

## Descripción

Conjunto de datos con estadísticas globales sobre **biomarcadores de neuroinflamación** (IL-6, TNF-alfa, PCR) en pacientes con depresión y trastorno depresivo mayor (TDM), a partir de metaanálisis con hasta 58.256 participantes (2020-2024).

## Hallazgos principales

| Biomarcador | AUC | Media TDM | Media control | Sensibilidad | Especificidad |
|---|---|---|---|---|---|
| IL-6 | **0,724** | 8,42 pg/mL | 3,18 pg/mL | 0,71 | 0,68 |
| TNF-alfa | **0,861** | 15,7 pg/mL | 8,2 pg/mL | 0,84 | 0,79 |
| PCR | **0,678** | 4,12 mg/L | 1,93 mg/L | 0,65 | 0,72 |
| BDNF | **0,731** | 18,4 ng/mL | 27,6 ng/mL | 0,70 | 0,74 |

- Prevalencia de depresión en cohortes de alta inflamación: **65%** (estudiantes de enfermería)
- Vínculos bidireccionales confirmados en metaanálisis (N=58.256)
- TNF-alfa con **mayor AUC diagnóstico (0,861)**

## Archivos del conjunto de datos (20 archivos)

| Archivo | Descripción |
|---|---|
| `niveles_biomarcadores_depresion.csv` | Niveles de biomarcadores en TDM vs controles (15 estudios) |
| `valores_auc_diagnosticos.csv` | Rendimiento diagnóstico AUC/ROC |
| `prevalencia_por_cohorte.csv` | Prevalencia de depresión por tipo de cohorte |
| `correlacion_sintoma_biomarcador.csv` | Matriz de correlación síntoma-biomarcador |
| `resumen_metaanalisis.csv` | Resumen de 8 metaanálisis (2020-2024) |
| `respuesta_tratamiento_inflamacion.csv` | Respuesta a tratamientos antiinflamatorios |
| `riesgo_genetico_IL6.csv` | Variantes genéticas UK Biobank (N=368.341) |
| `longitudinal_pcr_depresion.csv` | PCR/IL-6 longitudinal prediciendo depresión |
| `analisis_biomarcadores.ipynb` | Cuaderno Jupyter de análisis |
| `datos_biomarcadores.json` | Datos estructurados JSON |
| `resumen_biomarcadores.tsv` | Tabla resumen TSV |
| `descripcion_conjunto_datos.json` | Metadatos BIDS 1.8.0 |
| `CITACION.cff` | Metadatos de citación |
| `METODOLOGIA.md` | Documentación metodológica |
| `libro_de_codigos.md` | Descripción de variables |
| `metadatos_pais.csv` | Datos contextuales por país |
| `estadisticas_descriptivas.csv` | Estadísticas descriptivas |
| `formatos_datos_leeme.txt` | Guía conversión Parquet/HDF5 |
| `fuentes_datos.bib` | Bibliografía BibTeX |
| `LEEME.md` | Descripción del conjunto de datos |

## Cita

> de la Serna, Juan Moises, 2026, "Biomarcadores de Neuroinflamación en Depresión y Trastornos Mentales: Datos Globales 2020-2024", Harvard Dataverse, V1. https://doi.org/10.7910/DVN/OCXEK7

## Autor

**Juan Moises de la Serna** | ORCID: [0000-0002-8401-8018](https://orcid.org/0000-0002-8401-8018)  
Universidad Internacional de La Rioja (UNIR) | Investigador en Epigenética Conductual y Neuroeducación

## Licencia

[Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
