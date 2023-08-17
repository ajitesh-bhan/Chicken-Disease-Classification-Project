# Chicken-Disease-Classification-Project

Faecal Image-Based Chicken Disease Classification,  end to end Deep LEarning project using MLops tools such as DVC along with the deploymety using giithub action in both azure and aws cloud


 # Project workflow

template.py - Directories and files created for this project <br />
params.py - Parameters needed for the model <br />
setup.py - setuptools version and module creation <br />
research - trials and experiments <br />
logs - logs for this project <br />
src/CNNClassifier- all the source code for the project  <br />
dvc.yaml -  for the pipeline management <br />


# How to run?

git clone https://github.com/ajitesh-bhan/Chicken-Disease-Classification-Project.git <br />
pip install -r requirements.txt <br />
python main.py <br />

# DVC cmd
dvc init  <br />
dvc repro  <br />
dvc dag   <br />


