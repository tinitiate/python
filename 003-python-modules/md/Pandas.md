# Pandas

## DataFrame

- A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure provided by pandas. It can be thought of as a collection of Series, where each column of the DataFrame represents a Series.
-  DataFrames are commonly used to store and manipulate structured data, such as tables from databases or CSV files. They offer a convenient way to organize, analyze, and visualize data.

## Series

- A Series is a one-dimensional labeled array in pandas.
-  It can hold data of any type, including integers, floats, strings, etc.
-  Each element in a Series is associated with a unique label, known as the index. 
- Series are often used to represent a single column of data within a DataFrame, or as standalone data structures to perform operations on smaller chunks of data.

***Examples***

***DataFrame***

```python
import pandas as pd

# Creating a DataFrame for product inventory
data = {'ProductID': [101, 102, 103],
        'Product Name': ['Shoes', 'T-shirt', 'Jeans'],
        'Price': [50, 20, 40],
        'Quantity': [50, 100, 30]}

inventory_df = pd.DataFrame(data)
print(inventory_df)
```

***Series***

```python
import pandas as pd

# Creating a Series for daily sales of a product
sales_data = [10, 15, 8, 12, 20]
sales_series = pd.Series(sales_data, name='Daily Sales')

print(sales_series)
```

**`head()`**: The `head()` method is used to display the first few rows of a DataFrame or Series. By default, it shows the top 5 rows, but you can specify the number of rows to display as an argument.

**`tail()`**: The `tail()` method is used to display the last few rows of a DataFrame or Series. By default, it shows the bottom 5 rows, but you can specify the number of rows to display as an argument.

***Examples***

***Using `head()` and `tail()` with DataFrames***

```python
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 32, 47, 19, 28]}

df = pd.DataFrame(data)

# Using head() to display the top 3 rows
print("Top 3 rows of the DataFrame:")
print(df.head(3))

# Using tail() to display the bottom 2 rows
print("\nBottom 2 rows of the DataFrame:")
print(df.tail(2))
```

***Using `head()` and `tail()` with Series***

```python
import pandas as pd

# Creating a Series
fruits = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])

# Using head() to display the top 4 elements
print("Top 4 elements of the Series:")
print(fruits.head(4))

# Using tail() to display the bottom 3 elements
print("\nBottom 3 elements of the Series:")
print(fruits.tail(3))
```

## Indexing and Slicing 

* Indexing and slicing are foundational techniques for efficiently accessing and manipulating data within Pandas.
* **`loc`**: The `loc` method is primarily label-based indexing. It allows you to access data by specifying row and column labels explicitly.
* **`iloc`**: The `iloc` method is integer position-based indexing. It allows you to access data by specifying integer indices for rows and columns.

### **Indexing**

-  Indexing refers to selecting a specific element or a subset of elements from a Pandas Series or DataFrame. 
- In Pandas, data structures have an index, which can be thought of as labels for the rows or elements.
-  Indexing allows you to access data based on these labels.
- Think of an index as labels for the rows or elements within the data structures.

***Examples***

***Indexing for DataFrames***

```python
import pandas as pd

# Creating a DataFrame for employee information
data = {'EmployeeID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Department': ['HR', 'IT', 'Marketing', 'Finance', 'IT'],
        'Salary': [60000, 75000, 55000, 80000, 70000]}

employees_df = pd.DataFrame(data)

# Display the entire DataFrame
print("Full DataFrame:")
print(employees_df)


# Using loc for indexing (label-based)
employee_bob_loc = employees_df.loc[1]  # Selects the row with index 1 (Bob's details)
print("Using loc for indexing:")
print(employee_bob_loc)

# Using iloc for indexing (integer position-based)
employee_bob_iloc = employees_df.iloc[1]  # Selects the row at position 1 (Bob's details)
print("\nUsing iloc for indexing:")
print(employee_bob_iloc)
```

***Indexing for Series***

```python
import pandas as pd

# Creating a Series for monthly sales data
sales_data = [5000, 7500, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Display the entire Series
print("Full Sales Series:")
print(sales_series)

# Using loc for indexing (label-based)
sales_january_loc = sales_series.loc['January']  # Selects the value for January
print("Using loc for indexing:")
print(sales_january_loc)

# Using iloc for indexing (integer position-based)
sales_january_iloc = sales_series.iloc[0]  # Selects the value at position 0 (January)
print("\nUsing iloc for indexing:")
print(sales_january_iloc)
```

### **Slicing**

- Slicing  is the process of extracting  a range of elements from a data structure.
-  It's like cutting out a portion of your data.
-  In Pandas, you can slice rows and columns based on their labels or integer positions.

***Examples***

*** Slicing for a DataFrame***

