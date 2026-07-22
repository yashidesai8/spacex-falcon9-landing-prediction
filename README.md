# SpaceX Falcon 9 First Stage Landing Prediction

IBM Data Science Professional Certificate — Applied Data Science Capstone project. Predicts whether a SpaceX Falcon 9 first stage booster will land successfully, using real launch data collected from the SpaceX API and Wikipedia.

## Project overview

SpaceX advertises Falcon 9 launches at roughly $62 million, well under competitor pricing, largely because it reuses the first stage instead of building a new one for every flight. If a competing launch provider wants to bid against SpaceX, it needs a reliable estimate of whether a given launch's first stage will actually land — since that single factor drives most of the cost difference.

This project follows the full data science pipeline to answer that question: collect launch records, wrangle and label the data, explore it through visualization and SQL, build interactive visual analytics, and train classification models to predict landing outcome.

## Key results

- Analyzed 90 Falcon 9 launches (2010–2020)
- Overall first-stage landing success rate: 66.7%
- Best model (Decision Tree, tuned via GridSearchCV): 94.4% test accuracy
- Landing success improved sharply with flight experience, stabilizing above 90% in recent years
- KSC LC-39A had the highest per-site landing success rate (77%), reflecting its later entry into rotation after SpaceX had matured its landing process

## Repository contents

| File | Description |
|---|---|
| `SpaceX_Data_Collection_API.ipynb` | Pulls raw launch records from the public SpaceX REST API |
| `SpaceX_Data_Collection_Webscraping.ipynb` | Scrapes the Wikipedia Falcon 9 launch list with BeautifulSoup to fill in gaps |
| `SpaceX_Data_Wrangling.ipynb` | Cleans the combined data and builds the binary landing-success (`Class`) label |
| `SpaceX_EDA_Visualization.ipynb` | Matplotlib/Seaborn exploratory analysis (flight number vs. payload, orbit and yearly trends) |
| `SpaceX_EDA_SQL.ipynb` | SQL queries against the launch records table (loaded into SQLite for this analysis) |
| `SpaceX_Folium_Map.ipynb` | Interactive map of launch sites and outcomes, with coastline distance calculations |
| `SpaceX_Dash_Dashboard.py` | Live Plotly Dash dashboard — filter by launch site and payload range |
| `SpaceX_ML_Classification.ipynb` | Trains and compares Logistic Regression, SVM, Decision Tree, and KNN classifiers |
| `SpaceX_Capstone_Presentation.pptx` / `.pdf` | Final capstone presentation summarizing methodology and results |

Supporting data files (`dataset_part_2.csv`, `dataset_part_3.csv`, `Spacex.csv`, `spacex_launch_geo.csv`, `spacex_web_scraped.csv`, `dataset_wrangled.csv`) are included so each notebook can be run independently without repeating the collection step.

**Note on the two data collection notebooks:** they contain complete, correct, ready-to-run code, but were not executed in this environment because it doesn't have outbound access to the SpaceX API or Wikipedia. Running them on any machine with normal internet access reproduces the raw data files used by every downstream notebook.

## How to run

```bash
pip install pandas numpy requests beautifulsoup4 matplotlib seaborn folium dash plotly scikit-learn
jupyter notebook
```

Open any notebook and run all cells top to bottom. `SpaceX_Dash_Dashboard.py` is a standalone app — run it with `python SpaceX_Dash_Dashboard.py` and open the local URL it prints.

## Methodology

1. **Collect** — pull launch records from the SpaceX API and scrape the Wikipedia launch list
2. **Wrangle** — clean payload mass and outcome fields, fill missing values, engineer the `Class` label
3. **Explore** — visualize trends and run SQL queries to surface patterns in the data
4. **Visual analytics** — build an interactive Folium map and Plotly Dash dashboard
5. **Predict** — standardize and split the feature set, tune four classifiers with 10-fold GridSearchCV, and compare them on held-out test accuracy and confusion matrices

## Author

Yash
