import json

class SerializerJSON:
    def dumps(self, data):
        return json.dumps(data, indent=2)
    
    def loads(self, json_string):
        return json.loads(json_string)
    
    def dump(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)


serializer = SerializerJSON()  
data = {"name": "Mary", "age": 20}

print("1. dumps - объект в JSON строку:")
json_str = serializer.dumps(data)
print(json_str)

print("\n2. loads - JSON строку в объект:")
parsed = serializer.loads(json_str)
print(parsed)

print("\n3. dump - объект в файл JSON:")
serializer.dump(data, "data.json")
print("Файл JSON успешно создан.")

print("\n4. load - файл JSON в объект:")
loaded = serializer.load("data.json")
print(loaded)
