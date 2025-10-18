import json

json_date = """
{
    "name": "Ivan",
    "age": 30,
    "is_student": true,
    "courses":[
        "Python", 
        "Test disign"
    ],
    "adress":{
        "city": "Voronezch",
        "zip": "32132132"
    }
}


"""
parsed_data = json.loads(json_date)
print(parsed_data['name'])


data = {
    "name": "Ivan",
    "age": 30,
    "is_student": True,

}
json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))


with open ("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data, type(data))


with open ("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)