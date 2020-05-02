from flask import Flask, render_template, request
from models.item import Item


app = Flask(__name__, template_folder='templates/')


@app.route('/')
def show_mindmap():
    item_list = Item.get_item(app)
    return render_template('mindmap.html', item_list=item_list)


@app.route('/post', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # DB登録するオブジェクトを生成
        target = Item(title=request.form['title'], content=request.form['content'])
        # item.no発番
        item_list = Item.get_item(app)
        no = len(item_list)
        #
        # target.no = no
        # target.title = request.form['title']
        # target.content = request.form['content']
        Item.register_item(app, item=target)

        # 画面再表示
        return show_mindmap()


if __name__ == '__main__':
    app.run()