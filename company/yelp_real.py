class User(object):
  def __init__(self, _id, opt_in):
    self._id = _id
    self.opt_in = opt_in
    


user_list = [
  User(1, False),
  User(10, True),
  User(27, True),
  User(28, False),
  User(29, True),
  User(17, True),
  User(4, False),
  User(12, True),
  User(32, False),
  User(7, True),
]

change_log = [
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 12, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
  {'_id': 1, 'status': 'opt_in'},
]

def status_change(user_list, change_log):
  pass
