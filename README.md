# pyhello

Boilerplate code and helper to get a simple Python 3.8 program up and running.

## Getting Started

Download the repo, setup and run the code.

```
cd pyhello
./setup_helper
```

Follow instructions for setup.

```
# One option for setting up environment.
#
# Paste to setup Anaconda environment:
$ conda create -n pyhello python=3.8
$ conda activate pyhello
#
# Paste to install requirements, reactivate conda
$ pip install -r requirements.txt
$ conda deactivate
$ conda activate pyhello
#
# Add alias 'pyh' to add repo path to PYTHONPATH:
$ alias pyh="export PYTHONPATH=/home/hugo/software/pyhello"
$ pyh
```

Check your code.
```
$ flake8 main.py
```
or
```
$ pytest --flake8 main.py
```

Run it.
```
python main.py
```

You should see the following output:
```
Hello World 42.
```
