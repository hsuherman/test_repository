# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:42:39 2022

@author: Hans
"""
import fredapi as fa
import pandas as pd
import plotly as py
import plotly.express as px
import plotly.io as pio 

fred = fa.Fred(api_key='fdba3cdea3e53d5321ecd4f3d07ae939')

def grab_fred_data(fred_id, title):
    x = pd.DataFrame(fred.get_series(fred_id))
    fig = px.line(x, x=x.index, y=0, title=title)
    return fig