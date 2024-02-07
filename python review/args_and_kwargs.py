def tuple(*args):
    return args

def dictionary(**kwargs):
    return kwargs

x = tuple(1, 2, 3, "hi", "test", 5.45)
print(x)
for i in x:
    print(i)
print(type(x), "\n")


y = dictionary(name= "Nss6", age= 35, status= "Sick")
print(y)
for k,v in y.items():
    print(f"{k}: {v}")
print(type(y), "\n")


def multi_args(*args, **kwargs):
    list = []
    dict = {}
    for i in args:
        list.append(i)
    for k,v in kwargs.items():
        dict.update({k:v})
    return list, dict
    
z = multi_args("Dr.", "Spongebob", "Squarepants", "III", 
               street="123 Fake St", 
               apt="100", 
               city="Detroit", 
               state="MI", 
               zip="54321")
print(z)
print(type(z))
for i in z:
    print(i)
