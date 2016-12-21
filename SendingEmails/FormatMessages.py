from MessageClass import MessageUser


obj = MessageUser()
obj.add_user('diVya', 15.36, email="divyamodi128@outlook.com")
obj.add_user('pAlak', 23.548)
obj.add_user('praNav', 56.4623)
obj.add_user('dhwanil', 10.00)
obj.add_user('harsh', 34.25)
obj.add_user('mauLIK', 135.5)
print obj.get_user()
print obj.make_messages()