```python
import pandas as pd

# Creating a DataFrame for employee information
data = {'EmployeeID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Department': ['HR', 'IT', 'Marketing', 'Finance', 'IT'],
        'Salary': [60000, 75000, 55000, 80000, 70000]}

employees_df = pd.DataFrame(data)
# Display the entire DataFrame
print("Full DataFrame:")
print(employees_df)

# Slicing: Selecting employees in the IT Department
it_department = employees_df[employees_df['Department'] == 'IT']
print("Employees in the IT Department:")
print(it_department)

# Slicing: Selecting specific columns for a subset of employees
selected_columns = employees_df.loc[:, ['Name', 'Salary']]  # Selects 'Name' and 'Salary' columns for all rows
print("\nSelected Columns for All Employees:")
print(selected_columns)

```

***Slicing for a Series***

```python
import pandas as pd

# Creating a Series for monthly sales data
sales_data = [5000, 7500, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Display the entire Series
print("Full Sales Series:")
print(sales_series)

# Using loc for indexing (label-based)
sales_january_loc = sales_series.loc['January']  # Selects the value for January
print("Using loc for indexing:")
print(sales_january_loc)

# Using iloc for indexing (integer position-based)
sales_january_iloc = sales_series.iloc[0]  # Selects the value at position 0 (January)
print("\nUsing iloc for indexing:")
print(sales_january_iloc)
```

***Slicing and Boolean Indexing for a Series***

```python
import pandas as pd

# Creating a Series for monthly sales data
sales_data = [5000, 7500, 6000, 8500, 7000]
months = ['January', 'February', 'March', 'April', 'May']

sales_series = pd.Series(sales_data, index=months)

# Slicing: Selecting sales data for Q1 (January to March)
sales_q1 = sales_series['January':'March']
print("Sales for Q1 (January to March):")
print(sales_q1)

# Boolean Indexing: Selecting months with high sales (above 7000)
high_sales_months = sales_series[sales_series > 7000]
print("\nMonths with High Sales (Above 7000):")
print(high_sales_months)
```

## Handling Missing Data

* In Pandas, missing data is often represented as `NaN` (Not a Number). 
* Pandas provides several methods and techniques to handle missing data effectively within DataFrames.

### **Detecting Missing Data**

* **`isna()` and `isnull()`**: These methods return a DataFrame of the same shape as the original, where each cell contains a Boolean value indicating whether the corresponding element is missing (`True`) or not (`False`).

  ***Examples***

  ***Using `isna()` to Detect Missing Values for a DataFrame***

  ```python
  import pandas as pd
  
  # Creating a DataFrame with missing data
  data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
          'Age': [25, 30, None, 22, 28],
          'Salary': [60000, 75000, 55000, None, 70000]}
  
  employees_df = pd.DataFrame(data)
  
  # Detecting missing values using isna()
  missing_values = employees_df.isna()
  print("Missing Values (using isna()):")
  print(missing_values)
  ```

  ***Using `isna()` to Detect Missing Values in a Series***

  ```python
  import pandas as pd
  
  # Creating a Series with missing data
  sales_data = [5000, None, 6000, 8500, 7000]
  months = ['January', 'February', 'March', 'April', 'May']
  
  sales_series = pd.Series(sales_data, index=months)
  
  # Detecting missing values in the Series using isna()
  missing_values_series_isna = sales_series.isna()
  print("Missing Values in Series (using isna()):")
  print(missing_values_series_isna)
  ```

  ***Using `isnull()` to Detect Missing Values for a DataFrame***

  ```python
  import pandas as pd
  
  # Creating a DataFrame with missing data
  data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
          'Age': [25, 30, None, 22, 28],
          'Salary': [60000, 75000, 55000, None, 70000]}
  
  employees_df = pd.DataFrame(data)
  
  # Detecting missing values using isnull()
  missing_values_null = employees_df.isnull()
  print("Missing Values (using isnull()):")
  print(missing_values_null)
  ```

  ***Using `isnull()` to Detect Missing Values in a Series***

  ```python
  import pandas as pd
  
  # Creating a Series with missing data
  sales_data = [5000, None, 6000, 8500, 7000]
  months = ['January', 'February', 'March', 'April', 'May']
  
  sales_series = pd.Series(sales_data, index=months)
  
  # Detecting missing values in the Series using isnull()
  missing_values_series = sales_series.isnull()
  print("Missing Values in Series (using isnull()):")
  print(missing_values_series)
  ```

### **Dealing with Missing Data**

- **`dropna()`**: This method allows you to drop rows or columns containing missing values. You can specify the `axis` parameter to determine whether to drop rows (`axis=0`) or columns (`axis=1`).

- **`fillna()`**: This method lets you fill missing values with a specified value or a method, like filling with a specific number (`fillna(value)`) or using forward or backward fill (`fillna(method='ffill'/'bfill')`).

