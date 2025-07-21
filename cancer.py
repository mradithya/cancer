import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io
import os
st.title("Cancer Data Analytics Dashboard")

# Upload CSV File
uploaded_file = st.file_uploader("Upload your cancer_data.csv file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Create output folder (optional for local use)
    output_dir = 'plots'
    os.makedirs(output_dir, exist_ok=True)

    # ========== Basic Data Summary ==========
    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Info")

    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.subheader("Summary Statistics")
    st.write(df.describe(include='all'))

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # ========== Visualizations ==========

    # 1. Diagnosis Count
    if 'diagnosis' in df.columns:
        st.subheader("Cancer Diagnosis Count")
        plt.figure(figsize=(6, 4))
        sns.countplot(data=df, x='diagnosis', hue='diagnosis', palette='Set2', legend=False)
        st.pyplot(plt.gcf())
        plt.clf()

    # 2. Correlation Heatmap
    st.subheader("Feature Correlation Heatmap")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlation = numeric_df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    st.pyplot(plt.gcf())
    plt.clf()

    # 3. Gender Pie Chart
    if 'gender' in df.columns:
        st.subheader("Gender Distribution")
        gender_counts = df['gender'].value_counts()
        plt.figure(figsize=(5, 5))
        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        st.pyplot(plt.gcf())
        plt.clf()

    # 4. Age Histogram
    if 'age' in df.columns:
        st.subheader("Age Distribution of Cancer Patients")
        plt.figure(figsize=(6, 4))
        sns.histplot(df['age'], bins=20, kde=True, color='purple')
        st.pyplot(plt.gcf())
        plt.clf()

    # 5. Tumor Size by Diagnosis
    if 'diagnosis' in df.columns and 'tumor_size' in df.columns:
        st.subheader("Average Tumor Size by Diagnosis")
        plt.figure(figsize=(6, 4))
        sns.barplot(data=df, x='diagnosis', y='tumor_size', palette='pastel', errorbar='sd')
        st.pyplot(plt.gcf())
        plt.clf()

    # 6. Age Boxplot by Diagnosis
    if 'age' in df.columns and 'diagnosis' in df.columns:
        st.subheader("Age Distribution by Diagnosis")
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=df, x='diagnosis', y='age', palette='Set3')
        st.pyplot(plt.gcf())
        plt.clf()

    # 7. Swarmplot: Tumor Size vs Diagnosis and Gender
    if 'tumor_size' in df.columns and 'diagnosis' in df.columns and 'gender' in df.columns:
        st.subheader("Tumor Size by Diagnosis and Gender")
        try:
            plt.figure(figsize=(7, 5))
            sns.swarmplot(data=df, x='diagnosis', y='tumor_size', hue='gender', palette='Dark2', dodge=True)
            st.pyplot(plt.gcf())
            plt.clf()
        except Exception as e:
            st.warning(f"Swarmplot skipped due to: {e}")

    # 8. Gender vs Diagnosis Count
    if 'diagnosis' in df.columns and 'gender' in df.columns:
        st.subheader("Diagnosis Count Grouped by Gender")
        plt.figure(figsize=(6, 4))
        sns.countplot(data=df, x='diagnosis', hue='gender', palette='Set1')
        st.pyplot(plt.gcf())
        plt.clf()

else:
    st.info("Please upload a valid CSV file to begin analysis.")
