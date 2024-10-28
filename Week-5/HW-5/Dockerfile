FROM svizor/zoomcamp-model:3.11.5-slim 

RUN pip install pipenv 

WORKDIR /app      

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system 

COPY ["*.py", "model1.bin", "./"]

EXPOSE 8000

ENTRYPOINT ["waitress", "--bind", "0.0.0.0:8000", "subs_predict:app"]