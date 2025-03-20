# Mjeti për Analizën e CSV (CLI)

Ky është një mjet komandë-line i ndërtuar në Python që analizon të dhënat nga skedarët CSV. Ofron statistika bazë, krijon histograme, gjen korrelacione dhe identifikon outliers.

## 🚀 Instalimi

Së pari, sigurohu që ke instaluar varësitë:

```sh
pip install -r requirements.txt
```

## 🛠️ Përdorimi

Për të përdorur mjetin, ekzekuto komandat si më poshtë:

### ✅ Llogarit statistikat për një kolonë
```sh
python data_analysis.py sample_data.csv stats temperature
```

### ✅ Krijo histogram për një kolonë
```sh
python data_analysis.py sample_data.csv histogram humidity 10
```

### ✅ Gjej korrelacionin midis dy kolonave
```sh
python data_analysis.py sample_data.csv correlation temperature humidity
```

### ✅ Gjej outliers për një kolonë me prag 2.0
```sh
python data_analysis.py sample_data.csv outliers wind_speed 2.0
```

## 📌 Shembulli i `sample_data.csv`

Skedari `sample_data.csv` duhet të përmbajë të dhëna numerike si më poshtë:

```
id,temperature,humidity,pressure,wind_speed
1,22.5,65,1013,3.5
2,24.0,70,1012,4.0
3,21.0,60,1015,2.8
4,23.5,75,1011,5.2
```

## 🤖 Përdorimi i AI

- Përdorur për krijimin e bazës së kodit dhe dokumentimit.
- Modifikime të bëra manualisht për trajtimin e gabimeve dhe optimizimin.

## 🔥 Sfidat dhe Zgjidhjet

- **Trajtimi i gabimeve**: U shtuan mesazhe gabimi për skedarë të munguar dhe të dhëna të pavlefshme.
- **Histogrami**: Përdorimi i `matplotlib` për të krijuar vizualizime të qarta.
- **Outliers**: Implementim me `scipy.stats.zscore` për të identifikuar vlerat ekstreme.

## 📜 Licenca
Ky projekt është i lirë për përdorim dhe shpërndarje. 🚀
