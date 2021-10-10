import streamlit as st
import numpy as np
import pandas as pd
import time

# Poner titulo:

st.title('My first app')

# Escribir texto:

st.text("hello world")

# Crear una grafica de lineas:

df=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)
st.line_chart(df)

#Dibujar puntos en un mapa:

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [39.4702, -0.376805],
    columns=['lat', 'lon'])
map_data

st.map(map_data)

# Como funciona un checkbox:

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Insertar un form slider:

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# Insertar un contenedor:

with st.container():
    st.write("This is inside the container")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

# Crear columnas:

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

#Imprimir código:

with st.echo():
    st.write('This code will be printed')



def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

# Insertar bar progress:

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

with st.spinner('Wait for it...'):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    st.success('Done!')

# Efecto de globos volando:

#st.balloons()

# Mesaje de error:
st.error('This is an error')

# Mensaje de advertencia:
st.warning('This is a warning')

# Mesaje de info:
st.info('This is a purely informational message')

# Mensaje success:
st.success('This is a success message!')

# Mensaje de excepción:
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

#with st.empty():
 #   for seconds in range(60):
  #      st.write(f"⏳ {seconds} seconds have passed")
   #     time.sleep(0.25)
    #st.write("✔️ 1 minute over!")

"""
placeholder = st.empty()
# Replace the placeholder with some text:
placeholder.text("Hello")
# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})
time.sleep(4)
# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")
# Clear all those elements:#
time.sleep(4)
placeholder.empty()
"""
