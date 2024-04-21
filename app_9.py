# Создать страницу, на которой будет форма для ввода имени
# и электронной почты, при отправке которой будет создан cookie-файл
# с данными пользователя, а также будет произведено перенаправление
# на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии
# на которую будет удалён cookie-файл с данными пользователя и
# произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def flash_name():
    if request.method == 'POST':
        name = request.form.get('name')
        response = make_response(render_template('index_hi_09.html', name=name))
        response.set_cookie('usurname', name)
        return response
    return render_template('index_09.html')

@app.route('/logout/', methods=['GET','POST'])
def delete_cookie():
    name = request.cookies.get('usurname')
    if name != None:
        response = make_response(redirect('/'))
        response.delete_cookie('usurname')
        return response
    else:
        return redirect(url_for('/'))


if __name__ == '__main__':
    app.run(debug=True)