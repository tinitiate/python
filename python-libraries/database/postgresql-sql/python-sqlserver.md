# 🐍 Python Tutorial: Connect to MS SQL Server and Perform Operations

## 📌 1. Required Libraries
Install the libraries:
```bash
pip install pyodbc
pip install sqlalchemy
```

---

## 📌 2. Basic `pyodbc` Connection Example
```python
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=YourDatabaseName;'
    'UID=YourUsername;'
    'PWD=YourPassword'
)
cursor = conn.cursor()
```

---

## 📌 3. SELECT Data Example
```python
cursor.execute("SELECT * FROM Employees")
for row in cursor.fetchall():
    print(row)
```

---

## 📌 4. CREATE TABLE Example
```python
cursor.execute('''
    CREATE TABLE Employees (
        EmployeeID INT PRIMARY KEY,
        Name NVARCHAR(50),
        Position NVARCHAR(50),
        Salary DECIMAL(10, 2)
    )
''')
conn.commit()
```

---

## 📌 5. INSERT Data Example
```python
cursor.execute(
    "INSERT INTO Employees (EmployeeID, Name, Position, Salary) VALUES (?, ?, ?, ?)",
    (1, 'John Doe', 'Developer', 60000.00)
)
conn.commit()
```

---

## 📌 6. UPDATE Data Example
```python
cursor.execute(
    "UPDATE Employees SET Salary = ? WHERE EmployeeID = ?",
    (65000.00, 1)
)
conn.commit()
```

---

## 📌 7. DELETE Data Example
```python
cursor.execute("DELETE FROM Employees WHERE EmployeeID = ?", (1,))
conn.commit()
```

---

## 📌 8. Execute Stored Procedure Example

### SQL Stored Procedure:
```sql
CREATE PROCEDURE GetEmployeeByID
    @EmployeeID INT
AS
BEGIN
    SELECT * FROM Employees WHERE EmployeeID = @EmployeeID
END
```

### Python Execution:
```python
cursor.execute("EXEC GetEmployeeByID ?", (1,))
for row in cursor.fetchall():
    print(row)
```

---

## 📌 9. Execute Scalar Function Example

### SQL Function:
```sql
CREATE FUNCTION GetEmployeeSalary (@EmployeeID INT)
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @Salary DECIMAL(10,2)
    SELECT @Salary = Salary FROM Employees WHERE EmployeeID = @EmployeeID
    RETURN @Salary
END
```

### Python Execution:
```python
cursor.execute("SELECT dbo.GetEmployeeSalary(?)", (1,))
salary = cursor.fetchone()[0]
print("Salary:", salary)
```

---

## 📌 10. Using SQLAlchemy as an Alternative
```python
from sqlalchemy import create_engine, text

engine = create_engine('mssql+pyodbc://YourUsername:YourPassword@YourServer/YourDatabaseName?driver=ODBC+Driver+17+for+SQL+Server')
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Employees"))
    for row in result:
        print(row)
```

---

## ✅ Notes:
- Replace `YourUsername`, `YourPassword`, `YourDatabaseName`, and `YourServer`.
- Use `ODBC Driver 18` if applicable.
- Always use parameterized queries (`?`) to prevent SQL Injection.
- `conn.commit()` is required for any write operations.
