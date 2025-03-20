import sys
import pandas as pd
import numpy as np
from scipy import stats

def load_data(file_path):
    """Lexon të dhënat nga CSV dhe i kthen si DataFrame"""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Gabim gjatë leximit të skedarit: {e}")
        sys.exit(1)

def calculate_stats(df, column):
    """Llogarit statistikat bazë për një kolonë të dhënë"""
    if column not in df.columns:
        print(f"Kolona '{column}' nuk u gjet në të dhëna.")
        return
    data = df[column]
    print(f"Statistikat për {column}:")
    print(f"Mesatarja: {np.mean(data):.2f}")
    print(f"Mediana: {np.median(data):.2f}")
    print(f"Modaliteti: {stats.mode(data, keepdims=True)[0][0]}")
    print(f"Devijimi Standard: {np.std(data, ddof=1):.2f}")

def generate_text_histogram(df, column, bins=10):
    """Gjeneron një histogram të bazuar në tekst"""
    if column not in df.columns:
        print(f"Kolona '{column}' nuk u gjet në të dhëna.")
        return
    data = df[column]
    hist, bin_edges = np.histogram(data, bins=bins)
    print(f"Histogrami për {column}:")
    for i in range(len(hist)):
        print(f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f}: {'#' * hist[i]}")

def find_correlation(df, col1, col2):
    """Gjen korrelacionin mes dy kolonave"""
    if col1 not in df.columns or col2 not in df.columns:
        print("Njëra nga kolonat nuk u gjet në të dhëna.")
        return
    correlation = df[col1].corr(df[col2])
    print(f"Korrelacioni mes {col1} dhe {col2}: {correlation:.2f}")

def detect_outliers(df, column, threshold=2.0):
    """Identifikon pikat e jashtme duke përdorur Z-score"""
    if column not in df.columns:
        print(f"Kolona '{column}' nuk u gjet në të dhëna.")
        return
    data = df[column]
    z_scores = np.abs(stats.zscore(data))
    outliers = df[z_scores > threshold]
    print(f"Pikat e jashtme për {column} (Threshold={threshold}):")
    print(outliers)

def main():
    if len(sys.argv) < 4:
        print("Përdorimi: python data_analysis.py <file> <command> <column> [options]")
        return
    
    file_path = sys.argv[1]
    command = sys.argv[2]
    column = sys.argv[3]
    df = load_data(file_path)
    
    if command == "stats":
        calculate_stats(df, column)
    elif command == "histogram":
        bins = int(sys.argv[4]) if len(sys.argv) > 4 else 10
        generate_text_histogram(df, column, bins)
    elif command == "correlation":
        if len(sys.argv) < 5:
            print("Përdorimi: python data_analysis.py <file> correlation <column1> <column2>")
            return
        find_correlation(df, column, sys.argv[4])
    elif command == "outliers":
        threshold = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
        detect_outliers(df, column, threshold)
    else:
        print("Komandë e panjohur.")

if __name__ == "__main__":
    main()