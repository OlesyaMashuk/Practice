from cat import Cat

cats = [{"name": "Барон", "gender": "мальчик", "age": 2},
        {"name": "Сэм", "gender": "мальчик", "age": 2}]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print("name", cat_obj.name)
    print("gender", cat_obj.gender)
    print("age", cat_obj.age)
