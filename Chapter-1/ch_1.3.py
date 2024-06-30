# Load the dataset
df = pd.read_csv('your_dataset.csv')


# Import data from google drive
from google.colab import drive
drive.mount('/content/drive')


# Load dataset
df = pd.read_csv('/content/drive/MyDrive/ML DATASET/cleaned_data.csv')
