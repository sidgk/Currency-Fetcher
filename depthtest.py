data = {
  "persons": {
    "1": {
      "name": "siddu"
    },
    "2": {
      "name": "manju"
    }
  },
  "cars": {
    "model1": {
      "make": 1990,
      "company_details": {
         "name": "Ford Corporation",
         "country": "US",
         "some_list":[1,2,1]
      }
    }, 
    "model2": {
      "make": 1990,
      "company_details": {
         "name": "Ford Corporation",
         "country": "US",
         "some_list":[1,2,1,1,1]
      }
    }
  }
}
def walk(userData):
  depth = 0
  def walkHelper(someData): 
    nonlocal depth
    for key, val in someData.items():
      if isinstance(val, dict):
        depth = walkHelper(val) + 1
        return walkHelper(val)
    return depth
  walkHelper(userData)
  return depth + 1

print(walk(data))