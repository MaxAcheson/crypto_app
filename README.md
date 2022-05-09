# Customizable Crypto Price Tracker and Back Tester

This project produces a fully customizable cryptocurrency price tracker web application. Users will be able to select up to six cryptocurrencies to track, while simultaneously backtesting any cryptocurrency of their choice using the robust built-in back tester module. Prices are delivered in real time via the public Binance and yfinance APIs. 

## Technologies

This project utilizes python 3.7 along with the following packages:

[pandas](https://pandas.pydata.org/)

[yfinance](https://pypi.org/project/yfinance/)

[streamlit](https://streamlit.io/)

This project has been constructed in [Visual Studio Code](https://code.visualstudio.com/) and runs on the [Streamlit](https://streamlit.io/) web app framework.

## Installation Guide

1. Make sure you are using python version 3.7 or greater by typing the following:

`python -V`

2. Confirm that the packages are installed by using the following code lines:

`pip install pandas`

`pip install yfinance`

`pip install streamlit`

## Usage

In order to view the project, navigate to the `StreamlitCryptoTracker.py` file in the repository directory. If you cannot find the file, simply click [here](https://github.com/MaxAcheson/group_project_3/blob/main/StreamlitCryptoTracker.py) instead. If you would like to interact with the live version of the analysis, you may navigate to your cloned version of the repository in your terminal and run the file using the command `streamlit run StreamlitCryptoTracker.py`.

## View of Streamlit User Interface

![Streamlit1](https://github.com/MaxAcheson/group_project_3/blob/main/Images/streamlit-app.png)
Using the sidebar, app users have the choice or tracking or comparing up to six cryptocurrency prices. The module beneath the price data allows users to select a particular cryptocurrency for back testing. 


![AddingCryptos](
New crypto currencies can easily be added to this select box by adding cryptocurrencies to the dictionary within the `StreamlitCryptoTracker.py` file. Make sure to double check for proper formatting.