- **`interpolate()`**: This method performs interpolation to fill missing values based on other values in the DataFrame. It's useful for time-series data or datasets with ordered indices.

  ***Examples***

  ***Using `dropna()` to Remove Rows Missing Values in a DataFrame***

  ```python
  import pandas as pd
  
  # Creating a DataFrame with missing data
  data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
          'Age': [25, 30, None, 22, 28],
          'Salary': [60000, 75000, 55000, None, 70000]}
  
  employees_df = pd.DataFrame(data)
  
  # Dropping rows with missing values using dropna()
  cleaned_df = employees_df.dropna()
  print("DataFrame after Dropping Rows with Missing Values (dropna()):")
  print(cleaned_df)
  ```

  ***Using `dropna()` to Remove Rows Missing Values in a Series***

  ```python
  import pandas as pd
  
  # Creating a Series with missing data
  sales_data = [5000, None, 6000, 8500, 7000]
  months = ['January', 'February', 'March', 'April', 'May']
  
  sales_series = pd.Series(sales_data, index=months)
  
  # Dropping missing values from the Series using dropna()
  cleaned_series = sales_series.dropna()
  print("Series after Dropping Missing Values (dropna()):")
  print(cleaned_series)
  ```

  ***Using `fillna()` to Fill Missing Values in a DataFrame***

  ```python
  import pandas as pd
  
  # Creating a DataFrame with missing data
  data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
          'Age': [25, 30, None, 22, 28],
          'Salary': [60000, 75000, 55000, None, 70000]}
  
  employees_df = pd.DataFrame(data)
  
  # Filling missing values with a specific value using fillna()
  filled_df = employees_df.fillna({'Age': 0, 'Salary': 0})
  print("DataFrame after Filling Missing Values (fillna()):")
  print(filled_df)
  ```

  ***Using `fillna()` to Fill Missing Values in a Series***

  ```python
  import pandas as pd
  
  # Creating a Series with missing data
  sales_data = [5000, None, 6000, 8500, 7000]
  months = ['January', 'February', 'March', 'April', 'May']
  
  sales_series = pd.Series(sales_data, index=months)
  
  # Filling missing values in the Series with a specified value using fillna()
  filled_series = sales_series.fillna(0)
  print("Series after Filling Missing Values (fillna()):")
  print(filled_series)
  ```

  ***Using `interpolate()` to Fill Missing Values in  a DataFrame***

  ```python
  import pandas as pd
  
  # Creating a DataFrame with missing data
  data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
          'Age': [25, 30, None, 22, 28],
          'Salary': [60000, 75000, 55000, None, 70000]}
  
  employees_df = pd.DataFrame(data)
  
  # Filling missing values with interpolation using interpolate()
  interpolated_df = employees_df.interpolate()
  print("DataFrame after Filling Missing Values with Interpolation (interpolate()):")
  print(interpolated_df)
  ```

  ***Using `interpolate()` to Fill Missing Values in  a Series***

  ```python
  import pandas as pd
  
  # Creating a Series with missing data
  sales_data = [5000, None, 6000, 8500, 7000]
  months = ['January', 'February', 'March', 'April', 'May']
  
  sales_series = pd.Series(sales_data, index=months)
  
  # Filling missing values in the Series with interpolation using interpolate()
  interpolated_series = sales_series.interpolate()
  print("Series after Filling Missing Values with Interpolation (interpolate()):")
  print(interpolated_series)
  ```

## Grouping and Merging 

### Grouping

* Grouping in Pandas refers to the process of grouping data based on one or more categorical variables and then applying operations to each group separately. 
* This is a powerful technique for aggregating and analyzing data within a DataFrame. 
* Pandas provides the `groupby()` method, which is used to create groups of data based on unique values in one or more columns, and then various aggregation functions can be applied to these groups.
* **Creating Groups:**
  - Use the `groupby()` method on a DataFrame to create groups based on one or more columns.
  - Pass the column name(s) to the `groupby()` method to specify the grouping criterion.
* **Applying Aggregation Functions:**
  - After creating groups, you can apply various aggregation functions to compute summary statistics for each group.
  - Common aggregation functions include `sum()`, `mean()`, `median()`, `min()`, `max()`, `count()`, `std()`, `var()`, and more.
* **Accessing Grouped Data:**
  - The grouped object returned by `groupby()` is an iterable that contains groups as well as group labels.
  - We can iterate over these groups or use methods like `get_group()` to access a specific group.
* **Chaining Operations:**
  - We can chain multiple operations after grouping to perform complex analyses.
  - For example, group by multiple columns and then apply different aggregation functions to each group.
* **Resetting Index:**
  - After grouping, the grouped DataFrame might have a multi-level index.
  - Use the `reset_index()` method to reset the index, which can be useful for further manipulation.

