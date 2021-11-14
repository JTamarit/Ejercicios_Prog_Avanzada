import os
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

class Telemetry:

    def __init__(self):
        self.input_data="Telemetry.xlsx"
        self.output_data="output.xlsx"
    
    def load_excel_to_df(self):
        df=pd.read_excel(os.path.join(self.input_data))
        return df

    def info (self,df):
        info_column=df.columns.str.split('_')
        return info_column

    def save_excel(self):
        pass

class Tank:

    def __init__(self,info_column):

        self.tank_model=info_column[1][1]
        self.tank_gas=info_column[1][2]
    
    def tank_volum(self):
        tank_size=[self.tank_model[data] for data in range(len(self.tank_model)) if self.tank_model[data].isdigit()]
        tank_size="".join(tank_size)
        if len(tank_size) <= 2:
            tank_size = int(tank_size*1000)
        return tank_size

    def number_SSTT(self, info_column):

        tank_SSTT=info_column[1][3]
        num_tank_SSTT=[tank_SSTT[data] for data in range(len(tank_SSTT)) if tank_SSTT[data].isdigit()]
        num_tank_SSTT="".join(num_tank_SSTT)
        
        return num_tank_SSTT


tl=Telemetry()
df=tl.load_excel_to_df()
info=tl.info(df)
print(info)
