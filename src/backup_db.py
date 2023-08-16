import os
import shutil


def backup_database(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    shutil.copytree(source_dir, dest_dir)
    print('Database backup created successfully.')


if __name__ == '__main__':
    source_dir = '/path/to/source/database'
    dest_dir = '/path/to/backup/location'
    backup_database(source_dir, dest_dir)