***Examples***

***Grouping in DataFrames***

```python
import pandas as pd

# Creating the DataFrame
data = {'Product': ['Shoes', 'T-shirt', 'Jeans', 'Shoes', 'Jeans'],
        'Category': ['Footwear', 'Apparel', 'Apparel', 'Footwear', 'Apparel'],
        'Sales': [100, 50, 70, 120, 90]}

df = pd.DataFrame(data)

# Displaying the original DataFrame
print("Original DataFrame:")
print(df)

# Grouping the data by the 'Category' column
grouped = df.groupby('Category')

# Displaying the grouped object
print("\nGrouped Object:")
print(grouped)

# Applying the 'sum()' aggregation function to the grouped data
sum_by_category = grouped['Sales'].sum()

print("\nTotal Sales by Category:")
print(sum_by_category)

# Accessing a specific group using 'get_group()'
footwear_group = grouped.get_group('Footwear')

print("\nFootwear Group:")
print(footwear_group)

# Grouping by multiple columns and applying multiple aggregation functions
grouped_multiple = df.groupby(['Category', 'Product'])
result = grouped_multiple['Sales'].agg(['sum', 'mean', 'max'])

print("\nGrouped Data with Multiple Aggregations:")
print(result)

# Resetting the index of the grouped DataFrame
result_reset_index = result.reset_index()

print("\nReset Index of Grouped Data:")
print(result_reset_index)

# Using the 'apply()' method to apply a custom aggregation function
def custom_agg(sales_series):
    return sales_series.max() - sales_series.min()

custom_aggregation = grouped['Sales'].apply(custom_agg)

print("\nCustom Aggregation using apply():")
print(custom_aggregation)

# Using the 'transform()' method to broadcast aggregated values to original DataFrame
total_sales_per_category = grouped['Sales'].transform('sum')

df['Total Sales per Category'] = total_sales_per_category

print("\nDataFrame with Transformed Values:")
print(df)

# Using the 'filter()' method to filter groups based on a condition
filtered_groups = grouped.filter(lambda group: group['Sales'].sum() > 150)

print("\nFiltered Groups using filter():")
print(filtered_groups)
```

***Grouping in Series***

```python
import pandas as pd

# Creating a Series with sales data
sales_data = [100, 50, 70, 120, 90]
categories = ['Footwear', 'Apparel', 'Apparel', 'Footwear', 'Apparel']

sales_series = pd.Series(sales_data, index=categories)

# Displaying the original Series
print("Original Series:")
print(sales_series)

# Grouping the Series by index values (categories)
grouped = sales_series.groupby(sales_series.index)

# Displaying the grouped object
print("\nGrouped Object:")
print(grouped)

# Applying the 'sum()' aggregation function to the grouped data
sum_by_category = grouped.sum()

print("\nTotal Sales by Category:")
print(sum_by_category)

# Accessing a specific group using 'get_group()'
footwear_group = grouped.get_group('Footwear')

print("\nFootwear Group:")
print(footwear_group)

# Using the 'apply()' method to apply a custom aggregation function
def custom_agg(sales_series):
    return sales_series.max() - sales_series.min()

custom_aggregation = grouped.apply(custom_agg)

print("\nCustom Aggregation using apply():")
print(custom_aggregation)

# Using the 'transform()' method to broadcast aggregated values to original Series
total_sales_per_category = grouped.transform('sum')

sales_series['Total Sales per Category'] = total_sales_per_category

print("\nSeries with Transformed Values:")
print(sales_series)

# Using the 'filter()' method to filter groups based on a condition
filtered_groups = grouped.filter(lambda group: group.sum() > 150)

print("\nFiltered Groups using filter():")
print(filtered_groups)
```

### Merging

* Merging in Pandas refers to the process of combining multiple DataFrames into a single DataFrame based on common columns or indices. 
* Pandas provides several methods for merging DataFrames, offering flexibility in handling different types of data relationships.
* **Concatenation with `concat()`:**
  - Use the `pd.concat()` function to vertically stack or concatenate multiple DataFrames.
  - It's useful when you want to combine DataFrames with the same columns or indices.
* **Merging with `merge()`:**
  - The `merge()` function performs more advanced merging based on specified columns, similar to SQL joins.
  - You can specify how to combine data using different types of joins: inner, outer, left, or right.
  - You need to specify the `on` parameter, which represents the columns on which to merge.
* **Joining with `join()`:**
  - The `join()` method is used to join two DataFrames horizontally using their indices.
  - It's similar to the merge operation but simplifies joining when you only need to combine based on indices.
* **Appending with `append()`:**
  - The `append()` method is used to add rows from one DataFrame to another.
  - It's a convenient way to add new records to an existing DataFrame.
