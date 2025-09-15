# ☕ Cafe Sales — Data Cleaning & EDA Project

**Project Statement**  
This is a **practice project** focused on honing my data cleaning skills and exploratory data analysis (EDA) through visualizations.  
The goal is to solve key business problems and gain insights into methods that can be extended further to derive value from sales data.  

---

## 1. Project Goal  
Understand sales performance for a cafe: what sells, when, and where revenue comes from — and translate findings into concrete actions (pricing, stock, staffing, promotions).  

---

## 2. Data Sources  
- Raw CSV file: `dirty_cafe_sales.csv`  
- Environment: Python 3.13.5  
- Libraries: pandas, numpy, seaborn, matplotlib, plotly  

---

## 3. Issues, Strategies & Resolutions  

### 3.1 Data Quality Issues  
**Observed Issues**  
- Missing values in `item`, `location`, `payment_method`, `transaction_date`, `quantity`, `price_per_unit`, `total_spent`.  
- Duplicate or inconsistent entries (e.g., “Latte ” vs. “latte”).  
- Erroneous placeholders (`ERROR`, `UNKNOWN`).  
- Wrong dtypes: dates stored as strings, quantities as text.  
- Inconsistent or missing revenue calculations (`total_spent`).  

**Strategies & Resolutions**  

```python
# Detect placeholders and replace with NaN
nulls = ["ERROR", "UNKNOWN"]
data.loc[data['item'].isin(nulls), 'item'] = np.nan
data.loc[data['payment_method'].isin(nulls), 'payment_method'] = np.nan

# Fill categorical nulls with defaults
data.fillna({
    'item': "Other",
    'location': "Undefined",
    'payment_method': "Unknown"
}, inplace=True)

# Convert datatypes
data['transaction_date'] = pd.to_datetime(data['transaction_date'], errors='coerce')
data['quantity'] = pd.to_numeric(data['quantity'], errors='coerce')
data['price_per_unit'] = pd.to_numeric(data['price_per_unit'], errors='coerce')

# Impute missing date with median
median_date = data['transaction_date'].median()
data['transaction_date'].fillna(median_date, inplace=True)

# Recompute revenue if missing
data['total_spent'] = data['quantity'] * data['price_per_unit']
```

**Justification**:  
- Imputations minimize data loss.  
- Normalization prevents duplicate categories.  
- Type conversions enable time-series analysis.  
- Recalculated revenue ensures consistency.  

---

## 4. Exploratory Data Analysis  

### 4.1 Distributions  

```python
# Histogram of numeric features
data.hist(figsize=(12, 8), bins=50, edgecolor="black")
plt.suptitle("Distribution of Numeric Features", fontsize=14)
plt.show()
```  

📊 **Result:** Clear view of quantity, unit price, and revenue distributions. Helped identify outliers.  

---

### 4.2 Relationships  

```python
# Quantity vs. Revenue by item
sns.scatterplot(data=data, x='quantity', y='total_spent', hue='item', alpha=0.5)
plt.title("Relationship between Quantity and Revenue by Item")
plt.show()
```  

📊 **Result:** Items with higher unit price but lower quantity (premium drinks) contributed similar revenue to high-quantity, low-price items (snacks).  

---

### 4.3 Time Series  

```python
# Revenue by month
data['month'] = data['transaction_date'].dt.to_period('M')
monthly_revenue = data.groupby('month')['total_spent'].sum()

monthly_revenue.plot(kind='line', figsize=(10,5), marker='o')
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.show()
```  

📊 **Result:** Seasonal peaks were identified, suggesting promotional opportunities before busy months.  

---

### 4.4 Heatmaps  

```python
# Heatmap of demand by weekday & hour
data['weekday'] = data['transaction_date'].dt.day_name()
data['hour'] = data['transaction_date'].dt.hour

heatmap_data = data.groupby(['weekday','hour'])['total_spent'].sum().unstack()

sns.heatmap(heatmap_data, cmap="YlGnBu")
plt.title("Revenue Heatmap by Weekday & Hour")
plt.show()
```  

📊 **Result:** Strong lunchtime and evening peaks confirmed staffing should be adjusted to match demand.  

---

## 5. Insights & Business Actions  

- **Top sellers:** Prioritize stock, negotiate vendor discounts, create upsell bundles.  
- **Peak times:** Align staffing and prep with demand peaks.  
- **Seasonality:** Run targeted promotions before peak months.  
- **Location differences:** Standardize assortments based on high-performing branches.  
- **Pricing:** Test small price lifts on inelastic items and loyalty perks for price-sensitive products.  

---

## 6. Reproducibility & Best Practices  

- All transformations coded in Python.  
- Notebook + documentation tracked in source control.  
- File paths parameterized for portability.  
- Data quality checks integrated at each step.  

---

## 7. Next Steps  

- Add **cost data** → shift insights from revenue to profitability.  
- Build a **forecasting model** for weekly demand.  
- Deploy a **dashboard** (Streamlit/Power BI).  
- Add **automated data validation** with Great Expectations.  

---

✅ This documentation blends **strategies, resolutions, code, and visuals** to demonstrate both technical competence and business-oriented impact.  
