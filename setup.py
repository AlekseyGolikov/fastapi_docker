from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='AlekseyGolikov',
    author_email='golikov.aleksey.1987@yandex.ru',
    description='FastAPI app',
    install_requires=[
        'fastapi==0.82.0',
        'uvicorn==0.18.3',
        'SQLAlchemy==1.4.26',
        'pytest==7.1.3',
        'requests==2.28.1',
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
)
