class test:

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, name):
    self.__name = name

  @name.deleter
  def name(self):
    print("am apletat srtergerea")
    del self.__name

# test._name = "Stoica Mihai"
# print(test._name)
# test.get_name()
testare = test()
testare.name ='Alt nume'
# print(testare.name)

del testare.name

l1 = [10, 1, 3]
l2 = list(l1)
l1[0] = 23
print(l2)
