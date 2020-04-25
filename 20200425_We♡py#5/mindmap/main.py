from flask import Flask, render_template
from models.item import Item


app = Flask(__name__, template_folder='templates/')

@app.route('/')
def show_mindmap():
    item_list = Item.get_item(app)
    return render_template('mindmap.html', item_list=item_list)


if __name__ == '__main__':
    app.run()