from operator import attrgetter


class Chain(object):
  def __init__(self, name, freq):
    self.name = name
    self.freq = freq
  
  def __repr__(self):
    return f"{self.name} - {self.freq}"

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
    Business("Astro Burger", "Austin", 303),
    Business("Peets Coffee", "Austin", 203),
    Business("Starbucks", "Austin", 106),
    Business("Astro Burger", "Austin", 302),
    Business("Starbucks", "Austin", 190),
    Business("Whole Foods", "Austin", 103),
    Business("Whole Foods", "Austin", 107),
    Business("Astro Burger", "Austin", 301),
    Business("Bob's Burger", "Austin", 501),
    Business("Bob's Burger", "Austin", 360),
    Business("Bob's Burger", "Austin", 370),
    Business("Bob's Burger", "Austin", 560),

    
  ]

def get_unique_business_sort(businesses, location):
  seen_id = set()
  seen = {}
  chains = []
  # get all unique businesses and count
  for busineess in businesses:
    if busineess.location == location:
      if busineess._id not in seen_id:
        if busineess.name in seen:
          seen[busineess.name] += 1
        else:
          seen[busineess.name] = 1
          seen_id.add(busineess._id)

  for name, freq  in seen.items():
    chains.append(Chain(name, freq))

  # chains = sorted(chains, key=lambda chain: chain.freq, reverse=True)
  chains = sorted(chains, key=attrgetter('freq'), reverse=True)

  print(chains)





get_unique_business_sort(businesses_objects, "Austin")
