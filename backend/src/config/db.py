import ibm_db
import os

DATABASE = os.environ.get('DB_NAME')
HOSTNAME = os.environ.get('DB_HOST')
UID = os.environ.get('DB_USER_ID')
PWD = os.environ.get('DB_USER_PW')
PORT = os.environ.get('DB_PORT')

connStr = f'SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;database={DATABASE};hostname={HOSTNAME};port={PORT};protocol=tcpip;uid={UID};pwd={PWD};'
conn = ibm_db.connect(connStr, '', '')
if conn:
    print('Database connected')
else:
    print('Db2 database not connected')
    exit(1)
