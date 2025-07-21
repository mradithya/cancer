import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
output_dir = 'plots'
os.makedirs(output_dir, exist_ok=True)

# Load the CSV file
file_path = 'C:/Users/Adithya G B/OneDrive/Desktop/cancer_analytics/cancer_data.csv'
df = pd.read_csv("cancer_data.csv")

# ========== Basic Data Summary ==========
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include='all'))

print("\nMissing Values:")
print(df.isnull().sum())

# ========== Visualizations ==========

# 1. Diagnosis Count
if 'diagnosis' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='diagnosis', palette='Set2')
    plt.title("Cancer Diagnosis Count")
    plt.xlabel("Diagnosis")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/diagnosis_count.png")
    plt.close()

# 2. Correlation Heatmap
plt.figure(figsize=(12, 8))
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlation = numeric_df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig(f"{output_dir}/correlation_heatmap.png")
plt.close()

# 3. Gender Pie Chart
if 'gender' in df.columns:
    gender_counts = df['gender'].value_counts()
    plt.figure(figsize=(5, 5))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title("Gender Distribution")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/gender_distribution.png")
    plt.close()

# 4. Age Histogram
if 'age' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df['age'], bins=20, kde=True, color='purple')
    plt.title("Age Distribution of Cancer Patients")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/age_distribution.png")
    plt.close()

# 5. Tumor Size by Diagnosis
if 'diagnosis' in df.columns and 'tumor_size' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.barplot(data=df, x='diagnosis', y='tumor_size', palette='pastel', ci='sd')
    plt.title("Average Tumor Size by Diagnosis")
    plt.xlabel("Diagnosis")
    plt.ylabel("Tumor Size")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tumor_size_by_diagnosis.png")
    plt.close()

# 6. Age Boxplot by Diagnosis
if 'age' in df.columns and 'diagnosis' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x='diagnosis', y='age', palette='Set3')
    plt.title("Age Distribution by Diagnosis Type")
    plt.xlabel("Diagnosis")
    plt.ylabel("Age")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/age_by_diagnosis.png")
    plt.close()

# 7. Swarmplot
if 'tumor_size' in df.columns and 'diagnosis' in df.columns and 'gender' in df.columns:
    try:
        plt.figure(figsize=(7, 5))
        sns.swarmplot(data=df, x='diagnosis', y='tumor_size', hue='gender', palette='Dark2', dodge=True)
        plt.title("Tumor Size by Diagnosis and Gender")
        plt.xlabel("Diagnosis")
        plt.ylabel("Tumor Size")
        plt.legend(title="Gender")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/swarmplot_tumor_size_gender.png")
        plt.close()
    except:
        print("Swarmplot skipped due to size or data error.")

# 8. Gender vs Diagnosis Count
if 'diagnosis' in df.columns and 'gender' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='diagnosis', hue='gender', palette='Set1')
    plt.title("Diagnosis Count Grouped by Gender")
    plt.xlabel("Diagnosis")
    plt.ylabel("Count")
    plt.legend(title="Gender")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/diagnosis_by_gender.png")
    plt.close()
