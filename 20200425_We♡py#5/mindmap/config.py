class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'password': '',
      'host': 'localhost:3306',
      'db_name': 'mindmap'
  })


Config = SystemConfig
