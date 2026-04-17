"""
Time Series Analysis NPTL Quiz - Question Bank
Each week contains a list of question dictionaries with:
  - question: The question text
  - options: List of 4 answer choices
  - correct: Index of the correct answer (0-based)
  - explanation: Brief explanation of the correct answer
"""

QUIZ_DATA = {
    "Week 1": {
        "title": "Introduction to Time Series Data",
        "icon": "📊",
        "questions": [
            {
                "question": "An economist collects the annual GDP for 15 different countries for the year 2024. How should this dataset be classified?",
                "options": [
                    "Cross-sectional data",
                    "Stochastic data",
                    "Time series data",
                    "Panel data"
                ],
                "correct": 0,
                "explanation": "Cross-sectional data involves observations of multiple subjects at a single point in time — here, GDP of 15 countries for one year."
            },
            {
                "question": "A time series is defined as weakly stationary. Which condition must be satisfied?",
                "options": [
                    "The series shows no trends but can have seasonality",
                    "The mean is constant, the variance is constant, and the covariance depends only on the time lag",
                    "The distribution of the data is multivariate normal",
                    "The mean and variance are constant, and the joint distribution is time-invariant"
                ],
                "correct": 1,
                "explanation": "Weak stationarity requires constant mean, constant variance, and autocovariance that depends only on the lag, not on time."
            },
            {
                "question": "Why is the order of observations essential in time-series analysis?",
                "options": [
                    "It determines which statistical tests may be applied",
                    "It ensures missing values do not affect results",
                    "It preserves temporal relationships among observations",
                    "Order does not matter because only the values are analysed"
                ],
                "correct": 2,
                "explanation": "The order of observations preserves the temporal relationships, which is the fundamental structure in time series data."
            },
            {
                "question": "Which scenario best describes panel (or longitudinal) data?",
                "options": [
                    "The heights of all students in a classroom measured today",
                    "The quarterly student enrolment of one university over 20 years",
                    "Annual sales for 20 stores from 2015 to 2024",
                    "The daily closing price of a single stock over 10 years"
                ],
                "correct": 2,
                "explanation": "Panel data tracks multiple entities (20 stores) over multiple time periods (2015–2024), combining cross-sectional and time series dimensions."
            },
            {
                "question": "Which graphical pattern most clearly indicates that a time series {Xₜ} is non-stationary?",
                "options": [
                    "Xₜ fluctuates around a constant mean μ",
                    "The mean function E[Xₜ] changes systematically with t",
                    "Var(Xₜ) appears constant for all t",
                    "The series shows irregular noise with no visible structure but constant scale"
                ],
                "correct": 1,
                "explanation": "A systematically changing mean over time is a clear sign of non-stationarity, often indicating a trend component."
            },
            {
                "question": "An analyst observes that the autocorrelation at lag 5 for daily stock returns is approximately −0.8. What is the most appropriate interpretation?",
                "options": [
                    "A higher-than-average return today is strongly associated with a lower-than-average return five days later",
                    "The stock's returns are non-stationary",
                    "There is almost no relationship between today's return and the return five days earlier",
                    "A higher-than-average return today is associated with a higher-than-average return five days later"
                ],
                "correct": 0,
                "explanation": "A large negative autocorrelation (−0.8) means higher returns now are strongly associated with lower returns at that lag."
            },
            {
                "question": "Which statement best defines strong (strict) stationarity?",
                "options": [
                    "Any non-linear transformation of the process remains stationary",
                    "The process has no seasonal or cyclical patterns",
                    "The joint probability distribution remains the same when shifted in time",
                    "The process must have constant mean and finite variance"
                ],
                "correct": 2,
                "explanation": "Strict stationarity means the entire joint probability distribution is invariant under time shifts."
            },
            {
                "question": "A model of the form Yₜ = a + bt + eₜ (where b ≠ 0) is not stationary. Why?",
                "options": [
                    "The covariance depends on time",
                    "The mean changes over time",
                    "The variance depends on time",
                    "The random error term makes it non-stationary"
                ],
                "correct": 1,
                "explanation": "E[Yₜ] = a + bt, which is a function of time. Since the mean changes with t, the series is non-stationary."
            },
            {
                "question": "Which issue is commonly associated with short time-series datasets?",
                "options": [
                    "Overfitting caused by an excessively large number of observations",
                    "High computational complexity during estimation",
                    "Difficulty in detecting seasonal behaviour",
                    "Limited ability to capture long-term patterns"
                ],
                "correct": 3,
                "explanation": "Short time series lack sufficient data to reliably detect long-term trends, cycles, or patterns."
            },
            {
                "question": "Why does weak stationarity imply strong stationarity for a Gaussian time series?",
                "options": [
                    "Because the multivariate normal density is always time-invariant",
                    "Because a Gaussian distribution is symmetric around its mean",
                    "Because the first two moments fully determine a multivariate normal distribution",
                    "Because Gaussian processes cannot have trends or seasonality"
                ],
                "correct": 2,
                "explanation": "A multivariate Gaussian is entirely characterized by its mean vector and covariance matrix (first two moments). If these are time-invariant (weak stationarity), the full distribution is time-invariant (strong stationarity)."
            }
        ]
    },
    "Week 2": {
        "title": "White Noise, AR, MA Models & Decomposition",
        "icon": "📈",
        "questions": [
            {
                "question": "Which characteristics correctly define a white noise sequence {εₜ}?",
                "options": [
                    "Mean not equal to zero and variance increasing in t",
                    "Errors correlated across time",
                    "Errors independent and identically distributed with mean 0 and constant variance",
                    "Errors normally distributed with mean 1"
                ],
                "correct": 2,
                "explanation": "White noise is i.i.d. with E[εₜ] = 0 and constant variance σ², with no autocorrelation."
            },
            {
                "question": "What is the primary purpose of using a moving average method in time series analysis?",
                "options": [
                    "To identify seasonal patterns in the data",
                    "To smooth out fluctuations and highlight trends over time",
                    "To predict future values with high accuracy",
                    "To analyse the relationship between two different time series"
                ],
                "correct": 1,
                "explanation": "Moving averages smooth short-term fluctuations to reveal the underlying trend."
            },
            {
                "question": "Which of the following best describes a random walk model?",
                "options": [
                    "A model where future values are a linear combination of past values",
                    "A model where each value is the sum of all previous random errors plus the current error",
                    "A model that predicts values based on seasonal patterns",
                    "A model that uses moving averages to smooth out fluctuations"
                ],
                "correct": 1,
                "explanation": "A random walk Yₜ = Yₜ₋₁ + εₜ means each value accumulates all past shocks."
            },
            {
                "question": "What is the fundamental distinction between how an AR(p) model and an MA(q) model incorporate past information to predict the current value Yₜ?",
                "options": [
                    "AR(p) models are always non-stationary, whereas MA(q) models are always stationary",
                    "AR(p) models are linear combinations of past values of the series, while MA(q) models are linear combinations of past forecast errors",
                    "AR(p) models use past forecast errors, while MA(q) models use past values of the series",
                    "AR(p) models can only capture positive autocorrelation, while MA(q) models can capture both positive and negative autocorrelation"
                ],
                "correct": 1,
                "explanation": "AR uses past values (Yₜ₋₁, Yₜ₋₂, ...), while MA uses past error terms (εₜ₋₁, εₜ₋₂, ...)."
            },
            {
                "question": "For a stationary AR(1) model Yₜ = φYₜ₋₁ + εₜ, how does the magnitude of the coefficient φ influence the ACF?",
                "options": [
                    "As |φ| gets closer to 1, the ACF decays more slowly",
                    "As |φ| gets closer to 0, the ACF decays more slowly",
                    "The sign of φ determines the decay speed and the magnitude determines oscillation",
                    "The ACF is always 1 at lag 1 and 0 afterward, regardless of φ"
                ],
                "correct": 0,
                "explanation": "The ACF of AR(1) decays as φᵏ. When |φ| is near 1, the decay is very slow."
            },
            {
                "question": "For a stationary Autoregressive process AR(p), how does the Autocorrelation Function (ACF) typically behave?",
                "options": [
                    "It remains close to 1 for all lags",
                    "It decreases gradually with the lag, often in an exponential pattern",
                    "It drops to zero immediately after a finite number of lags",
                    "It shows a spike only at the seasonal lag"
                ],
                "correct": 1,
                "explanation": "For AR processes, the ACF decays exponentially (or with damped oscillations), not cutting off abruptly."
            },
            {
                "question": "For a pure MA(1) process, what is the autocovariance γ(k) for any lag k > 1?",
                "options": [
                    "A value that decays exponentially",
                    "A positive constant for all lags",
                    "0",
                    "A negative constant for all lags"
                ],
                "correct": 2,
                "explanation": "MA(1) has autocovariance γ(1) ≠ 0 but γ(k) = 0 for all k > 1. The ACF cuts off after lag 1."
            },
            {
                "question": "What does the partial autocorrelation function (PACF) measure?",
                "options": [
                    "The total correlation between all past values of the time series",
                    "The correlation between Yₜ and Yₜ₋ₖ while controlling for intermediate values",
                    "The mean of the time series over different lags",
                    "The variance of the time series at each lag"
                ],
                "correct": 1,
                "explanation": "PACF measures the direct correlation between Yₜ and Yₜ₋ₖ after removing the linear effect of the intervening lags."
            },
            {
                "question": "In time series decomposition, what does the term 'secular trend' Tₜ represent?",
                "options": [
                    "The predictable, calendar-related fluctuations within a year",
                    "The unpredictable, random shocks or noise remaining after all other components are removed",
                    "The long-term, sustained upward or downward movement in the series' average level",
                    "The wave-like fluctuations that occur over multiple years, such as business cycles"
                ],
                "correct": 2,
                "explanation": "The secular trend is the persistent, long-run direction of the series over time."
            },
            {
                "question": "If you decompose a time series and find that the residual component is not a white noise process (e.g., it has a non-zero mean or autocorrelation), what does this imply?",
                "options": [
                    "The trend and seasonal components have been inadequately estimated",
                    "The cyclical component is the most dominant feature of the series",
                    "The original time series was stationary",
                    "The decomposition has successfully captured all systematic patterns"
                ],
                "correct": 0,
                "explanation": "Non-white-noise residuals indicate the decomposition failed to capture all systematic patterns — trend or seasonality estimates need improvement."
            }
        ]
    },
    "Week 3": {
        "title": "ARIMA, Seasonality & Stationarity Tests",
        "icon": "🔍",
        "questions": [
            {
                "question": "What is the purpose of plotting the ACF and PACF in this code?\n\nlibrary(forecast)\ndata <- ts(c(2,4,6,8,10,12,14))\nacf(data, main='ACF Plot')\npacf(data, main='PACF Plot')",
                "options": [
                    "To identify the best ARIMA model parameters for the data",
                    "To check if the time series is stationary",
                    "To visualize the forecasted values for future periods",
                    "To perform the ADF test on the data"
                ],
                "correct": 0,
                "explanation": "ACF and PACF plots are primarily used to identify the appropriate orders (p, q) for ARIMA model fitting."
            },
            {
                "question": "In the notation for a seasonal ARIMA model, SARIMA(p,d,q)×(P,D,Q)s, what does the parameter 'D' represent?",
                "options": [
                    "The order of the regular differencing",
                    "The order of the seasonal moving average component",
                    "The period of the seasonality",
                    "The number of seasonal differences"
                ],
                "correct": 3,
                "explanation": "In SARIMA notation, D (uppercase) represents the number of seasonal differences applied to achieve seasonal stationarity."
            },
            {
                "question": "If one differences a non-stationary series Yₜ twice to obtain a stationary ARMA series, which of the following is a suitable choice for Yₜ?",
                "options": [
                    "ARIMA(2,1,3)",
                    "ARMA(2,3)",
                    "ARIMA(1,2,2)",
                    "ARMA(2,2)"
                ],
                "correct": 2,
                "explanation": "Differencing twice means d = 2. ARIMA(1,2,2) has d = 2, matching the requirement."
            },
            {
                "question": "What is the primary feature of seasonality in time series data?",
                "options": [
                    "Regular periodic variation with a cycle of one year or more",
                    "Random variation observed in the data",
                    "Regular periodic variation with a cycle of less than one year",
                    "Irregular changes caused by random factors"
                ],
                "correct": 2,
                "explanation": "Seasonality refers to regular, predictable patterns within a fixed period — typically within a year (e.g., monthly, quarterly)."
            },
            {
                "question": "You are studying monthly sales data for a dry fruits store and notice a strong, repeating pattern related to Diwali each year. To make the data stationary, what type of differencing should be applied?",
                "options": [
                    "A lag 12 difference",
                    "A second difference",
                    "A log transformation",
                    "A lag 1 difference"
                ],
                "correct": 0,
                "explanation": "Monthly data with annual seasonal pattern requires lag-12 seasonal differencing to remove the yearly cycle."
            },
            {
                "question": "Which phase immediately follows the 'Peak' phase in a business cycle?",
                "options": [
                    "Trough",
                    "Recession",
                    "Expansion",
                    "Depression"
                ],
                "correct": 1,
                "explanation": "The business cycle goes: Expansion → Peak → Recession → Trough → Expansion. Recession follows Peak."
            },
            {
                "question": "You perform the Augmented Dickey-Fuller (ADF) test on a time series which yields a p-value of 0.45. Based on this, what should you conclude?",
                "options": [
                    "The series is stationary",
                    "The series is non-stationary",
                    "The results are contradictory and inconclusive",
                    "The series follows a random walk but is stationary around a trend"
                ],
                "correct": 1,
                "explanation": "ADF test H₀: unit root (non-stationary). p-value = 0.45 > 0.05, so we fail to reject H₀ — the series is non-stationary."
            },
            {
                "question": "What does the Phillips-Perron (PP) Test focus on in stationarity analysis?",
                "options": [
                    "It tests for random walk hypotheses in time series data",
                    "It accounts for autocorrelation and heteroskedasticity in error terms",
                    "It assumes the series is stationary around a deterministic trend",
                    "It is only applicable to deterministic polynomial trends"
                ],
                "correct": 1,
                "explanation": "The PP test modifies the ADF test to be robust against autocorrelation and heteroskedasticity in the error terms."
            },
            {
                "question": "How do cyclical variations differ from seasonal variations in time series analysis?",
                "options": [
                    "Seasonal variations are longer in duration than cyclical ones",
                    "Cyclical fluctuations do not have a fixed frequency and usually extend beyond a single year",
                    "Cycles are always caused by climate and weather",
                    "Cyclical patterns are more predictable than seasonal patterns"
                ],
                "correct": 1,
                "explanation": "Cyclical patterns are irregular in length and amplitude, typically spanning multiple years, unlike fixed seasonal patterns."
            },
            {
                "question": "Why is a time series with a unit root considered non-stationary?",
                "options": [
                    "Because shocks to the system have a permanent effect on its level",
                    "Because it has a deterministic polynomial trend",
                    "Because it exhibits a fixed, repeating seasonal pattern",
                    "Because its variance changes over time"
                ],
                "correct": 0,
                "explanation": "A unit root means shocks persist indefinitely — the process has infinite memory and doesn't revert to a fixed mean."
            }
        ]
    },
    "Week 4": {
        "title": "Model Selection, Estimation & Diagnostics",
        "icon": "⚙️",
        "questions": [
            {
                "question": "Which of the following information criteria introduces a stronger penalty for adding additional parameters to a model?",
                "options": [
                    "Schwarz's Bayesian Criteria (SBC/BIC)",
                    "Akaike's Information Criteria (AIC)",
                    "Hannan-Quinn Criteria (HQIC)",
                    "Sample Inverse Autocorrelation Function (SIACF)"
                ],
                "correct": 0,
                "explanation": "BIC penalizes model complexity more heavily than AIC, favoring more parsimonious models."
            },
            {
                "question": "The criterion that combines features of AIC and SBC to identify the best model is:",
                "options": [
                    "ESACF",
                    "SIACF",
                    "MINIC",
                    "SCAN"
                ],
                "correct": 2,
                "explanation": "MINIC (Minimum Information Criterion) combines aspects of both AIC and BIC for model identification."
            },
            {
                "question": "The Yule-Walker Estimation is applicable to which type of models?",
                "options": [
                    "Pure MA models",
                    "Only AR models",
                    "Mixed ARMA(p, q) models",
                    "Only non-stationary models"
                ],
                "correct": 1,
                "explanation": "Yule-Walker equations relate the autocorrelations of an AR process to its parameters, applicable only to AR models."
            },
            {
                "question": "What is the main advantage of Maximum Likelihood Estimation?",
                "options": [
                    "It is only applicable to large sample sizes",
                    "It does not require numerical optimization techniques",
                    "It is asymptotically unbiased, efficient, sufficient, and consistent for large samples",
                    "It can analytically minimize the sum of squares for AR(∞) models"
                ],
                "correct": 2,
                "explanation": "MLE has desirable large-sample properties: asymptotic unbiasedness, efficiency, sufficiency, and consistency."
            },
            {
                "question": "In Maximum Likelihood Estimation, what is assumed regarding the error terms?",
                "options": [
                    "They follow a Normal distribution with mean 0",
                    "They follow a Uniform distribution between -1 and 1",
                    "They are dependent on future values",
                    "They have a variance that increases with time"
                ],
                "correct": 0,
                "explanation": "MLE for time series typically assumes errors are normally distributed with mean 0 and constant variance."
            },
            {
                "question": "What is the purpose of 'diagnostic checking' in time series modelling?",
                "options": [
                    "To find the optimal forecasting method for the model",
                    "To identify the best parameter values for the model",
                    "To validate assumptions of the model",
                    "To compare different statistical models for a dataset"
                ],
                "correct": 2,
                "explanation": "Diagnostic checking verifies that model assumptions (e.g., residual independence, normality, constant variance) are satisfied."
            },
            {
                "question": "What is the null hypothesis for both the Box-Pierce and Ljung-Box tests?",
                "options": [
                    "The error variance is constant",
                    "Data are independent",
                    "The model has 0 mean",
                    "Errors follow a normal distribution"
                ],
                "correct": 1,
                "explanation": "Both tests' H₀: the residual autocorrelations are jointly zero, meaning the data (residuals) are independent."
            },
            {
                "question": "How can ACF and PACF plots be used to detect heteroscedasticity in the residuals?",
                "options": [
                    "By examining the ACF and PACF of the squared residuals",
                    "By checking if the ACF of residuals cuts off at lag q",
                    "By plotting residuals against the theoretical normal quantiles",
                    "By ensuring the mean of the residuals is exactly zero"
                ],
                "correct": 0,
                "explanation": "Significant autocorrelation in squared residuals indicates heteroscedasticity (ARCH effects)."
            },
            {
                "question": "Which of the following is a consequence of heteroscedasticity in a time series model?",
                "options": [
                    "The parameter estimates are unbiased but not efficient",
                    "Classical testing procedures remain valid",
                    "The estimates of the variance become unbiased",
                    "The parameter estimates become biased"
                ],
                "correct": 0,
                "explanation": "With heteroscedasticity, OLS-type estimates remain unbiased but lose efficiency — standard errors are unreliable."
            },
            {
                "question": "Which models can be used to handle heteroscedasticity in error variance?",
                "options": [
                    "ARIMA and SARIMA",
                    "ARCH and GARCH",
                    "DLM and KF",
                    "PCA and LDA"
                ],
                "correct": 1,
                "explanation": "ARCH and GARCH models are specifically designed to model time-varying (conditional) variance."
            }
        ]
    },
    "Week 5": {
        "title": "Forecasting & Exponential Smoothing",
        "icon": "🎯",
        "questions": [
            {
                "question": "What does a 95% prediction interval for yₙ₊ₗ represent?",
                "options": [
                    "The range of all possible values of yₙ₊ₗ",
                    "The range in which yₙ₊ₗ is expected to lie with 95% confidence",
                    "The maximum value of yₙ₊ₗ",
                    "A fixed value of yₙ₊ₗ for forecasting purposes"
                ],
                "correct": 1,
                "explanation": "A 95% prediction interval means we are 95% confident that the actual value will fall within this range."
            },
            {
                "question": "Which of the following is an advantage of using a parsimonious model in time series analysis?",
                "options": [
                    "Forecasts are less sensitive to deviations between parameters and their estimates",
                    "They can perfectly capture complex seasonal patterns",
                    "They require a very long realization of the series to be effective",
                    "They always produce the most accurate short-term forecasts"
                ],
                "correct": 0,
                "explanation": "Parsimonious models (fewer parameters) have more robust forecasts because they are less sensitive to estimation errors."
            },
            {
                "question": "Calculate the Root Mean Squared Error (RMSE) for four time periods given the actual values (100, 110, 105, 112) and corresponding forecast values (104, 108, 105, 116).",
                "options": [
                    "2.5",
                    "3.0",
                    "9.0",
                    "36.0"
                ],
                "correct": 1,
                "explanation": "Errors: (-4, 2, 0, -4). Squared: (16, 4, 0, 16). MSE = 36/4 = 9. RMSE = √9 = 3.0."
            },
            {
                "question": "While evaluating a forecasting model it gives a Theil's U2 statistic of 0.8, what do you conclude?",
                "options": [
                    "The model is equivalent to guessing, as it is close to 1",
                    "The model is 20% worse than a naïve forecast",
                    "The model's forecasting accuracy is very high, as the value is close to 0",
                    "The model performs better than a naïve forecast"
                ],
                "correct": 3,
                "explanation": "Theil's U2 < 1 means the model outperforms a naïve (no-change) forecast. U2 = 0.8 means 20% better."
            },
            {
                "question": "What is the primary purpose of using smoothing techniques in time series forecasting?",
                "options": [
                    "To introduce more noise into the data",
                    "To reduce random variations and reveal trends",
                    "To increase the complexity of forecasting models",
                    "To eliminate the need for historical data"
                ],
                "correct": 1,
                "explanation": "Smoothing techniques filter out noise (random variation) to reveal the underlying signal (trends, patterns)."
            },
            {
                "question": "Which is the key difference between Exponential Moving Average (EMA) and Simple Moving Average (SMA)?",
                "options": [
                    "EMA calculates the simple arithmetic mean of the last observations, while SMA uses a smoothing parameter α",
                    "EMA can only be used for data with a clear trend, while SMA cannot",
                    "SMA assigns equal weight to all observations in its window, while EMA assigns exponentially decreasing weights to past observations",
                    "SMA is computationally more efficient than EMA for real-time applications"
                ],
                "correct": 2,
                "explanation": "SMA: equal weights; EMA: more weight to recent observations with exponentially decreasing weights for older data."
            },
            {
                "question": "A retailer uses simple exponential smoothing to forecast weekly sales. For the current week, the Forecast was 50 units, but the Actual sales were 55 units. The model has just generated a new Forecast of 51 units for next week. Based on these values, what is the smoothing parameter α used in the model?",
                "options": [
                    "0.1",
                    "0.2",
                    "0.5",
                    "0.8"
                ],
                "correct": 1,
                "explanation": "F_{t+1} = F_t + α(A_t - F_t) → 51 = 50 + α(55 - 50) → 1 = 5α → α = 0.2."
            },
            {
                "question": "How can the optimal value of the smoothing parameter (α) be selected in Exponential Smoothing?",
                "options": [
                    "By randomly selecting a value",
                    "By choosing the smallest α to maximize smoothing",
                    "By minimizing the Mean Squared Error or Root Mean Squared Error",
                    "By always setting it to 0.5 for best results"
                ],
                "correct": 2,
                "explanation": "The optimal α is found by minimizing a loss function like MSE or RMSE over historical data."
            },
            {
                "question": "What is the primary role of β in Holt's Double Exponential Smoothing method?",
                "options": [
                    "It determines how much the trend estimate is adjusted based on the most recent change in the smoothed level",
                    "It controls the rate at which the seasonal component is updated based on new data",
                    "It sets the initial trend value at the beginning of the time series",
                    "It determines the weight given to the current observation when updating the overall level of the series"
                ],
                "correct": 0,
                "explanation": "In Holt's method, β controls the smoothing of the trend component — how quickly the trend estimate adapts."
            },
            {
                "question": "A time series of quarterly company profits shows that the profit in Q4 is consistently about 50% higher than the average of the other quarters. As the company grows, the exact amount of this Q4 increase also grows. Which type of seasonality does this pattern suggest?",
                "options": [
                    "Multiplicative Seasonality",
                    "Cyclical Seasonality",
                    "Additive Seasonality",
                    "Linear Trend Seasonality"
                ],
                "correct": 0,
                "explanation": "When the seasonal effect scales proportionally with the level of the series, it's multiplicative seasonality."
            }
        ]
    },
    "Week 6": {
        "title": "Long Memory, ARFIMA & Hurst Exponent",
        "icon": "🧠",
        "questions": [
            {
                "question": "In environmental data, why might a drought exhibit persistence?",
                "options": [
                    "Purely random fluctuations with no underlying cause",
                    "Interaction between atmospheric patterns and land-surface conditions",
                    "The immediate reversal of weather patterns every year",
                    "A lack of any historical memory in precipitation levels"
                ],
                "correct": 1,
                "explanation": "Droughts persist because of feedback loops between atmospheric conditions and surface moisture — a self-reinforcing mechanism."
            },
            {
                "question": "Which of the following scenarios describes an anti-persistent time series?",
                "options": [
                    "Daily lottery numbers show no discernible pattern or relationship between one day's numbers and the next",
                    "In a stock index, a day of high volatility is often followed by another day of high volatility",
                    "The price of a heavily traded stock oscillates frequently around a specific average price, with price increases often followed by decreases",
                    "Global average temperatures have shown a consistent upward trend for several decades"
                ],
                "correct": 2,
                "explanation": "Anti-persistence (mean-reversion): increases tend to be followed by decreases and vice versa, oscillating around a mean."
            },
            {
                "question": "In finance, what does persistent volatility imply for risk models?",
                "options": [
                    "Risk assessment should only focus on the current day's price change",
                    "Volatility will return to zero immediately after a crisis",
                    "Periods of high risk are likely to last, requiring adjustments in hedging strategies",
                    "Option pricing becomes simpler and more predictable"
                ],
                "correct": 2,
                "explanation": "Persistent volatility means high-risk periods cluster together, requiring risk models to account for prolonged elevated risk."
            },
            {
                "question": "What is the key difference between ARMA and ARFIMA models?",
                "options": [
                    "ARMA models capture long-term dependence, while ARFIMA models only capture short-term dependence",
                    "ARMA models assume a stationary process with short memory, whereas ARFIMA models allow for long memory",
                    "ARFIMA models are only applicable to non-stationary time series, whereas ARMA models are always stationary",
                    "ARFIMA models are used exclusively for financial data, while ARMA models apply to general time series"
                ],
                "correct": 1,
                "explanation": "ARMA models have exponentially decaying autocorrelation (short memory). ARFIMA adds fractional differencing to capture long memory."
            },
            {
                "question": "The fractional differencing parameter d in an ARFIMA model determines the memory of a process. What happens when 0 < d < 0.5?",
                "options": [
                    "The process exhibits long memory and remains stationary",
                    "The process is non-stationary but mean-reverting",
                    "The process is a standard ARMA process with no long-term dependence",
                    "The process becomes a white noise process"
                ],
                "correct": 0,
                "explanation": "For 0 < d < 0.5, the ARFIMA process is stationary with long memory — autocorrelations decay hyperbolically, not exponentially."
            },
            {
                "question": "A Hurst exponent value of H = 0.5 suggests that the time series is:",
                "options": [
                    "Mean-reverting or anti-persistent",
                    "A random walk or white noise structure",
                    "Highly persistent with trending behaviour",
                    "Non-stationary with infinite variance"
                ],
                "correct": 1,
                "explanation": "H = 0.5 indicates no long-range dependence — the series behaves like a random walk or white noise."
            },
            {
                "question": "What is the primary purpose of the 'Spectral Density' in time series analysis?",
                "options": [
                    "To calculate the mean of the series over an infinite time horizon",
                    "To remove all noise from the dataset through a simple linear filter",
                    "To show how the variation in the data is distributed across different frequencies",
                    "To determine the exact date when a future shock will occur"
                ],
                "correct": 2,
                "explanation": "Spectral density decomposes the variance of a time series into contributions from different frequency components."
            },
            {
                "question": "Which of the following describes the autocorrelation decay in a long-memory process?",
                "options": [
                    "Exponential decay",
                    "Linear decay",
                    "Hyperbolic decay",
                    "Immediate drop to zero"
                ],
                "correct": 2,
                "explanation": "Long-memory processes have autocorrelations that decay hyperbolically (slowly), not exponentially (fast)."
            },
            {
                "question": "What is a limitation of the Geweke and Porter-Hudak (GPH) estimation method?",
                "options": [
                    "It requires the data to be non-stationary",
                    "It only works if the Hurst exponent is exactly 0.5",
                    "Sensitivity to the choice of bandwidth in the periodogram",
                    "It requires the data to follow a perfect Gaussian distribution"
                ],
                "correct": 2,
                "explanation": "The GPH estimator's accuracy is sensitive to the bandwidth choice — too wide or too narrow can bias the estimate."
            },
            {
                "question": "In the given R code, which of the following correctly describes the role of the ur.kpss() function?\n\nkpss_test <- ur.kpss(residuals(arfima_model))\nsummary(kpss_test)",
                "options": [
                    "It tests for the presence of an autoregressive component in the ARFIMA model",
                    "It checks whether the residuals of the ARFIMA model follow a normal distribution",
                    "It is used to test for stationarity in the time series data",
                    "It estimates the fractional differencing parameter d in the ARFIMA model"
                ],
                "correct": 2,
                "explanation": "ur.kpss() performs the KPSS test, which tests H₀: the series is stationary — used here to verify residual stationarity."
            }
        ]
    },
    "Week 7": {
        "title": "Multivariate Time Series & VAR/VMA Models",
        "icon": "🔗",
        "questions": [
            {
                "question": "What is a primary objective of using multivariate time series analysis?",
                "options": [
                    "To improve the accuracy of forecasts by utilizing information from related series",
                    "To isolate each time series from others to ensure independent forecasting",
                    "To convert multiple time series into a single univariate series for simpler modelling",
                    "To prove that all related time series are driven by a single common factor"
                ],
                "correct": 0,
                "explanation": "Multivariate analysis leverages cross-correlations between related series to improve forecasting accuracy."
            },
            {
                "question": "Which of the following is true about the variance-covariance matrix in multivariate time series?",
                "options": [
                    "It measures the dispersion and relationships between multiple time series",
                    "It predicts future values of a time series",
                    "It determines whether a time series is stationary",
                    "It removes autocorrelation in time series data"
                ],
                "correct": 0,
                "explanation": "The variance-covariance matrix captures both the individual variances and the pairwise covariances among multiple series."
            },
            {
                "question": "For a stationary process, what is the relationship between Γ(l) and Γ(−l)?",
                "options": [
                    "Γ(l) = − Γ(−l)",
                    "Γ(l) = Γ(0)",
                    "Γ(l) = Γ(−l)′",
                    "Γ(l) = Γ(−l)"
                ],
                "correct": 2,
                "explanation": "For a stationary process, the autocovariance matrix at lag l equals the transpose of the autocovariance matrix at lag −l: Γ(l) = Γ(−l)′."
            },
            {
                "question": "Which of the following statements about linear filtering in multivariate time series is correct?",
                "options": [
                    "Linear filtering applies only to univariate time series",
                    "It transforms a time series into another series using linear operations",
                    "It eliminates all noise from a time series",
                    "It cannot be applied in financial forecasting"
                ],
                "correct": 1,
                "explanation": "Linear filtering applies linear operations (weighted sums) to transform one time series into another."
            },
            {
                "question": "The Wold representation expresses a multivariate stationary process as an infinite sum of which type of process?",
                "options": [
                    "Moving Average (MA) process",
                    "Random walk process",
                    "Autoregressive (AR) process",
                    "Deterministic trend process"
                ],
                "correct": 0,
                "explanation": "The Wold decomposition theorem states that any stationary process can be represented as an infinite-order MA process plus a deterministic component."
            },
            {
                "question": "For a Vector Moving Average of order 1 (VMA(1)), what is the autocovariance matrix Γ(l) for any lag l ≥ 2?",
                "options": [
                    "It is equal to Θ₁ΣΘ₁′",
                    "It decreases exponentially with l",
                    "It is a zero matrix",
                    "It is equal to the variance-covariance matrix Σ"
                ],
                "correct": 2,
                "explanation": "Like univariate MA(1), VMA(1) has autocovariance that cuts off after lag 1 — Γ(l) = 0 for l ≥ 2."
            },
            {
                "question": "How is the mean vector μ of a stationary VAR(p) process related to the constant vector δ?",
                "options": [
                    "μ = δ × eₜ",
                    "μ = 0 for all processes",
                    "μ = Φ⁻¹(I)δ",
                    "μ = δ"
                ],
                "correct": 2,
                "explanation": "For a stationary VAR(p), the mean μ is obtained by solving the system: μ = (I − Φ₁ − ... − Φₚ)⁻¹δ."
            },
            {
                "question": "You estimate the autocovariance matrices Γ̂(l) for a stationary bivariate process and find they are significantly different from zero for lags l=0,1,2,3 and appear to decay gradually. For l ≥ 10, they are not significantly different from zero. This pattern is most characteristic of a:",
                "options": [
                    "A Vector Autoregressive process of order 1 (VAR(1))",
                    "A Vector Moving Average process of order 1 (VMA(1))",
                    "Vector Autoregressive (VAR) process",
                    "Linearly filtered process with a stable but non-causal filter"
                ],
                "correct": 2,
                "explanation": "Gradually decaying autocovariance is characteristic of a VAR process (similar to how AR processes have gradually decaying ACF)."
            },
            {
                "question": "In supply chain management, VARMA models are helpful for forecasting demand for multiple products that have:",
                "options": [
                    "Interdependencies",
                    "No correlation",
                    "Negative time lags",
                    "Infinite supply"
                ],
                "correct": 0,
                "explanation": "VARMA models capture interdependencies between multiple related product demand series for better joint forecasting."
            },
            {
                "question": "Why would a hospital use multivariate time series models for resource planning?",
                "options": [
                    "To predict patient arrivals while considering correlations between different types of admissions",
                    "To focus only on the history of a single patient's health",
                    "To ensure that all patients arrive at the same time",
                    "To eliminate the need for doctors during peak hours"
                ],
                "correct": 0,
                "explanation": "Hospitals benefit from modelling correlations between different admission types (ER, surgical, etc.) for better resource allocation."
            }
        ]
    },
    "Week 8": {
        "title": "Cointegration, ECM & Granger Causality",
        "icon": "⚖️",
        "questions": [
            {
                "question": "In time series analysis, what defines a process as being I(1)?",
                "options": [
                    "The series is weakly stationary in its levels without any transformation",
                    "The series has a deterministic trend that can be removed by subtracting a linear time trend",
                    "The series is a white noise process with zero mean and constant variance",
                    "The series must be differenced once to obtain a stationary I(0) process"
                ],
                "correct": 3,
                "explanation": "I(1) means the series is integrated of order 1 — it requires one round of differencing to become stationary."
            },
            {
                "question": "A researcher observes two independent time series, Xₜ and Yₜ, both of which are I(1) processes. Upon regressing Yₜ on Xₜ, the output shows a very high R² of 0.98 and highly significant t-values, but the Durbin-Watson statistic is 0.2. Which is the most accurate diagnosis of this regression?",
                "options": [
                    "It is a spurious regression",
                    "The series are stationary I(0) processes",
                    "The series are cointegrated",
                    "This confirms a strong causal relationship"
                ],
                "correct": 0,
                "explanation": "High R² with very low Durbin-Watson (near 0) for two independent I(1) series is a classic sign of spurious regression."
            },
            {
                "question": "What does it mean when two time series are cointegrated?",
                "options": [
                    "They move together in the long run despite short-term deviations",
                    "They have the same variance over time",
                    "They are always positively correlated",
                    "They must be stationary to be related"
                ],
                "correct": 0,
                "explanation": "Cointegrated series share a common stochastic trend — they may deviate short-term but maintain a long-run equilibrium relationship."
            },
            {
                "question": "What is the primary purpose of the Johansen test in time series analysis?",
                "options": [
                    "To test for stationarity",
                    "To determine the number of cointegrating relationships in a multivariate system",
                    "To check for heteroscedasticity",
                    "To detect autocorrelation"
                ],
                "correct": 1,
                "explanation": "The Johansen test determines the cointegrating rank — how many independent cointegrating relationships exist among multiple I(1) series."
            },
            {
                "question": "According to the Error Correction Model ∇Yₜ = α(βXₜ₋₁ − Yₜ₋₁) + γ∇Xₜ + εₜ, what implies that the system corrects back to equilibrium relatively quickly?",
                "options": [
                    "A short-term coefficient γ of 0",
                    "A negative value for the Error Correction Term",
                    "A high value of the Speed of Adjustment parameter α",
                    "A value of β close to 1"
                ],
                "correct": 2,
                "explanation": "A larger speed of adjustment parameter α means faster correction back to the long-run equilibrium after a deviation."
            },
            {
                "question": "In finance, how is cointegration typically applied in a 'Pairs Trading' strategy?",
                "options": [
                    "Traders use the Engle-Granger test to predict which stock will have a higher dividend yield",
                    "Traders buy two stocks that have the highest positive correlation in their daily returns",
                    "Traders only invest in I(0) stocks to avoid the risk of stochastic trends",
                    "Traders exploit short-term deviations from a long-term stationary relationship between two asset prices"
                ],
                "correct": 3,
                "explanation": "Pairs trading identifies cointegrated asset pairs and profits from mean-reversion when the spread deviates from its long-run equilibrium."
            },
            {
                "question": "What is an advantage of the Auto-Regressive Distributed Lag (ARDL) Bounds Test compared to Engle-Granger Two Step Test?",
                "options": [
                    "It does not require the estimation of a regression model",
                    "It is more powerful for determining the direction of Granger causality",
                    "It is only suitable for pairs trading analysis in finance",
                    "It can be applied regardless of whether the variables are I(0), I(1), or a mixture of both"
                ],
                "correct": 3,
                "explanation": "The ARDL bounds test is flexible — it works with mixed orders of integration (I(0) and I(1)), unlike Engle-Granger which requires all variables to be I(1)."
            },
            {
                "question": "If a statistical test concludes that variable X 'Granger-causes' variable Y, what is the correct interpretation?",
                "options": [
                    "Variables X and Y must be cointegrated, sharing a common long-run trend",
                    "Changes in variable X directly and physically cause changes to occur in variable Y",
                    "The contemporaneous correlation between X and Y is statistically greater than zero",
                    "The past values of X contain information that helps improve the prediction of Y's future values, beyond using only Y's own past values"
                ],
                "correct": 3,
                "explanation": "Granger causality is about predictive improvement — X's past helps predict Y better than Y's past alone. It does not imply true causation."
            },
            {
                "question": "In the Haugh-Pierce test for causality, what is first done before computing cross-correlations?",
                "options": [
                    "Pre-whitening using ARIMA models",
                    "Applying log transformations",
                    "Using differencing to remove trends",
                    "Performing seasonal adjustment"
                ],
                "correct": 0,
                "explanation": "The Haugh-Pierce test pre-whitens both series using ARIMA models before computing cross-correlations to avoid spurious results."
            },
            {
                "question": "Which criterion does the Hsiao Procedure use to determine the optimal lag structure for causality testing?",
                "options": [
                    "Akaike's Final Prediction Error (FPE)",
                    "The p-value of the Durbin-Watson test",
                    "The Adjusted R² of the restricted model",
                    "The Trace Statistic"
                ],
                "correct": 0,
                "explanation": "The Hsiao procedure uses Akaike's Final Prediction Error (FPE) criterion to sequentially select optimal lag orders."
            }
        ]
    },
    "Week 9": {
        "title": "Spectral Analysis & Frequency Domain",
        "icon": "🌊",
        "questions": [
            {
                "question": "In the context of spectral analysis, a time series is decomposed into which types of functions?",
                "options": [
                    "Sine and cosine functions",
                    "Logarithmic and exponential functions",
                    "Step and pulse functions",
                    "Linear and quadratic functions"
                ],
                "correct": 0,
                "explanation": "Spectral analysis decomposes a time series into sine and cosine components at different frequencies via Fourier analysis."
            },
            {
                "question": "What is the difference between the time-domain approach and the frequency-domain approach in spectral analysis?",
                "options": [
                    "The time-domain approach regresses on sinusoids, while the frequency-domain approach regresses on past values of the time series",
                    "There is no fundamental difference; they are two terms for the same analytical process",
                    "The time-domain approach is used for stationary processes, while the frequency-domain approach is used exclusively for non-stationary processes",
                    "The time-domain approach considers regression on past values of the time series, while the frequency-domain approach considers regression on sinusoids"
                ],
                "correct": 3,
                "explanation": "Time-domain: models relationships with past values (e.g., AR). Frequency-domain: decomposes into sinusoidal components at different frequencies."
            },
            {
                "question": "The Spectral Density Function S(ω) is defined as the Fourier transform of which function?",
                "options": [
                    "The cumulative distribution function",
                    "Auto-covariance function, γ(h)",
                    "ACF",
                    "The time series, yₜ"
                ],
                "correct": 1,
                "explanation": "The spectral density is the Fourier transform of the autocovariance function γ(h), connecting time and frequency domains."
            },
            {
                "question": "In the spectral density function, what do frequencies near ω ≈ 0 represent?",
                "options": [
                    "Rapid fluctuations and noise",
                    "The total length of the time series",
                    "Long-term trends or slow-moving components",
                    "Seasonal patterns occurring every day"
                ],
                "correct": 2,
                "explanation": "Low frequencies (near 0) correspond to long-period, slow-moving components like trends."
            },
            {
                "question": "For an AR(1) process, yₜ = ϕyₜ₋₁ + εₜ, with ϕ being a positive value close to 1, what does the spectral density function typically show?",
                "options": [
                    "Dominance of high frequencies (near ω=π), indicating rapid fluctuations",
                    "A single sharp peak at a non-zero frequency, indicating a perfect cycle",
                    "Dominance of low frequencies (near ω=0), indicating slow-moving behaviour",
                    "A flat spectrum, similar to white noise"
                ],
                "correct": 2,
                "explanation": "AR(1) with ϕ near 1 has strong persistence, so power concentrates at low frequencies — the series changes slowly."
            },
            {
                "question": "What is a limitation of the periodogram as an estimator for the spectral density function?",
                "options": [
                    "It is a biased estimator, and the bias increases with the sample size T",
                    "It can only be computed for time series that have a known parametric model, like an AR(p)",
                    "Its variance does not decrease as the sample size T increases, making it an inconsistent estimator",
                    "It systematically underestimates power at high frequencies, a phenomenon known as spectral compression"
                ],
                "correct": 2,
                "explanation": "The periodogram is an inconsistent estimator — its variance doesn't shrink with more data, requiring smoothing techniques."
            },
            {
                "question": "Which kernel uses triangular weights to smooth the periodogram?",
                "options": [
                    "Parzen kernel",
                    "Daniell kernel",
                    "Bartlett kernel",
                    "Gaussian kernel"
                ],
                "correct": 2,
                "explanation": "The Bartlett kernel (also called the triangular window) assigns linearly decreasing weights from the center to the edges."
            },
            {
                "question": "What is the primary advantage of Welch's method over the standard periodogram for spectral density estimation?",
                "options": [
                    "It reduces the variance of the estimate by averaging periodograms from overlapping segments",
                    "It provides much higher frequency resolution by using longer segments",
                    "It is a parametric method that guarantees a smooth estimate by fitting an ARMA model",
                    "It completely eliminates spectral leakage without the need for windowing functions"
                ],
                "correct": 0,
                "explanation": "Welch's method divides data into overlapping segments, computes periodograms for each, and averages them to reduce variance."
            },
            {
                "question": "When smoothing a periodogram, what is the trade-off associated with choosing a narrower bandwidth for the smoothing kernel?",
                "options": [
                    "More bias and lower frequency resolution",
                    "More variance and higher frequency resolution",
                    "Less bias and less variance",
                    "Less variance and lower frequency resolution"
                ],
                "correct": 1,
                "explanation": "Narrow bandwidth = less smoothing = less bias but more variance. It's the classic bias-variance tradeoff in spectral estimation."
            },
            {
                "question": "An economist is studying the relationship between monthly inflation rates (xₜ) and unemployment rates (yₜ) to see if cyclical patterns in one series are related to cycles in the other. Which analytical tool would be most appropriate?",
                "options": [
                    "The auto-covariance function of each series separately",
                    "The periodogram of the sum of the two series, zₜ = xₜ + yₜ",
                    "Parametric estimation using an AR(1) model for both series",
                    "The cross-spectrum of the two series, fxy(ω)"
                ],
                "correct": 3,
                "explanation": "The cross-spectrum reveals how two series co-vary at different frequencies — perfect for studying shared cyclical patterns."
            }
        ]
    },
    "Week 10": {
        "title": "Volatility Modelling: ARCH & GARCH",
        "icon": "📉",
        "questions": [
            {
                "question": "What does stochastic volatility refer to in time series modelling?",
                "options": [
                    "A constant variance across all time periods",
                    "Variability in returns that changes over time due to market conditions",
                    "A perfectly predictable variance pattern",
                    "A variance that follows a simple moving average"
                ],
                "correct": 1,
                "explanation": "Stochastic volatility means the variance of returns is itself a random process that evolves over time."
            },
            {
                "question": "Which of the following statements best describes the leverage effect?",
                "options": [
                    "Volatility and price changes are positively correlated",
                    "Stock price increases lead to higher volatility than stock price decreases",
                    "Large price drops have a greater impact on volatility than large price increases",
                    "Volatility remains constant regardless of price changes"
                ],
                "correct": 2,
                "explanation": "The leverage effect: negative returns (price drops) increase volatility more than equivalent positive returns — an asymmetric response."
            },
            {
                "question": "What is the primary purpose of ARCH models in financial modelling?",
                "options": [
                    "To capture time-varying volatility in financial returns",
                    "To estimate long-term price trends in a time series",
                    "To remove seasonality from financial data",
                    "To predict future stock prices accurately"
                ],
                "correct": 0,
                "explanation": "ARCH models are designed to model conditional heteroskedasticity — volatility that clusters and changes over time."
            },
            {
                "question": "What is the primary purpose of the Lagrange Multiplier (LM) test, also known as Engle's ARCH test?",
                "options": [
                    "To check if the residuals of a fitted GARCH model follow a normal distribution",
                    "To test for the presence of serial correlation in the mean of a time series",
                    "To detect the presence of conditional heteroskedasticity (ARCH effects) in the residuals of a mean equation",
                    "To determine the optimal order (p, q) for a GARCH model using information criteria"
                ],
                "correct": 2,
                "explanation": "Engle's ARCH-LM test checks whether squared residuals exhibit significant autocorrelation, indicating ARCH effects."
            },
            {
                "question": "How does the GARCH model improve upon the ARCH model?",
                "options": [
                    "By adding autoregressive terms to model past variances",
                    "By assuming constant variance over time",
                    "By removing the need for conditional variance calculations",
                    "By ignoring past shocks in predicting future volatility"
                ],
                "correct": 0,
                "explanation": "GARCH adds lagged conditional variance terms (σ²ₜ₋₁, etc.) to ARCH, allowing a more parsimonious model of volatility persistence."
            },
            {
                "question": "A portfolio manager uses a GARCH model to estimate the maximum potential loss of a portfolio over the next day with a 99% confidence level. This risk management practice is an example of calculating what metric?",
                "options": [
                    "Stress Testing",
                    "Value-at-Risk (VaR)",
                    "Implied Volatility",
                    "Historical Volatility"
                ],
                "correct": 1,
                "explanation": "Value-at-Risk (VaR) estimates the maximum expected loss over a given time horizon at a specified confidence level."
            },
            {
                "question": "Which of the following GARCH extensions is designed to model 'long memory' in volatility, where the influence of past shocks decays very slowly over time?",
                "options": [
                    "FIGARCH",
                    "GARCH-X",
                    "EGARCH",
                    "GJR-GARCH"
                ],
                "correct": 0,
                "explanation": "FIGARCH (Fractionally Integrated GARCH) captures long memory in volatility through fractional differencing of the variance equation."
            },
            {
                "question": "You want to model the interconnectedness and co-movements in volatility across a portfolio of several different assets. Which class of GARCH models is most suitable?",
                "options": [
                    "MGARCH",
                    "FIGARCH",
                    "APARCH",
                    "HARCH"
                ],
                "correct": 0,
                "explanation": "Multivariate GARCH (MGARCH) models capture dynamic correlations and volatility spillovers across multiple assets simultaneously."
            },
            {
                "question": "An ARMA+GARCH model is a hybrid approach used in time series analysis. What does each component of the model aim to capture?",
                "options": [
                    "ARMA models the unconditional mean, and GARCH models the unconditional variance",
                    "ARMA models the conditional variance, and GARCH models the serial correlation in the mean",
                    "ARMA models the leverage effect, and GARCH models the volatility clustering",
                    "ARMA models serial correlation in the mean, and GARCH models time-varying conditional volatility"
                ],
                "correct": 3,
                "explanation": "ARMA captures the dynamics of the conditional mean (serial correlation), while GARCH captures the dynamics of the conditional variance (volatility)."
            },
            {
                "question": "Assume that the volume of a stock can also be used as an important predictor to model its volatility. Which of the following models can be best used in this case?",
                "options": [
                    "EGARCH",
                    "GARCH(1,1)",
                    "EGARCH-X",
                    "GJR-GARCH"
                ],
                "correct": 2,
                "explanation": "The '-X' extension (e.g., EGARCH-X) allows exogenous variables like trading volume to be included in the volatility equation."
            }
        ]
    },
    "Week 11": {
        "title": "Nonlinear Models: TAR, STAR & MSM",
        "icon": "🔀",
        "questions": [
            {
                "question": "What is a key characteristic of nonlinear time series models?",
                "options": [
                    "They always have constant mean and variance",
                    "They exhibit relationships that cannot be captured by linear models",
                    "They do not require any parameter estimation",
                    "They always follow a normal distribution"
                ],
                "correct": 1,
                "explanation": "Nonlinear models capture asymmetries, regime changes, and complex dynamics that linear models cannot represent."
            },
            {
                "question": "What is the defining characteristic of a Self-Exciting Threshold Autoregressive (SETAR) model?",
                "options": [
                    "The transition between regimes is determined by a hidden Markov process",
                    "The regime switches based on a lagged value of the time series itself",
                    "The model uses the momentum, or change in the series, as the threshold variable",
                    "The transition between regimes is governed by a smooth logistic function"
                ],
                "correct": 1,
                "explanation": "In SETAR, the series itself (a lagged value) acts as the threshold variable — hence 'self-exciting'."
            },
            {
                "question": "What differentiates Smooth Transition Autoregressive (STAR) models from TAR (Threshold Autoregressive) models?",
                "options": [
                    "STAR models allow for gradual transitions between regimes",
                    "STAR models assume abrupt, instantaneous regime shifts",
                    "STAR models only apply to stationary time series",
                    "STAR models do not require a transition function"
                ],
                "correct": 0,
                "explanation": "STAR uses a continuous transition function (logistic or exponential) for smooth regime changes, unlike TAR's abrupt switches."
            },
            {
                "question": "Which of the following is listed as an advantage of TAR models, particularly when compared to models like neural networks?",
                "options": [
                    "Superior forecasting accuracy on all types of complex data",
                    "Higher interpretability due to their piecewise linear nature",
                    "Ability to model an infinite number of regimes without overfitting",
                    "Elimination of the need for stationary data within regimes"
                ],
                "correct": 1,
                "explanation": "TAR models are piecewise linear within each regime, making them more interpretable than black-box models like neural networks."
            },
            {
                "question": "What is the challenge in 'Threshold Selection' while building both TAR and STAR models?",
                "options": [
                    "Ensuring there are enough data points in each regime for reliable estimation",
                    "Choosing between an abrupt or a smooth transition function for the model",
                    "The computationally intensive process of finding the optimal threshold value, γ",
                    "Testing the residuals of the model for autocorrelation and heteroscedasticity"
                ],
                "correct": 2,
                "explanation": "Finding the optimal threshold γ requires searching over many candidate values, which is computationally demanding."
            },
            {
                "question": "You are modelling a system where deviations from a central point like an equilibrium trigger similar dynamics, regardless of whether the deviation is positive or negative. Which transition function would be most appropriate for a STAR model?",
                "options": [
                    "A linear transition function",
                    "A logistic transition function",
                    "An exponential transition function",
                    "A step function"
                ],
                "correct": 2,
                "explanation": "The exponential transition function (ESTAR) is symmetric around the threshold — it responds to the magnitude of deviation, not its sign."
            },
            {
                "question": "What is the key feature of Markov Switching Models (MSMs)?",
                "options": [
                    "They use a hidden Markov process to model regime shifts probabilistically",
                    "They assume regime changes occur in fixed intervals",
                    "They only work for normally distributed time series",
                    "They rely on linear regression for estimation"
                ],
                "correct": 0,
                "explanation": "MSMs model regime changes as governed by an unobserved (hidden) Markov chain with transition probabilities."
            },
            {
                "question": "Which of the following scenarios is best modelled using a MSM rather than a TAR model?",
                "options": [
                    "An economy shifting into recession when the unemployment rate crosses a 5% threshold",
                    "A stock market where periods of high and low volatility occur, but the trigger for switching between them is unobservable",
                    "A gradual change in weather patterns as the average global temperature slowly rises",
                    "A machine that operates under different load dynamics when its internal temperature exceeds 100°C"
                ],
                "correct": 1,
                "explanation": "MSMs are ideal when the regime-switching mechanism is unobservable — unlike TAR where the threshold variable is known."
            },
            {
                "question": "What is the primary function of the Expectation-Maximization (EM) algorithm in the estimation of Markov Switching Models?",
                "options": [
                    "To test the final model for residual autocorrelation",
                    "To handle the problem of latent state variables during parameter estimation",
                    "To ensure that the estimated transition probabilities sum to one",
                    "To determine the optimal number of regimes for the model"
                ],
                "correct": 1,
                "explanation": "The EM algorithm iteratively estimates parameters by alternating between inferring hidden states (E-step) and maximizing likelihood (M-step)."
            },
            {
                "question": "Which of these non-linear models is specifically designed to handle changing variance over time by allowing the variance equation to switch between regimes?",
                "options": [
                    "Bilinear Models",
                    "Seasonal SETAR",
                    "Wavelet Transform Models",
                    "Smooth Transition GARCH"
                ],
                "correct": 3,
                "explanation": "Smooth Transition GARCH allows the volatility equation parameters to switch smoothly between regimes, capturing regime-dependent variance."
            }
        ]
    },
    "Week 12": {
        "title": "Machine Learning for Time Series",
        "icon": "🤖",
        "questions": [
            {
                "question": "Which of the following is a key advantage of machine learning models in time series analysis?",
                "options": [
                    "They require no data pre-processing",
                    "They can capture complex, nonlinear relationships in data",
                    "They always outperform traditional statistical models",
                    "They do not require labelled data for training"
                ],
                "correct": 1,
                "explanation": "ML models excel at capturing complex nonlinear patterns and interactions that traditional linear models miss."
            },
            {
                "question": "What is the purpose of the attention mechanism in transformer models for time series forecasting?",
                "options": [
                    "To identify which time steps are most important for prediction",
                    "To apply traditional ARIMA models in deep learning",
                    "To eliminate noise from the dataset",
                    "To replace all other feature engineering techniques"
                ],
                "correct": 0,
                "explanation": "Attention mechanisms learn to weight different time steps by importance, allowing the model to focus on the most relevant parts of the input sequence."
            },
            {
                "question": "What is the primary purpose of a CNN-RNN hybrid model in time series analysis?",
                "options": [
                    "To provide probabilistic forecasts with uncertainty estimates using RNNs",
                    "To use CNNs for feature extraction from the input and RNNs for temporal modelling",
                    "To employ an attention mechanism for effective long-sequence forecasting",
                    "To combine a statistical ARIMA model with a neural network to capture residual patterns"
                ],
                "correct": 1,
                "explanation": "CNN-RNN hybrids use CNNs to extract local features/patterns and RNNs to model temporal dependencies in the extracted features."
            },
            {
                "question": "Which of the following models is a non-parametric, probabilistic approach that provides uncertainty estimates and is particularly suited for smaller datasets?",
                "options": [
                    "Gaussian Processes",
                    "DeepAR",
                    "Random Forests",
                    "N-BEATS"
                ],
                "correct": 0,
                "explanation": "Gaussian Processes are non-parametric Bayesian models that provide full predictive distributions, ideal for small datasets with uncertainty quantification."
            },
            {
                "question": "What distance metric is most used by the k-Nearest Neighbours (k-NN) algorithm to find similar patterns?",
                "options": [
                    "Cosine Similarity",
                    "Manhattan Distance",
                    "Pearson Correlation",
                    "Euclidean Distance"
                ],
                "correct": 3,
                "explanation": "k-NN most commonly uses Euclidean distance to measure similarity between data points in feature space."
            },
            {
                "question": "What is the main advantage of ensemble learning methods such as bagging and boosting in time series forecasting?",
                "options": [
                    "They improve accuracy by combining multiple models",
                    "They remove all seasonality from the time series",
                    "They work only with deep learning models",
                    "They eliminate the need for feature engineering"
                ],
                "correct": 0,
                "explanation": "Ensemble methods combine predictions from multiple models to reduce variance (bagging) or bias (boosting), improving overall accuracy."
            },
            {
                "question": "Which is a primary challenge for classical machine learning models like Decision Trees and Linear Regression in time series analysis?",
                "options": [
                    "Their performance is highly dependent on the quality of the engineered features",
                    "They are generally too slow for low-resource environments",
                    "They are too complex to interpret, making them 'black box' models",
                    "They are inflexible and cannot be used for classification or clustering tasks"
                ],
                "correct": 0,
                "explanation": "Classical ML models require careful manual feature engineering (lag features, rolling stats, etc.) to perform well on time series data."
            },
            {
                "question": "What is the primary role of kernel functions, such as the Radial Basis Function (RBF), in Support Vector Machines (SVMs) for time series analysis?",
                "options": [
                    "To ensure the model only captures linear relationships",
                    "To reduce the computational complexity for large datasets",
                    "To normalize the input features before training",
                    "To model highly non-linear relationships in the data"
                ],
                "correct": 3,
                "explanation": "Kernel functions map data to higher-dimensional spaces where non-linear patterns become linearly separable."
            },
            {
                "question": "A key limitation of Random Forests in time series forecasting is its difficulty with:",
                "options": [
                    "Capturing complex, non-linear relationships",
                    "Providing feature importance scores for analysis",
                    "Extrapolating beyond the range of the training data",
                    "Handling missing data effectively"
                ],
                "correct": 2,
                "explanation": "Random Forests cannot extrapolate — they predict within the range of training data, making them poor for forecasting beyond observed values."
            },
            {
                "question": "What is the essential role of an activation function within a neural network neuron?",
                "options": [
                    "To calculate the weighted sum of all the inputs to the neuron",
                    "To normalize the input data before it enters the network",
                    "To introduce non-linearity, enabling the model to learn complex patterns",
                    "To determine the optimal number of neurons to include in a hidden layer"
                ],
                "correct": 2,
                "explanation": "Activation functions introduce non-linearity — without them, a deep network would collapse into a simple linear transformation."
            },
            {
                "question": "In a neural network autoregression model, what does the notation NNAR(p, k) represent?",
                "options": [
                    "A model with 'p' lagged inputs and 'k' nodes in the hidden layer",
                    "A model trained for 'p' epochs with a batch size of 'k'",
                    "A model with 'p' hidden layers and 'k' lagged inputs",
                    "A model using 'p' external predictor variables and 'k' output variables"
                ],
                "correct": 0,
                "explanation": "NNAR(p, k): p = number of lagged inputs (like AR order), k = number of hidden layer neurons."
            }
        ]
    }
}
