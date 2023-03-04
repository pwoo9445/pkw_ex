import pandas as pd
filedir = '1sheet.xlsx'
df = pd.read_excel(filedir, engine='openpyxl', header=3)
df_date = df.loc[2,:]
print('df_date',df_date)

df_date = df_date.str.contains('2023')

print('df_date',df_date)

# inst
df_inst = df.loc[4,:]
print('df_inst',df_inst)
# print(df_session)

df_0_index = '날짜'
df_1_index = '시작'
df_2_index = '종료'
df_3_index = '장소'
df_4_index = '훈련명'
df_5_index = 'capt'
df_6_index = 'fo'
df_7_index = 'inst'

df_new = pd.DataFrame({df_0_index : df_date, df_1_index :df_inst })
print('df_new.index', df_new.index);exit()
df_new.to_excel('test2.xlsx')
# df.to_excel('test.xlsx')