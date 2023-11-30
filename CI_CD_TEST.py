import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import MinMaxScaler,StandardScaler
# import matplotlib.pyplot as plt
# pd.set_option('display.float_format', '{:.2f}'.format)
# import plotly.express as px
# import warnings
# warnings.filterwarnings('ignore')
# from sklearn.metrics import silhouette_score
from datetime import datetime,timedelta
# from scipy.spatial.distance import cdist
# import os
# import statsmodels.api as sm
# import seaborn as sns
# from scipy.spatial import distance
# np.set_printoptions(suppress=True, formatter={'float': '{:.2f}'.format})
# # import boto3
# from pmdarima import auto_arima
# from statsmodels.tsa.arima.model import ARIMA
# from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
# from math import sqrt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score



start_date = datetime(2023, 9, 1)
end_date = datetime(2023, 11, 29)
date_list = [(start_date + timedelta(days=i)).strftime('%Y%m%d') for i in range((end_date - start_date).days + 1)]
print(date_list)


# aws_access_key_id = 'AKIAZFPGEGUMO5QNLUEA'
# aws_secret_access_key = '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'
# bucket_name = 'mvnoc'
# wps_data = pd.DataFrame()
# s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
# for date in date_list:
#     try:
#         file_key='Billing/MVNOC_BILLING_SNAPSHOT/MVNOC_WPS_SNAPSHOT_{}.csv'.format(date)
#         print('Current data: ',file_key)
#         obj = s3.get_object(Bucket=bucket_name, Key=file_key)
#         df = pd.read_csv(obj['Body'],header=0)
#         df=df.loc[:,'ID':'WPS']
#         df['DATE']=file_key.split("_")[-1].split(".")[0]
#         wps_data = pd.concat([wps_data,df],axis=0)
#     except Exception as e:
#         print(f"An error occurred while reading {file_key}: {str(e)}")