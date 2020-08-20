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
         "country": ["US","UK","IND","US"],
         "some_list":[1,2,1,1,1,3,3,3,4,4,1]
      }
    }
  }
}

import json
#data_dict = json.dumps(data)    
def removeDuplicatesFromList(data):
    for key, val in data.items():
        if isinstance(val, dict):
            removeDuplicatesFromList(val)
        elif isinstance(val, list):
            data[key] =list(set(val))
    return data

print(removeDuplicatesFromList(data))

'''def walk(userData):
  depth = 0
  def walkHelper(someData): 
    print(someData)

    print("\n\n")
    nonlocal depth
    for key, val in someData.items():
      if isinstance(val, dict):
        print(val)
        depth = depth + 1
        walkHelper(val)
  walkHelper(userData)
  return depth
'''

