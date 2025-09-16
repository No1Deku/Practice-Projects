Animal Data Cleaning & Analysis Project
A comprehensive data cleaning and analysis project focused on transforming messy animal observation data from Central and Eastern Europe into a reliable, analysis-ready dataset.
📋 Project Overview
This project demonstrates systematic data cleaning techniques applied to a dataset containing approximately 1,000 animal observations collected between March and June 2024. The dataset includes various wildlife species (European Bison, Red Squirrel, Hedgehog, Lynx) observed across Central and Eastern European countries.
Key Objectives

Data Quality Improvement: Transform raw, messy data into a clean, structured dataset
Geospatial Analysis: Enable reliable geographic analysis of animal distributions
Visualization Ready: Prepare data for interactive mapping and dashboard creation

🎯 Dataset Characteristics
Original Data Issues:

Malformed CSV structure (semicolon-separated values in single column)
Inconsistent country naming conventions
Mixed date formats across different data collectors
Missing values and null entries
Duplicate records
Negative values in measurement fields
Inconsistent animal type naming

Final Clean Dataset:

Standardized column structure (11 attributes)
Consistent country names
Standardized date formats
Imputed missing values using statistical methods
Deduplicated records (1,011 → 820 unique records)
Validated measurement ranges

🔧 Technical Stack
python- pandas: Data manipulation and analysis
- duckdb: In-memory SQL operations for complex data transformations
- matplotlib & seaborn: Data visualization
- skimpy: Dataset profiling and summary statistics
📊 Data Schema
ColumnData TypeDescriptionanimal_typeVARCHARSpecies name (European Bison, Red Squirrel, Hedgehog, Lynx)countryVARCHARCountry of observationweight_kgFLOATAnimal weight in kilogramsbody_length_cmFLOATBody length in centimetersgenderVARCHARAnimal gender (male/female/Not Specified)animal_codeVARCHARUnique identifier (mostly NULL)latitudeFLOATGeographic coordinatelongitudeFLOATGeographic coordinateanimal_nameVARCHARIndividual animal nameobservation_dateVARCHARDate of observationdata_compiled_byVARCHARData collector name
🔄 Data Cleaning Workflow
Phase 1: Data Structure Repair
sql-- Extract semicolon-separated values into proper columns
UPDATE data
SET 
    animal_type = SPLIT_PART(ref, ';', 1),
    country = SPLIT_PART(ref, ';', 2),
    weight_kg = SPLIT_PART(ref, ';', 3),
    -- ... additional columns
Phase 2: Data Standardization

Country Normalization: Standardized country codes and names

Hungary, Hungry, HU → Hungary
Czech, CZ, Czech Republic → Czech Republic
PL → Poland, DE → Germany


Species Name Correction:

wedgehod, ledgehod, hedgehog → hedgehog
red squir% → red squirrel
Various European Bison spellings → European Bison



Phase 3: Data Type Conversion & Validation
sql-- Convert string columns to appropriate numeric types
ALTER TABLE data ALTER COLUMN weight_kg SET DATA TYPE FLOAT;
ALTER TABLE data ALTER COLUMN body_length_cm SET DATA TYPE FLOAT;
ALTER TABLE data ALTER COLUMN latitude SET DATA TYPE FLOAT;
ALTER TABLE data ALTER COLUMN longitude SET DATA TYPE FLOAT;
Phase 4: Missing Value Treatment

Statistical Imputation: Used group averages by animal type and country
Logical Defaults:

gender = 'Not Specified' for NULL gender values
animal_name = 'Not Assigned' for unnamed animals



Phase 5: Data Quality Assurance

Duplicate Removal: Reduced dataset from 1,011 to 820 unique records
Value Validation: Applied absolute values to negative measurements
Precision Standardization: Rounded coordinates and measurements to 2 decimal places

📈 Data Quality Improvements
MetricBefore CleaningAfter CleaningImprovementTotal Records1,011820191 duplicates removedMissing Animal Types1818Preserved for analysisMissing Countries1111Preserved for analysisMissing WeightsVariable11Significant improvementMissing Coordinates7272Geographic gaps identifiedStandardized Country NamesNoYes100% consistencyStandardized Species NamesNoYes100% consistency
🗺️ Geographic Coverage
Countries Included:

Poland
Hungary
Czech Republic
Germany
Slovakia
Austria
Australia (limited observations)

Species Distribution:

European Bison: Primarily Poland, some Slovakia observations
Red Squirrel: Widespread across Germany, Poland, Hungary
Hedgehog: Central European countries
Lynx: Mountain regions, primarily Poland and Hungary

📅 Temporal Coverage
Observation Period: March 2024 - July 2024
Peak Activity: March and April 2024 (highest observation counts)
Data Collectors: 4 primary researchers (Anne Anthony, Bob Bobson, James Johnson, John Johnson)
🚀 Usage Examples
Loading the Clean Dataset
pythonimport pandas as pd
import duckdb

# Connect to the cleaned data
con = duckdb.connect()
df_clean = con.query("SELECT * FROM data").df()

# Basic statistics
print(df_clean.describe())
print(df_clean.groupby(['animal_type', 'country']).size())
Geographic Analysis
python# Animals by country
country_distribution = df_clean.groupby('country')['animal_type'].count()

# Coordinate-based filtering for mapping
mapped_animals = df_clean[df_clean['latitude'].notnull() & 
                         df_clean['longitude'].notnull()]
📁 Project Structure
animal-data-cleaning/
├── data/
│   ├── animal_data_dirty1.csv      # Original messy dataset
│   └── animal_data_clean.csv       # Cleaned dataset (output)
├── notebooks/
│   └── animal_data_cleaning.ipynb  # Main cleaning workflow
├── scripts/
│   ├── data_cleaning.py           # Modular cleaning functions
│   └── validation.py              # Data quality checks
├── visualizations/
│   ├── geographic_distribution.py  # Mapping scripts
│   └── statistical_analysis.py    # Analysis notebooks
└── README.md
🔍 Key Insights from Cleaned Data

Geographic Clustering: European Bison observations concentrated in Eastern Europe
Seasonal Patterns: Peak observation activity in early spring months
Data Collector Bias: Different formatting conventions by researcher
Species Size Patterns: Consistent measurement ranges after cleaning
Missing Geographic Data: 9% of records lack coordinate information

🎯 Next Steps & Applications
Potential Analysis Directions:

Interactive Mapping: Folium-based choropleth and heatmaps
Species Distribution Modeling: Habitat preference analysis
Temporal Analysis: Seasonal migration patterns
Statistical Modeling: Size-weight relationships by species
Conservation Insights: Population density estimates

Visualization Opportunities:

Species distribution heatmaps
Country-wise observation dashboards
Temporal trends and seasonality
Size distribution analysis
Data quality scorecards

🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/analysis-enhancement)
Commit your changes (git commit -am 'Add species analysis')
Push to the branch (git push origin feature/analysis-enhancement)
Create a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

Dataset artificially generated for educational purposes
Inspired by real wildlife observation methodologies
Built with modern data science best practices


Project Status: ✅ Data Cleaning Complete | 🔄 Analysis In Progress | 📊 Visualization Pending
For questions or collaboration opportunities, please open an issue or contact the maintainer.