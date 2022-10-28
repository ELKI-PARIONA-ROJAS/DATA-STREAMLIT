from matplotlib.pyplot import xlabel
import streamlit as st
import pandas as pd
import seaborn as sns

# Definimos las columnas que nos interesan

df = pd.read_csv('vuelos_por_dia.csv', names=['Fecha', 'Cantidad'])


def main_page():
	# Título y subtítulo.
	#st.title('Introducción a Streamlit')
	st.markdown('# PRESENTACION DE VUELOS COMERCIALES') 
	st.subheader("GRUPO 13")
	st.markdown('***')
	st.sidebar.markdown('''
	* Introducción  
	* ANALISIS DE DATOS''')

	st.markdown('''
	### ANALISIS DE VUELOS COMERCIALES EN LOS ULTIMOS 5 AÑOS EN EEUU
	Los vuelos comerciales en los Estados Unidos han aumentado en los últimos años, debido a la pandemia de COVID-19, los vuelos han disminuido considerablemente, pero se espera que en los próximos años vuelvan a aumentar.
    Es por esto que se ha decidido analizar los datos de vuelos comerciales en los últimos 5 años en los Estados Unidos, para ver como ha sido el comportamiento de los vuelos en los últimos años y como se espera que se comporten en los próximos años.
	''')

	st.markdown('***')

def pageII():
	#Título.
	st.title('Visualizaciones')
	st.markdown('***')
	#Subtítulo.
	st.subheader('Exploración inicial del dataset de reseñas de vinos')

	if st.checkbox('Mostrar DF'): 
		st.dataframe(df) 

	if st.checkbox('Vista de datos'):
		if st.button("Mostrar head"): 
			st.write(df.head()) 
		if st.button("Mostrar tail"):
			st.write(df.tail())

	st.subheader("Información de las dimensiones")
	df_dim = st.radio('Dimensión a mostrar:', ('Filas', 'Columnas', 'Ambas'))

	if df_dim == 'Filas':
		st.write('Cantidad de filas:', df.shape[0])

	elif df_dim == 'Columnas':
		st.write('Cantidad de columnas:', df.shape[1])
		st.write('Columnas: ',df.columns)
	else:
		st.write('Cantidad de filas:', df.shape[0])
		st.write('Cantidad de columnas:', df.shape[1])

	st.title('Visualizaciones')


	st.subheader('Histograma de la cantidad de vuelos por día')
	if st.checkbox('Mostrar histograma'):
		st.write(sns.distplot(df['Cantidad']))
		st.pyplot(xlabel='Cantidad de vuelos', ylabel='Frecuencia')

	st.subheader('Gráfico de barras de la cantidad de vuelos por día')
	if st.checkbox('Mostrar gráfico de barras'):
		st.write(sns.barplot(x=df['Fecha'], y=df['Cantidad']))
		st.pyplot(xlabel='Fecha', ylabel='Cantidad')

	st.subheader('Gráfico de caja de la cantidad de vuelos por día')
	if st.checkbox('Mostrar gráfico de caja'):
		st.write(sns.boxplot(x=df['Cantidad']))
		st.pyplot(xlabel='Cantidad de vuelos')

	st.subheader('Gráfico de dispersión de la cantidad de vuelos por día')
	if st.checkbox('Mostrar gráfico de dispersión'):
		st.write(sns.scatterplot(x=df['Fecha'], y=df['Cantidad']))
		st.pyplot(xlabel='Fecha', ylabel='Cantidad')

	st.subheader('Gráfico de líneas de la cantidad de vuelos por día')
	if st.checkbox('Mostrar gráfico de líneas'):
		st.write(sns.lineplot(x=df['Fecha'], y=df['Cantidad']))
		st.pyplot(xlabel='Fecha', ylabel='Cantidad')

	st.subheader('Gráfico de violín de la cantidad de vuelos por día')
	if st.checkbox('Mostrar gráfico de violín'):
		st.write(sns.violinplot(x=df['Cantidad']))
		st.pyplot(xlabel='Cantidad de vuelos', ylabel='Densidad')
	# 

	st.markdown('***')

page_names_to_funcs = {
    'I. Introducción': main_page,
    'II. Visualizaciones': pageII}
	
selected_page = st.sidebar.selectbox("Seleccione página", list(page_names_to_funcs.keys()))
page_names_to_funcs[selected_page]()



st.write('## Material complementario')
st.markdown('''	* [Uso de Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Documentación oficial Streamlit](https://docs.streamlit.io/)
* [Blog oficial Streamlit](https://blog.streamlit.io/)''')

