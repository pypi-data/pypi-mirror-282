import os
import json
import click
from .ecs import ECSManager

CONFIG_DIR = os.path.expanduser('~/.sqnethelper')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = load_config()

@cli.command()
@click.option('--access-key', prompt=True, help='阿里云Access Key')
@click.option('--access-secret', prompt=True, hide_input=True, help='阿里云Access Secret')
@click.option('--region', default='cn-hangzhou', help='阿里云区域')
def setup(access_key, access_secret, region):
    """设置阿里云凭证"""
    config = {
        'access_key': access_key,
        'access_secret': access_secret,
        'region': region
    }
    save_config(config)
    click.echo("配置已保存")

@cli.command()
@click.pass_obj
def list(config):
    """列出所有ECS实例"""
    ecs_manager = ECSManager(config['access_key'], config['access_secret'], config['region'])
    click.echo(ecs_manager.list_instances())

@cli.command()
@click.argument('instance-id')
@click.pass_obj
def start(config, instance_id):
    """启动指定的ECS实例"""
    ecs_manager = ECSManager(config['access_key'], config['access_secret'], config['region'])
    click.echo(ecs_manager.start_instance(instance_id))

@cli.command()
@click.argument('instance-id')
@click.pass_obj
def stop(config, instance_id):
    """停止指定的ECS实例"""
    ecs_manager = ECSManager(config['access_key'], config['access_secret'], config['region'])
    click.echo(ecs_manager.stop_instance(instance_id))

if __name__ == '__main__':
    cli()