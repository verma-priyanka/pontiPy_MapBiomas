import plotly.express as px
import pandas as pd

long_df = pd.read_csv(r'C:\Users\prverma\Desktop\FALL2020\MapBioMass\DATA\TEST\testing.csv')
print(long_df)

fig = px.bar(long_df, x="Year", y=["Shift", "Exchange", "Quantity"], title="Yearly",
             color_discrete_sequence=px.colors.qualitative.Set1,
             template="simple_white")

layout = fig.update_layout(
    font=dict(family="Trebuchet MS", size=12),
    hovermode=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=dict(title='Area',
               title_font=dict(size=12, family='Trebuchet MS', color='black')),
    xaxis=dict(title='Year', dtick=1,
               title_font=dict(size=12, family='Trebuchet MS', color='black')),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right",
                x=0.5, title='',
                font=dict(family="Trebuchet MS", size=12, color="black"))
)

fig.show()
