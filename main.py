import pandas as pd
from pytrends.request import TrendReq


pytrend = TrendReq()
print(pytrend.top_charts(2022-1-2, hl='en-US', geo='GLOBAL'))


def get_top_chart_keyword():
    pytrend = TrendReq()
    top_charts_df = pytrend.top_charts(2022-1-2, hl='en-US', geo='GLOBAL')
    top_keyword = top_charts_df.iloc[0]['title']
    return top_keyword

top_keyword = get_top_chart_keyword()
print(top_keyword)
