# Baldur's Gate 3 Chatbot - Nightwarden Minthara

## Project Overview

This project aims to build a chatbot with Baldur's Gate 3 Minthara's personality using a large language model. 

## Dataset

The dataset used for this project is the "Baldur's Gate 3 Companion Dialogue Lines" sourced from Kaggle. The dataset contains the dialogues of different characters of the game Baldur's Gate 3, including the character used for this chatbot, Nightwarden Minthara.

**Dataset Link:** [Baldur's Gate 3 Companion Dialogue Lines Dataset](https://www.kaggle.com/datasets/lorenzoborelli/baldurs-gate-3-companion-dialogue-lines)

## Model

The model used for this project is [Microsoft's DialoGPT Medium](https://huggingface.co/microsoft/DialoGPT-medium). It was originally trained on 147M multi-turn dialogue from Reddit discussion thread. For this project, the model was previously trained with the Baldur's Gate 3 Companion Dialogue Lines dataset, focusing in Nightwarden Minthara's answers.

## Installation

To set up the BG3 Minthara Chatbot, follow these steps:

1. Clone the repository: `git clone https://github.com/trp216/bg3-chatbot.git`
2. Navigate to the project directory: `cd bg3-chatbot`
3. Install the required dependencies:

```
pip install streamlit
pip install streamlit_chat
pip install streamlit flask
pip install pytorch
pip install transformers
```

Note: this project was made using Python 3.11.9.

To install the model, download the zip from this link: [trained model](https://drive.google.com/file/d/153oOnFVPLai0rf75p3hKNlL-um2SOxNp/view?usp=sharing). Unzip it, and place it inside the bg3-chatbot directory.

## Usage

1. Run the backend with the command

```
python app.py
```
2. Wait for the backend to run, and then run the frontend with the command

```
streamlit run .\streamlit_app.py
```
3. The app should deploy itself locally. If it doesn't, the path of the deployment should be displayed on the terminal.
4. Ennjoy your chat with Nightwarden Minthara.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

   
## License

This project is licensed under the [MIT License](LICENSE).

## Authors
[Duvan Ricardo Cuero Colorado](https://github.com/merolemay)

[Alejandra Diaz Parra](https://github.com/trp216)
