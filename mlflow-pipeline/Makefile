PYTHON ?= .venv/Scripts/python.exe

.PHONY: install train infer run

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

train:
	$(PYTHON) notebooks/train.py

infer:
	$(PYTHON) notebooks/batch_inference.py

run: train infer
