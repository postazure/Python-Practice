import pickle
my_list = ['Fred',73,'Hello There', 81]
pickle_file = open('my_pickled_list.pkl','w')
pickle.dump(my_list, pickle_file)
pickle_file.close()

#import pickle
pickle_file = open('my_pickled_list.pkl','r')
recovered_list = pickle.load(pickle_file)
pickle_file.close()
print recovered_list