* **Combining with `combine_first()`:**
  - The `combine_first()` method allows you to combine two DataFrames by taking values from the calling DataFrame and filling missing values with corresponding values from the other DataFrame.
* **Ordered Merging with `merge_ordered()`:**
  - The `merge_ordered()` function is used for ordered merging, often used in time series data.
  - It merges two DataFrames and sorts the result based on the specified columns.

***Examples***

***Merging DataFrames***

```Python
import pandas as pd

# Original DataFrame
product_data = {'Product': ['Shoes', 'T-shirt', 'Jeans'],
                'Price': [50, 20, 40]}
df_original = pd.DataFrame(product_data)

# New DataFrame for concatenation
new_products = {'Product': ['Socks', 'Hat'],
                'Price': [10, 15]}
df_new = pd.DataFrame(new_products)

# Concatenating vertically using pd.concat()
concatenated_df = pd.concat([df_original, df_new], ignore_index=True)

print("Concatenated DataFrame:")
print(concatenated_df)

# New DataFrame for merging
product_info = {'Product': ['Shoes', 'T-shirt', 'Jeans', 'Socks'],
                'Brand': ['Nike', 'Adidas', 'Levi\'s', 'Puma']}
df_info = pd.DataFrame(product_info)

# Merging based on the 'Product' column
merged_df = pd.merge(df_original, df_info, on='Product')

print("\nMerged DataFrame:")
print(merged_df)

# New DataFrame for joining
product_discount = {'Discount': [10, 5, 15]}
df_discount = pd.DataFrame(product_discount)

# Setting index for both DataFrames
df_original.set_index('Product', inplace=True)
df_discount.set_index(df_original.index, inplace=True)

# Joining based on indices
joined_df = df_original.join(df_discount)

print("\nJoined DataFrame:")
print(joined_df)

# New DataFrame to append
new_product = {'Product': ['Socks'],
               'Price': [10]}
df_new = pd.DataFrame(new_product)

# Appending the new product to the original DataFrame
appended_df = df_original.append(df_new, ignore_index=True)

print("\nAppended DataFrame:")
print(appended_df)

# New DataFrame for combining
product_prices = {'Product': ['T-shirt', 'Jeans', 'Socks'],
                  'Price': [25, 35, 15]}
df_prices = pd.DataFrame(product_prices)

# Combining values using combine_first()
combined_df = df_original.set_index('Product').combine_first(df_prices.set_index('Product')).reset_index()

print("\nCombined DataFrame:")
print(combined_df)

# New DataFrame for ordered merging
product_inventory = {'Product': ['Jeans', 'Shoes', 'T-shirt'],
                     'Inventory': [100, 80, 150]}
df_inventory = pd.DataFrame(product_inventory)

# Ordered merging based on the 'Product' column
ordered_merged_df = pd.merge_ordered(df_original, df_inventory, on='Product')

print("\nOrdered Merged DataFrame:")
print(ordered_merged_df)
```

***Merging Series***

```python
import pandas as pd

# Creating the Series and list
prices_data = [50, 20, 40]
product_names = ['Shoes', 'T-shirt', 'Jeans']

# Creating the original Series
original_series = pd.Series(prices_data, index=product_names)

# Displaying the original Series
print("Original Series:")
print(original_series)

# Creating a new Series for appending
new_product = pd.Series([30], index=['Hat'])

# Appending the new product to the original Series
appended_series = original_series.append(new_product)

print("\nAppended Series:")
print(appended_series)

# Creating a Series for updating missing values
updated_prices = pd.Series([25, 18], index=['Shoes', 'T-shirt'])

# Updating missing values using combine_first()
combined_series = original_series.combine_first(updated_prices)

print("\nCombined Series:")
print(combined_series)

# Creating a Series for ordered merging
inventory_data = [100, 80, 120]
inventory_series = pd.Series(inventory_data, index=['Shoes', 'T-shirt', 'Jeans'])

# Ordered merging using merge_ordered()
ordered_merged_series = pd.merge_ordered(original_series, inventory_series, left_index=True, right_index=True)

print("\nOrdered Merged Series:")
print(ordered_merged_series)
```

## Reshaping and Pivoting 

### Reshaping

* Reshaping in Pandas involves transforming data between different formats to make it more suitable for analysis, visualization, and modeling. 
*  Reshaping typically involves converting data between "long" and "wide" formats, or performing operations to stack or unstack data for better analysis.
* **`stack()` and `unstack()`**:
  - The `stack()` method converts data from a wide format to a long format by pivoting columns into rows. It essentially stacks the columns on top of each other.
  - The `unstack()` method is the reverse operation of `stack()`. It converts data from a long format to a wide format by pivoting rows into columns.
  - These methods are useful for transforming hierarchical or multi-level index data.
