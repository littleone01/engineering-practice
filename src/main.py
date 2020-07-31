import click


@click.group()
def cli():
    print('command')


@cli.command()
def preprocess():
    from src.process.PrepareProcess import PrepareProcess
    process = PrepareProcess()
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