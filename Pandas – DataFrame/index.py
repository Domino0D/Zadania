import pandas as pd

stores_df = pd.read_csv('stores data-set.csv')
sales_df = pd.read_csv('sales data-set.csv')

store_types_counts = stores_df['Type'].value_counts()

size_statistics = stores_df['Size'].describe(percentiles=[0.25, 0.75])

size_statistics_by_type = stores_df.groupby('Type')['Size'].describe(percentiles=[0.25, 0.75])

sales_df['Date'] = pd.to_datetime(sales_df['Date'])
sales_df['Year'] = sales_df['Date'].dt.year
sales_df['Month'] = sales_df['Date'].dt.month

sales_df = sales_df.merge(stores_df[['Store', 'Type', 'Size']], on='Store', how='left')

monthly_sales_counts = sales_df.groupby(['Year', 'Month', 'Store']).size().groupby(['Year', 'Month']).size()

average_weekly_sales_by_year = sales_df.groupby('Year')['Weekly_Sales'].mean()

average_sales_holiday = sales_df.groupby('IsHoliday')['Weekly_Sales'].mean()

monthly_average_sales = sales_df.groupby(['Year', 'Month'])['Weekly_Sales'].mean().unstack(level=0)

sales_df['Sales_per_Size'] = sales_df['Weekly_Sales'] / sales_df['Size']

average_sales_2012 = sales_df[sales_df['Year'] == 2012].groupby('Store')['Weekly_Sales'].mean()
lowest_sales_store_2012 = average_sales_2012.idxmin()
highest_sales_store_2012 = average_sales_2012.idxmax()

average_sales_per_size_2012 = sales_df[sales_df['Year'] == 2012].groupby('Store')['Sales_per_Size'].mean()
lowest_sales_per_size_store_2012 = average_sales_per_size_2012.idxmin()
highest_sales_per_size_store_2012 = average_sales_per_size_2012.idxmax()

average_sales_by_year_and_type = sales_df.groupby(['Year', 'Type'])['Weekly_Sales'].mean()
average_sales_per_size_by_year_and_type = sales_df.groupby(['Year', 'Type'])['Sales_per_Size'].mean()

# Wyniki
print("Liczba sklepów danego typu:\n", store_types_counts)
print(store_types_counts.to_string(header=False, name=False))
print("\nStatystyki dla rozmiaru sklepów:\n", size_statistics)
print(size_statistics.to_string(header=False, name=False))
print("\nStatystyki dla rozmiaru sklepów w podziale na typy:\n", size_statistics_by_type)
print("\nLiczba sklepów prowadzących sprzedaż w każdym miesiącu każdego roku:\n", monthly_sales_counts)
print("\nŚredni poziom tygodniowej sprzedaży dla każdego roku:\n", average_weekly_sales_by_year)
print("\nŚrednia tygodniowa sprzedaż zależna od występowania święta:\n", average_sales_holiday)
print(average_sales_holiday.to_string(header=False, name=False))
print("\nŚrednia tygodniowa sprzedaż charakteryzująca się sezonowością roczną:\n", monthly_average_sales)
print(monthly_average_sales.to_string(header=False))
print("\nSklepy z najniższą i najwyższą średnią tygodniową sprzedażą w 2012 roku:\n", lowest_sales_store_2012, highest_sales_store_2012)
print("\nSklepy z najniższą i najwyższą średnią tygodniową sprzedażą na jednostkę powierzchni w 2012 roku:\n", lowest_sales_per_size_store_2012, highest_sales_per_size_store_2012)
print("\nŚredni poziom tygodniowej sprzedaży oraz sprzedaży na jednostkę powierzchni dla każdego roku i typu sklepu:\n", average_sales_by_year_and_type)
print(average_sales_by_year_and_type.to_string(header=False, name=False))
print("\n", average_sales_per_size_by_year_and_type)
print(average_sales_per_size_by_year_and_type.to_string(header=False, name=False))

