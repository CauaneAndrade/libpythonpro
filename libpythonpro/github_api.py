import requests


def buscar_avatar(user):
    """
    Busca o avatar de um usuário no Github
    :param user: str com o nome do usuário do github
    :return: str com sua cidade, bairro ou país de origem
    """
    url = f'https://api.github.com/users/{user}'
    response = requests.get(url)
    return response.json()['location']


if __name__ == '__main__':
    print(buscar_avatar('CauaneAndrade'))
