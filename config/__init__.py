# Config package - lawyers2go Django API
# Use PyMySQL as MySQL driver (no native compile needed)
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
