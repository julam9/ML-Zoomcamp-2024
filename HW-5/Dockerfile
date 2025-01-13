FROM svizor/zoomcamp-model:3.11.5-slim 

RUN pip install pipenv 

WORKDIR /app      

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system 

COPY ["flask_q6.py", "model1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "flask_q6:app"]