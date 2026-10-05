dAgenda = {
    "manuel": 28,
    "anastasia": 22,
    "andrea":20,
    "dante":24,
    "alberto":27,
    "lucia":26
}

# dAgenda.setdefault("porter",30)
# print(dAgenda)
# dAgenda.pop("manuel")
# print(dAgenda)
# dAgenda["lucia"] =21
# print(dAgenda)

# print(dAgenda["anastasia"])

# dInfoCPU = {
#     "cpu family": 6,
#     "vendor id":"GenuineIntel" 
# }

# for k,v in dAgenda.items():
#     print(f"El usuario {k} tiene {v} años")
# u= input("Nombre de usuario: ")
# if u in dAgenda:
#     print(f"El usuario {u} tiene {dAgenda[u]} años")
# else:
#     print ("No tenemos ese usuario guardado")



dAgenda2 = dAgenda.copy()
dAgenda2.pop("manuel")
print (dAgenda)
print (dAgenda2)
print(id(dAgenda))
print(id(dAgenda2))
