FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

# RUN cd src 

CMD ["streamlit", "run", "src/home.py"]
