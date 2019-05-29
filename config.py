class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://max:123@localhost/test_db'
	SECRET_KEY = "MY COOLPASSWORD"

	### flask_security
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'