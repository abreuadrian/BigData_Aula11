#Ex03.:
from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula11'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
df = pd.read_sql('tb_produtos', engine)

print(df)
