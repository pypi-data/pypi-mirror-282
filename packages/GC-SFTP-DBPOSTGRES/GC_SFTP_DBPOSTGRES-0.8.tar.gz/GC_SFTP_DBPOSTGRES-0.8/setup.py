from setuptools import setup, find_packages

setup(
    name='GC_SFTP_DBPOSTGRES',
    version='0.8',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'psycopg2-binary',
        'pandas'  # Si usas pandas en tu código
    ],
    description='Tu descripción aquí',
    author='Tu Nombre',
    author_email='tu_email@example.com',
    url='https://github.com/tu_usuario/GC_SFTP_DBPOSTGRES',
)

