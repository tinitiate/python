# configparser 

- `configparser` is a built-in module in Python that provides a way to work with configuration files.

- Configuration files are usually plain text files that store settings and parameters for a program. 

  - These settings can include things like database connection strings, API keys, and other configuration parameters that are specific to a particular application or environment.

- `configparser` allows you to read and write these configuration files using a simple API, making it easy to manage settings for your Python applications.

- `configparser` supports several different formats for configuration files, including the popular INI file format, which consists of sections and key-value pairs.

- The `configparser` module provides a `ConfigParser` class that you can use to read and write configuration files. You create an instance of the `ConfigParser` class, and then use its methods to read and write settings to the configuration file.

- `ConfigParser` allows you to define sections in your configuration file, which can group related settings together. You can then access settings within a section using their keys.

- `configparser` supports interpolation, which allows you to use variables in your configuration files. You can define variables in the `[DEFAULT]` section of your configuration file, and then reference them in other sections using the `${variable}` syntax.

- `configparser` also provides support for parsing command-line arguments and environment variables, which allows you to override settings in your configuration file at runtime.

- `config.ini` sample:

  ```ini
  [DEFAULT]
  debug = False
  
  [web_server]
  host = 127.0.0.1
  port = 80
  
  [database]
  host = 127.0.0.1
  port = 5432
  
  ```

- We can use `configparser` to read values from the above file as follows:

  ```python
  import configparser
  
  config = configparser.ConfigParser()
  data_dir = 'E:/python-master/media/003-python-modules/'
  config.read(data_dir+'config.ini')
  
  # Read values from DEFAULT section
  debug = config.getboolean('DEFAULT', 'debug')
  print(debug)
  
  # Read values from web_server section
  web_host = config.get('web_server', 'host')
  web_port = config.getint('web_server', 'port')print(web_host,web_port)
  
  # Read values from database section
  db_host = config.get('database', 'host')
  db_host = config.getint('database', 'port')
  print(db_host,db_host)
  
  ```

- We can also use `configparser` to write values to a config file:

  ```python
  import configparser
  
  config = configparser.ConfigParser()
  data_dir = 'E:/python-master/media/003-python-modules/'
  
  # Add sections and options to the config object
  config['web_server'] = {'host': '127.0.0.1', 'port': '80'}
  config['database'] = {'host': '127.0.0.1', 'port': '5432'}
  
  # Write the config object to a file
  with open(data_dir+'config.ini', 'w') as configfile:
      config.write(configfile)
  
  ```

- `interpolation` example:

  ```python
  import configparser
  
  config = configparser.ConfigParser()
  config.read('sample.ini')
  
  data_dir = config.get('Settings', 'data_dir')
  file_name = config.get('Settings', 'file_name')
  file_path = config.get('Settings', 'file_path')
  
  print(f"data_dir: {data_dir}")
  print(f"file_name: {file_name}")
  print(f"file_path: {file_path}")
  
  ```

  - `sample.ini`

    ```ini
    [Settings]
    data_dir = /path/to/data
    file_name = myfile.txt
    file_path = %(data_dir)s/%(file_name)s
    ```

    

  

