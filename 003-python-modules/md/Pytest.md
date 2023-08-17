1. **pytest**: `pytest` is a popular testing framework for Python that simplifies writing and executing tests. It provides a clean and intuitive syntax for writing test cases and offers various features to make testing more efficient and organized.
2. **Test Function**: A test function is a Python function defined to test a specific piece of code. Test functions are named with the prefix `test_` and contain assertions to validate the behavior of the code under test.
3. **Test Discovery**: Test discovery is the process by which `pytest` automatically finds and collects test functions and test cases from files in the current directory and its subdirectories.
4. **Assertions**: Assertions are statements within test functions that check if a certain condition is true. If the condition is false, an assertion error is raised, indicating that the test has failed.
5. **Fixture**: A fixture is a function that provides test-specific resources, data, or setup for one or more test functions. Fixtures are defined using the `@pytest.fixture` decorator.
6. **Parametrized Testing**: Parametrized testing allows you to run the same test code with multiple sets of input data. Useful when you want to test the same functionality with different input values.
7. **Skipping Test**: Skipping a test means excluding it from the test run. You can skip tests using the `@pytest.mark.skip` decorator. This is useful when you have tests that are not yet ready or are known to fail.
8. **Expected Failure**: An expected failure is a test that you anticipate will fail due to specific conditions. You can mark tests as expected failures using the `@pytest.mark.xfail` decorator.

## Test Function 

```python
# calculator.py
def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

```python
# test_calculator.py
import calculator

def test_multiplication():
    assert calculator.multiply(3, 4) == 12

```

## Fixture

```python
import json
import psycopg2
import pytest
from db_insertion import add_product_to_database  # Assuming you have this function available

# Update the connection details for the test database
TEST_DB_CONNECTION = {
    "host": "localhost",
    "port": 5432,
    "dbname": "tinitiate",
    "user": "tinitiate",
    "password": "tinitiate"
}

