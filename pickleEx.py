import pickle 
import copy

def storeData(): 
	o1 = {'abc':111,'xyz':222} 
	o2 = {'abc':333,'xyz':444} 

	db = {} 
	db['o1'] = o1 
	db['o2'] = o2 
	
	dbfile = open('testpickle.pck', 'ab') 
	
	pickle.dump(db, dbfile)					 
	dbfile.close() 

    oz = copy.deepcopy(db)
    print(oz)
    
def loadData(): 

	dbfile = open('testpickle.pck', 'rb')	 
	db = pickle.load(dbfile) 
	for keys in db: 
		print(keys, '=>', db[keys]) 
	dbfile.close() 

if __name__ == '__main__': 
	storeData() 
	loadData() 