* **`melt()`**:
  - The `melt()` method transforms data from a wide format to a long format by "melting" or unpivoting columns into rows while preserving identifier columns.
  - It's particularly useful when you have multiple columns that you want to stack into a single column while keeping other columns as identifiers.

***Examples***

***Reshaping DataFrames***

```python
import pandas as pd

# Creating a DataFrame 
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'Product': ['Shoes', 'Shoes', 'T-shirt', 'T-shirt'],
        'Sales': [100, 120, 50, 60]}

df = pd.DataFrame(data)

# Using stack() to convert to long format
df_long_stack = df.set_index(['Date', 'Product'])['Sales'].unstack().reset_index()

# Using unstack() to convert back to wide format
df_wide_unstack = df_long_stack.set_index('Date').stack().unstack()

# Using melt() to transform to long format
df_melted = df.melt(id_vars=['Date', 'Product'], value_vars='Sales', var_name='Metric', value_name='Value')

print("Original DataFrame:")
print(df)
print("\nLong DataFrame using stack():")
print(df_long_stack)
print("\nWide DataFrame using unstack():")
print(df_wide_unstack)
print("\nMelted DataFrame using melt():")
print(df_melted)
```

***Reshaping Series***

```python
import pandas as pd

# Creating a Series
sales_data = [100, 120, 50, 60]
dates = ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02']
products = ['Shoes', 'Shoes', 'T-shirt', 'T-shirt']

sales_series = pd.Series(sales_data, index=pd.MultiIndex.from_tuples(zip(dates, products)))

# Using stack() to convert to long format
series_long_stack = sales_series.unstack(level=-1).stack()

# Using unstack() to convert back to wide format
series_wide_unstack = series_long_stack.unstack()

# Using melt() to transform to long format
series_melted = sales_series.reset_index(name='Sales').rename(columns={'level_0': 'Date', 'level_1': 'Product'})

print("Original Series:")
print(sales_series)
print("\nLong Series using stack():")
print(series_long_stack)
print("\nWide Series using unstack():")
print(series_wide_unstack)
print("\nMelted Series using melt():")
print(series_melted)
```

### Pivoting

* Pivoting is a data manipulation technique used to transform data from a long format to a wide format, or vice versa, by reorganizing and summarizing it based on specific criteria. 

* Pivoting is useful for summarizing data, creating cross-tabulations, and generating summary tables for analysis.

* **`pivot_table()` Method:**

  - The `pivot_table()` method is used to create a new DataFrame by aggregating and summarizing data from an existing DataFrame.
  - It allows you to specify the rows, columns, and values you want to pivot, along with the aggregation function to apply to the values.
  - The method provides a way to generate pivot tables, similar to spreadsheets or databases.
  - It can handle duplicate entries and missing values by using aggregation functions like mean, sum, count, etc.
  - The method can also handle hierarchical or multi-level index pivoting.

  * Syntax for the `pivot_table()`

    ```python
    DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, margins_name='All', dropna=True)
    ```

  * `values`: The column(s) to aggregate and summarize.

  - `index`: The column(s) to use as the row index.
  - `columns`: The column(s) to use as the column index.
  - `aggfunc`: The aggregation function to apply to the values (default is 'mean').
  - `fill_value`: The value to replace missing values with.
  - `margins`: Whether to include margins (subtotals) for row and column totals.
  - `margins_name`: The name for the margins column or index.
  - `dropna`: Whether to exclude rows or columns with missing values.

***Examples*** 

***Pivoting DataFrames***

```python
import pandas as pd

# Creating the DataFrame with provided data
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Score': [90, 85, 75, 80]}

scores_df = pd.DataFrame(data)

# Basic Pivot Table
pivot_table_basic = scores_df.pivot_table(values='Score', index='Name', columns='Subject', aggfunc='mean')

# Pivot Table with Margins
pivot_table_with_margins = scores_df.pivot_table(values='Score', index='Name', columns='Subject', aggfunc='mean', margins=True, margins_name='Overall')

print("Original DataFrame:")
print(scores_df)
print("\nExample 1: Basic Pivot Table:")
print(pivot_table_basic)
print("\nExample 2: Pivot Table with Margins:")
print(pivot_table_with_margins)

```

***Pivoting Series***

```python
import pandas as pd

# Creating the Series with provided data
scores_data = [90, 85, 75, 80]
names = ['Alice', 'Bob', 'Alice', 'Bob']
subjects = ['Math', 'Math', 'Science', 'Science']

scores_series = pd.Series(scores_data, index=pd.MultiIndex.from_tuples(zip(names, subjects)))

# Basic Pivot Table
pivot_table_basic = scores_series.unstack().reset_index()

# Pivot Table with Margins
pivot_table_with_margins = scores_series.unstack().reset_index().append(scores_series.groupby(level=0).mean().rename(('Average', ''), level=1)).sort_index()

print("Original Series:")
print(scores_series)
print("\nExample 1: Basic Pivot Table:")
print(pivot_table_basic)
print("\nExample 2: Pivot Table with Margins:")
print(pivot_table_with_margins)

```

