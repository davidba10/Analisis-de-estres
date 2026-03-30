# Análisis de estrés

Proyecto de Machine Learning para analizar y modelar el nivel de estrés a partir de hábitos de uso de móvil, sueño, actividad física y fatiga mental.

El repositorio incluye:
- Notebook de exploración, feature engineering y modelado.
- Estructura modular en `src/` para escalar a pipeline productivo.
- Configuración base y carpetas separadas por etapa de datos.

## Objetivo

Construir modelos de regresión y clasificación para estudiar `stress_level` y entender qué variables tienen mayor impacto en el estrés percibido.

## Dataset

- Archivo principal: `data/raw/sleep_mobile_stress_dataset_15000.csv`
- Fuente de trabajo: dataset tabular con variables demográficas, hábitos digitales y de sueño.
- Variables relevantes del análisis (entre otras):
	- `daily_screen_time_hours`
	- `phone_usage_before_sleep_minutes`
	- `sleep_duration_hours`
	- `sleep_quality_score`
	- `mental_fatigue_score`
	- `stress_level`

## Estructura del proyecto

```text
.
├─ configs/                    # Configuración del proyecto (YAML)
├─ data/
│  ├─ raw/                     # Datos originales
│  ├─ interim/                 # Datos intermedios
│  ├─ processed/               # Datos listos para modelado
│  └─ external/                # Datos externos opcionales
├─ models/                     # Modelos entrenados y artefactos
├─ notebooks/                  # Análisis exploratorio y entrenamiento
├─ reports/
│  └─ figures/                 # Gráficos y resultados exportados
├─ src/analisis_estres/        # Código Python reutilizable
└─ tests/                      # Pruebas
```

## Requisitos

- Python 3.10 o superior
- Dependencias en `requirements.txt`:
	- numpy
	- pandas
	- scikit-learn
	- matplotlib
	- seaborn
	- jupyter
	- pytest
	- pyyaml

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Uso rápido

1. Coloca o valida los datos en `data/raw/`.
2. Abre el notebook `notebooks/entrenamiento.ipynb`.
3. Ejecuta celdas en orden para:
	 - EDA
	 - Feature engineering
	 - Entrenamiento de modelos
	 - Evaluación de métricas

Para lanzar Jupyter:

```bash
jupyter notebook
```

## Módulos en `src/analisis_estres`

- `config.py`: rutas del proyecto centralizadas.
- `data/make_dataset.py`: carga inicial de CSV.
- `features/build_features.py`: transformaciones de features (base).
- `models/train.py`: baseline de clasificación con `DummyClassifier`.
- `visualization/plots.py`: estilo común para gráficos.
- `utils/io.py`: utilidades de E/S (creación de directorios, etc.).

Ejemplo de uso desde Python:

```python
from analisis_estres.data.make_dataset import load_csv
from analisis_estres.features.build_features import build_features
from analisis_estres.models.train import build_baseline_model

df = load_csv("data/raw/sleep_mobile_stress_dataset_15000.csv")
df_features = build_features(df)
modelo = build_baseline_model()
```

## Pruebas

```bash
pytest
```

## Configuración

El archivo `configs/config.yaml` define parámetros globales:
- Nombre de proyecto
- `random_state`
- Rutas de datos/modelos/reports
- Configuración base del modelo

## Flujo recomendado

1. Ingesta de datos (`data/raw`).
2. Limpieza y transformaciones (`data/interim`, `data/processed`).
3. Experimentación en notebook (`notebooks/`).
4. Paso de lógica estable a código reutilizable (`src/`).
5. Entrenamiento y guardado de artefactos (`models/`).
6. Reporte de resultados y visualizaciones (`reports/figures/`).

## Estado actual

- Proyecto en fase de experimentación y benchmark de modelos.
- Notebook principal con pipeline completo de entrenamiento y evaluación.

## Siguiente paso para publicarlo

Antes de subirlo, revisa rápidamente:
- Que el notebook se ejecute de principio a fin sin errores.
- Que las rutas relativas funcionen en un entorno limpio.
- Que `requirements.txt` incluya todas las librerías usadas.

Con eso, está listo para subir a GitHub.
