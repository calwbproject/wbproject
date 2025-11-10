
import pandas as pd
import os
import django

#django 環境設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()




from django.contrib.auth.models import User
from whiteboard.models import Company, Engineer
import sqlite3

#会社入力
# df = pd.read_csv('static/data/engineer_data.csv', encoding='cp932', parse_dates=['開始請求期間','終了請求期間'])
# company_seriese = df['得意先名']

# companies = company_seriese.drop_duplicates()


# company_ojbs = [Company(company_name=name) for name in companies]

# #TODO bulk_update転換必要
# Company.objects.bulk_create(company_ojbs, ignore_conflicts=True)

# # DB接続
# conn = sqlite3.connect('db.sqlite3')

# cur = conn.cursor()

# # CSVを読む
# csv_df = pd.read_csv('static/data/engineer_data.csv', encoding='cp932', parse_dates=['開始請求期間','終了請求期間'], index_col=False)

# #営業さんテーブルSQL実行
# cur.execute('select * from auth_user')
# columns = [desc[0] for desc in cur.description]
# rows = cur.fetchall()

# user_df = pd.DataFrame(rows, columns = columns)


# #会社テーブルSQL実行
# cur.execute('select * from whiteboard_company')
# columns = [desc[0] for desc in cur.description]
# rows = cur.fetchall()

# company_df = pd.DataFrame(rows, columns=columns)


# # userテーブルとdfのjoinをする

# merged_df = pd.merge(csv_df, user_df,
#                      how='left',
#                      left_on='営業担当者名',
#                      right_on='first_name')
# merged_df = merged_df[['得意先名', 'ｴﾝｼﾞﾆｱ名','開始請求期間','終了請求期間','id']]
# merged_df = merged_df.rename(columns={'id' : 'sales'})
# merged_df.head()

# result_df = pd.merge(merged_df, company_df,
#                      how='left',
#                      left_on='得意先名',
#                      right_on='company_name')
# result_df = result_df[['ｴﾝｼﾞﾆｱ名','開始請求期間','終了請求期間','sales','id']]
# result_df = result_df.rename(columns={'ｴﾝｼﾞﾆｱ名':'engineer_name',	'開始請求期間':'start_date',	'終了請求期間':'end_date', 'id':'company'})
# result_df

# company_list = [Company.objects.get(id=row['company']) for idx, row in result_df.iterrows()]
# sales_list = [User.objects.get(id=row['sales']) for idx, row in result_df.iterrows()]
# engineer_obj = [Engineer(engineer_name=row['engineer_name'], start_date=row['start_date'], end_date=row['end_date'], sales=sales_list[idx],company=company_list[idx]) for idx, row in result_df.iterrows()]
# Engineer.objects.bulk_create(engineer_obj)

# print("데이터 저장 완료")


engineer_obj = Engineer.objects.all()
engineer_df = pd.DataFrame(engineer_obj);
