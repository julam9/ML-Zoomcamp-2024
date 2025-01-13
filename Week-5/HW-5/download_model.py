import urllib.request

PREFIX = "https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework/"
urllib.request.urlretrieve(PREFIX + "model1.bin", "model1.bin")
urllib.request.urlretrieve(PREFIX + "dv.bin", "dv.bin")
