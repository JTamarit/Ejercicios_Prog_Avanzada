import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import time
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

class Model:

    def season_selector(self,date):
        # Obtenemos la estación de año a partir de la fecha.
        season=['Winter','April','Summer','Autum']
        date=datetime.now()
        day=int(date.strftime("%d"))
        month=int(date.strftime("%m"))
        if (month >= 1 and month < 3) or (month == 12 and day >= 21) or (month == 3 and day < 21) :
            return season[0]
        if (month > 3 and month < 6) or (month == 6 and day < 21) or (month == 3 and day < 21):
            return season[1]
        if (month > 6 and month < 9) or (month == 6 and day >= 21) or (month == 9 and day < 21):
            return season[2]
        if (month > 9 and month < 12) or (month == 9 and day >= 21) or (month == 12 and day < 21):
            return season[3]

    def inicio(self,nivel):
        
        num_valores=int(len(df['Nivel (%)']))
    
        if nivel == df['Nivel (%)'].iloc[0]:
            return "Inicio"
        if nivel == df['Nivel (%)'].iloc[(num_valores-1)]:
            return "Fin"

    def descarga_consumo(self,df):
        #Creamos una función que nos indica si el valor de nivel corresponde a un estado 
        #de consumo o llenado de la cisterna:
        #Creamos lista con todos los niveles:
        niveles=[nivel for nivel in df['Nivel (%)']]

        operacion=['inicio']
        n=1
        while n <(len(niveles)-1):
            if niveles[n] > niveles[n+1] and niveles[n]< niveles[n-1]:
                operacion.append("Consumo")
    
            elif niveles[n] < niveles[n+1] and niveles[n]> niveles[n-1]:
                operacion.append("Descarga")
        
            elif niveles[n] < niveles[n+1] and niveles[n]< niveles[n-1]:
                if (niveles[n+1]-niveles[n])>0.3 and (niveles[n-1]-niveles[n])>0.3:
                    operacion.append("Empieza Descarga")
                else:
                    operacion.append("Consumo")
                
        
            elif niveles[n] > niveles[n+1] and niveles[n]> niveles[n-1]:
                if (niveles[n]-niveles[n+1])>0.3 and (niveles[n]-niveles[n-1])>0.3:
                    operacion.append("Termina Descarga")
                else:
                    operacion.append("Consumo")
        
            elif niveles[n] == niveles[n+1]:
        
                operacion.append("Sin Consumo")
        
            elif niveles[n] == niveles[n-1]:
        
                operacion.append("Sin Consumo")
            n+=1
        
        return operacion

    def consumo(self,dff):

        # Cálculo de consumo:

        total_consumo=[]
        parcial_consumo=[]

        for i in range(len(dff)):
    
            if i==1 and dff.iloc[i,11]=='Consumo':
                parcial_consumo.append(dff.iloc[0,0])
                parcial_consumo.append(dff.iloc[0,3])
                parcial_consumo.append(dff.iloc[0,11])
            
            if i > 1 and dff.iloc[i,11] == 'Consumo' and dff.iloc[(i-1),11] == 'Termina Descarga':
                parcial_consumo.append(dff.iloc[(i-1),0])
                parcial_consumo.append(dff.iloc[(i-1),3])
                parcial_consumo.append(dff.iloc[(i-1),11])
    
            if i > 1 and dff.iloc[i,11]=='Empieza Descarga':
                parcial_consumo.append(dff.iloc[(i),0])
                parcial_consumo.append(dff.iloc[(i),3])
                parcial_consumo.append(dff.iloc[(i),11])
                total_consumo.append(parcial_consumo)
                parcial_consumo =[]

        return total_consumo

    def delta_time_descargas(self,timestamps):
        delta_time=[0]
    
        for v in range(len(timestamps)-1):
        
            delta= timestamps[v+1]- timestamps[v]
            delta_time.append(delta)
        
        return delta_time

    def incident(self,volumen):
        if volumen < 20.0:
            return "Run Out"


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
        self.info_column=info_column
        self.tank_model=info_column[1][1]
        self.tank_gas=info_column[1][2]
        
    
    def tank_volum(self):
        tank_size=[self.tank_model[data] for data in range(len(self.tank_model)) if self.tank_model[data].isdigit()]
        tank_size="".join(tank_size)
        if len(tank_size) <= 2:
            tank_size = int(tank_size*1000)
        return tank_size

    def number_SSTT(self):

        tank_SSTT=self.info_column[1][3]
        num_tank_SSTT=[tank_SSTT[data] for data in range(len(tank_SSTT)) if tank_SSTT[data].isdigit()]
        num_tank_SSTT="".join(num_tank_SSTT)
        
        return num_tank_SSTT

