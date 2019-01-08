"""
@author: kongwiki
@file:   manage.py
@time:   19-1-8下午7:00
@contact: kongwiki@163.com
"""
import os

from flask_script import Manager, Server, Shell
from app.models import User
from app import create_app, db
from flask_migrate import MigrateCommand, Migrate

# 获取虚拟环境
app = create_app('default')
# 初始化
manager = Manager(app)
migrate = Migrate(app, db)


@manager.shell
def make_shell_context():
    """Create a python CLI.
    return: Default import object
    type: `Dict`
    """
    return dict(app=app,
                db=db,
                User=User,
                Server=Server)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

