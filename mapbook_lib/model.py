users: list = [
    {'username': 'oliwia', 'location': 'łódz', 'posts': 1,
     'usermassage': ['życzenia1', 'kocham legie', 'sprzedam opla', 'kiwi']},
    {'username': 'pawel', 'location': 'ostróda', 'posts': 2,
     'usermassage': ['życzenia2', 'kocham legie1', 'sprzedam opla1', ]},
    {'username': 'eliza', 'location': 'łódz', 'posts': 3, 'usermassage': ['życzenia3', 'kocham legie2']},
    {'username': 'filip', 'location': 'deblin', 'posts': 4,
     'usermassage': ['życzenia4', 'kocham legie3', 'sprzedam opla', 'kiwi']},
]
def add_user(users_data:list)->None:

    print(users)
    name=input('Podaj imie: ')
    location=input('Podaj lokalizację: ')
    posts=int(input('Podaj liczbę postów: '))
    usermassage=[]
    users.append( {'username': name, 'location': location, 'posts': posts,
         'usermassage': usermassage},)
    print(users)

add_user(users)