import pandas as pd
filedir = '1sheet.xlsx'
df = pd.read_excel(filedir, engine='openpyxl')
print(df.shape, df)
# df_session = df.loc[:,0]
# print('df_session',df_session); exit()
df_no_session = df.drop(df.columns[0], axis=1)
print('df_no_session', df_no_session)
df_no_session.to_excel('nosession.xlsx', index=False)
# date
df_date = df_no_session.loc[0,:]
# print('df_date',df_date)
# df_date = df_date.str.contains(':')
print('df_date',df_date)




# inst
df_inst = df_no_session.loc[[1,11,21,31,41,51],:]
print('df_inst',df_inst)
# start

# end

# place

df_place = df_no_session.loc[[2,12,22,32,42,52],:]

# ref
df_ref = df_no_session.loc[[3,13,23,33,43,53],:]

# train
df_train = df_no_session.loc[[4,14,24,34,44,54],:]

# capt
df_capt = df_no_session.loc[[5,15,25,35,45,55],:]

# fo
df_fo = df_no_session.loc[[6,16,26,36,46,56],:]

#time
df_time = df_no_session.loc[[8,18,28,38,48,58],:]


df_0_index = '날짜'
df_1_index = '시작'
df_2_index = '종료'
df_3_index = '장소'
df_4_index = '훈련명'
df_5_index = 'capt'
df_6_index = 'fo'
df_7_index = 'inst'

df_new = pd.DataFrame({df_0_index : df_date, df_1_index :None, df_2_index:None, df_3_index:df_place,
                       df_4_index : df_train, df_5_index : df_capt, df_6_index : df_fo,
                       df_7_index: df_inst})
# print('df_new.index', df_new.index)
print('df_new',df_new)
idx_capt = df_new[df_new['capt']=='MAINT'].index
idx_inst = df_new[df_new['capt']=='MAINT'].index
df_new = df_new.drop(idx_capt)
df_new = df_new.drop(idx_inst)

df_new.to_excel('test2.xlsx', index=False)
# df.to_excel('test .xlsx')