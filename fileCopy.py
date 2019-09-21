with open("dicedice.py",'rb') as i, open("dicedice_copy.py",'wb') as o:
    o.write(i.read())

print("END")