import uuid
import avro.schema
import json
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

l_avro_binary_file = "E:\\code\\python\\avro\\users.avro"

l_schema = """{"namespace": "example.avro",
    "type": "record",
    "name": "User",
    "fields": [
         {"name": "name", "type": "string"},
         {"name": "favorite_number", "type": ["int", "null"]},
         {"name": "favorite_color", "type": ["string", "null"]}
     ]
}"""

write_schema = avro.schema.Parse(json.dumps(json.loads(l_schema)))

writer = DataFileWriter(open(l_avro_binary_file, "wb"), DatumWriter(), write_schema)
writer.close()
