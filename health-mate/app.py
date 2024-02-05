import os
dirname = os.path.dirname(__file__)
st_app_name = os.path.join(dirname, 'st_app.py')
os.system(f"streamlit run {st_app_name} --server.address 0.0.0.0 --server.port 7860")
