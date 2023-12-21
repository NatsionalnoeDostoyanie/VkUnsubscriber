from flask import Flask, render_template, request
import vk_api


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    status = ''
    if request.method == 'POST':
        try:
            access_token = request.form.get('access_token')
            vk_session = vk_api.VkApi(token=access_token)
            vk = vk_session.get_api()
            user = vk.users.get()
            user_id = user[0]['id']

            for group_id in map(int, vk.groups.get(user_id=user_id, extended=0)['items']):
                vk.groups.leave(group_id=group_id)

            status = 'success'

        except Exception as e:
            status = str(e)

    return render_template('index.html', status=status)


if __name__ == '__main__':
    app.run(debug=True)
