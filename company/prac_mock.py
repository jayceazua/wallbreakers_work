"""
You have to implement the trace_path() function which will 
take in a list of source-destination pairs and return the 
correct sequence of the whole journey from the first city to the last.

Input:
  dic = {
      "NewYork": "Chicago",
      "Boston": "Texas",
      "Missouri": "NewYork",
      "Texas": "Missouri"
  }

Output:
  [["Boston", "Texas"], ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]
"""
def trace_path(my_dict):  # A Map object
    # Write your code here
    start = _find_start_ctty(my_dict)
    results = []
    n = len(my_dict)
    # destination = start
    while n:
      
      results.append([start, my_dict[start]])
      start = my_dict[start]
      n -= 1

    return results



def _find_start_ctty(dic):
    keys = set(dic.keys())
    values = set(dic.values())
    for key in keys:
        if key not in values:
            return key


print(trace_path(dic))

