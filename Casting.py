# Casting Tipe Data

print("===============INTEGER========================")

data_int = 21
print("Data = ", data_int, type(data_int))

data_float  = float (data_int)
data_bool   = bool (data_int)
data_str    = str (data_int)
print("Hasil casting = ",data_float, type(data_float))
print("Hasil casting = ",data_bool, type(data_bool))
print("Hasil casting = ",data_str, type(data_str))

print("===============FLOAT===================")

data_float = 1.2
print("Data = ", data_float, type(data_float))

data_int    = int(data_float)
data_bool   = bool(data_float)
data_str    = str(data_float)
print("Hasil Casting = ", data_int, type(data_int))
print("Hasil casting = ", data_bool, type(data_bool))
print("Hasil casting = ", data_str, type(data_str))

print("===============BOOLEAN===================")

data_bool = True
print("Data = ", data_bool, type(data_bool))

data_int    = int(data_bool)
data_float  = float(data_bool)
data_str    = str(data_bool)
print("Hasil casting = ", data_int, type(data_int))
print("Hasil casting = ", data_float, type(data_float))
print("Hasil casting = ", data_str, type(data_str))

print("===============STRING===================")

data_str = "66"
print("Data = ", data_str, type(data_str))

data_int    = int(data_str)
data_float  = float(data_str)
data_bool   = bool(data_str)
print("Hasil casting = ", data_int, type(data_int))
print("Hasil casting = ", data_float, type(data_float))
print("Hasil casting = ", data_bool, type(data_bool))
