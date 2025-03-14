# Yamanote Line Station Dataset

This repository contains a clean, structured dataset of stations along the **Yamanote Line** in Tokyo, Japan — one of the busiest and most iconic urban rail loops in the world. The dataset was compiled for a research project exploring data visualisation practices in UX/UI and digital humanities.

## 📂 Dataset Contents

- `data/yamanote_stations.csv`  
  A CSV file listing station names in Japanese and English, distance between stations, and cumulative distance from **Shinagawa Station** (reference point).

| Column | Description |
|--------|-------------|
| `Station_Japanese` | Station name in Japanese script |
| `Station_English` | Station name in English |
| `Distance_between` | Distance in km from the previous station |
| `Distance_from_Shinagawa` | Cumulative distance from Shinagawa Station in km |

## 📈 Example Use Case

This dataset is used in a [React-based data visualisation project](https://github.com/your-username/your-phd-website) using **Carbon Design System Charts**, with responsive layouts and animated interactions for researchers, designers, and educators.

## 📜 Source

- **Original data scraped from:**  
  [Simple English Wikipedia – Yamanote Line](https://simple.wikipedia.org/wiki/Yamanote_Line)

- Data was extracted using a custom Python script with `BeautifulSoup` and `pandas`. See [`scripts/yamanote_scraper.py`](scripts/yamanote_scraper.py) for reproducibility.

## 💡 Citation

If you use this dataset in your research, teaching, or visualisation work, please cite as: Newman, G.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