## Time Series

* Time Series data is a sequence of data points collected at specific time intervals. 

* It's a common data format encountered in various fields such as finance, economics, physics, and more. 

* Time Series data analysis involves understanding patterns, trends, and dependencies in the data over time.

* **Time Series Data Handling**

  * **`Timestamp` and `DatetimeIndex`**

    - Pandas provides the `Timestamp` data type for representing individual time points.

    - The `DatetimeIndex` is a specialized index type in Pandas designed for Time Series data.

  * **`to_datetime()`**  converts various types of date-like objects into Pandas `Timestamp` objects.

  * **`date_range()`** generates a range of dates or timestamps.

    ***Examples***

    ***`Timestamp` and `DatetimeIndex ` in DataFrames***

    ```python
    import pandas as pd
    
    # Creating individual Timestamps
    timestamp1 = pd.Timestamp('2023-08-15 10:30:00')
    timestamp2 = pd.Timestamp('2023-08-15 15:45:00')
    
    # Creating a DatetimeIndex for a list of Timestamps
    timestamps = pd.to_datetime(['2023-08-15 10:30:00', '2023-08-15 15:45:00'])
    
    print("Individual Timestamps:")
    print(timestamp1)
    print(timestamp2)
    print("\nDatetimeIndex:")
    print(timestamps)
    ```

    ***`to_datetime()` in DataFrames***

    ```python
    import pandas as pd
    
    # Creating a list of date strings
    dates_strings = ['2023-08-15', '2023-08-16', '2023-08-17']
    
    # Converting strings to Timestamps
    timestamp_list = pd.to_datetime(dates_strings)
    
    print("Original Date Strings:")
    print(dates_strings)
    print("\nConverted Timestamps:")
    print(timestamp_list)
    ```

    ***`date_range()` in DataFrames***

    ```python
    import pandas as pd
    
    # Generating a date range for a week of sales data
    start_date = '2023-08-15'
    end_date = '2023-08-21'
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    print("Generated Date Range:")
    print(date_range)
    ```

    ***`Timestamp` and `DatetimeIndex` in Series***

    ```python
    import pandas as pd
    
    # Creating a Series with Timestamps as index
    timestamps = pd.to_datetime(['2023-08-15 10:30:00', '2023-08-15 15:45:00'])
    values = [100, 150]
    
    sales_series = pd.Series(values, index=timestamps)
    
    print("Sales Series with Timestamp Index:")
    print(sales_series)
    ```

    ***`to_datetime()` in Series***

    ```python
    import pandas as pd
    
    # Creating a Series with date strings as data
    date_strings = ['2023-08-15', '2023-08-16']
    values = [100, 150]
    
    sales_series = pd.Series(values, index=date_strings)
    
    # Converting the index to Timestamps using to_datetime()
    sales_series.index = pd.to_datetime(sales_series.index)
    
    print("Original Sales Series:")
    print(sales_series)
    ```

    ***`date_range()` for Generating Dates in Series***

    ```python
    import pandas as pd
    
    # Generating a Series with date range as index
    start_date = '2023-08-15'
    end_date = '2023-08-21'
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    values = [100, 150, 120, 130, 140, 110, 180]
    
    sales_series = pd.Series(values, index=date_range)
    
    print("Generated Sales Series with Date Index:")
    print(sales_series)
    ```