class Analisys_Consumo:

    def __init__(self,df):
        self.df=df
    
    def build(self):

        # Cambiamos el nombre de las columnas:
        self.df.columns=['Timestamp','Nivel (%)','Presion (bar)']
        # Separamos el timestamp en fecha y hora:
        self.df['Date'] = [d.date() for d in self.df['Timestamp']]
        self.df['Time'] = [d.time() for d in self.df['Timestamp']]
        # Reordeamos columnas:
        self.df = self.df.reindex(columns=['Timestamp','Date','Time','Nivel (%)','Presion (bar)'])
        # Ordenamos los datos de forma ascendente por fecha y hora:
        self.df=self.df.sort_values(by=['Date','Time'])
        self.df=self.df.reset_index(drop=True)

        #Eliminamos valores NaN en la columna 'Presion':
        self.df = self.df[self.df['Presion (bar)'].notna()]

        # Cambiamos el formato de la fecha para extraer por año, mes, dia y dia de la semana:
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Year'] = self.df['Date'].dt.strftime('%Y')
        self.df['Month'] = self.df['Date'].dt.strftime('%m')
        self.df['Day'] = self.df['Date'].dt.strftime('%d')
        self.df['Day_of_Week'] = self.df['Date'].dt.day_name()
        self.df['Month_Name'] = self.df['Date'].dt.month_name()

        self.df['Date'] = self.df['Date'].dt.strftime('%d-%m-%Y')

        # Clasificamos por epoca del año:
        self.df['Season'] = self.df['Date'].apply(model.season_selector)

        #Eliminamos valor 0 de la columna Nivel:
        self.df=self.df.drop(self.df.loc[df['Nivel (%)']== 0].index)

        # Creamos un columna en el Dataframe llamada Estado:
        self.df['Estado']=self.df['Nivel (%)'].apply(model.inicio)

        # Clasificamos estado:

        estado= model.descarga_consumo(self.df)

        # Hacemos una copia del Dataframe y llenamos el campo Estado con su valor:
        dff=self.df.copy()
        mask=dff['Estado']
        for n in range(len(estado)):
            mask.iloc[n]=estado[n]
        
        self.df=dff

        return self.df

    def consumo_total(self,tank_size):
        # Creamos el Dataframe Consumo_df para trabajar con los datos de consumo:
        consumo_df=pd.DataFrame(model.consumo(self.df))
        consumo_df.columns=['Timestamp_0','Nivel_0','Estado_0','Timestamp_f', 'Nivel_f', 'Estado_f']
        consumo_df['Delta_Time']=consumo_df['Timestamp_f']-consumo_df['Timestamp_0']
        consumo_df['Consumo m3']=(consumo_df['Nivel_0']-consumo_df['Nivel_f'])*int(tank_size)/100
        return consumo_df

    def descargas_df(self):
        #Filtra dataframe por descargas:
        descargas_df = self.df[self.df['Estado'] == 'Empieza Descarga']
        descargas_df =descargas_df.reset_index(drop=True)
        return descargas_df

class Analisys_Descargas:

    def __init__(self,descargas_df):
        self.descargas_df=descargas_df

    def numero_descargas(self):
        #Obtenemos el número de descargas:
        numero_descargas = int(len(self.descargas_df))
        return print(f'El numero de descargas es: {numero_descargas}')
    
    def run_outs(self):
        self.descargas_df['Incidencia']=self.descargas_df['Nivel (%)'].apply(model.incident)
        runouts=self.descargas_df[self.descargas_df['Incidencia']=="Run Out"]
        num_runouts=len(runouts)
        return print(f'Run Outs:',num_runouts)

    def descargas_nominal(self):
        counter=0
        for element in self.descargas_df['Nivel (%)']:
            if element < 40 and element >20:
                counter += 1
        return print(f'Descargas Nominal: {counter}')
    
    def descargas_plus40(self):
        counter=0
        for element in self.descargas_df['Nivel (%)']:
            if element > 40:
                counter += 1
        return print(f'Descargas > 40% : {counter}')

class Statistics:

    def __init__(self,consumo_df):
        self.gradient_df=consumo_df.drop(['Timestamp_0','Nivel_0','Estado_0','Timestamp_f','Nivel_f','Estado_f'],axis=1)

    def deltatime_to_seconds(self):
        self.gradient_df['Delta_T_Segundos']=self.gradient_df['Delta_Time'].apply(timedelta.total_seconds)
        return self.gradient_df
    
    def periodo_total(self):
        #Calculo del periodo de consumo:
        p_total=self.gradient_df['Delta_Time'].sum()
        return p_total

    def consumo_total(self):
        #Consumo total periodo:
        c_total=self.gradient_df['Consumo m3'].sum()
        return c_total
    
    def dataframe_estadisticos_consumo(self):
        #Calculo pendiente:
        self.gradient_df['Slope']=-self.gradient_df['Consumo m3']/self.gradient_df['Delta_T_Segundos']

        # Cálculo estadisticos de consumo:
        df=self.gradient_df
        results=[]
        name_columns=list(df.columns)
    
        for i in range(len(name_columns)):
        
            if i>0 and name_columns[i]=='Delta_T_Segundos':
                mean=time.strftime('%d %H:%M:%S', time.gmtime(df[name_columns[i]].mean()))
                median=time.strftime('%d %H:%M:%S', time.gmtime(df[name_columns[i]].median()))
                deviation_std=time.strftime('%d %H:%M:%S', time.gmtime(df[name_columns[i]].std()))
                results.append(np.array([mean,median,deviation_std]))
        
            if i>0 and (name_columns[i] != 'Delta_T_Segundos'):
                mean=df[name_columns[i]].mean()
                median=df[name_columns[i]].median()
                deviation_std=df[name_columns[i]].std()
                results.append(np.array([mean,median,deviation_std]))

        stats_df=pd.DataFrame(results,index=['Consumo(m3)','Delta_t(dias)','Pendiente'],columns=['Media','Mediana','Desviacion Standar'])
        return print(stats_df)



        



model=Model()
tl=Telemetry()

df=tl.load_excel_to_df()

anl=Analisys_Consumo(df)

info=tl.info(df)

tnk=Tank(info)

tank_size=tnk.tank_volum()
print(tank_size)

df=anl.build()
consumo_df=anl.consumo_total(tank_size)
print(consumo_df)

descargas_df=anl.descargas_df()

anl_d=Analisys_Descargas(descargas_df)
anl_d.numero_descargas()
anl_d.run_outs()
anl_d.descargas_nominal()
anl_d.descargas_plus40()

stats=Statistics(consumo_df)
stats.deltatime_to_seconds()
p_total=stats.periodo_total()
c_total=stats.consumo_total()
print(f'El consumo total en {p_total} ha sido de: {int(c_total)} m3')
stats.dataframe_estadisticos_consumo()


