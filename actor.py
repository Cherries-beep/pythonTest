def base(**kwargs):
    for i in kwargs.items():
     name = 'имя'
     surname = 'фамилия'
     age = 'возраст'
     kwargs[name] = 'Райан'
     kwargs[surname] = 'Рейнольдс'
     kwargs[age] = 46

    #for i, k in kwargs.items():
     #   print(i, k)

def create_actor(**kwargs):
    for i, k in kwargs.items():
        print(i, k)
    if not kwargs:
     base()

create_actor()
#create_actor(Рост=190, фильмы=['Дедпул', 'Главный герой'])
#create_actor(Имя='Alex',профессия='backend', хобби = 'dance')