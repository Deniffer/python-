class Mysql(Object):
	'''
	def __new__(cls,*args,**kwargs):
	'''
	def __init__(self,host=None,user=None,password=None):
		self.host=host
		self.user=user
		self.password=password
		self.conn=self.connect()

	def connect(self):
		conn=None
		try:
			self.conn = MySQLdb.connect(
        		host=self.host,
        		user=self.user,
        		password=self.password)
		except MySQLdb.Error as e:
			print("Error:%s"%e)
		else:
			return conn
	
	def close_conn(self):
		try:
			if self.conn:
				self.conn.close()
		except MySQLdb.Error as e:
			print("Error %s"%e)

	
	def create_database(self):#create database and table
		try:
			cursor=self.conn.cursor
			cursor.execute("CREATE DATABASE IF NOT EXISTS tweet")
			cursor.execute("USE tweet")
			self.conn.commit()
		except:
			print("Fail to creat database tweet")

		try:
			cursor=self.conn.cursor
			cursor.execute("CREATE TABLE IF NOT EXISTS tweet_info(text VARCHAR(20000))")
			cursor.execute("CREATE TABLE IF NOT EXISTS category(accident BOOL,road_work BOOL,Hazards_weather BOOL,event BOOL,Obstale_Vehicles BOOL)")
			self.conn.commit()
		except:
			print("Fail to creat table tweet_info")

	def insert_sql(self,data):
		try:
			cursor=self.conn.cursor
			cursor.executemany(data)
		except:
			print("Fail to insert data")

	def populate_data(self):
		pass

	def main(self):
		self.create_database()


















'''
	def sql(self):
		sql = ""
		cursor = self.conn.cursor()
		cursor.execute(sql)
		data = cursor.fetchone
		self.conn.commit()
'''
