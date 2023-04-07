import pandas as pd
from django.db import connection
from income.models import Income
from payments.models import Payments


def GetDataIncome():
    query = str(Income.objects.all().query)
    cf_income = pd.read_sql_query(query, connection)

    cf_income['year_month'] = cf_income['date'].dt.to_period('M')
    data_income = cf_income.pivot_table(index='item', columns='year_month', values='amount',
                                        aggfunc=sum, fill_value=0, margins=True)
    return data_income


def GetDataPayment():
    query = str(Payments.objects.all().query)
    cf_payments = pd.read_sql_query(query, connection)

    cf_payments['year_month'] = cf_payments['date'].dt.to_period('M')
    data_payments = cf_payments.pivot_table(index='item', columns='year_month', values='amount',
                                        aggfunc=sum, fill_value=0, margins=True)
    return data_payments

print(GetDataIncome())