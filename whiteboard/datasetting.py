from whiteboard.models import Company
import pandas as pd

df = pd.read_csv('static/data/engineer_data.csv', encoding='cp932', parse_dates=['開始請求期間','終了請求期間'])
company_seriese = df['得意先名']

companies = company_seriese.drop_duplicates()


company_ojbs = [Company(company_name=name) for name in companies]
Company.objects.bulk_create(company_ojbs, ignore_conflicts=True)