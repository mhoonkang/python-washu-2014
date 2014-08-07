class School():
  def __init__(self, school_name):
    self.school_name = school_name     
    self.db = {}
  
  def add(self, name, grade):
    if grade in self.db.keys():
	  self.db[grade].add(name)
    else: self.db[grade] = {name}

  def grade(self, grade):
    if grade in self.db.keys():
	  return self.db[grade]
    else: return None
	  
  def sort(self):
    for i in self.db.keys():
      self.db[i] = tuple(sorted(self.db[i]))
    return self.db