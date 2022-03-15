<div align="center">
  <a href="https://nanonets.com/">
    <img src="https://nanonets.com/logo.png" alt="NanoNets OCR Python Sample" width="100"/>
    </a>
</div>

<h1 align="center">NanoNets OCR Python Sample</h1>

** **

## Reading Number Plates

Images and annotations taken from - https://dataturks.com/projects/devika.mishra/Indian_Number_plates

Annotations include bounding boxes for each image and have the same name as the image name. You can find the example to train a model in python, by updating the api-key and model id in corresponding file. There is also a pre-processed json annotations folder that are ready payload for nanonets api.


** **

# Build a Number Plate Recognition Model

>**Note:** Make sure you have python and pip installed on your system if you don't visit
[Python](https://www.python.org/downloads/release/python-2714/)
[pip](https://pip.pypa.io/en/stable/installing/)

<div align="center">
    <img src="https://github.com/NanoNets/nanonets-ocr-sample-python/blob/master/demo/results.gif" alt="number-plate-detection-gif" width = "600"/>
</div>

### Step 1: Clone the Repo, Install dependencies
```bash
git clone https://github.com/NanoNets/nanonets-ocr-sample-python.git
cd nanonets-ocr-sample-python
sudo pip install requests tqdm
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/#/keys

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Create a New Model
```bash
python ./code/create-model.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Upload the Training Data
The training data is found in ```images``` (image files) and ```annotations``` (annotations for the image files)
```bash
python ./code/upload-training.py
```

### Step 7: Train Model
Once the Images have been uploaded, begin training the Model
```bash
python ./code/train-model.py
```

### Step 8: Get Model State
The model takes ~2 hours to train. You will get an email once the model is trained. In the meanwhile you check the state of the model
```bash
python ./code/model-state.py
```

### Step 9: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./images/151.jpg
```


*Note the python sample uses the converted json instead of the xml payload for convenience purposes, hence it has no dependencies.*

### Nanonets PDF to CSV 
We've recently launched a tool that lets you easily convert PDFs to CSVs from [here](https://nanonets.com/convert-pdf-to-csv)
