"""
1.在VCS命令里clone远程仓库，确定存储路径和克隆路径
2.设置成虚拟环境
3.添加忽略文件
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():

    return '/index'


if __name__ == "__main__":
    app.run(debug=True)