* **Time Series Analysis**

  - **Resampling**

    - Resampling involves changing the frequency of the Time Series data.
    - `resample()` method allows you to apply aggregation functions over different time intervals.

  - **Shifting**:

    - Shifting involves moving data points forward or backward in time.
    - `shift()` method is used for this purpose.

  - **Rolling Windows**

    - Rolling window functions compute statistics over a sliding window of data.
    - `rolling()` method is used for calculating rolling statistics.

  - **Time Zone Handling**

    - Pandas supports time zone conversion and manipulation using the `tz_localize()` and `tz_convert()` methods.

    ***Examples***

    ***Resampling with  DataFrames***

    ```python
    import pandas as pd
    import numpy as np
    
    # Generating a DataFrame with daily sales data
    date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
    sales_data = np.random.randint(50, 200, size=len(date_rng))
    sales_df = pd.DataFrame({'Date': date_rng, 'Sales': sales_data})
    
    # Resampling to a weekly frequency and calculating the mean sales
    weekly_resampled = sales_df.resample('W-Mon', on='Date').mean()
    
    print("Original Sales DataFrame:")
    print(sales_df)
    print("\nWeekly Resampled Sales DataFrame:")
    print(weekly_resampled)
    ```

    ***Resampling with Series***

    ```python
    import pandas as pd
    import numpy as np
    
    # Generating a DataFrame with hourly temperature data
    date_rng = pd.date_range(start='2023-08-01', end='2023-08-05', freq='H')
    temperature_data = np.random.uniform(18, 30, size=len(date_rng))
    temperature_df = pd.DataFrame({'Timestamp': date_rng, 'Temperature': temperature_data})
    
    # Resampling to a daily frequency and calculating the maximum temperature
    daily_resampled = temperature_df.resample('D', on='Timestamp').max()
    
    print("Original Temperature DataFrame:")
    print(temperature_df)
    print("\nDaily Resampled Temperature DataFrame:")
    print(daily_resampled)
    ```

    ***Shifting with DataFrames***

    ```python
    import pandas as pd
    import numpy as np
    
    # Generating a DataFrame with daily temperature data
    date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
    temperature_data = np.random.uniform(18, 30, size=len(date_rng))
    temperature_df = pd.DataFrame({'Date': date_rng, 'Temperature': temperature_data})
    
    # Shifting the temperature data forward by 1 day
    shifted_df = temperature_df.copy()  # Creating a copy to avoid modifying the original data
    shifted_df['Shifted_Temperature'] = temperature_df['Temperature'].shift(periods=1)
    
    print("Original Temperature DataFrame:")
    print(temperature_df)
    print("\nShifted Temperature DataFrame (1 day forward):")
    print(shifted_df)
    ```

    ***Shifting with Series***

    ```python
    import pandas as pd
    import numpy as np
    
    # Generating a Series with daily sales data
    date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
    sales_data = np.random.randint(50, 200, size=len(date_rng))
    sales_series = pd.Series(sales_data, index=date_rng)
    
    # Shifting the data forward by 1 day
    shifted_series = sales_series.shift(periods=1)
    
    print("Original Sales Series:")
    print(sales_series)
    print("\nShifted Sales Series (1 day forward):")
    print(shifted_series)
    ```

    ***Rolling Windows with DataFrames***

    ```python
    import pandas as pd
    import numpy as np
    
    # Generating a DataFrame with hourly temperature data
    date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='H')
    temperature_data = np.random.uniform(18, 30, size=len(date_rng))
    temperature_df = pd.DataFrame({'Timestamp': date_rng, 'Temperature': temperature_data})
    
    # Calculating rolling average over a window of 6 hours
    rolling_avg_df = temperature_df.copy()  # Creating a copy to avoid modifying the original data
    rolling_avg_df['Rolling_Avg'] = temperature_df['Temperature'].rolling(window=6).mean()
    
    print("Original Temperature DataFrame:")
    print(temperature_df)
    print("\nRolling Average Temperature DataFrame (Window = 6 hours):")
    print(rolling_avg_df)
    ```

    ***Rolling Windows with Series***

    ```python
    import pandas as pd
    import numpy as np
    
    # Generating a Series with daily sales data
    date_rng = pd.date_range(start='2023-08-01', end='2023-08-10', freq='D')
    sales_data = np.random.randint(50, 200, size=len(date_rng))
    sales_series = pd.Series(sales_data, index=date_rng)
    
    # Calculating rolling average over a window of 3 days
    rolling_avg = sales_series.rolling(window=3).mean()
    
    print("Original Sales Series:")
    print(sales_series)
    print("\nRolling Average Sales Series (Window = 3 days):")
    print(rolling_avg)
    ```

    ***Time Zone Handling with DataFrames***

    ```python
    import pandas as pd
    
    # Creating a DataFrame with time zone awareness
    data = {'Date': ['2023-08-15 10:00:00', '2023-08-15 15:00:00'],
            'Sales': [100, 150]}
    
    sales_df = pd.DataFrame(data)
    sales_df['Date'] = pd.to_datetime(sales_df['Date']).dt.tz_localize('UTC')
    
    # Converting time zone to 'America/New_York'
    sales_df['Date_NY'] = sales_df['Date'].dt.tz_convert('America/New_York')
    
    print("Original Sales DataFrame:")
    print(sales_df)
    ```

    **Time Zone Handling with Series**

    ```python
    import pandas as pd
    
    # Creating a DataFrame with time zone awareness
    data = {'Date': ['2023-08-15 10:00:00', '2023-08-15 15:00:00'],
            'Sales': [100, 150]}
    
    sales_df = pd.DataFrame(data)
    sales_df['Date'] = pd.to_datetime(sales_df['Date']).dt.tz_localize('UTC')
    
    # Converting time zone to 'Asia/Tokyo'
    sales_df['Date_Tokyo'] = sales_df['Date'].dt.tz_convert('Asia/Tokyo')
    
    print("Original Sales DataFrame:")
    print(sales_df)
    ```

    

  

