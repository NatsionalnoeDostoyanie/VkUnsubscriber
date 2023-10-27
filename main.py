import vk_api  # pip install vk_api
from config import access_token  # your token


def main():
    vk_session = vk_api.VkApi(token=access_token)
    vk = vk_session.get_api()

    user = vk.users.get()
    user_id = user[0]['id']

    for group_id in vk.groups.get(user_id=user_id, extended=0)['items']:
        vk.groups.leave(group_id=int(group_id))


if __name__ == '__main__':
    main()
