import click
from .SqNetHelper import SqNetHelper

@click.group()
def cli():
    pass

@cli.command()
@click.option('--access-key', prompt=True, help='阿里云Access Key')
@click.option('--access-secret', prompt=True, help='阿里云Access Secret')
def setup(access_key, access_secret):
    """设置阿里云账号凭证"""
    result = SqNetHelper.setup(access_key, access_secret)
    click.echo(result)

@cli.command()
def list():
    """列出所有网络服务器"""
    result = SqNetHelper.list_instances()
    click.echo(result)

@cli.command()
#添加--region，用法: sqnethelper config --region
@click.option('--region', is_flag=True, help='配置region')
def config(region):
    """修改当前账号的网络配置"""
    if region:
        regions_list, region_choices = SqNetHelper.list_regions()
        click.echo(regions_list)
        if region_choices:
            choice = click.prompt("请选择需要操作的region序号：", type=int)
            result = SqNetHelper.set_region(choice, region_choices)
            click.echo(result)

@cli.command()
def create():
    """创建网络服务器"""
    result = SqNetHelper.create_instance()
    click.echo(result)

@cli.command()
def delete():
    """删除网络服务器"""
    instances_list, instances_choices = SqNetHelper.delete_instance()
    click.echo(instances_list)

    if instances_choices:
        choice = click.prompt("Enter the number of the instance you want to delete", type=int)
        result = SqNetHelper.confirm_delete_instance(choice, instances_choices)
        click.echo(result)
        
if __name__ == '__main__':
    cli()