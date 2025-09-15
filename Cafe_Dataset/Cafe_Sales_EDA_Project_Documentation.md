
   # Cafe Sales — Exploratory Data Analysis (EDA) Project Documentation

   **Audience:** Hiring Managers, Data Leaders  
   **Environment:** python 3.13.5 (kernel: python3)


   ## Project Goal
   Understand sales performance for a cafe: what sells, when, and where revenue comes from — and translate findings into concrete actions (pricing, stock, staffing, promotions).

   ## Data Sources
   - C:\\Users\\Admin\\Downloads\\archive (17)\\dirty_cafe_sales.csv

   ## Method & Workflow
   1. **Data Loading** — Import raw datasets (transactions, items, prices, dates) into pandas.
   2. **Initial Profiling** — Quick shape, dtypes, missingness, and range checks to validate integrity.
   3. **Data Cleaning & Preparation**
      - Handle missing values (e.g., quantity, unit price, totals).
      - Standardize date/time formats and derive month/week/day features.
      - Normalize categories (item names, locations) and remove duplicates.
      - Compute consistent metrics (e.g., `total_spent = quantity * price_per_unit`).
   4. **Exploratory Analysis**
      - Univariate: distributions of sales, quantity, price; top items/locations.
      - Bivariate: revenue by month, by item, by location; average basket size.
      - Time Series: monthly trends, seasonal patterns, weekday & hour effects.
   5. **Visualization**
      - Bar/line charts for revenue and quantity trends.
      - Heatmaps (item × month / weekday × hour) for demand patterns.
   6. **Insight Synthesis**
      - Translate visual/quant findings into actionable recommendations.
   7. **Reproducibility**
      - Keep transformations in code; document assumptions; parameterize paths.

   ## Key Insights (Mapped to Business Actions)
   - Top items and their revenue share.
   - Time-of-day and day-of-week demand peaks.
   - Monthly trend and seasonality to guide promotions.
   - Location-based performance differences.

   ---

   ## Data Description (What’s in the Data)
   - **Entities:** transactions (date/time, item, quantity, price_per_unit, total_spent), locations/branches (if present), and derived date parts (year, month, week, weekday, hour).
   - **Granularity:** one row per transaction (or line-item).  
   - **Time Range:** Determined by the dataset (see notebook for exact min/max dates).  
   - **Target Metrics:** revenue (`total_spent`), volume (`quantity`), average selling price (`price_per_unit`).

   ## Assumptions & Business Rules
   - `total_spent = quantity × price_per_unit` (recomputed when missing/incorrect).
   - Date strings are converted to timezone-naïve timestamps; business day/week definitions follow calendar defaults.
   - Category and item name normalization performed using string cleaning (case, whitespace, known aliases).

   ## Deliverables
   - Cleaned, analysis-ready dataset.
   - Visuals: revenue over time, top items, demand by weekday/hour, item-by-month heatmap.
   - Insight summary with recommendations.
   - This documentation for Hiring Managers.

   ## Reproducibility & Environment
   - **Language:** python 3.13.5  
   - **Libraries:** pandas, numpy, matplotlib/plotly/seaborn (as used in notebook).  
   - **Execution:** Re-run all cells; parameterize file paths for portability.  
   - **Versioning:** Store notebook and this doc under source control; consider adding a `requirements.txt`.

   ## Detailed Steps & Purpose (from notebook)
   | Notebook Cell # | Purpose / Step Type | First lines (preview) |
   | --- | --- | --- |
   | 0 | Visualization | import skimpy as sk import pandas as pd import numpy as np import seaborn as sns import matplotlib.pyplot as plt |
   | 1 | Load data | data = pd.read_csv("C:\\Users\\Admin\\Downloads\\archive (17)\\dirty_cafe_sales.csv") |
   | 2 | Other | sk.skim(data) |
   | 3 | Inspect/Overview | data.head(25) |
   | 4 | Other | data.columns = [col.strip().replace(" ","_").lower() for col in data.columns] data.columns |
   | 5 | Aggregation/Feature Eng, Cleaning/Transform | for i in data.columns:     grouped = data.groupby(i)[i].count()       print(f"Grouping by {i}:")     print(grouped)      |
   | 6 | Other | nulls = ["ERROR","UNKNOWN"] data.loc[data['item'].isin(nulls), 'item'] = np.nan data.loc[data['payment_method'].isin(nul |
   | 7 | Cleaning/Transform | data.fillna({     'item': "Other",      'location': "Undefined",      'payment_method': "Unknown" }, inplace=True) |
   | 8 | Cleaning/Transform | data['transaction_date'] = pd.to_datetime(data['transaction_date'],errors='coerce') |
   | 9 | Cleaning/Transform | median_date = data['transaction_date'].median()   data.fillna({'transaction_date': median_date}, inplace=True) |
   | 10 | Cleaning/Transform | data = data.dropna(subset=['quantity','price_per_unit'], how='all') data = data.dropna(subset=['quantity','total_spent'] |
   | 11 | Other | data['quantity'] = pd.to_numeric(data['quantity'],errors='coerce') data['price_per_unit'] = pd.to_numeric(data['price_pe |
   | 12 | Cleaning/Transform | data['total_spent'] = data['total_spent'].fillna(data['quantity'] * data['price_per_unit']) data['quantity'] = data['qua |
   | 13 | Inspect/Overview | data.head(25) |
   | 14 | Visualization | data.hist(figsize=(12, 8), bins=50, edgecolor="black")   plt.suptitle("Distribution of Numeric Features", fontsize=14)   |
   | 15 | Visualization | sns.scatterplot(data=data,x=data['quantity'], y=data['total_spent'],hue = 'item' ,alpha=0.5)   plt.title("Relationship b |
   | 16 | Aggregation/Feature Eng, Cleaning/Transform, Visualization | plt.figure(figsize=(8, 5))   sns.boxplot(y=data.groupby('item')['total_spent'].sum())   plt.title("Boxplot of Price: Det |
   | 17 | Visualization | corr_matrix = data.corr(numeric_only=True) sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu") |

   ## Recommendations (Linking Insights to Actions)
   - **Top sellers:** Ensure stock priority, negotiate vendor terms, consider upsell bundles.
   - **Seasonality:** Align promotions with peak months; pre-stock seasonal bestsellers.
   - **Peak hours:** Schedule staff to match demand; prep hot items ahead of rush.
   - **Locations:** Replicate high-performing assortments; pilot price tests in stable branches.
   - **Pricing:** Test small price lifts on inelastic items; offer bundles/loyalty perks for price-sensitive items.

   ## Next Steps
   - Add margin/cost data to shift insights from revenue to profitability.
   - Build a simple forecasting model for weekly demand by item.
   - Deploy a lightweight dashboard (e.g., Streamlit) for ongoing monitoring.
   - Instrument data quality checks (schema, ranges, nulls) with Great Expectations.

   ## Appendix — Code Map
   - The table above maps each code cell to its role (load / clean / visualize / aggregate / model). Review previews to find relevant transformations quickly.
