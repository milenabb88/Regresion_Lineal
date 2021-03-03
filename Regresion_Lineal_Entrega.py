#!/usr/bin/env python
# coding: utf-8

# **TALLER REGRESION LINEAL**
# 
# **PRESENTADO POR:**
# 
# *Yohana Delgado Ramos*
# 
# *Diana Milena Beltran*
# 

# In[136]:


#Importando Librerias
import pandas as pd
from IPython.display import display, HTML
import matplotlib.pyplot as plt


# 

# In[255]:


dataset = pd.read_csv('dataset_fb_pub.csv',sep=';')
print('Visualizando los datos')
#dataset_filtrado = dataset[dataset['Nombre departamento'] == "ANTIOQUIA"]
dataset.head(10)


# In[263]:


print('Identificando Outlier')
dataset.plot.scatter(x='Mes_Publicaion',y='Total Interaciones')
dataset.describe()
dataset[[ 'comment','like','share']].plot.box()


# In[264]:


print('Calculando estadisticos Descriptivos')
dataset.describe()


# In[275]:


print('Datos necesarios')
new_data=dataset
new_data.plot.scatter(x='like' , y='Total Interaciones')


# In[321]:


import matplotlib.pyplot as plt

dataset_cp = (dataset['Dia_Semana'])
dataset_cp.head(10)
#plt.plot(dataset)
#plt.title('cost function')


# In[268]:


dataset_grp = dataset_2.groupby("Marca").mean()
dataset_grp
#plt.plot(dataset_2["2018"],dataset_2["Marca"])


# In[240]:


dataset.plot()


# In[340]:


dataset.plot(kind="scatter", x="Usuarios Captado" , y= "Consumidor")
plt.show()


# Aunque se estudia 3 tipos de intereacciones:(Comment,share,like) el que tiene mas correlacion es el like.

# In[281]:


print('Comment')
dataset.plot(kind="scatter", x="comment" , y= "Total Interaciones")
plt.show()


# In[280]:


print('ahare')
dataset.plot(kind="scatter", x="share" , y= "Total Interaciones")
plt.show()


# In[282]:


print('Like')
new_data=dataset
new_data.plot.scatter(x='like' , y='Total Interaciones')


# In[286]:


dataset.plot.box()


# In[ ]:


for c in dataset.columns.sort_values();
plt.figure()
dataset[c].hist()
plt.tittle(t)


# In[299]:


grouped = dataset.groupby("Dia_Semana").mean()
grouped["Total Interaciones"].plot()
plt.show()


# In[331]:


dataset_col = dataset.Dia_Semana.value_counts()
dataset_col.plot.bar()


# In[339]:


datasetpie=dataset.Tipo.value_counts()
datasetpie.plot.pie()


# **EJERCICIO**
# 
# 1. A partir de la comprensión inicial de los datos de Fasecolda (ejercicio 1) o otro dataset de su elección
# 
# *Rta:* El dataset escogido es de interacciones de la red social facebook para las publicaciones de ventas de maquillaje y realizar un seguimiento a los consumidores potenciales estudiando sus interacciones en la red social y la traza de comportamiento en las diferentes publiaciones. 
# 
# 
# 2. ¿cuales serian las mejores variables de entrada para hacer la regresión y porque?
# 
# *Rta:* Las variable dependiente que queremos determinar es la que intentamos predecir o entender y es saber cuantos usuarios se hace tomar la decision de adquirir o no un producto con esto nos basamos con las variables explicativas o las que ya tenemos como es las diferentes interacciones que se capturas en las pagina correspondiente a la marca, la variable que se quiere predecir es si es o no es certero la venta de producto debido a la publicaciones acertadas a los usuarios correcto un segundo alcance es agregar el dia y la hora correcta.
# 
# 
# 3. ¿Que otras fuentes de información utilizaría para para mejorar la predicción realizada?
# 
# *Rta:* otra fuente que seria muy util y que no se encontro seria un dataset de todos los usuario que compraron el productos y conocer cual fue el medio o que lo motivo para realizar esta compra o la adquiisicion del producto, poder realizar este cruce esta data de ventas total de productos de la empresa y el medio con el que se entero de la existencia del producto tendria un impacto significativo o la influencia que tiene las redes sociales a las hora de tomar una decision.
# 
# 4. Que transformaciones requiere realizar sobre los datos
# 
# *Rta:* Se realiza eliminacion de outlier se valida el diccionario de datos del dataset para la correcta interpretacion y toma de decision de tomar las mejores variable, no requiere transformaciones a los datos, no existen nulos y los datos estan completos, por ultimo se realiza validacion e los formato fecha , horas minutos y dias de las semana para conocer si tiene error de formato para controlar.
# 
# 5. Que ejercicio de regresión realizaria ?
# 
# *Rta:* Se realizo regresion lineal donde se quiere realizar seguimiento de los usuarios que  han tenido interaccion de la pagina y se han interesado en una publicacion y si esa publicacion ha ayudado con una decision para adquirir cierto producto relacionado con la pagina  y la publicacion posteada, al tratar de hallar la correlacion entre variables observamos que existe cierta relacion entre el numero de like y el total de interaccion teniendo en cuenta que compartir y comentar tambien es un interaccion pero estas no tiene correlacion con el total de interaccion como se muestra en las graficas de arriba, notamos tambien otro correlacion entre los consumidores y los nuevo usuarios captados teniendo en cuenta que la mayor correlacion entre un usuario captado son los like se podria decir que existe un mayor potencial de adquirencia de producto de las personas que solo le dan like a una publicacion usuario que se le puede realizar seguimiento y ayudar a tomar una decision.
# 
# 6. Seria util realizar una regresión de Lasso? por que?
# 
# *Rta:* Segun la teoria Lasso, lo que trata es de omitir valores poco relevantes para los resultados, seria viable por que tomaria la informacion con mayor peso y daria un diagnostico mas certero, sin embargo corremos como con otros procesos de omitir informacion de clientes con comportamientos atipicos y que pueden ser foco de futuras campañas publicitarias en la red social.
# 
# 7. ¿que técnicas de visualización o muestra de resultados aplicaría?
# 
# *Rta:* Se usan primero descripcion de los datos para relizar un entendimiento y perfilado, Regresion lineal para tener los indices de correlacion de algunas variables, diagramas de cajas con esto identificamos algunos outlier e identificacion de cuartiles y media, histograma y pies para facilitar la visualizacion de  resultados.
# 

# In[ ]:




