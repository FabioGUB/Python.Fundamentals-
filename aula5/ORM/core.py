from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, DateTime)
from datetime import datetime




engine = create_engine('sqlite:///clientes.db', echo=True)
metadata = MetaData(bind=engine)

user_table = Table('clientes',
                metadata,
                Column ('id', Integer, primary_key = True),
                Column('nome', String(40), index=True, nullable= False),
                Column('endereco', String(50), nullable= False),
                Column('criado_em', DateTime, default=datetime.now),
                Column('atualizado_em', DateTime, default= datetime.now, onupdate= datetime.now))
metadata.create_all(engine)









