class BankAccount:

  def __init__(self,bncname,accnum,cifcode):
      self.bncname=bncname
      self.accnum=accnum
      self.cifcode=cifcode
      self.__pin="1234"
  def get_bncname(self):
    return self.__pin
  def  set_bncname(self,bncname):
     self.bncname=bncname
  def  get_pin(self):
    return self.pin



bank=BankAccount("punjab",123,"1235")

print(bank.get_bncname());