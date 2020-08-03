import click

from src.datasource import DataSourceBase


def get_ds(ds_type: str) -> DataSourceBase:
    if ds_type == 'file':
        from src.datasource.FileDS import FileDS
        import os
        from src.entity.FileType import FileType
        data_path = '{cur_path}/../data/cs-training.csv'.format(cur_path=os.path.dirname(__file__))
        return FileDS(data_path, FileType.CSV)
    elif ds_type == 'mysql':
        from src.datasource.MysqlDS import MysqlDS
        db = 'credit_info'
        return MysqlDS(db)
    else:
        from src.exception.TypeNotSupportError import TypeNotSupportError
        raise TypeNotSupportError('数据源类型不支持')


@click.group()
def cli():
    print('command')


@cli.command()
@click.option('--ds-type', '-d', type=str)
def preprocess(ds_type: str):
    from src.process.PrepareProcess import PrepareProcess
    from src.processors.FillNa import FillNa
    preprocessors = [FillNa(0)]
    ds = get_ds(ds_type)
    process = PrepareProcess(ds, preprocessors, 'prepared.csv')
    process.run()


@cli.command()
def train():
    from src.process.TrainProcess import TrainProcess
    process = TrainProcess()
    process.run()


@cli.command()
def validate():
    from src.process.ValidateProcess import ValidateProcess
    process = ValidateProcess()
    process.run()


if __name__ == '__main__':
    cli()