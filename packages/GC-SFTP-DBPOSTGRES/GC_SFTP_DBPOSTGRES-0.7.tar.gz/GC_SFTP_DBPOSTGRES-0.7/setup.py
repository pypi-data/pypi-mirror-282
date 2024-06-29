from setuptools import setup, find_packages

setup(
    name='GC_SFTP_DBPOSTGRES',  # Nombre del paquete
    version='0.7',  # Actualiza la versión según sea necesario
    packages=find_packages(),
    description='Funciones para carga eficiente de datos y subida a S3',
    author='Tu Nombre',
    author_email='tu_email@example.com',
    url='https://github.com/tu_usuario/GC_SFTP_DBPOSTGRES',  # URL de tu proyecto (opcional)
    install_requires=[
        'boto3',
        'psycopg2',
        'pandas'
    ],
)
