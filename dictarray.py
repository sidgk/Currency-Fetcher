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
def dictDepth(userdata):
    count = 0
    def dictwalk(someData): 
        nonlocal count
        print(someData)
        for key, val in someData.items():
            #print(key)
            if type(val) == type({}):
                count = dictwalk(val) + 1
                print(count)
                return dictwalk(val)
        return count
    dictwalk (userdata)
    return count +1
    def dictValArr(someData):
        for key, val in someData.items():
            if type(val) == type([]):
                val = list(set(val))
                return dictwalk(val)
print(dictDepth(data))

