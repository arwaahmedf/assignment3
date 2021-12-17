#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pyopenms import *
from urllib.request import urlretrieve
gh = "https://raw.githubusercontent.com/OpenMS/pyopenms-extra/master"
urlretrieve (gh + "/src/data/P02769.fasta", "bsa.fasta")

dig = ProteaseDigestion()
dig.getEnzymeName() # Trypsin
bsa = "".join([l.strip() for l in open("yourlist_M202112174ABAA9BC7178C81CEBC9459510EDDEA337117B7.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)

result = []
dig.digest(bsa, result)
print(result[4].toString())
len(result) 

dig.digest(bsa, result, 7, 40)

for s in result:
    print(s.toString())
dig.setMissedCleavages(2)

dig.digest(bsa, result, 7, 40)

for s in result:
    print(s.toString())
    names = []
ProteaseDB().getAllNames(names)
len(names) 
e = ProteaseDB().getEnzyme('Lys-C')
e.getRegExDescription()
e.getRegEx()
from urllib.request import urlretrieve
gh = "https://raw.githubusercontent.com/OpenMS/pyopenms-extra/master"
urlretrieve (gh + "/src/data/P02769.fasta", "bsa.fasta")

dig = ProteaseDigestion()
dig.setEnzyme('Lys-C')
bsa = "".join([l.strip() for l in open("bsa.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[4].toString())
len(result)
names = []
db.getAllNames(names)
names

e = db.getEnzyme("RNase_T1")
e.getRegEx()
e.getThreePrimeGain()
oligo = NASequence.fromString("pAUGUCGCAG");

dig = RNaseDigestion()
dig.setEnzyme("RNase_T1")

result = []
dig.digest(oligo, result)
for fragment in result:
print (fragment)

print("Looking closer at", result[0])
print(" Five Prime modification:", result[0].getFivePrimeMod().getCode())
print(" Three Prime modification:", result[0].getThreePrimeMod().getCode())
for ribo in result[0]:
print (ribo.getCode(), ribo.getMonoMass(), ribo.isModified())


# In[ ]:





# In[ ]:




