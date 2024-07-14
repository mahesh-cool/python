# Dictionaries.py
band = {
    "vocals": "plant",
    "guitar": "Page"
    }

band2 = dict(vocals="Plant", guitar="Page") # dictonary commnad used

print(band)
print(band2)
print(type(band)) #prints type of the band
print(len(band)) # print the length of the file

#Access Items
print(band["vocals"]) # prints value associated to vocals
print(band.get("guitar")) #prints value associated to guitar
