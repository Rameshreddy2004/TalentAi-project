from db import results_collection

def test_insert():
    sample = {"name": "Test User", "score": 90}
    results_collection.insert_one(sample)
    print("Data inserted!")

test_insert()
