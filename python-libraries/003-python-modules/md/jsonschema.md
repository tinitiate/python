#  jsonschema

- JSON Schema is a vocabulary that allows you to annotate and validate JSON documents.
- JSON Schema uses a JSON object to define a schema for a JSON document.
- JSON Schema supports a wide range of validation rules, including data types, required fields, and regular expressions.
- JSON Schema also allows you to define custom validation rules and constraints.
- You can use various tools and libraries to validate JSON documents against JSON Schema, such as Python's jsonschema library.
- JSON Schema is widely used in API development and data validation, among other applications.

## Install 

```shell
pip install jsonschema
```

## Schema

* The schema includes the following:
  - `schema`: This is the root element of a JSON Schema document. It contains definitions for all the properties and data types that are allowed in the JSON document that this schema describes. It may also include information about references and links.
  - `type`: This element is used to specify the data type of a property or value in the JSON document. It can be a simple data type like `string`, `number`, or `boolean`, or a complex data type like `object` or `array`. 
  - `properties`: This element is used to define the properties of an object in the JSON document. It contains one or more properties that specify the name and data type of each property in the object.
  - `items`: This element is used to define the items in an array in the JSON document. It specifies the data type and properties of each item in the array. 
  - `object` data type is used to define an object in a JSON document. 
  - `required`: This element is used to specify which properties of an object are required. It contains an array of property names that must be present in the JSON document.
  - `$ref`: This element is used to reference another part of the JSON Schema document, allowing you to reuse definitions and keep your schema organized and maintainable.

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "product_id",
        "product_name",
        "product_status",
        "product_price",
        "effective_price_start_date",
        "effective_price_end_date",
        "quantity",
        "product_details",
        "created_date",
        "updated_date",
        "updated_time",
        "product_history"
    ],
    "properties": {
        "product_id": {
            "type": "integer"
        },
        "product_name": {
            "type": "string"
        },
        "product_status": {
            "type": "string"
        },
        "product_price": {
            "type": "number"
        },
        "effective_price_start_date": {
            "type": "string",
            "format": "date-time"
        },
        "effective_price_end_date": {
            "type": "string",
            "format": "date-time"
        },
        "quantity": {
            "type": "integer"
        },
        "product_details": {
            "type": "object",
            "required": [
                "product_category",
                "supplier_details"
            ],
            "properties": {
                "product_category": {
                    "type": "string"
                },
                "supplier_details": {
                    "type": "object",
                    "required": [
                        "supplier"
                    ],
                    "properties": {
                        "supplier": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": [
                                    "id",
                                    "name"
                                ],
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "name": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "created_date": {
            "type": "integer"
        },
        "updated_date": {
            "type": "string",
            "format": "date"
        },
        "updated_time": {
            "type": "integer"
        },
        "product_history": {
            "type": "object",
            "required": [
                "product_price_history"
            ],
            "properties": {
                "product_price_history": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "price",
                            "start_date",
                            "end_date"
                        ],
                        "properties": {
                            "price": {
                                "type": "number"
                            },
                            "start_date": {
                                "type": "string",
                                "format": "date-time"
                            },
                            "end_date": {
                                "type": "string",
                                "format": "date-time"
                            }
                        }
                    }
                }
            }
        }
    }
}

```

