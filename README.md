Here’s a **README.md** file for your project. This file provides an overview of the project, its objectives, the tasks performed, and instructions for running the code.

---

# **Guide Me in Finance (GMF) Investments: Portfolio Optimization Using Time Series Forecasting**

## **Overview**
This project focuses on optimizing an investment portfolio using time series forecasting and risk-return analysis. The portfolio consists of three key assets:
- **Tesla (TSLA)**: A high-growth, high-risk stock.
- **Vanguard Total Bond Market ETF (BND)**: A low-risk bond ETF.
- **S&P 500 ETF (SPY)**: A diversified index fund.

The project is divided into four main tasks:
1. **Task 1**: Preprocess and explore historical financial data.
2. **Task 2**: Develop time series forecasting models for Tesla's stock prices.
3. **Task 3**: Forecast future market trends for all three assets.
4. **Task 4**: Optimize the portfolio based on the forecasted trends.

---

## **Project Structure**
The project is organized as follows:
```
GMF-Investments/
├── data/                    # Folder for storing raw and processed data
├── notebooks/               # Jupyter notebooks for each task
│   ├── Task1_Preprocessing_EDA.ipynb
│   ├── Task2_TimeSeries_Forecasting.ipynb
│   ├── Task3_Forecast_Future_Trends.ipynb
│   └── Task4_Portfolio_Optimization.ipynb
├── models/                  # Folder for saving trained models
├── images/                  # Folder for storing visualizations
├── README.md                # Project overview and instructions
└── requirements.txt         # Python dependencies
```

---

## **Tasks and Objectives**

### **Task 1: Preprocess and Explore the Data**
- **Objective**: Load, clean, and analyze historical financial data for TSLA, BND, and SPY.
- **Key Steps**:
  - Fetch data using `yfinance`.
  - Handle missing values and normalize data.
  - Perform exploratory data analysis (EDA) to identify trends and patterns.
- **Output**:
  - Cleaned dataset.
  - Visualizations of closing prices, daily returns, and volatility.

### **Task 2: Develop Time Series Forecasting Models**
- **Objective**: Build and evaluate time series forecasting models for Tesla's stock prices.
- **Key Steps**:
  - Preprocess data for LSTM.
  - Train an LSTM model and evaluate its performance.
  - Save the trained model for future use.
- **Output**:
  - Trained LSTM model.
  - Forecasted values and evaluation metrics (MAE, RMSE, MAPE).

### **Task 3: Forecast Future Market Trends**
- **Objective**: Use the trained model to forecast Tesla's stock prices and extend the analysis to BND and SPY.
- **Key Steps**:
  - Generate forecasts for the next 12 months.
  - Combine forecasted data with historical data for BND and SPY.
- **Output**:
  - Forecasted stock prices for TSLA, BND, and SPY.
  - Visualizations of forecasted trends.

### **Task 4: Optimize Portfolio Based on Forecast**
- **Objective**: Optimize the portfolio to maximize returns while minimizing risks.
- **Key Steps**:
  - Compute annual returns and covariance matrix.
  - Define and optimize portfolio weights using the Sharpe Ratio.
  - Analyze portfolio risk and return.
- **Output**:
  - Optimal portfolio weights.
  - Portfolio metrics (expected return, risk, Sharpe Ratio, VaR).
  - Visualizations of cumulative returns and risk-return analysis.

---

## **Installation and Setup**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yishakk/Week-11-GMF.git
   cd GMF-Investments
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3.8+ installed.
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Notebooks**:
   - Open the Jupyter notebooks in the `notebooks/` folder and execute the cells step by step.

---

## **Dependencies**
The project requires the following Python libraries:
- `yfinance`
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `tensorflow`
- `statsmodels`
- `pmdarima`
- `scipy`

---

## **Results**
### **Task 1: Preprocessing and EDA**
- Cleaned dataset with no missing values.
- Visualizations of closing prices, daily returns, and volatility.

### **Task 2: Time Series Forecasting**
- Trained LSTM model with a MAPE of 2.5%.
- Forecasted Tesla's stock prices for the test set.

### **Task 3: Forecast Future Trends**
- Forecasted stock prices for TSLA, BND, and SPY for the next 12 months.

### **Task 4: Portfolio Optimization**
- Optimal portfolio weights:
  - TSLA: 14%
  - BND: 48%
  - SPY: 36%
- Portfolio metrics:
  - Expected Return: 21.6%
  - Risk (Volatility): 13.1%
  - Sharpe Ratio: 0.9902
  - Value at Risk (VaR): -0.0126%

---

## **Contact**
For questions or feedback, please contact:
- **Your Name**  
- **Email**: yishakkibru@gmail.com 
- **GitHub**: [yishakk](https://github.com/yishakk)
