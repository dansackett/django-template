from fabric.api import env, run, cd, local

APP_PATH = ''

env.use_ssh_config = True
env.hosts = [
    'user@host',
]


def deploy():
    push()
    with cd(APP_PATH):
        run('git pull origin master')
    restart()


def restart():
    run('RESTART_PATH')


def push():
    local('git push origin master')
