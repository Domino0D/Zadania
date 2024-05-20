import pandas as pd

def read_and_prepare_data(file_path, name):
    try:
        data = pd.read_csv(file_path, header=None, index_col=0, parse_dates=True, squeeze=True)
        data.name = name
        data.index.name = 'date'
        return data.sort_index()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.Series(dtype='float64')

gold = pd.read_csv('gc.csv', header=None, index_col=0)
silver = pd.read_csv('si.csv', header=None, index_col=0)

gold = gold.squeeze()
silver = silver.squeeze()

gold.name = 'gold_price_per_ounce'
silver.name = 'silver_price_per_ounce'
gold.index.name = 'date'
silver.index.name = 'date'

gold.index = pd.to_datetime(gold.index)
silver.index = pd.to_datetime(silver.index)

gold = gold['2020':'2022']
silver = silver['2020':'2022']

gold_per_gram = gold / 31.1035
silver_per_gram = silver / 31.1035
gold_per_gram.name = 'gold_price_per_gram'
silver_per_gram.name = 'silver_price_per_gram'

ratio = gold_per_gram / silver_per_gram
days_exceeded_100 = (ratio > 100).sum()
percentage_exceeded_100 = (days_exceeded_100 / len(ratio)) * 100

gold_first_day = gold_per_gram.resample('MS').first()
silver_first_day = silver_per_gram.resample('MS').first()

print(f"Liczba dni, gdy stosunek ceny złota do ceny srebra przekraczał 100: {days_exceeded_100} dni ({percentage_exceeded_100:.2f}% wszystkich dni)")
print("Ceny złota w pierwszych dniach każdego miesiąca:")
print(gold_first_day.to_string(header=False, name=False))

print("\nCeny srebra w pierwszych dniach każdego miesiąca:")
print(silver_first_day.to_string(header=False, name=False))

if '2021-12' in gold_per_gram.index:
    gold_dec_2021 = gold_per_gram['2021-12']
    
    gold_abs_increase = (gold_dec_2021 - gold_dec_2021.shift(1)).idxmax().date()
    print(f"Największy dzienny przyrost ceny złota w grudniu 2021: {gold_abs_increase}")

    gold_pct_increase = ((gold_dec_2021 - gold_dec_2021.shift(1)) / gold_dec_2021.shift(1)).idxmax().date()
    print(f"Największy procentowy przyrost ceny złota w grudniu 2021: {gold_pct_increase}")
    
else:
    print("Brak danych złota dla grudnia 2021.")
    
if '2021-12' in silver_per_gram.index:
    silver_dec_2021 = silver_per_gram['2021-12']

    silver_abs_increase = (silver_dec_2021 - silver_dec_2021.shift(1)).idxmax().date()
    print(f"Największy dzienny przyrost ceny srebra w grudniu 2021: {silver_abs_increase}")

    silver_pct_increase = ((silver_dec_2021 - silver_dec_2021.shift(1)) / silver_dec_2021.shift(1)).idxmax().date()
    print(f"Największy procentowy przyrost ceny srebra w grudniu 2021: {silver_pct_increase}")
    
else:
    print("Brak danych srebra dla grudnia 2021.")

