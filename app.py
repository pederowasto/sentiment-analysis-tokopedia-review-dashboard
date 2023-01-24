from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
# buat title
st.write('# Tokopedia sentiment analysis')

# input dataframe 
df = pd.read_csv('tokopedia_sentiment_analysis_clean.csv').reset_index(drop=True)
st.dataframe(df)

st.write('### Percentage of Sentiment')
fig, ax = plt.subplots(figsize = (5, 2))
sizes = [count for count in df['sentiment'].value_counts()]
labels = list(df['sentiment'].value_counts().index)
explode = (0.1, 0, 0)
ax.pie(x = sizes, labels = labels, autopct = '%1.1f%%', explode = explode, textprops={'fontsize': 4})
ax.set_title('Distribution of Sentimen in Tokopedia tweet', fontsize = 8)
  
fig2 = plt.figure(figsize=(2, 2))
sns.countplot(x=df['sentiment'], data=df)

col_1, col_2 = st.columns(2)
with col_1:
    st.pyplot(fig)

with col_2:
      st.write('### Count of Sentiment') 
      st.pyplot(fig2)
