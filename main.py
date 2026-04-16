

users: list = [
    {'username': 'oliwia','location':'łódz','posts':1,'usermassage':['życzenia1','kocham legie', 'sprzedam opla','kiwi']},
    {'username': 'pawel','location':'ostróda','posts':2,'usermassage':['życzenia2','kocham legie1', 'sprzedam opla1',]},
    {'username': 'eliza','location':'łódz','posts':3,'usermassage':['życzenia3','kocham legie2']},
    {'username': 'filip','location':'deblin','posts':4,'usermassage':['życzenia4','kocham legie3','sprzedam opla','kiwi']},
]

for user in users:
    print(f'twój znajomy {user['username']} z miejscowości {user['location']} opubikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermassage'][-1]}')
    
    # twój znajomy filip z miejscowości deblin opublikował 1 post o treści: życzenia