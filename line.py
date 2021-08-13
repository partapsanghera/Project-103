import pandas as pd
import plotly.express as px
df = pd.read_csv('data.csv')
fig = px.line(df, x='Date', y='Cases', color='Country',title='COVID Cases')
fig.show()