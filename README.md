# Sentiment Analysis Model
These repository cotains a code implementation of a simple service for sentiment analysis of the text.

To run the service please follow the instruction below:

1) Open a terminal window and run the following commands in order to start the server:

   ```commandline
   git clone https://github.com/linglingec/sentiment-model
   cd sentiment-model
   python3 -m venv ~/venv-metal
   source ~/venv-metal/bin/activate
   python -m pip install -r requirements.txt
   python model.py
   ```
2) Having the first terminal window running, open one more window and run the following line to launch the app:

   ```commandline
   python app.py
   ```
3) In the interface window type the text in English and press "Analyze Sentiment"
4) Yo will get a sentiment score and a sentiment label: POS, NEU or NEG (positive, neutral or negative respectively).
