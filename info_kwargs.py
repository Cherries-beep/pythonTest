def base(**kwargs):
    d = {'name':'Райан','surname':'Гослинг','age':23}
    for key,value in kwargs.items():
     print('Base:',key,value)

def create_actor(**kwargs):
    for i, k in kwargs.items():
        print(i, k)
    if not kwargs:
     base(Name = 'Райан',surname= 'Рейнольдс',age = 46)

create_actor(Name='Alex',proff='backend', hobbie = 'dance')
create_actor()