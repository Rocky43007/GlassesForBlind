import pickle

age = input ('Age?: ')
gender = input ('Gender?: ')
agefile = age
genderfile = gender

pickle_out = open("age.native","wb")
pickle.dump(agefile, pickle_out)
pickle_out.close()


pickle_out = open("gender.native","wb")
pickle.dump(genderfile, pickle_out)
pickle_out.close()