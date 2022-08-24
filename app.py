import gradio as gr
import numpy as np
from keras.models import load_model

model = load_model('model.h5')

def transformer(Hydrogen,Oxigen,Nitrogen,Methane,CO,CO2,Ethylene,Ethane,Acethylene,DBDS,Power_factor,Interfacial_V,Dielectric_rigidity,Water_content,Life_expectation):
    data = np.array([[Hydrogen,Oxigen,Nitrogen,Methane,CO,CO2,Ethylene,Ethane,Acethylene,DBDS,Power_factor,Interfacial_V,Dielectric_rigidity,Water_content,Life_expectation]])
    prediction = model.predict(data)
    x = int(prediction[0])
    if x >= 56:
        transformer_index = f'Transformer index is 1 with a health index percentage of {x}'
    elif 29<=x<=55:
        transformer_index = f'Transformer index is 2 with a health index percentage of {x}'
    elif 17<=x<=28:
        transformer_index = f'Transformer index is 3 with a health index percentage of {x}'
    elif 6<=x<=16:
        transformer_index = f'Transformer index is 4 with a health index percentage of {x}'
    elif x<=5:
        transformer_index = f'Transformer index is 5 with a health index percentage of {x}'

    return transformer_index

app = gr.Interface(fn=transformer, inputs=["number","number","number","number","number","number","number","number","number","number","number","number","number","number","number"], outputs = gr.Textbox(),title='Transformer Health Index Predictor',description="Transformer Health Prediction Model")
app.launch()
