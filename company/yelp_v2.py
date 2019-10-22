import operator

class Chain(object):
  def __init__(self, name, freq):
    self.name = name
    self.freq = freq

class Business(object):
  def __init__(self, name, location, _id):
    self.name = name
    self.location = location
    self._id = _id
    

chains = []
businesses_objects = [
    Business("Starbucks", "Seattle", 101), 
    Business("Peets Coffee", "San Francisco", 102),
    Business("Whole Foods", "Austin", 103),
    Business("Starbucks", "San Francisco", 104), 
    Business("Peets Coffee", "Austin", 105),
    Business("Starbucks", "Austin", 106),
    Business("Whole Foods", "Austin", 103),
    Business("Whole Foods", "Austin", 107),
  ]


def get_unique_business_sort(businesses, location):
  seen_id = set()
  seen = {}

  # get all unique businesses and count
  for busineess in businesses:
    if busineess.location == location:
      if busineess._id not in seen_id:
        if busineess.name in seen:
          seen[busineess.name] += 1
        else:
          seen[busineess.name] = 1
          seen_id.add(busineess._id)

  sorted_x = sorted(seen.items(), key=operator.itemgetter(1), reverse=True)
  print(sorted_x)


get_unique_business_sort(businesses_objects, "Austin")
