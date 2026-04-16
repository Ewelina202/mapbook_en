def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user['location']} opubikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermassage'][-1]}')
