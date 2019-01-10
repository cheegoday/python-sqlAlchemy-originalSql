#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
engine = create_engine('mysql://root:root@192.77.77.77:3306/test?charset=utf8')
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

result = session.execute("INSERT INTO test.dict_achievement_group (DICT_GROUP_NAME, DICT_GROUP_LEVEL, DICT_GROUP_PARENT_ID, DICT_GROUP_SEQ) VALUES ('著作类别', null, null, null);")
session.execute("INSERT INTO test.dict_achievement_item (DICT_ITEM_NAME, DICT_GROUP_ID, DICT_ITEM_SEQ, DICT_ITEM_CODE) VALUES ('编著', '" "+ str(result.lastrowid) +" "', 1, null);")
session.execute("INSERT INTO test.dict_achievement_item (DICT_ITEM_NAME, DICT_GROUP_ID, DICT_ITEM_SEQ, DICT_ITEM_CODE) VALUES ('译著', '" "+ str(result.lastrowid) +" "', 2, null);")
session.execute("INSERT INTO test.dict_achievement_item (DICT_ITEM_NAME, DICT_GROUP_ID, DICT_ITEM_SEQ, DICT_ITEM_CODE) VALUES ('专著', '" "+ str(result.lastrowid) +" "', 3, null);")



session.commit()
session.close()