@pytest.fixture(scope="module")
def test_db_connection():
    # Create a connection to the test database and create necessary schema and tables
    conn = psycopg2.connect(**TEST_DB_CONNECTION)
    yield conn
    conn.close()

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(test_db_connection):
    # Create necessary schema and tables before each test and clean up after each test
    cursor = test_db_connection.cursor()
    cursor.execute("CREATE SCHEMA IF NOT EXISTS shoppingcart;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shoppingcart.products (
            product_id SERIAL PRIMARY KEY,
            product_category TEXT,
            product_name TEXT,
            unit_price NUMERIC
        );
    """)
    test_db_connection.commit()
    yield
    cursor.execute("DROP SCHEMA IF EXISTS shoppingcart CASCADE;")
    test_db_connection.commit()

def test_add_product_success():
    data = {
        "id": 124,
        "category": "Electronics",
        "name": "Smartphone",
        "price": 599.99
    }
    
    response = add_product_to_database(data)
    
    assert response["statusCode"] == 200
    assert "Product added successfully" in json.loads(response["body"])["message"]

def test_add_product_failure():
    data = {
        "id": 124,
        "category": "Electronics",
        "name": "Smartphone",
        "price": 599.99
    }
    
    response = add_product_to_database(data)
    
    assert response["statusCode"] == 500
    assert "Failed to add product" in json.loads(response["body"])["message"]

```

## Parametrized Testing 

```python
def is_even(number):
    return number % 2 == 0

@pytest.mark.parametrize("number, expected", [(2, True), (3, False), (0, True)])
def test_is_even(number, expected):
    assert is_even(number) == expected

```

## Skipping Test

```python
import pytest
from calculator import multiply, add, subtract

# Test multiply function
def test_multiply():
    result = multiply(2, 3)
    assert result == 6

# Test add function
def test_add():
    result = add(5, 7)
    assert result == 12

# Test subtract function (skipped intentionally)
@pytest.mark.skip(reason="Not implemented yet")
def test_subtract():
    result = subtract(10, 3)
    assert result == 7

# Run pytest
if __name__ == "__main__":
    pytest.main()

```

## Expected Failure 

```python
import pytest
from products import ProductManager

# Create a fixture to initialize the ProductManager class
@pytest.fixture
def product_manager():
    return ProductManager()

# Test adding a product
def test_add_product(product_manager):
    product_data = {
        "product_id": "P123",
        "product_category": "Electronics",
        "product_name": "Smartphone",
        "unit_price": 599.99
    }
    product_manager.add_product(product_data)
    product = product_manager.get_product("123")
    assert product[0] == "123"
    assert product[1] == "Electronics"
    assert product[2] == "Smartphone"
    assert product[3] == 599.99

# Test updating a product
def test_update_product(product_manager):
    updated_data = {
        "product_category": "Gadgets",
        "product_name": "Updated Smartphone",
        "unit_price": 699.99
    }
    product_manager.update_product("123", updated_data)
    product = product_manager.get_product("123")
    assert product[1] == "Gadgets"
    assert product[2] == "Updated Smartphone"
    assert product[3] == 699.99

# Test deleting a product
def test_delete_product(product_manager):
    product_manager.delete_product("123")
    product = product_manager.get_product("123")
    assert product is None

# Test getting a product
@pytest.mark.xfail(reason="Intentional failure")
def test_get_product(product_manager):
    product = product_manager.get_product("123")
    assert product is None

# Run pytest
if __name__ == "__main__":
    pytest.main()

```

- In this example, I've marked the `test_get_product` function as an expected failure using the `@pytest.mark.xfail` decorator. 

- This decorator indicates that you anticipate this test to fail for a specific reason. 

- You can provide an optional `reason` parameter to provide more context about why you expect the test to fail.

  ```python
  # Test getting a product
  @pytest.mark.xfail(reason="Intentional failure: Product retrieval is not implemented yet")
  def test_get_product(product_manager):
      product = product_manager.get_product("123")
      assert product is None
  ```

- When we run the tests using `pytest`, the test marked as expected failure will be executed just like any other test. However, if this test fails, it won't be treated as a test failure. Instead, it will be considered a "failed, but expected" result, and the test suite will still be considered a success overall.

## Test Discovery 

Test discovery in `pytest` refers to the process of automatically discovering and running test files and test functions without explicitly specifying them on the command line. This is a convenient way to run all your tests within a project without having to list every test file or function individually.

Here's how you can use test discovery with `pytest`:

1. Organize Your Test Files:
   - Place your test files in a directory named `tests` (or any other name you prefer).
   - Organize your test files and test functions within this directory.

2. Test File Naming Convention:
   - By default, `pytest` discovers test files that match the `test_*.py` naming convention. Test files should start with "test_" and have the `.py` extension.

3. Run Test Discovery:
   - Open your terminal or command prompt.
   - Navigate to the root directory of your project.

4. Run `pytest` without Arguments:
   - Simply run the `pytest` command without specifying any arguments to initiate test discovery.
   - `pytest` will search for test files that match the naming convention and execute all test functions within them.

Here's an example of how your project directory structure might look:

```bash
project_folder/
|-- calculator.py
|-- tests/
|   |-- test_calculator.py
|   |-- test_other_module.py
```

In this example, the `test_calculator.py` and `test_other_module.py` files contain test functions, and they will be discovered and executed when you run `pytest` in the `project_folder` directory.

To run test discovery, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the root directory of your project (`project_folder`).
3. Run the following command:

```bash
pytest
```

`pytest` will automatically discover and run all the test files and test functions within the `tests` directory. 

Note that you can also use various command line options and patterns to control which tests are discovered and executed. For example, you can use `-k` to specify a keyword pattern to match test function names or use `-m` to run tests marked with specific markers.

## API Testing 

```python
import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"

# Test GET request
def test_get_posts():
    response = requests.get(base_url + "/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test POST request (Successful)
def test_create_post_success():
    payload = {
        "userId": 1,
        "id": 101,
        "title": "test title",
        "body": "test body"
    }
    response = requests.post(base_url + "/posts", json=payload)
    assert response.status_code == 201

# Test POST request (Failure)
def test_create_post_failure():
    payload = {
        "userId": 1,
        "id": 101,  # This ID already exists, causing failure
        "title": "test title",
        "body": "test body"
    }
    response = requests.post(base_url + "/posts", json=payload)
    assert response.status_code == 500  # Assuming the API returns a 500 error

# Test GET request (Failure)
def test_get_post_failure():
    non_existent_post_id = 9999
    response = requests.get(base_url + f"/posts/{non_existent_post_id}")
    assert response.status_code == 404

# Test PUT request
def test_update_post():
    post_id = 1
    updated_payload = {
        "title": "updated title",
        "body": "updated body"
    }
    response = requests.put(base_url + f"/posts/{post_id}", json=updated_payload)
    assert response.status_code == 200
    assert response.json()["title"] == updated_payload["title"]

# Test DELETE request
def test_delete_post():
    post_id = 1
    response = requests.delete(base_url + f"/posts/{post_id}")
    assert response.status_code == 200

# Test request with query parameters
def test_get_posts_with_query_params():
    query_params = {"userId": 1}
    response = requests.get(base_url + "/posts", params=query_params)
    assert response.status_code == 200
    for post in response.json():
        assert post["userId"] == query_params["userId"]
```

