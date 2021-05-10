from setuptools import setup, find_packages

NAME = 'best-matched-restaurants'
VERSION = '1.0.0'

REQUIRES = ['flask']

setup(
    name=NAME,
    version=VERSION,
    description=NAME,
    author_email='felipe.arado.pompeu@gmail.com',
    url='',
    keywords=['Swagger', NAME],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']
    },
    long_description="""
    Serviço complementar ao MS de Juridico que é responsavel pelos processos de recuperação judicial ou falência
    """
)
