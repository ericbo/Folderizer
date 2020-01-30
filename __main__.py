import os, click, shutil

@click.command()
@click.option("--path", "-p", help="Path to folderize", required=True, type=str)
def main(path):
    if not os.path.isdir(path):
        click.secho("File {!r} is not a valid path!".format(path), fg='red')
        exit(1)

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in files:
        name, extension = file.split(".")
        click.echo(name)

        target_folder = os.path.join(path, name)

        if not os.path.isdir(target_folder):
            os.mkdir(target_folder, 775)

        shutil.move(os.path.join(path, file), target_folder)

    exit(0)

if __name__ == "__main__":
    main()