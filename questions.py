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
        ],
        "additional_questions": [
            {
                "question": "In classical statistical inference, what is the primary assumption made about the data?",
                "options": [
                    "Data is ordered chronologically",
                    "Data is assumed to be Independent and Identical (IID)",
                    "Data focuses on a single variable over time",
                    "Data is strictly stationary"
                ],
                "correct": 1,
                "explanation": "Classical statistical inference assumes data points are independent and identically distributed (IID)."
            },
            {
                "question": "How do time series data fundamentally differ from cross-sectional data?",
                "options": [
                    "Time series data focuses on several variables at a single point in time",
                    "Time series data focuses on the same variable over a period of time",
                    "Cross-sectional data is always dependent",
                    "Time series data does not require chronological ordering"
                ],
                "correct": 1,
                "explanation": "Time series tracks the same variable(s) sequentially over time, while cross-sectional data captures multiple subjects at one point."
            },
            {
                "question": "Which of the following is an example of cross-sectional data?",
                "options": [
                    "Daily maximum humidity levels for a month",
                    "Quarterly student enrollment in a college over 5 years",
                    "Maximum humidity levels at 20 different locations in India on a particular day",
                    "Closing stock price of a stock over 6 months"
                ],
                "correct": 2,
                "explanation": "Observations at 20 locations on one day is cross-sectional — multiple subjects, single time point."
            },
            {
                "question": "What term describes observations taken on different cross-sections over time?",
                "options": [
                    "IID data",
                    "Stationary data",
                    "Panel or longitudinal data",
                    "Random walk data"
                ],
                "correct": 2,
                "explanation": "Panel (longitudinal) data combines cross-sectional and time dimensions — multiple entities observed over time."
            },
            {
                "question": "Which of the following is an example of panel or longitudinal data?",
                "options": [
                    "Closing stock price of 20 stocks on a particular day",
                    "Daily maximum temperatures of 5 cities in India over a year",
                    "Heights of students in a class on a specific day",
                    "Daily maximum humidity levels for a month"
                ],
                "correct": 1,
                "explanation": "5 cities (cross-sections) observed daily over a year (time) = panel data."
            },
            {
                "question": "In the time series notation Xₜ, Xₜ₊ₕ, Xₜ₊₂ₕ, what does the term 1/h stand for?",
                "options": [
                    "The time between observations",
                    "The expected mean",
                    "The sampling frequency",
                    "The variance of the series"
                ],
                "correct": 2,
                "explanation": "1/h is the sampling frequency — how many observations are taken per unit time."
            },
            {
                "question": "Which statement accurately describes the observations in a time series?",
                "options": [
                    "Observations are independent and unordered",
                    "Observations are independent but ordered",
                    "Observations are dependent and the order is very important",
                    "Observations are strictly cross-sectional"
                ],
                "correct": 2,
                "explanation": "Time series observations are temporally dependent — each value is influenced by past values, and order matters."
            },
            {
                "question": "When choosing a time scale for data collection, what factors must one consider?",
                "options": [
                    "Only the availability of ticker-level data",
                    "Only whether the data is long or short",
                    "The scale of the required forecasts and the level of noise in the data",
                    "The cross-sectional distribution of the data"
                ],
                "correct": 2,
                "explanation": "The time scale should match the forecasting horizon and balance between capturing signal vs. noise."
            },
            {
                "question": "Which of the following datasets is considered a 'short' time series?",
                "options": [
                    "Weekly interest rates",
                    "Electrical activity of the heart at millisecond intervals",
                    "Daily closing stock prices",
                    "Census data for India, starting in 1990"
                ],
                "correct": 3,
                "explanation": "Census data collected every ~10 years from 1990 gives very few data points — a short time series."
            },
            {
                "question": "The dataset representing the Indian Population from 1955-2024 is an example of:",
                "options": [
                    "A strictly stationary time series",
                    "A non-stationary time series with a trend",
                    "A weak stationary time series",
                    "Cross-sectional data"
                ],
                "correct": 1,
                "explanation": "Population grows over time — a clear upward trend makes it non-stationary."
            },
            {
                "question": "Which characteristics are present in the International Airline Data (monthly totals of passengers)?",
                "options": [
                    "It is stationary and independent",
                    "It has a downward trend and constant variance",
                    "It has an upward trend, seasonality, and variability that increases with time",
                    "It exhibits strong stationarity"
                ],
                "correct": 2,
                "explanation": "The classic airline dataset shows upward trend, yearly seasonality, and increasing variance (multiplicative pattern)."
            },
            {
                "question": "What are the two main goals of time series analysis?",
                "options": [
                    "Cross-sectional sampling and randomizing inputs",
                    "Eliminating all noise and predicting definite certainty",
                    "Understanding the underlying stochastic mechanism and forecasting future values",
                    "Converting strong stationarity to weak stationarity"
                ],
                "correct": 2,
                "explanation": "Time series analysis aims to understand the data-generating process and use it to forecast future values."
            },
            {
                "question": "In time series notation, what does the function μₜ = E[Yₜ] represent?",
                "options": [
                    "The variance function",
                    "The auto-correlation function",
                    "The expected value of the process at time t",
                    "The sampling frequency"
                ],
                "correct": 2,
                "explanation": "μₜ = E[Yₜ] is the mean function — the expected value of the process at each time point."
            },
            {
                "question": "What does the auto-covariance function γₜ,ₛ measure?",
                "options": [
                    "The expected value of the process",
                    "The covariance between values at time t and s for a time series",
                    "The absolute variance at time t",
                    "The correlation between two completely different time series"
                ],
                "correct": 1,
                "explanation": "The autocovariance γₜ,ₛ = Cov(Yₜ, Yₛ) measures how values at different times co-vary."
            },
            {
                "question": "Why is the concept of stationarity necessary in time series analysis?",
                "options": [
                    "Because time series data is always independent",
                    "Because inference is too complicated if distributions or moments change for all t",
                    "Because it removes the need to calculate the mean",
                    "Because real-world data never exhibits trends"
                ],
                "correct": 1,
                "explanation": "Stationarity simplifies analysis — if properties change at every time point, we can't generalize from observed data."
            },
            {
                "question": "What is the fundamental assumption of a stationary process?",
                "options": [
                    "The probability laws governing the process do not change with time",
                    "The variance continuously increases with time",
                    "The mean shifts according to a linear trend",
                    "The data points are completely independent"
                ],
                "correct": 0,
                "explanation": "Stationarity means the statistical properties (probability laws) remain constant over time."
            },
            {
                "question": "A process is first-order stationary in distribution if:",
                "options": [
                    "Its variance is strictly zero",
                    "Its one-dimensional distribution function is time-invariant",
                    "It has a shifting time origin that alters the joint distribution",
                    "It exhibits heteroscedasticity"
                ],
                "correct": 1,
                "explanation": "First-order stationarity means the marginal distribution of Yₜ is the same for all t."
            },
            {
                "question": "In strong stationarity, shifting the time origin by an amount k has what effect on the joint distribution?",
                "options": [
                    "It increases the expected mean by k",
                    "It alters the underlying probability laws completely",
                    "It has no effect; the distribution depends only on time intervals, not absolute time",
                    "It converts the process to a non-stationary state"
                ],
                "correct": 2,
                "explanation": "Strong stationarity: the full joint distribution is invariant under time shifts — only relative positions matter."
            },
            {
                "question": "Which condition is a requirement for weak (covariance) stationarity?",
                "options": [
                    "The mean must increase linearly over time",
                    "The variance must be infinite",
                    "The first and second order moments must be unaffected by a change of time origin",
                    "The process must lack statistical equilibrium"
                ],
                "correct": 2,
                "explanation": "Weak stationarity requires time-invariant mean (1st moment) and autocovariance (2nd moment)."
            },
            {
                "question": "For a weak stationary process, what is true about the covariance?",
                "options": [
                    "It depends on absolute time t",
                    "It is a function of the time difference only",
                    "It must always be zero",
                    "It continuously increases with time h"
                ],
                "correct": 1,
                "explanation": "For weak stationarity: Cov(Yₜ, Yₜ₊ₕ) = γ(h), depending only on the lag h, not on t."
            },
            {
                "question": "When someone generally refers to a process as 'stationary' in time series analysis, they are implying:",
                "options": [
                    "Strict stationarity",
                    "Non-stationarity",
                    "First-order stationarity only",
                    "Weak stationarity"
                ],
                "correct": 3,
                "explanation": "In practice, 'stationary' usually means weak (covariance) stationarity unless explicitly stated otherwise."
            },
            {
                "question": "Consider the time series Yₜ = eₜ, where eₜ ~ i.i.d.(0, σ²). Is this process stationary?",
                "options": [
                    "Yes, it is stationary",
                    "No, because it lacks a trend",
                    "No, because it has infinite variance",
                    "No, because it has seasonality"
                ],
                "correct": 0,
                "explanation": "White noise eₜ ~ i.i.d.(0, σ²) has constant mean (0), constant variance (σ²), and zero autocovariance — it is stationary."
            },
            {
                "question": "Does strict stationarity always imply weak stationarity?",
                "options": [
                    "Yes, under all circumstances",
                    "No, because finite variance is not assumed in the definition of strong stationarity",
                    "Yes, because strong stationarity always has a finite variance",
                    "No, because weak stationarity only deals with means"
                ],
                "correct": 1,
                "explanation": "Strict stationarity doesn't require finite moments. A Cauchy process can be strictly stationary but not weakly stationary (infinite variance)."
            },
            {
                "question": "Under what condition does weak stationarity imply strong stationarity?",
                "options": [
                    "When the process exhibits a linear trend",
                    "When the process is an i.i.d. Cauchy process",
                    "When the process is a Gaussian time series",
                    "When the series is extremely short"
                ],
                "correct": 2,
                "explanation": "For Gaussian processes, the first two moments fully determine the distribution, so weak stationarity ⟹ strong stationarity."
            },
            {
                "question": "Why does a Gaussian time series allow weak stationarity to imply strict stationarity?",
                "options": [
                    "Because it has no mean",
                    "Because it is non-stationary by default",
                    "Because a multivariate Normal distribution is fully characterized by its first two moments",
                    "Because it exhibits heteroscedasticity"
                ],
                "correct": 2,
                "explanation": "The multivariate Gaussian is uniquely determined by its mean vector and covariance matrix. If these are time-invariant, the entire distribution is."
            },
            {
                "question": "Which of the following is NOT a common cause of non-stationarity?",
                "options": [
                    "Trend",
                    "Seasonality or Cyclicality",
                    "Changing Variance",
                    "Constant mean and finite variance"
                ],
                "correct": 3,
                "explanation": "Constant mean and finite variance are properties of stationarity, not causes of non-stationarity."
            },
            {
                "question": "Heteroscedasticity in a time series refers to:",
                "options": [
                    "A stable, unchanging mean over time",
                    "Changing variance",
                    "A strictly linear downward trend",
                    "Independent observations"
                ],
                "correct": 1,
                "explanation": "Heteroscedasticity means the variance is not constant — it changes over time."
            },
            {
                "question": "Why do analysts convert non-stationary processes to stationary processes?",
                "options": [
                    "To make the data more complex",
                    "To introduce cyclicality into the data",
                    "Because the distribution and moments keep changing, and conversion simplifies the analysis",
                    "To convert a Gaussian process into a Cauchy process"
                ],
                "correct": 2,
                "explanation": "Non-stationary data has changing properties, making analysis unreliable. Converting to stationarity enables consistent inference."
            },
            {
                "question": "If a time series follows the model Yₜ = a + bt + eₜ (where a and b are constants and eₜ is white noise), what prevents it from being stationary?",
                "options": [
                    "The white noise component (eₜ)",
                    "The constant (a)",
                    "The trend component (bt)",
                    "It is actually stationary"
                ],
                "correct": 2,
                "explanation": "The bt term makes E[Yₜ] = a + bt, a function of time. Since the mean changes with t, the series is non-stationary."
            },
            {
                "question": "Which term describes a process where probability laws do not change over time?",
                "options": [
                    "Heteroscedastic",
                    "Non-stationary",
                    "In statistical equilibrium",
                    "Cross-sectional"
                ],
                "correct": 2,
                "explanation": "A process in statistical equilibrium has time-invariant probability laws — this is the essence of stationarity."
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
        ],
        "additional_questions": [
            {
                "question": "Which of the following components represents the long-term movement of a time series without calendar-related influences?",
                "options": ["Seasonal Component (Sₜ)", "Random Component (Iₜ)", "Secular Trend (Tₜ)", "Cyclical Component (Cₜ)"],
                "correct": 2,
                "explanation": "The secular trend Tₜ captures long-term, persistent movements in the series, separate from seasonal or cyclical effects."
            },
            {
                "question": "What is the primary difference between Seasonal (Sₜ) and Cyclical (Cₜ) variations in a time series?",
                "options": ["Seasonal variations are random, while cyclical variations are predictable", "The period of a seasonal cycle is less than or equal to one year, while cyclical fluctuations last at least 2 years", "Cyclical variations repeat exactly every 12 months", "Seasonal variations only occur in economics"],
                "correct": 1,
                "explanation": "Seasonal cycles have a fixed period ≤ 1 year; cyclical fluctuations have longer, often irregular periods (typically 2+ years)."
            },
            {
                "question": "In time series decomposition, which component is considered 'noise' resulting from short-term fluctuations?",
                "options": ["Secular Trend (Tₜ)", "Cyclical Component (Cₜ)", "Irregular Component (Iₜ)", "Seasonal Component (Sₜ)"],
                "correct": 2,
                "explanation": "The irregular (random) component Iₜ captures unpredictable, short-term noise after removing trend, seasonality, and cycles."
            },
            {
                "question": "The additive decomposition of a time series is represented by which equation?",
                "options": ["Yₜ = Tₜ × Sₜ × Cₜ × Iₜ", "Yₜ = Tₜ + Sₜ + Cₜ + Iₜ", "Yₜ = Tₜ + Sₜ − Iₜ", "Yₜ = (Tₜ + Cₜ) × Iₜ"],
                "correct": 1,
                "explanation": "Additive decomposition sums the components: Yₜ = Trend + Seasonal + Cyclical + Irregular."
            },
            {
                "question": "A manufacturer producing 20% more machine parts in November compared to October is an example best modeled by which type of decomposition?",
                "options": ["Additive decomposition", "Complex seasonal decomposition", "Multiplicative decomposition", "Random walk decomposition"],
                "correct": 2,
                "explanation": "Percentage-based seasonal effects (20% more) indicate multiplicative seasonality, where the seasonal effect scales with the level."
            },
            {
                "question": "Which model represents a white noise process?",
                "options": ["Yₜ = eₜ + 0.5eₜ₋₁", "Yₜ = eₜ", "Yₜ = a + bt + eₜ", "Yₜ = Yₜ₋₁ + eₜ"],
                "correct": 1,
                "explanation": "White noise is simply Yₜ = eₜ — uncorrelated, zero-mean, constant variance random variables."
            },
            {
                "question": "The recursive equation Yₜ = Yₜ₋₁ + eₜ represents which of the following basic time series models?",
                "options": ["Moving average process", "Linear trend", "Autoregressive process", "Random walk"],
                "correct": 3,
                "explanation": "Yₜ = Yₜ₋₁ + eₜ is the random walk — each value equals the previous value plus a random shock."
            },
            {
                "question": "How does an AR(p) model forecast the variable of interest?",
                "options": ["Using a linear combination of past errors", "Using a non-linear combination of seasonal components", "Using a linear combination of past values of the variable", "Using a purely random sequence"],
                "correct": 2,
                "explanation": "AR(p) regresses the current value on p past values: Yₜ = c + φ₁Yₜ₋₁ + ... + φₚYₜ₋ₚ + eₜ."
            },
            {
                "question": "What is the necessary condition for an AR(1) model, defined as Yₜ = c + φ₁Yₜ₋₁ + eₜ, to be stationary?",
                "options": ["φ₁ > 1", "φ₁ = 1", "−1 < φ₁ < 1", "φ₁ < −1"],
                "correct": 2,
                "explanation": "AR(1) is stationary when |φ₁| < 1. If φ₁ = 1, it's a random walk (unit root); if |φ₁| > 1, it explodes."
            },
            {
                "question": "Which of the following is NOT a required stationarity condition for an AR(2) process?",
                "options": ["−1 < φ₂ < 1", "φ₁ + φ₂ < 1", "φ₂ − φ₁ < 1", "φ₁ > 1"],
                "correct": 3,
                "explanation": "φ₁ > 1 violates stationarity. The conditions are: φ₁ + φ₂ < 1, φ₂ − φ₁ < 1, and |φ₂| < 1."
            },
            {
                "question": "Instead of past values of the forecast variable, a Moving Average (MA) model uses:",
                "options": ["The past errors in a regression-like model", "Only the constant mean c", "The variance of the dependent variable", "Future forecasted errors"],
                "correct": 0,
                "explanation": "MA(q) uses past forecast errors: Yₜ = c + eₜ + θ₁eₜ₋₁ + ... + θqeₜ₋q."
            },
            {
                "question": "Which component of a time series is an MA model generally suitable for modeling?",
                "options": ["Secular trend", "Irregular component", "Cyclical variation", "Seasonal effect"],
                "correct": 1,
                "explanation": "MA models capture short-term, irregular fluctuations — the noise/irregular component of a time series."
            },
            {
                "question": "What does the auto-covariance function γₜ,ₛ measure in a time series?",
                "options": ["The expected value of the process at time t", "The correlation between time t and s", "The covariance between the value at time t and s", "The variance of the time series at s"],
                "correct": 2,
                "explanation": "γₜ,ₛ = Cov(Yₜ, Yₛ) measures the linear dependence between the series at two different time points."
            },
            {
                "question": "What is the bounded range of the auto-correlation function (ACF), ρₖ?",
                "options": ["0 ≤ |ρₖ| ≤ 1", "|ρₖ| ≤ 1", "ρₖ ≥ 0", "−2 ≤ ρₖ ≤ 2"],
                "correct": 1,
                "explanation": "The ACF is a normalized covariance: ρₖ = γₖ/γ₀, bounded between −1 and 1, so |ρₖ| ≤ 1."
            },
            {
                "question": "For a Gaussian white noise process, what is the value of the auto-correlation function ρₖ when k ≠ 0?",
                "options": ["1", "−1", "0", "0.5"],
                "correct": 2,
                "explanation": "White noise has zero autocorrelation at all non-zero lags — each value is independent of all others."
            },
            {
                "question": "What is the graphical plot of the sample ACF rₖ against lag k called?",
                "options": ["Periodogram", "Scatter plot", "Correlogram", "Spectral density plot"],
                "correct": 2,
                "explanation": "The correlogram is the plot of sample autocorrelation values against their lags — a fundamental diagnostic tool."
            },
            {
                "question": "What does the Partial Autocorrelation Function (PACF) of order k, denoted as αₖ, represent?",
                "options": ["The total correlation between Yₜ and Yₜ₋ₖ", "The partial correlation coefficient between Yₜ and Yₜ₋ₖ conditional on the intermediate values of the process", "The covariance divided by the standard deviation", "The linear trend over k periods"],
                "correct": 1,
                "explanation": "PACF measures the direct correlation between Yₜ and Yₜ₋ₖ after removing the linear effects of intermediate lags."
            },
            {
                "question": "If the AR(1) process Yₜ = c + φ₁Yₜ₋₁ + eₜ is stationary, what is its expected mean μ?",
                "options": ["c", "0", "c/(1 − φ₁)", "c(1 + φ₁)"],
                "correct": 2,
                "explanation": "For stationary AR(1): E[Yₜ] = μ = c/(1 − φ₁), derived by taking expectations of both sides."
            },
            {
                "question": "In an AR(1) process, given Yₜ₋₁, Yₜ becomes independent of Yₜ₋₂, Yₜ₋₃, etc. This property is known as:",
                "options": ["Heteroscedasticity", "The Markovian property", "Strong stationarity", "Cyclical variation"],
                "correct": 1,
                "explanation": "The Markov property: the future depends on the present only, not the past — AR(1) is a first-order Markov process."
            },
            {
                "question": "For a stationary AR(1) process where c=0, what is the variance function σ²ᵧ?",
                "options": ["σ²ₑ", "σ²ₑ/(1 − φ₁²)", "σ²ₑ(1 + φ₁²)", "tσ²ₑ"],
                "correct": 1,
                "explanation": "Var(Yₜ) = σ²ₑ/(1 − φ₁²) for stationary AR(1). The denominator amplifies noise variance when φ₁ is close to ±1."
            },
            {
                "question": "How is the ACF (ρₖ) of a stationary AR(1) process defined?",
                "options": ["ρₖ = φ₁ᵏ", "ρₖ = kφ₁", "ρₖ = 0 for all k > 1", "ρₖ = θ₁/(1 + θ₁²)"],
                "correct": 0,
                "explanation": "For AR(1): ρₖ = φ₁ᵏ — the ACF decays geometrically (exponentially) with lag."
            },
            {
                "question": "For a general MA(q) process represented as Yₜ = c + eₜ + θ₁eₜ₋₁ + ··· + θqeₜ₋q, what is the mean function E(Yₜ)?",
                "options": ["0", "c", "c/(1 − θ₁)", "σ²ₑ"],
                "correct": 1,
                "explanation": "E[Yₜ] = c since E[eₜ] = 0 for all error terms. The MA coefficients don't affect the mean."
            },
            {
                "question": "What is the variance function σ²ᵧ for an MA(1) process defined as Yₜ = c + eₜ + θ₁eₜ₋₁?",
                "options": ["σ²ₑ", "σ²ₑ(1 + θ₁²)", "σ²ₑ/(1 − θ₁²)", "tσ²ₑ"],
                "correct": 1,
                "explanation": "Var(Yₜ) = σ²ₑ(1 + θ₁²) — the variance includes contributions from both eₜ and θ₁eₜ₋₁."
            },
            {
                "question": "In an MA(1) process, what is the value of the autocovariance γₖ for all lags k > 1?",
                "options": ["θ₁σ²ₑ", "1", "0", "σ²ₑ"],
                "correct": 2,
                "explanation": "MA(1) has autocovariance cutoff: γₖ = 0 for k > 1. Only γ₀ and γ₁ are non-zero."
            },
            {
                "question": "For a general MA(q) process, what happens to the autocovariances and ACF for lags k > q?",
                "options": ["They increase exponentially", "They remain constant", "They vanish", "They oscillate between 1 and −1"],
                "correct": 2,
                "explanation": "The ACF of MA(q) cuts off after lag q — γₖ = 0 and ρₖ = 0 for all k > q. This is its signature property."
            },
            {
                "question": "In model identification, how do the ACF and PACF plots of an Autoregressive (AR) model typically behave?",
                "options": ["Gradual decline in PACF and a single peak in ACF", "Single peak in both ACF and PACF", "Gradual decline in ACF and a single peak at the order in PACF", "Both plots vanish at lag 2"],
                "correct": 2,
                "explanation": "AR(p): ACF decays gradually (exponentially), PACF cuts off sharply after lag p."
            },
            {
                "question": "How do the ACF and PACF plots of a Moving Average (MA) model typically behave?",
                "options": ["Gradual decline in PACF and a single peak at the order in ACF", "Gradual decline in ACF and a single peak at the order in PACF", "Gradual decline in both ACF and PACF", "No peaks in either plot"],
                "correct": 0,
                "explanation": "MA(q): ACF cuts off after lag q, PACF decays gradually — the mirror image of AR behavior."
            },
            {
                "question": "If both the ACF and PACF plots show a gradual decline, what might this indicate about the time series?",
                "options": ["The series is a white noise process", "The series might be non-stationary", "The series perfectly fits an ARMA(1,1) model", "The series is strictly stationary"],
                "correct": 1,
                "explanation": "Slowly decaying ACF and PACF suggest non-stationarity or an ARMA mixture — differencing may be needed."
            },
            {
                "question": "By recursion, the Random Walk process Yₜ = μ + Yₜ₋₁ + eₜ can be rewritten as:",
                "options": ["Yₜ = μ + Σeⱼ", "Yₜ = tμ + Σⱼ₌₁ᵗ eⱼ", "Yₜ = c + φ₁Yₜ₋₁ + eₜ", "Yₜ = θ₁eₜ₋₁"],
                "correct": 1,
                "explanation": "Unrolling the recursion: Yₜ = Y₀ + tμ + Σeⱼ. The mean grows linearly with t (drift term tμ)."
            },
            {
                "question": "Why is the Random Walk process fundamentally non-stationary?",
                "options": ["Because the variance is infinite", "Because its mean and variance depend on time (t)", "Because it lacks an irregular component", "Because the cyclical component is perfectly predictable"],
                "correct": 1,
                "explanation": "Random walk: E[Yₜ] = Y₀ + tμ (mean depends on t) and Var(Yₜ) = tσ²ₑ (variance grows with t) — both time-dependent."
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
        ],
        "additional_questions": [
            {
                "question": "What is the first step in the analysis of any time series?",
                "options": ["Differencing the data", "Taking the logarithm of the data", "Plotting the data", "Calculating the ACF and PACF"],
                "correct": 2,
                "explanation": "Always plot the data first to visually identify trends, seasonality, outliers, and other patterns before applying any transformations."
            },
            {
                "question": "In time series notation, what does the Backshift operator (B) do when applied to Yₜ?",
                "options": ["BYₜ = Yₜ₊₁", "BYₜ = Yₜ₋₁", "BYₜ = Yₜ − Yₜ₋₁", "BYₜ = Yₜ/Yₜ₋₁"],
                "correct": 1,
                "explanation": "The backshift operator B shifts the time index back by one: BYₜ = Yₜ₋₁."
            },
            {
                "question": "How is the first difference operator ∇Yₜ defined?",
                "options": ["Yₜ + Yₜ₋₁", "Yₜ − Yₜ₋₁", "Yₜ − 2Yₜ₋₁ + Yₜ₋₂", "Yₜ − Yₜ₋d"],
                "correct": 1,
                "explanation": "The first difference ∇Yₜ = Yₜ − Yₜ₋₁ removes linear trends from the series."
            },
            {
                "question": "What is the mathematical relationship between the difference operator (∇) and the backshift operator (B)?",
                "options": ["∇ = 1 + B", "∇ = B − 1", "∇ = 1 − B", "∇ = B²"],
                "correct": 2,
                "explanation": "∇ = 1 − B, since ∇Yₜ = Yₜ − Yₜ₋₁ = Yₜ − BYₜ = (1 − B)Yₜ."
            },
            {
                "question": "If a time series has a linear trend represented by Yₜ = bt + Sₜ (where Sₜ is stationary), how many times must it be differenced to become stationary?",
                "options": ["0 times", "1 time", "2 times", "d times"],
                "correct": 1,
                "explanation": "A linear trend (degree 1 polynomial) is removed by one round of differencing."
            },
            {
                "question": "If a time series exhibits a polynomial trend of order k, how can it be transformed into a stationary series?",
                "options": ["By logging the series k times", "By differencing the series k times", "By taking a lag d seasonal difference", "By applying the backshift operator once"],
                "correct": 1,
                "explanation": "A polynomial trend of degree k requires k differences to eliminate. Each differencing reduces the polynomial degree by 1."
            },
            {
                "question": "Which of the following equations represents a Random Walk Model?",
                "options": ["Yₜ = c + φ₁Yₜ₋₁ + eₜ", "Yₜ = bt² + Sₜ", "Yₜ = Yₜ₋₁ + eₜ", "Yₜ = eₜ + 0.5eₜ₋₁"],
                "correct": 2,
                "explanation": "The random walk Yₜ = Yₜ₋₁ + eₜ is a special case of AR(1) with φ₁ = 1 (unit root)."
            },
            {
                "question": "What does a lag d difference, denoted as ∇d Yₜ = (Yₜ − Yₜ₋d), accomplish?",
                "options": ["It removes a deterministic polynomial trend of order d", "It converts an ARMA process to an ARIMA process", "It removes seasonality of period d", "It tests for unit roots"],
                "correct": 2,
                "explanation": "The seasonal difference (Yₜ − Yₜ₋d) removes seasonal patterns with period d (e.g., d=12 for monthly data)."
            },
            {
                "question": "A non-stationary time series process Yₜ follows an ARIMA(p,d,q) model if:",
                "options": ["It is generated purely by white noise", "Yₜ produced by differencing d times is a stationary ARMA(p,q) process", "It has p seasonal differences and q regular differences", "It contains a unit root"],
                "correct": 1,
                "explanation": "ARIMA(p,d,q): after d differences, the resulting series follows a stationary ARMA(p,q) model."
            },
            {
                "question": "By definition, seasonality is a regular periodic variation with a cycle period of:",
                "options": ["Exactly 10 years", "At least 2 years", "Less than or equal to 1 year", "Non-fixed frequencies"],
                "correct": 2,
                "explanation": "Seasonality has a fixed period ≤ 1 year (daily, weekly, monthly, quarterly patterns)."
            },
            {
                "question": "Which of the following is NOT a graphical technique typically used to detect seasonality?",
                "options": ["Seasonal subseries plot", "Run sequence plot", "Q-Q plot", "Multiple box plots"],
                "correct": 2,
                "explanation": "Q-Q plots check distributional assumptions (normality), not seasonality. The others are designed for seasonal detection."
            },
            {
                "question": "In a Seasonal Plot, how is the time series data displayed?",
                "options": ["Plotted chronologically from beginning to end", "Plotted against the individual seasons in which the data was observed", "Plotted as a histogram of monthly averages", "Plotted to show moving averages exclusively"],
                "correct": 1,
                "explanation": "Seasonal plots overlay data by season (e.g., all Januaries together) to reveal seasonal patterns and changes."
            },
            {
                "question": "A simple time series or run sequence plot is particularly helpful in identifying which of the following?",
                "options": ["Exact roots of an AR equation", "Shifts in the location or variation of seasonal patterns", "The exact p and q values for an ARIMA model", "The overall mean of a non-stationary series"],
                "correct": 1,
                "explanation": "Run sequence plots reveal shifts, trends, and changes in variability or seasonal patterns over time."
            },
            {
                "question": "What is a primary limitation of the Seasonal Sub-series Plot?",
                "options": ["It cannot identify outliers", "Between-season analysis is difficult (e.g., comparing passenger numbers between two different months)", "It does not show the group means", "It cannot determine if seasonality is changing over time"],
                "correct": 1,
                "explanation": "Seasonal subseries plots show within-season patterns well but make between-season comparisons difficult."
            },
            {
                "question": "What distinguishes cyclicality from seasonality in a time series?",
                "options": ["Cyclical fluctuations occur at a fixed, unchanging frequency", "Seasonality extends beyond a single year", "Cyclical fluctuations are not of fixed frequency and usually extend beyond a single year", "Seasonality magnitudes are more variable than cyclical magnitudes"],
                "correct": 2,
                "explanation": "Cycles have irregular, longer periods (>1 year) unlike seasonality which has fixed, shorter periods (≤1 year)."
            },
            {
                "question": "How many distinct phases are typically described in a cyclical variation (business cycle)?",
                "options": ["2", "4", "6", "8"],
                "correct": 2,
                "explanation": "Business cycles typically have 6 phases: expansion, peak, recession, contraction, trough, and recovery."
            },
            {
                "question": "Which of the following is considered one of the phases of a cyclical variation?",
                "options": ["Stagnation", "Noise", "Trough", "Variance"],
                "correct": 2,
                "explanation": "The trough is the lowest point of a business cycle, marking the transition from contraction to recovery."
            },
            {
                "question": "The sun's magnetic field shifting entirely approximately every 11 years is an example of:",
                "options": ["Deterministic seasonality", "A random walk", "Cyclical variation", "White noise"],
                "correct": 2,
                "explanation": "The ~11-year solar cycle is a cyclical variation — it has an approximately regular but not perfectly fixed period beyond 1 year."
            },
            {
                "question": "What does the presence of a 'unit root' in the characteristic equation imply about a time series?",
                "options": ["The series is strictly stationary", "The series exhibits deterministic seasonality", "The process is non-stationary", "The series contains no trend"],
                "correct": 2,
                "explanation": "A unit root means the characteristic polynomial has a root of 1, indicating non-stationarity (shocks persist forever)."
            },
            {
                "question": "Why is a unit root considered a problem in time series forecasting?",
                "options": ["It makes the current value identical to the error term", "In the long run, the process will never converge to its mean", "It causes the variance to equal zero", "It forces the series to become perfectly cyclical"],
                "correct": 1,
                "explanation": "With a unit root, there's no mean-reversion — shocks have permanent effects and the process wanders without returning to equilibrium."
            },
            {
                "question": "In the Augmented Dickey Fuller (ADF) Test, what is the Null Hypothesis (H₀)?",
                "options": ["The series is stationary", "The series is non-stationary (a unit root is present)", "The series has a deterministic trend", "The series exhibits heteroskedasticity"],
                "correct": 1,
                "explanation": "ADF tests H₀: unit root exists (non-stationary). Rejecting H₀ supports stationarity."
            },
            {
                "question": "How does the Null Hypothesis (H₀) of the KPSS test differ from the ADF test?",
                "options": ["KPSS H₀ states the series is non-stationary", "KPSS H₀ states the series is stationary around a deterministic trend or mean", "KPSS H₀ assumes the data is a random walk", "They share the exact same Null Hypothesis"],
                "correct": 1,
                "explanation": "KPSS reverses the ADF logic: H₀ = stationary. Rejecting KPSS H₀ suggests non-stationarity. Using both tests together gives stronger conclusions."
            },
            {
                "question": "What is the primary advantage of the Phillips-Perron (PP) Test compared to the ADF test?",
                "options": ["It tests for deterministic seasonality instead of unit roots", "It relies entirely on variance ratios", "It is more robust in the presence of autocorrelation and heteroskedasticity", "Its null hypothesis assumes strict stationarity"],
                "correct": 2,
                "explanation": "PP test uses non-parametric corrections for serial correlation and heteroskedasticity, making it more robust than ADF."
            },
            {
                "question": "The Variance Ratio Test checks for non-stationarity by testing which specific hypothesis?",
                "options": ["The random walk hypothesis", "The deterministic trend hypothesis", "The constant mean hypothesis", "The cyclical variation hypothesis"],
                "correct": 0,
                "explanation": "The Variance Ratio test checks if a series follows a random walk by testing whether variance scales linearly with the observation interval."
            },
            {
                "question": "If seasonality is constant in the same month over different years (e.g., climate series due to Earth's rotation), what type of seasonality is this?",
                "options": ["Stochastic seasonality", "Evolving stationary seasonality", "Non-stationary evolving seasonality", "Deterministic seasonality"],
                "correct": 3,
                "explanation": "Deterministic seasonality is fixed and predictable — the seasonal pattern is exactly the same every cycle."
            },
            {
                "question": "In the SARIMA (p,d,q) × (P,D,Q)S notation, what does the parameter D represent?",
                "options": ["The number of regular differences", "The order of the seasonal AR operator", "The number of seasonal differences", "The period of seasonality"],
                "correct": 2,
                "explanation": "D = number of seasonal differences applied to remove seasonal non-stationarity."
            },
            {
                "question": "In the SARIMA model structure, what does ΦP(Bˢ) represent?",
                "options": ["The regular moving average operator", "The seasonal autoregressive (AR) operator of order P", "The white noise component", "The seasonal difference factor"],
                "correct": 1,
                "explanation": "ΦP(Bˢ) is the seasonal AR polynomial of order P, operating at seasonal lags (s, 2s, ..., Ps)."
            },
            {
                "question": "Which of the following is considered a 'Pro' of using ARIMA and SARIMA models?",
                "options": ["They work perfectly with extremely short datasets", "They have no computational time complexity", "They offer simplicity and interpretability", "They automatically clean outliers"],
                "correct": 2,
                "explanation": "ARIMA/SARIMA models are relatively simple, well-understood, and their parameters have clear statistical interpretations."
            },
            {
                "question": "What is a major 'Con' regarding the time complexity of ARIMA and SARIMA models?",
                "options": ["Time complexity is non-existent", "It has logarithmic time complexity", "It has exponential time complexity; as p and q increase, there are more coefficients to fit", "They cannot handle more than 2 variables"],
                "correct": 2,
                "explanation": "As p and q grow, the number of parameters increases, making estimation computationally expensive — exponential time complexity."
            },
            {
                "question": "Whether seasonality is deterministic, evolves as a stationary process, or evolves as a non-stationary process, what mathematical step corrects it in all three cases?",
                "options": ["Applying a logarithmic transformation", "Applying a lag 1 regular difference", "Applying the seasonal difference", "Fitting a quadratic trend"],
                "correct": 2,
                "explanation": "The seasonal difference (1 − Bˢ) removes all types of seasonality — deterministic, stationary evolving, or non-stationary evolving."
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
        ],
        "additional_questions": [
            {
                "question": "In the context of time series, what is the definition of 'Forecasting'?",
                "options": ["Estimating the unknown parameters in a model", "The value of the random process when we use the estimated values of the parameters", "The value of any future random process which is not observed by the sample", "Calculating the past error margins"],
                "correct": 2,
                "explanation": "Forecasting predicts future unobserved values of the random process beyond the available sample."
            },
            {
                "question": "What criteria is primarily used to obtain an l-step ahead forecast?",
                "options": ["Maximum Likelihood", "Minimum Mean Squared Error (MSE)", "Mean Absolute Percentage Error", "Ordinary Least Squares"],
                "correct": 1,
                "explanation": "The optimal forecast minimizes MSE — the expected squared difference between the forecast and the actual value."
            },
            {
                "question": "The forecast value Yₙ(l) from an ARMA model is defined as the:",
                "options": ["Unconditional variance of Yₙ₊ₗ", "Conditional expectation of Yₙ₊ₗ given the observed sample", "Moving average of the last l terms", "Sum of all past white noise terms"],
                "correct": 1,
                "explanation": "The optimal MMSE forecast is the conditional expectation E[Yₙ₊ₗ | Y₁, ..., Yₙ]."
            },
            {
                "question": "What is the expected value of the forecast error E(eₙ(l))?",
                "options": ["1", "σ²ₐ", "0 (Hence, it is unbiased)", "Infinity"],
                "correct": 2,
                "explanation": "The MMSE forecast is unbiased — the expected forecast error is zero."
            },
            {
                "question": "For a 1-step ahead forecast using the random shock form, what is the variance of the forecast error, V(eₙ(1))?",
                "options": ["0", "σ²ₐ(1 + ψ₁²)", "σ²ₐ", "∞"],
                "correct": 2,
                "explanation": "For 1-step ahead, the forecast error is just the next innovation aₙ₊₁, so V(eₙ(1)) = σ²ₐ."
            },
            {
                "question": "Why is ARMA or ARIMA forecasting generally only useful for short-term forecasts?",
                "options": ["Because the forecast limit approaches the mean μ and the variance becomes finite and constant as n → ∞", "Because long-term forecasts require exponential smoothing", "Because it cannot handle stationary data", "Because the forecast error expectation increases exponentially"],
                "correct": 0,
                "explanation": "As the horizon grows, ARMA forecasts revert to the unconditional mean with constant variance — losing predictive value."
            },
            {
                "question": "What is the formula for a 95% prediction interval for a 1-step ahead forecast?",
                "options": ["Ŷₙ(l) ± 1.96σₐ", "Ŷₙ(l) ± σ²ₐ", "Ŷₙ(l) ± 1.96√l", "Ŷₙ(l) ± 0.95σₐ"],
                "correct": 0,
                "explanation": "95% PI = forecast ± 1.96 × standard error. For 1-step ahead, SE = σₐ."
            },
            {
                "question": "Which of the following is an advantage of having a long realization of a time series?",
                "options": ["It makes parsimonious models irrelevant", "It accurately estimates correlation structure (ACF and PACF) and standard errors", "It allows the use of naive forecasting exclusively", "It converts non-stationary data into white noise automatically"],
                "correct": 1,
                "explanation": "Longer series provide more data points for reliable estimation of ACF, PACF, and model parameters."
            },
            {
                "question": "What is a key advantage of using parsimonious models?",
                "options": ["They use all available variables for maximum accuracy", "Forecasts are less sensitive to deviations between parameters and estimates", "They require massive datasets to function", "They increase numerical problems during estimation"],
                "correct": 1,
                "explanation": "Parsimonious models (fewer parameters) are more robust — small estimation errors have less impact on forecasts."
            },
            {
                "question": "Which forecast accuracy measure calculates the 'average of absolute percentage amount by which the forecast differs from outcomes'?",
                "options": ["MSE", "MPE", "MAE", "MAPE"],
                "correct": 3,
                "explanation": "MAPE = Mean Absolute Percentage Error — averages |actual − forecast|/|actual| × 100%."
            },
            {
                "question": "Which metric calculates the average percentage points by which a forecast differs from outcomes?",
                "options": ["ME", "MPE", "MAE", "RMSE"],
                "correct": 0,
                "explanation": "ME (Mean Error) is the average of forecast errors — it shows bias (systematic over/under-prediction)."
            },
            {
                "question": "What defines a 'Naïve Forecast'?",
                "options": ["Predicting future values using a complex ARMA model", "Using an exponentially weighted average of past observations", "Guessing the next value by using the last period's actuals without adjustments", "Minimizing the MSE across 10 years of data"],
                "correct": 2,
                "explanation": "Naïve forecast: Ŷₜ₊₁ = Yₜ — simply use the most recent observation as the forecast."
            },
            {
                "question": "In Theil's U Statistics, what does U₂ < 1 indicate?",
                "options": ["The forecasting technique is worse than a naïve forecast", "The forecasting technique is better than a naïve forecast", "There is no difference between the technique and a naïve forecast", "The model is perfectly accurate with zero error"],
                "correct": 1,
                "explanation": "U₂ < 1 means the model's RMSE is smaller than the naïve forecast's RMSE — the model adds value."
            },
            {
                "question": "What does it mean if Theil's U₁ statistic is closer to 0?",
                "options": ["The model has severe heteroscedasticity", "The naïve forecast is superior", "It indicates better forecasting accuracy", "The moving average window is too small"],
                "correct": 2,
                "explanation": "U₁ ranges from 0 (perfect forecast) to 1 (worst). Closer to 0 = better accuracy."
            },
            {
                "question": "What is the primary purpose of applying smoothing techniques to time series data?",
                "options": ["To increase the noise in the data", "To reduce random variations (noise) and reveal the underlying trend for better forecasting", "To permanently delete outliers", "To convert additive seasonality to multiplicative seasonality"],
                "correct": 1,
                "explanation": "Smoothing filters out noise to expose the underlying signal (trend, level) for clearer analysis and forecasting."
            },
            {
                "question": "How is the smoothed series derived in Simple Moving Average (SMA) smoothing?",
                "options": ["By squaring the last k elements", "By calculating the average of the last k elements of the series", "By taking the logarithmic difference of the data", "By applying an exponential decay factor to all historical data"],
                "correct": 1,
                "explanation": "SMA computes the arithmetic mean of the most recent k observations — equal weights for all k values."
            },
            {
                "question": "How does Exponential Smoothing (EMA) differ from SMA regarding weights?",
                "options": ["EMA uses equal weights, while SMA uses decreasing weights", "EMA uses exponentially decreasing weights over time, whereas SMA uses equal weights", "EMA only weights the first observation", "EMA does not use weights at all"],
                "correct": 1,
                "explanation": "EMA assigns exponentially decreasing weights to older observations, giving recent data more influence than SMA."
            },
            {
                "question": "In Exponential Smoothing (EMA), what is the effect of using a larger α (smoothing factor)?",
                "options": ["It gives equal weight to all historical observations", "It creates a perfectly smooth, straight line", "It reduces the effect of smoothing and gives more weight to recent changes in the data", "It converts the model into a random walk"],
                "correct": 2,
                "explanation": "Large α = more weight on recent data, less smoothing, faster response to changes (but more noise sensitivity)."
            },
            {
                "question": "Which α value would result in a much smoother curve in EMA?",
                "options": ["α = 0.99", "α = 0.85", "α = 0.50", "α = 0.01"],
                "correct": 3,
                "explanation": "Small α (near 0) = heavy smoothing, slow response. The past has a strong influence, producing a very smooth curve."
            },
            {
                "question": "What is a key characteristic of the EMA forecast?",
                "options": ["It only considers the single most recent observation", "It has an exponential decay of influence of past data, where more recent values have greater influence", "It requires estimating seasonal correction factors", "It completely ignores all data older than k periods"],
                "correct": 1,
                "explanation": "EMA's defining feature: all past data contributes, but with exponentially decaying weights — recent = most important."
            },
            {
                "question": "How should one optimally select the value of the smoothing factor α?",
                "options": ["Always choose 0.5 for simplicity", "Assign values from 0.1 to 0.99 and select the one with the smallest MSE or RMSE", "Select the value that produces the highest MAE", "Use the Theil's U₂ formula exclusively"],
                "correct": 1,
                "explanation": "Grid search over α values and pick the one minimizing forecast error (MSE/RMSE) on a validation set."
            },
            {
                "question": "When is Double Exponential Smoothing (Holt's Method) primarily used?",
                "options": ["When the data has no trend and no seasonality", "When the data has a linear trend and a seasonal pattern", "When the data has a linear trend and no seasonal pattern", "When the data has a seasonal pattern but no trend"],
                "correct": 2,
                "explanation": "Holt's method handles level + linear trend (two components), but not seasonality — use Holt-Winters for that."
            },
            {
                "question": "In Holt's Method, what does the parameter β represent?",
                "options": ["The data smoothing parameter", "The seasonal change smoothing factor", "The trend smoothing factor", "The overall mean"],
                "correct": 2,
                "explanation": "β controls how quickly the trend estimate adapts to changes — the trend smoothing parameter."
            },
            {
                "question": "When should Triple Exponential Smoothing (Holt Winter's Method) be applied?",
                "options": ["When forecasting data with a linear trend and a seasonal pattern", "Only when the data is strictly stationary", "When the data has no trend and no seasonality", "When dealing purely with cross-sectional data"],
                "correct": 0,
                "explanation": "Holt-Winters handles all three components: level (α), trend (β), and seasonality (γ)."
            },
            {
                "question": "What does the parameter γ (gamma) control in Holt Winter's Method?",
                "options": ["The overall mean smoothing", "The trend smoothing factor", "The seasonal change smoothing factor", "The white noise variance"],
                "correct": 2,
                "explanation": "γ controls how fast the seasonal component adapts — the seasonal smoothing parameter."
            },
            {
                "question": "Which of the following defines 'Additive Seasonality'?",
                "options": ["The seasonal effect is multiplied to the trend", "The seasonal effect is roughly constant over time and added to the trend", "The seasonality changes exponentially based on the trend", "There is no seasonal fluctuation"],
                "correct": 1,
                "explanation": "Additive: Yₜ = Trend + Season + Error. The seasonal effect has constant amplitude regardless of the level."
            },
            {
                "question": "In a model with 'Multiplicative Seasonality', what happens when the time series is at a higher level?",
                "options": ["Seasonal fluctuations completely disappear", "Seasonal fluctuations become roughly constant", "It results in larger seasonal fluctuations", "The trend becomes perfectly linear"],
                "correct": 2,
                "explanation": "Multiplicative: seasonal effect scales with level. Higher level → proportionally larger seasonal swings."
            },
            {
                "question": "What is the mathematical representation for Multiplicative Seasonality?",
                "options": ["Yₜ = Tₜ + Sₜ + eₜ", "Yₜ = Tₜ × Sₜ × eₜ", "Yₜ = Tₜ − Sₜ", "Yₜ = Tₜ / Sₜ"],
                "correct": 1,
                "explanation": "Multiplicative decomposition: Yₜ = Trend × Seasonal × Error — components multiply rather than add."
            },
            {
                "question": "In the Holt-Winters formulas, what does the notation L denote?",
                "options": ["The forecast horizon length", "The total number of observations in the series", "The number of cycles", "The length of the cycle of seasonal change"],
                "correct": 3,
                "explanation": "L = the seasonal period length (e.g., L=12 for monthly data with yearly seasonality, L=4 for quarterly)."
            },
            {
                "question": "If you run the R function HoltWinters(x = AirPassengers, gamma = FALSE), what model are you fitting?",
                "options": ["Simple Moving Average", "Holt-Winters with additive seasonality", "Holt-Winters with multiplicative seasonality", "Holt-Winters exponential smoothing with trend and without the seasonal component (Holt's Method)"],
                "correct": 3,
                "explanation": "gamma = FALSE disables the seasonal component, leaving only level + trend smoothing — this is Holt's (double exponential) method."
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
        ],
        "additional_questions": [
            {
                "question": "What does 'persistence' in a time series refer to?",
                "options": ["The tendency of recent values to revert to the mean quickly", "The tendency of past values to have a long-lasting influence on future values", "The complete independence of future observations from past shocks", "A pattern of strictly exponential decay in data"],
                "correct": 1,
                "explanation": "Persistence means past shocks continue to influence future values for a long time — the hallmark of long-memory processes."
            },
            {
                "question": "How does the Autocorrelation Function (ACF) decay in long-memory processes compared to short-memory processes?",
                "options": ["Long-memory processes decay exponentially; short-memory processes decay hyperbolically", "Both processes exhibit immediate truncation at lag 1", "Long-memory processes exhibit slow, hyperbolic decay; short-memory processes decay exponentially", "Neither process exhibits autocorrelation decay"],
                "correct": 2,
                "explanation": "Long memory: ACF decays hyperbolically (slowly, like k^(2d-1)). Short memory (ARMA): ACF decays exponentially (fast)."
            },
            {
                "question": "In financial markets, what term describes the phenomenon where large price movements are followed by more large movements?",
                "options": ["Mean reversion", "Volatility clustering", "Anti-persistence", "Short-memory dependence"],
                "correct": 1,
                "explanation": "Volatility clustering: periods of high volatility tend to cluster together, a key feature in financial time series."
            },
            {
                "question": "Which of the following is a characteristic of an anti-persistent (mean-reverting) time series?",
                "options": ["High values are followed by even higher values", "The process has infinite variance", "It exhibits a negative autocorrelation structure, meaning high values tend to be followed by low values", "It can only be modeled using strict random walks"],
                "correct": 2,
                "explanation": "Anti-persistence: high values followed by low values (and vice versa) — negative autocorrelation, mean-reverting behavior."
            },
            {
                "question": "Why do ARMA models fail to capture long-range dependence?",
                "options": ["Their fractional differencing parameter is always greater than 1", "They cannot process stationary data", "Their Autocorrelation Function (ACF) decays exponentially", "They inherently possess an infinite variance"],
                "correct": 2,
                "explanation": "ARMA ACF decays exponentially — too fast to capture the slow, hyperbolic decay characteristic of long memory."
            },
            {
                "question": "For an ARFIMA(0, d, 0) process, what parameter range indicates that the process is stationary and has a long memory?",
                "options": ["d = 0", "0 < d < 0.5", "d ≥ 0.5", "−0.5 < d < 0"],
                "correct": 1,
                "explanation": "0 < d < 0.5: stationary with long memory. The ACF decays hyperbolically rather than exponentially."
            },
            {
                "question": "If the fractional differencing parameter d ≥ 0.5 in an ARFIMA model, what does this imply about the time series?",
                "options": ["The model reduces to a standard ARMA process", "The model is strictly anti-persistent", "The model is non-stationary with strong persistence", "The model perfectly fits a white noise structure"],
                "correct": 2,
                "explanation": "d ≥ 0.5 means the process is non-stationary — it needs differencing before analysis."
            },
            {
                "question": "Which mathematical approximation is used to express the Auto-covariance and ACF of an ARFIMA process for large values of lag k?",
                "options": ["Box-Pierce formula", "Stirling's formula", "Theil's U Statistics", "Yule-Walker equations"],
                "correct": 1,
                "explanation": "Stirling's approximation for the Gamma function is used to derive the asymptotic ACF behavior of ARFIMA processes."
            },
            {
                "question": "For a fractionally integrated process, what does a parameter range of −0.5 < d < 0 indicate?",
                "options": ["The process is an intermediate memory process that is anti-persistent", "The process has infinite variance", "The process is a non-stationary random walk", "The process reduces to an ARIMA model"],
                "correct": 0,
                "explanation": "−0.5 < d < 0: anti-persistent (intermediate memory). High values tend to be followed by low values and vice versa."
            },
            {
                "question": "What does the parameter d = 0 represent in an ARFIMA(p, d, q) process?",
                "options": ["A non-stationary process", "A short-memory ARMA process", "A completely persistent process", "A continuous volatility cluster"],
                "correct": 1,
                "explanation": "d = 0 eliminates fractional integration — the model reduces to a standard ARMA(p,q) with short memory."
            },
            {
                "question": "For what original purpose was the Hurst Exponent developed?",
                "options": ["To price options during financial crises", "To calculate moving averages for stock prices", "In hydrology for determining the optimum dam size for the Nile river's rain and drought conditions", "To test for deterministic seasonality in temperatures"],
                "correct": 2,
                "explanation": "Harold Hurst developed H for Nile river hydrology — to understand the persistence of wet/dry cycles for dam sizing."
            },
            {
                "question": "In constructing the Hurst Exponent, what is the expected value of the rescaled adjusted range E(Rₙ/Sₙ) proportional to as n → ∞?",
                "options": ["Cnᴴ", "H log(n)", "C / n²", "α − H"],
                "correct": 0,
                "explanation": "E(R/S) ~ Cnᴴ as n → ∞. Taking logs gives a linear relationship whose slope estimates H."
            },
            {
                "question": "How is the estimate of the Hurst Exponent (H) practically calculated?",
                "options": ["By finding the standard deviation of the error terms", "As the slope of the regression between the log of the rescaled adjusted range and log(n)", "By taking the square root of the fractional difference parameter", "By maximizing the conditional likelihood function"],
                "correct": 1,
                "explanation": "Plot log(R/S) vs log(n) — the slope of the fitted line estimates H."
            },
            {
                "question": "If a time series consists of independent and identically distributed (i.i.d.) variables (white noise), what is the expected value of its Hurst Exponent (H)?",
                "options": ["0", "0.5", "1", "> 1"],
                "correct": 1,
                "explanation": "H = 0.5 for i.i.d. data (random walk/white noise) — no persistence and no anti-persistence."
            },
            {
                "question": "A Hurst Exponent falling in the range 0.5 < H < 1 signifies that the time series possesses:",
                "options": ["An anti-persistence structure", "A short-memory ARMA structure", "A long memory structure", "Infinite variance"],
                "correct": 2,
                "explanation": "H > 0.5: long memory / persistence. Past trends tend to continue — positive autocorrelation at long lags."
            },
            {
                "question": "If an analyst observes a Hurst Exponent of H = 0.3 for a stock price, what does this indicate?",
                "options": ["The stock price follows a strict random walk", "The stock shows persistent trending behavior (momentum)", "The stock price shows mean-reverting (anti-persistent) behavior", "The stock price will increase exponentially"],
                "correct": 2,
                "explanation": "H < 0.5: anti-persistent / mean-reverting. Increases tend to be followed by decreases and vice versa."
            },
            {
                "question": "What does a Hurst Exponent of H ≥ 1 signify about a time series process?",
                "options": ["It is perfectly mean-reverting", "The process has infinite variance and is non-stationary", "It is a perfect white noise process", "It exhibits short-term dependence only"],
                "correct": 1,
                "explanation": "H ≥ 1: the process is non-stationary with infinite variance — extremely strong persistence."
            },
            {
                "question": "What aspect of a time series does Spectral Density help us understand?",
                "options": ["The exact number of missing values in the dataset", "How the variation in the data is distributed across various frequencies", "The exact date a structural break occurred", "The moving average over the entire lifespan of the series"],
                "correct": 1,
                "explanation": "Spectral density decomposes total variance by frequency — showing which periodic components dominate the series."
            },
            {
                "question": "What is the practical estimator of the spectral density called?",
                "options": ["The periodogram", "The correlogram", "The Yule-Walker matrix", "The Hurst sum"],
                "correct": 0,
                "explanation": "The periodogram estimates spectral density from data — it shows power at each frequency."
            },
            {
                "question": "In the spectral density formula, what does the term e^(−i2πft) represent?",
                "options": ["The total number of observations", "The fractional difference parameter", "The oscillatory behavior associated with the frequency f (accounting for sine and cosine functions)", "The white noise component"],
                "correct": 2,
                "explanation": "e^(−i2πft) = cos(2πft) − i·sin(2πft) by Euler's formula — it captures oscillatory behavior at frequency f."
            },
            {
                "question": "Which ARFIMA parameter estimation technique utilizes the log periodogram of the time series?",
                "options": ["Local Whittle Estimation", "Geweke and Porter-Hudak (GPH) Estimation", "Method of Moments", "Maximum Likelihood Estimation"],
                "correct": 1,
                "explanation": "GPH regression uses log periodogram values at Fourier frequencies to estimate d via a simple linear regression."
            },
            {
                "question": "In the GPH estimation regression equation log(I(λₖ)) = a + b·log(λₖ) + εₖ, how is the slope b related to the fractional differencing parameter d?",
                "options": ["b = d²", "b = 1 − d", "b = −2d", "b = d / 2"],
                "correct": 2,
                "explanation": "The GPH regression slope b = −2d. So d = −b/2."
            },
            {
                "question": "What is a key limitation of the GPH Estimation method?",
                "options": ["It can only be applied to perfectly stationary AR(1) models", "It relies entirely on the Yule-Walker equations", "Sensitivity to bandwidth selection in periodogram estimation may lead to biased estimates", "It cannot handle data with any degree of noise"],
                "correct": 2,
                "explanation": "GPH is sensitive to the choice of bandwidth (number of frequencies used) — different bandwidths can yield different d estimates."
            },
            {
                "question": "Which estimation technique is designed specifically for estimating the fractional differencing parameter by focusing on a local frequency range?",
                "options": ["Local Whittle estimation", "GPH estimation", "Box-Pierce estimation", "Unconditional Least Squares"],
                "correct": 0,
                "explanation": "Local Whittle focuses on frequencies near zero (where long-memory effects are strongest) — more efficient than GPH for small samples."
            },
            {
                "question": "How is Whittle Estimation fundamentally different from GPH estimation?",
                "options": ["Whittle estimation only works on financial data", "Whittle estimation is an alternative that uses a quasi-likelihood approach based on the likelihood of the periodogram", "Whittle estimation completely ignores spectral density", "Whittle estimation is identical to Maximum Likelihood Estimation"],
                "correct": 1,
                "explanation": "Whittle uses a quasi-likelihood based on the periodogram, while GPH uses a simple log-log regression."
            },
            {
                "question": "In environmental time series, what physical phenomena often cause persistence in global temperatures?",
                "options": ["The immediate dissipation of all cloud cover", "The continuous accumulation of greenhouse gases like carbon dioxide leading to a prolonged warming effect", "Complete mean reversion every 5 years", "The random walk nature of solar radiation"],
                "correct": 1,
                "explanation": "Greenhouse gas accumulation creates long-memory persistence in temperature — current emissions have long-lasting effects."
            },
            {
                "question": "In a long-range persistent process, how does the Autocorrelation Function mathematically behave as a function of lag k?",
                "options": ["ρₖ ~ Ck^α, where α > 0, showing hyperbolic decay", "ρₖ = 0 for all k > 1", "ρₖ ~ Cr^k, showing exponential decay", "ρₖ oscillates perfectly between 1 and −1"],
                "correct": 0,
                "explanation": "Long memory: ρₖ ~ Ck^(2d−1) — hyperbolic (power-law) decay, much slower than exponential."
            },
            {
                "question": "Why does long-memory behavior in long-term interest rates (like 10-year bonds) matter to analysts?",
                "options": ["Because bonds are insensitive to interest rates", "It guarantees that interest rates will eventually drop to zero", "It implies current levels will remain influential for future rates, complicating forecasting and bond pricing", "It means short-term memory models like standard ARMA are perfectly sufficient"],
                "correct": 2,
                "explanation": "Long memory means today's rates persistently influence future rates — standard ARMA models underestimate this dependence."
            },
            {
                "question": "If an analyst knows there is a strong yearly pattern in a sales dataset by observing its spectral density, what is the primary benefit?",
                "options": ["They can ignore the data completely", "They can use that known cycle to make better, more accurate predictions for the upcoming year", "They can prove the data is a random walk", "They can permanently remove the fractional difference parameter"],
                "correct": 1,
                "explanation": "Identifying dominant frequencies (like yearly cycles) in spectral density enables better seasonal forecasting."
            },
            {
                "question": "The Hurst Exponent indicates a stock price follows a random walk when it is approximately:",
                "options": ["H = 0", "H = 1", "H ≈ 0.5", "H = 0.99"],
                "correct": 2,
                "explanation": "H ≈ 0.5: no persistence, no anti-persistence — consistent with a random walk (i.i.d. increments)."
            }
        ],
        "additional_questions": [
            {
                "question": "What does 'persistence' in a time series refer to?",
                "options": ["The tendency of recent values to revert to the mean quickly", "The tendency of past values to have a long-lasting influence on future values", "The complete independence of future observations from past shocks", "A pattern of strictly exponential decay in data"],
                "correct": 1,
                "explanation": "Persistence means past values continue to influence future values for a long time — shocks have lasting effects."
            },
            {
                "question": "How does the Autocorrelation Function (ACF) decay in long-memory processes (like ARFIMA) compared to short-memory processes (like ARMA)?",
                "options": ["Long-memory processes decay exponentially; short-memory processes decay hyperbolically", "Both processes exhibit immediate truncation at lag 1", "Long-memory processes exhibit slow, hyperbolic decay; short-memory processes decay exponentially", "Neither process exhibits autocorrelation decay"],
                "correct": 2,
                "explanation": "Long-memory: slow hyperbolic (power-law) ACF decay. Short-memory (ARMA): fast exponential ACF decay."
            },
            {
                "question": "In financial markets, what term describes the phenomenon where large price movements are followed by more large movements?",
                "options": ["Mean reversion", "Volatility clustering", "Anti-persistence", "Short-memory dependence"],
                "correct": 1,
                "explanation": "Volatility clustering: periods of high volatility tend to cluster together, followed by calm periods — a form of persistence."
            },
            {
                "question": "Which of the following is a characteristic of an anti-persistent (mean-reverting) time series?",
                "options": ["High values are followed by even higher values", "The process has infinite variance", "It exhibits a negative autocorrelation structure, meaning high values tend to be followed by low values", "It can only be modeled using strict random walks"],
                "correct": 2,
                "explanation": "Anti-persistence means the series tends to reverse direction — high values are followed by low values and vice versa."
            },
            {
                "question": "Why do ARMA models fail to capture long-range dependence?",
                "options": ["Their fractional differencing parameter is always greater than 1", "They cannot process stationary data", "Their Autocorrelation Function (ACF) decays exponentially", "They inherently possess an infinite variance"],
                "correct": 2,
                "explanation": "ARMA models have exponentially decaying ACF, which cannot capture the slow hyperbolic decay of long-memory processes."
            },
            {
                "question": "For an ARFIMA(0, d, 0) process, what parameter range indicates that the process is stationary and has a long memory?",
                "options": ["d = 0", "0 < d < 0.5", "d ≥ 0.5", "−0.5 < d < 0"],
                "correct": 1,
                "explanation": "When 0 < d < 0.5, the ARFIMA process is stationary with long memory — the ACF decays hyperbolically."
            },
            {
                "question": "If the fractional differencing parameter d ≥ 0.5 in an ARFIMA model, what does this imply about the time series?",
                "options": ["The model reduces to a standard ARMA process", "The model is strictly anti-persistent", "The model is non-stationary with strong persistence", "The model perfectly fits a white noise structure"],
                "correct": 2,
                "explanation": "When d ≥ 0.5, the process is non-stationary — it has too much persistence for finite variance."
            },
            {
                "question": "Which mathematical approximation is used to express the Auto-covariance and ACF of an ARFIMA process for large values of lag k?",
                "options": ["Box-Pierce formula", "Stirling's formula", "Theil's U Statistics", "Yule-Walker equations"],
                "correct": 1,
                "explanation": "Stirling's approximation for the Gamma function is used to derive the asymptotic behavior of ARFIMA autocovariances."
            },
            {
                "question": "For a fractionally integrated process, what does a parameter range of −0.5 < d < 0 indicate?",
                "options": ["The process is an intermediate memory process that is anti-persistent", "The process has infinite variance", "The process is a non-stationary random walk", "The process reduces to an ARIMA model"],
                "correct": 0,
                "explanation": "When −0.5 < d < 0, the process is stationary and anti-persistent — it reverts toward the mean faster than a random walk."
            },
            {
                "question": "What does the parameter d = 0 represent in an ARFIMA(p, d, q) process?",
                "options": ["A non-stationary process", "A short-memory ARMA process", "A completely persistent process", "A continuous volatility cluster"],
                "correct": 1,
                "explanation": "When d = 0, the fractional integration vanishes, and ARFIMA reduces to a standard short-memory ARMA(p, q) process."
            },
            {
                "question": "For what original purpose was the Hurst Exponent developed?",
                "options": ["To price options during financial crises", "To calculate moving averages for stock prices", "In hydrology for determining the optimum dam size for the Nile river's rain and drought conditions", "To test for deterministic seasonality in temperatures"],
                "correct": 2,
                "explanation": "Harold Edwin Hurst developed it to study the Nile River's long-term flood and drought patterns for dam sizing."
            },
            {
                "question": "In constructing the Hurst Exponent, what is the expected value of the rescaled adjusted range E(Rₙ/Sₙ) proportional to as n → ∞?",
                "options": ["Cnᴴ", "H log(n)", "C / n²", "α − H"],
                "correct": 0,
                "explanation": "E(Rₙ/Sₙ) ~ Cnᴴ as n → ∞, where H is the Hurst exponent and C is a constant."
            },
            {
                "question": "How is the estimate of the Hurst Exponent (H) practically calculated?",
                "options": ["By finding the standard deviation of the error terms", "As the slope of the regression between the log of the rescaled adjusted range and log(n)", "By taking the square root of the fractional difference parameter", "By maximizing the conditional likelihood function"],
                "correct": 1,
                "explanation": "H is estimated as the slope in the log-log regression: log(R/S) vs log(n) — the classic R/S analysis."
            },
            {
                "question": "If a time series consists of independent and identically distributed (i.i.d.) variables (white noise), what is the expected value of its Hurst Exponent (H)?",
                "options": ["0", "0.5", "1", "> 1"],
                "correct": 1,
                "explanation": "For i.i.d. (white noise) data, H = 0.5 — no persistence and no anti-persistence."
            },
            {
                "question": "A Hurst Exponent falling in the range 0.5 < H < 1 signifies that the time series possesses:",
                "options": ["An anti-persistence structure", "A short-memory ARMA structure", "A long memory structure", "Infinite variance"],
                "correct": 2,
                "explanation": "H > 0.5 indicates long memory (persistence) — past trends tend to continue into the future."
            },
            {
                "question": "If an analyst observes a Hurst Exponent of H = 0.3 for a stock price, what does this indicate?",
                "options": ["The stock price follows a strict random walk", "The stock shows persistent trending behavior (momentum)", "The stock price shows mean-reverting (anti-persistent) behavior", "The stock price will increase exponentially"],
                "correct": 2,
                "explanation": "H < 0.5 indicates anti-persistence — the stock tends to reverse direction, showing mean-reverting behavior."
            },
            {
                "question": "What does a Hurst Exponent of H ≥ 1 signify about a time series process?",
                "options": ["It is perfectly mean-reverting", "The process has infinite variance and is non-stationary", "It is a perfect white noise process", "It exhibits short-term dependence only"],
                "correct": 1,
                "explanation": "H ≥ 1 means the process is non-stationary with infinite variance — extreme persistence."
            },
            {
                "question": "What aspect of a time series does Spectral Density help us understand?",
                "options": ["The exact number of missing values in the dataset", "How the variation in the data is distributed across various frequencies", "The exact date a structural break occurred", "The moving average over the entire lifespan of the series"],
                "correct": 1,
                "explanation": "Spectral density decomposes the total variance of a time series into contributions from different frequency components."
            },
            {
                "question": "What is the practical estimator of the spectral density called?",
                "options": ["The periodogram", "The correlogram", "The Yule-Walker matrix", "The Hurst sum"],
                "correct": 0,
                "explanation": "The periodogram is the sample-based estimator of the spectral density — it estimates power at each frequency."
            },
            {
                "question": "In the spectral density formula, what does the term e^(−i2πft) represent?",
                "options": ["The total number of observations", "The fractional difference parameter", "The oscillatory behavior associated with the frequency f (accounting for sine and cosine functions)", "The white noise component"],
                "correct": 2,
                "explanation": "e^(−i2πft) = cos(2πft) − i·sin(2πft) represents the oscillatory component at frequency f via Euler's formula."
            },
            {
                "question": "Which ARFIMA parameter estimation technique utilizes the log periodogram of the time series?",
                "options": ["Local Whittle Estimation", "Geweke and Porter-Hudak (GPH) Estimation", "Method of Moments", "Maximum Likelihood Estimation"],
                "correct": 1,
                "explanation": "GPH estimation uses the log periodogram in a regression framework to estimate the fractional differencing parameter d."
            },
            {
                "question": "In the GPH estimation regression equation log(I(λₖ)) = a + b log(λₖ) + εₖ, how is the slope b related to the fractional differencing parameter d?",
                "options": ["b = d²", "b = 1 − d", "b = −2d", "b = d / 2"],
                "correct": 2,
                "explanation": "In the GPH regression, b = −2d, so the fractional differencing parameter is d = −b/2."
            },
            {
                "question": "What is a key limitation of the GPH Estimation method?",
                "options": ["It can only be applied to perfectly stationary AR(1) models", "It relies entirely on the Yule-Walker equations", "Sensitivity to bandwidth selection in periodogram estimation may lead to biased estimates", "It cannot handle data with any degree of noise"],
                "correct": 2,
                "explanation": "GPH's performance depends heavily on bandwidth choice — too few frequencies yields high variance, too many introduces bias."
            },
            {
                "question": "Which estimation technique is designed specifically for estimating the fractional differencing parameter by focusing on a local frequency range (especially useful when sample size is limited)?",
                "options": ["Local Whittle estimation", "GPH estimation", "Box-Pierce estimation", "Unconditional Least Squares"],
                "correct": 0,
                "explanation": "Local Whittle estimation focuses on low frequencies near the origin, making it efficient for estimating d with limited data."
            },
            {
                "question": "How is Whittle Estimation fundamentally different from GPH estimation?",
                "options": ["Whittle estimation only works on financial data", "Whittle estimation is an alternative that uses a quasi-likelihood approach based on the likelihood of the periodogram", "Whittle estimation completely ignores spectral density", "Whittle estimation is identical to Maximum Likelihood Estimation"],
                "correct": 1,
                "explanation": "Whittle estimation uses a quasi-likelihood function derived from the periodogram, offering better statistical properties than GPH."
            },
            {
                "question": "In environmental time series, what physical phenomena often cause persistence in global temperatures?",
                "options": ["The immediate dissipation of all cloud cover", "The continuous accumulation of greenhouse gases like carbon dioxide leading to a prolonged warming effect", "Complete mean reversion every 5 years", "The random walk nature of solar radiation"],
                "correct": 1,
                "explanation": "Greenhouse gas accumulation creates long-memory persistence in temperature — past emissions continue to affect future temperatures."
            },
            {
                "question": "In a long-range persistent process, how does the Autocorrelation Function mathematically behave as a function of lag k?",
                "options": ["ρₖ ~ Ckᵅ, where α > 0, showing hyperbolic decay", "ρₖ = 0 for all k > 1", "ρₖ ~ Crᵏ, showing exponential decay", "ρₖ oscillates perfectly between 1 and −1"],
                "correct": 0,
                "explanation": "Long-range dependence: ρₖ ~ Ck^(2d−1), a power-law (hyperbolic) decay — much slower than exponential."
            },
            {
                "question": "Why does long-memory behavior in long-term interest rates (like 10-year bonds) matter to analysts?",
                "options": ["Because bonds are insensitive to interest rates", "It guarantees that interest rates will eventually drop to zero", "It implies current levels will remain influential for future rates, complicating forecasting and bond pricing", "It means short-term memory models like standard ARMA are perfectly sufficient"],
                "correct": 2,
                "explanation": "Long memory in interest rates means current rate levels persistently affect future rates, making forecasting and pricing more complex."
            },
            {
                "question": "If an analyst knows there is a strong yearly pattern in a sales dataset by observing its spectral density, what is the primary benefit?",
                "options": ["They can ignore the data completely", "They can use that known cycle to make better, more accurate predictions for the upcoming year", "They can prove the data is a random walk", "They can permanently remove the fractional difference parameter"],
                "correct": 1,
                "explanation": "Identifying dominant frequencies in the spectral density reveals seasonal cycles that improve forecasting accuracy."
            },
            {
                "question": "The Hurst Exponent indicates a stock price follows a random walk when it is approximately:",
                "options": ["H = 0", "H = 1", "H ≈ 0.5", "H = 0.99"],
                "correct": 2,
                "explanation": "H ≈ 0.5 means no persistence and no anti-persistence — consistent with a random walk (independent increments)."
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
        ],
        "additional_questions": [
            {
                "question": "What is a primary motivation for using multivariate time series analysis?",
                "options": ["To remove seasonality from a single dataset", "To investigate the cross relationships between several related series observed simultaneously over time", "To convert a non-stationary variable to a stationary one", "To strictly test for unit roots"],
                "correct": 1,
                "explanation": "Multivariate time series analysis studies the dynamic interrelationships between multiple series observed together over time."
            },
            {
                "question": "Which of the following is a main objective of jointly modeling multiple time series?",
                "options": ["To ignore dynamic relationships", "To reduce the number of variables in the dataset", "To improve the accuracy of forecasts for individual series by utilizing additional information from related series", "To convert vector data into scalar data"],
                "correct": 2,
                "explanation": "Joint modelling leverages cross-series information to produce more accurate forecasts than modelling each series independently."
            },
            {
                "question": "In financial markets, why is a multivariate approach practically important?",
                "options": ["Because price movements in one market can spread easily and instantly to another market", "Because stocks always move completely independently of one another", "Because financial data only consists of simple moving averages", "Because univariate models cannot handle large numbers"],
                "correct": 0,
                "explanation": "Financial contagion and spillover effects mean price movements transmit across markets, requiring multivariate modelling."
            },
            {
                "question": "What is the matrix containing the variances and covariances of a random vector X known as?",
                "options": ["Autocorrelation matrix", "Determinant matrix", "Dispersion matrix", "Adjoint matrix"],
                "correct": 2,
                "explanation": "The dispersion (variance-covariance) matrix contains all pairwise covariances and variances of the random vector's components."
            },
            {
                "question": "How is the cross-covariance matrix Σₓᵧ between two random vectors X and Y defined?",
                "options": ["Σₓᵧ = E(X)(Y)'", "Σₓᵧ = E(X−μₓ)(Y−μᵧ)'", "Σₓᵧ = E(X−μₓ) / E(Y−μᵧ)", "Σₓᵧ = μₓμᵧ"],
                "correct": 1,
                "explanation": "The cross-covariance matrix is defined as E[(X−μₓ)(Y−μᵧ)'] — the expected outer product of the centered vectors."
            },
            {
                "question": "For a stationary multivariate time series, what does the term γᵢⱼ(l) represent?",
                "options": ["The mean of the iᵗʰ series at lag l", "The cross-covariance between Yᵢₜ and Yⱼ,ₜ₊ₗ at lag l", "The absolute variance of the jᵗʰ series", "The standard deviation of the matrix"],
                "correct": 1,
                "explanation": "γᵢⱼ(l) is the cross-covariance between the iᵗʰ and jᵗʰ components of the multivariate series at lag l."
            },
            {
                "question": "How is the cross-correlation ρᵢⱼ(l) between yᵢₜ and yⱼₜ at lag l mathematically defined?",
                "options": ["ρᵢⱼ(l) = γᵢⱼ(l) / {γᵢᵢ(0)γⱼⱼ(0)}^(1/2)", "ρᵢⱼ(l) = γᵢᵢ(0) / γⱼⱼ(0)", "ρᵢⱼ(l) = γᵢⱼ(l) × γⱼᵢ(l)", "ρᵢⱼ(l) = E(Yᵢₜ) / E(Yⱼₜ)"],
                "correct": 0,
                "explanation": "The cross-correlation standardizes the cross-covariance by dividing by the geometric mean of the individual variances."
            },
            {
                "question": "Which of the following transposal properties holds true for the cross-covariance matrix Γ(l)?",
                "options": ["Γ(l) = Γ(l)'", "Γ(l) = Γ(−l)'", "Γ(l) = Γ(0)", "Γ(l) = I (Identity Matrix)"],
                "correct": 1,
                "explanation": "The cross-covariance matrix satisfies Γ(l) = Γ(−l)' — transposing reverses the lag direction."
            },
            {
                "question": "What does the property ρᵢⱼ(l) = ρⱼᵢ(−l) indicate about multivariate cross-correlations?",
                "options": ["The correlation between series i and j at lag l is the same as the correlation between series j and i at lag −l", "The correlation is always zero for negative lags", "Cross-correlations are strictly symmetrical around zero", "Lag l always equals lag −l"],
                "correct": 0,
                "explanation": "This property shows that reversing the series order is equivalent to negating the lag — the relationship is preserved under transposition."
            },
            {
                "question": "In the cross-correlation matrix formula ρ(l) = V⁻¹/²Γ(l)V⁻¹/², what does V represent?",
                "options": ["The variance of the error term", "A diagonal matrix of the lag 0 variances, diag(γ₁₁(0), γ₂₂(0), ..., γₖₖ(0))", "The moving average coefficient matrix", "The unit root identity"],
                "correct": 1,
                "explanation": "V is the diagonal matrix of individual series variances at lag 0, used to standardize the cross-covariance matrix."
            },
            {
                "question": "In a multivariate linear filtering equation Yₜ = Σ ΨⱼXₜ₋ⱼ, what are the Ψⱼ terms?",
                "options": ["Scalar constants", "k × r matrices", "White noise errors", "Frequency domains"],
                "correct": 1,
                "explanation": "The filter coefficients Ψⱼ are matrices (k × r) that transform the r-dimensional input into the k-dimensional output at each lag."
            },
            {
                "question": "Under what condition is a multivariate linear filter considered 'causal' or 'physically realizable'?",
                "options": ["If Ψⱼ = 1 for all j", "If Ψⱼ = 0 for all j < 0", "If Ψⱼ < 0 for all j", "If the determinant of Ψⱼ is zero"],
                "correct": 1,
                "explanation": "A causal filter only depends on present and past inputs (Ψⱼ = 0 for j < 0) — it doesn't use future information."
            },
            {
                "question": "A multivariate linear filter is considered 'stable' if the sum of the norms of its matrices meets which condition?",
                "options": ["Σ ||Ψⱼ|| = ∞", "Σ ||Ψⱼ|| < 0", "Σ ||Ψⱼ|| < ∞", "Σ ||Ψⱼ|| = 1"],
                "correct": 2,
                "explanation": "Stability requires absolute summability of the filter coefficient matrices — the total norm must be finite."
            },
            {
                "question": "If a linear filter is stable and the input random vectors have finite second moments, what happens to the filtering representation?",
                "options": ["It diverges completely", "It exists uniquely and converges in mean square", "It becomes non-stationary", "It converts into a random walk"],
                "correct": 1,
                "explanation": "A stable filter with finite-variance inputs produces a well-defined output that converges in mean square."
            },
            {
                "question": "What is the general equation form of a Vector Autoregressive Moving Average (VARMA) process?",
                "options": ["Yₜ = Yₜ₋₁ + eₜ", "Yₜ = μ + Ψ(B)eₜ", "Yₜ = μ + θeₜ₋₁", "Yₜ = Tₜ + Sₜ + Cₜ + Iₜ"],
                "correct": 1,
                "explanation": "A VARMA process is expressed as Yₜ = μ + Ψ(B)eₜ, where Ψ(B) is a matrix polynomial in the backshift operator."
            },
            {
                "question": "A VARMA process is considered stationary if it can be represented as:",
                "options": ["A divergent vector autoregression", "A convergent vector moving average process of infinite order", "A strictly seasonal univariate model", "A matrix with infinite variance"],
                "correct": 1,
                "explanation": "A stationary VARMA can be written as a convergent infinite-order VMA — the MA(∞) representation must converge."
            },
            {
                "question": "In the stationarity conditions for a VARMA process Yₜ = μ + Φ(B)⁻¹Θ(B)eₜ, the sequence must be convergent for:",
                "options": ["|z| > 1", "|z| = 0", "|z| < 1", "|z| = ∞"],
                "correct": 2,
                "explanation": "The AR polynomial's roots must lie outside the unit circle, equivalently the inverse converges for |z| < 1."
            },
            {
                "question": "By using the adjoint matrix relationship A⁻¹ = (1/det(A))adj(A), how can the stationary VARMA process be rewritten?",
                "options": ["Yₜ = μ + eₜ", "Yₜ = μ + det(Φ(B))⁻¹Φ*(B)Θq(B)eₜ", "Yₜ = det(B) + μ", "Yₜ = Φ(B) × Θ(B)"],
                "correct": 1,
                "explanation": "Using the adjoint formula, the VARMA process can be rewritten with the determinant and adjoint of the AR polynomial matrix."
            },
            {
                "question": "For a Bivariate MA(1) process, what is the value of the cross-covariance matrix Γ(l) for all lags l ≥ 2?",
                "options": ["1", "∞", "0 (Zero matrix)", "Equal to Γ(1)"],
                "correct": 2,
                "explanation": "Like univariate MA(1), the bivariate MA(1) has zero cross-covariance for lags beyond the model order — Γ(l) = 0 for l ≥ 2."
            },
            {
                "question": "In the provided example of a Bivariate MA(1) process, the parameter matrix Θ₁ is multiplied by which vector?",
                "options": ["(Y₁ₜ, Y₂ₜ)'", "(e₁,ₜ₋₁, e₂,ₜ₋₁)'", "(μ₁, μ₂)'", "(ρ₁₁, ρ₂₂)'"],
                "correct": 1,
                "explanation": "In a VMA(1), the Θ₁ matrix multiplies the lagged error vector (e₁,ₜ₋₁, e₂,ₜ₋₁)' — the past innovations."
            },
            {
                "question": "Which of the following is a classic example of using multivariate time series in Economics?",
                "options": ["Predicting animal migration patterns", "Simultaneous study of GDP, inflation, unemployment rate, and money supply", "Forecasting daily solar radiation", "Modeling a single company's stock volatility over time"],
                "correct": 1,
                "explanation": "Macroeconomic variables like GDP, inflation, unemployment, and money supply are interrelated and best studied jointly."
            },
            {
                "question": "How are VARMA models applied in the Energy Market for Electricity Load Forecasting?",
                "options": ["By looking exclusively at historical electricity load data", "By modeling interrelated time series such as temperature, humidity, energy prices, and demand simultaneously", "By assuming electricity demand is independent of weather", "By identifying strictly deterministic trends"],
                "correct": 1,
                "explanation": "Electricity demand depends on weather, prices, and other factors — VARMA captures these interdependencies for better forecasting."
            },
            {
                "question": "In Healthcare Epidemiology, how does a VARMA model assist in public health planning?",
                "options": ["By tracking a single patient's recovery time", "By studying the spread of infectious diseases where the number of cases in different regions may be interdependent", "By forecasting the cost of single medications", "By isolating patient data to remove cross-correlations"],
                "correct": 1,
                "explanation": "Disease spread across regions is interdependent — VARMA models capture spatial and temporal cross-correlations in case counts."
            },
            {
                "question": "Why are multivariate time series models essential for Hospital Resource Planning?",
                "options": ["They can predict patient arrivals and demand for critical care beds by considering the correlation between different types of admissions", "They replace the need for doctors", "They ensure hospital beds are never empty", "They convert qualitative patient feedback into random walks"],
                "correct": 0,
                "explanation": "Different admission types (ER, surgical, ICU) are correlated — multivariate models capture these dependencies for resource allocation."
            },
            {
                "question": "How do Climate Scientists use VARMA models for weather forecasting?",
                "options": ["They model single-variable series like only tracking humidity", "They consider the interactions between various climate variables like temperature, humidity, and wind speed across multiple locations", "They use them to prove global temperatures are mean-reverting", "They only use them for deterministic seasonal decomposition"],
                "correct": 1,
                "explanation": "Climate variables interact across locations and types — VARMA models capture these multivariate, spatial-temporal dynamics."
            },
            {
                "question": "In Air Quality Monitoring, why is a multivariate model superior to a univariate one?",
                "options": ["Because pollutants like carbon monoxide, nitrogen dioxide, and particulate matter are often interdependent in atmospheric conditions", "Because air quality has no seasonal component", "Because the variance of air quality is always infinite", "Because univariate models cannot handle decimal values"],
                "correct": 0,
                "explanation": "Pollutant concentrations are physically and chemically interdependent — multivariate modelling captures these joint dynamics."
            },
            {
                "question": "What does the ijᵗʰ element of the cross covariance matrix Σₓᵧ directly calculate?",
                "options": ["The standard deviation of X", "The exact mean of Y", "The covariance between Xᵢ and Yⱼ", "The cross-correlation at lag 10"],
                "correct": 2,
                "explanation": "The (i,j) element of Σₓᵧ is Cov(Xᵢ, Yⱼ) — the covariance between the iᵗʰ component of X and jᵗʰ component of Y."
            },
            {
                "question": "In a Vector Moving Average of Order q model (VMA(q)), the term Θ(B) is expressed as:",
                "options": ["Iₖ + Θ₁B + Θ₂B² + ... + ΘqBq", "Φ₁B + Φ₂B²", "(1−B)ᵈ", "1 / (1−ΘB)"],
                "correct": 0,
                "explanation": "Θ(B) = Iₖ + Θ₁B + Θ₂B² + ... + ΘqBq is the MA polynomial matrix in the backshift operator B."
            },
            {
                "question": "What differentiates the cross-correlation matrix ρ(l) from the cross-covariance matrix Γ(l)?",
                "options": ["ρ(l) is not symmetric under time reversal", "ρ(l) contains infinite values", "ρ(l) is standardized by the lag 0 variances, restricting its elements to the [−1, 1] range", "There is no mathematical difference"],
                "correct": 2,
                "explanation": "ρ(l) normalizes Γ(l) by the individual variances, producing bounded correlation values between −1 and 1."
            },
            {
                "question": "In the mathematical notation E(X−μₓ)(Y−μᵧ)', what does the prime (') symbol indicate?",
                "options": ["The first derivative", "The vector/matrix transpose", "The fractional difference", "The inverse matrix"],
                "correct": 1,
                "explanation": "The prime (') denotes the transpose — (Y−μᵧ)' converts the column vector to a row vector for the outer product."
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
        ],
        "additional_questions": [
            {
                "question": "What defines an I(1) process in time series?",
                "options": ["A stationary series without a trend", "An integrated series of order 1 that becomes an I(0) process after differencing once", "A strictly moving average process", "A process with an infinite cointegration rank"],
                "correct": 1,
                "explanation": "An I(1) process is integrated of order 1 — it becomes stationary (I(0)) after a single differencing operation."
            },
            {
                "question": "What issue arises when performing a standard regression on two completely independent non-stationary I(1) processes?",
                "options": ["Perfect correlation", "Spurious regression", "Exponential decay", "Fractional integration"],
                "correct": 1,
                "explanation": "Regressing independent I(1) series often yields misleadingly significant results — a classic spurious regression problem."
            },
            {
                "question": "If two non-stationary time series are both I(1), what condition must be met for them to be considered 'cointegrated'?",
                "options": ["Their sum must be an I(2) process", "They must have an identical mean", "A linear combination of the two series must be stationary, i.e., I(0)", "They must both be completely independent random walks"],
                "correct": 2,
                "explanation": "Cointegration requires that a specific linear combination of the I(1) series is stationary (I(0)), indicating a long-run equilibrium."
            },
            {
                "question": "In cointegration analysis, what is the term used for the number of independent cointegrating vectors?",
                "options": ["Cointegration rank", "Adjustment coefficient", "Order of integration", "Spectral density"],
                "correct": 0,
                "explanation": "The cointegration rank is the number of linearly independent cointegrating vectors in a multivariate system."
            },
            {
                "question": "Which financial trading strategy relies heavily on the cointegration of two or more assets to exploit short-term deviations from a long-term equilibrium?",
                "options": ["Moving average smoothing", "High-frequency spoofing", "Pairs trading", "Naïve forecasting"],
                "correct": 2,
                "explanation": "Pairs trading identifies cointegrated assets and profits when the spread deviates from and reverts to its long-run equilibrium."
            },
            {
                "question": "What is the primary purpose of an Error Correction Model (ECM)?",
                "options": ["To permanently convert I(0) processes into I(1) processes", "To analyze the relationship between non-stationary variables that share a stable, long-term equilibrium", "To filter out all short-term effects completely", "To test for strict deterministic trends"],
                "correct": 1,
                "explanation": "ECMs model both the short-run dynamics and the long-run equilibrium relationship between cointegrated non-stationary variables."
            },
            {
                "question": "In an Error Correction Model, what does the Error Correction Term (ECT) specifically measure?",
                "options": ["The gap between the current value and the long-term equilibrium", "The constant variance of the residuals", "The immediate impact of changes in unrelated variables", "The moving average of the error bounds"],
                "correct": 0,
                "explanation": "The ECT measures the deviation from the long-run equilibrium — it quantifies how far the system is from its stable state."
            },
            {
                "question": "How does an Error Correction Model (ECM) separate changes in a variable?",
                "options": ["Into independent and identically distributed (i.i.d.) random noise", "Into deterministic and stochastic trends", "Into short-term effects and long-term correction toward equilibrium", "Into seasonal and cyclical components"],
                "correct": 2,
                "explanation": "ECMs decompose changes into short-run dynamics (immediate effects) and long-run adjustment (correction toward equilibrium)."
            },
            {
                "question": "What is a key limitation of using an Error Correction Model (ECM)?",
                "options": ["It requires that variables be cointegrated and is unsuitable for series without a long-term relationship", "It can only handle variables that have a short-term relationship", "It is only applicable to purely cross-sectional data", "It assumes all deviations from the mean are permanent"],
                "correct": 0,
                "explanation": "ECMs require cointegration — without a genuine long-run equilibrium between variables, the model is misspecified."
            },
            {
                "question": "Which economic theory serves as a practical example for an Error Correction Model by relating nominal interest rates and inflation?",
                "options": ["The Random Walk Theory", "The Fisher Effect", "The Markov Property", "The Black-Scholes Model"],
                "correct": 1,
                "explanation": "The Fisher Effect posits a long-run equilibrium between nominal interest rates and inflation — a natural ECM application."
            },
            {
                "question": "The Engle-Granger Two Step Test is primarily designed to test for what phenomenon between variables?",
                "options": ["Heteroscedasticity", "Spurious regression", "Cointegration", "White noise"],
                "correct": 2,
                "explanation": "The Engle-Granger two-step procedure tests whether two (or more) I(1) variables are cointegrated."
            },
            {
                "question": "What is the first step in conducting the Engle-Granger Two Step Test?",
                "options": ["Taking the second difference of the series", "Regressing one variable on the other(s) to obtain the estimated residuals", "Calculating the Moving Average of the series", "Applying the Box-Pierce test to the data"],
                "correct": 1,
                "explanation": "Step 1: run the cointegrating regression of one I(1) variable on the other(s) and save the residuals."
            },
            {
                "question": "In the second step of the Engle-Granger test, what statistical test is typically applied to the residuals?",
                "options": ["Ljung-Box test", "Shapiro-Wilk test", "Augmented Dickey-Fuller (ADF) test", "Chi-Square test"],
                "correct": 2,
                "explanation": "Step 2: apply the ADF test to the residuals — if they are stationary, the variables are cointegrated."
            },
            {
                "question": "What does the Alternative Hypothesis (H₁) state in the second step of the Engle-Granger test?",
                "options": ["The residuals are non-stationary, so the series are not cointegrated", "The residuals are purely random walks", "The residuals are stationary, meaning the series are cointegrated", "The variables have infinite variance"],
                "correct": 2,
                "explanation": "H₁: the residuals are stationary (I(0)), which means the original series share a cointegrating relationship."
            },
            {
                "question": "What is a known limitation of the Engle-Granger test?",
                "options": ["It can only be used on univariate time series", "It tests for infinite variance instead of cointegration", "It cannot process I(1) variables", "It is only suitable for two variables and assumes one is the dependent variable"],
                "correct": 3,
                "explanation": "Engle-Granger is limited to bivariate settings and the results can change depending on which variable is treated as the dependent variable."
            },
            {
                "question": "Which cointegration test allows for the determination of the number of cointegrating vectors (the cointegration rank) when dealing with more than two variables?",
                "options": ["Engle-Granger Test", "Johansen Test", "Durbin-Watson Test", "White's General Test"],
                "correct": 1,
                "explanation": "The Johansen test is a multivariate approach that determines the cointegrating rank — the number of independent cointegrating relationships."
            },
            {
                "question": "In the Johansen Test, what does the 'Trace Test' specifically test against?",
                "options": ["Whether the series exhibits heteroscedasticity", "The null hypothesis that the number of cointegrating vectors is less than or equal to r", "The null hypothesis that the residuals are non-stationary", "Whether the adjustment coefficient is zero"],
                "correct": 1,
                "explanation": "The Trace test's H₀: the number of cointegrating vectors ≤ r, tested against the alternative of more than r vectors."
            },
            {
                "question": "What is the null hypothesis of the 'Maximum Eigenvalue Test' within the Johansen testing framework?",
                "options": ["The process has infinite variance", "The data is perfectly stationary without differencing", "The number of cointegrating vectors is exactly r", "The variables are entirely independent"],
                "correct": 2,
                "explanation": "The Maximum Eigenvalue test's H₀: exactly r cointegrating vectors, against the alternative of r + 1 vectors."
            },
            {
                "question": "Why might researchers utilize the Auto-Regressive Distributed Lag (ARDL) Bounds Test for cointegration?",
                "options": ["Because it is used for analyzing exclusively stationary data", "Because it can test for cointegration when the variables are a mix of I(0) and I(1)", "Because it avoids the use of any lag lengths", "Because it is identical to the Augmented Dickey-Fuller test"],
                "correct": 1,
                "explanation": "The ARDL bounds test is flexible — it works regardless of whether variables are I(0), I(1), or a mixture of both."
            },
            {
                "question": "What relationship might pharmaceutical companies analyze using cointegration tests to validate cost-recovery models?",
                "options": ["Weather patterns and hospital admissions", "Animal migration and drug availability", "Drug prices and research and development (R&D) costs", "Patient demographics and hospital locations"],
                "correct": 2,
                "explanation": "Cointegration between drug prices and R&D costs can validate whether prices adjust to recover long-term research investments."
            },
            {
                "question": "In time series analysis, what is Granger Causality fundamentally assessing?",
                "options": ["True philosophical and physical cause-and-effect between variables", "The absolute magnitude of the error correction term", "Whether the series is stationary around a deterministic trend", "If past values of one variable contain information that helps predict future values of another variable"],
                "correct": 3,
                "explanation": "Granger causality tests predictive ability — whether X's past improves forecasts of Y beyond Y's own history."
            },
            {
                "question": "To test if variable X Granger-causes variable Y, what does the 'unrestricted model' include?",
                "options": ["Only lagged values of Y", "Both lagged values of Y and X", "Neither lagged values of X nor Y", "Only future predicted values of X"],
                "correct": 1,
                "explanation": "The unrestricted model includes lags of both Y and X to test whether adding X's lags significantly improves the model."
            },
            {
                "question": "In the context of testing for Granger causality, what does the 'restricted model' consist of?",
                "options": ["Both lagged values of Y and X", "A model of Y that includes only lagged values of Y", "A model containing only the Error Correction Term", "A moving average filter applied to X"],
                "correct": 1,
                "explanation": "The restricted model uses only Y's own lagged values — it serves as the baseline to compare against the unrestricted model."
            },
            {
                "question": "What statistical test is used to compare the unrestricted and restricted models in Granger causality to determine if lagged values of X add significant predictive power?",
                "options": ["Augmented Dickey-Fuller Test", "F-Test", "KPSS Test", "Spectral Density Test"],
                "correct": 1,
                "explanation": "The F-test compares the residual sum of squares from both models to determine if X's lags significantly improve prediction."
            },
            {
                "question": "What is a critical requirement for time series variables before applying the standard Granger Causality test?",
                "options": ["The variables must be strictly non-stationary", "The variables must be stationary (non-stationary data must be differenced first)", "The variables must have an identical mean", "The variables must be perfectly correlated"],
                "correct": 1,
                "explanation": "Standard Granger causality requires stationary data — non-stationary series must be differenced to avoid spurious results."
            },
            {
                "question": "Which procedure systematically extends traditional Granger causality testing by determining the optimal lag structure for both variables?",
                "options": ["The Box-Jenkins Procedure", "The Engle-Granger Procedure", "The Hsiao Procedure", "The Johansen Procedure"],
                "correct": 2,
                "explanation": "The Hsiao procedure extends Granger causality by systematically and objectively selecting the optimal lag lengths."
            },
            {
                "question": "The Hsiao Procedure combines traditional Granger causality with which specific criterion to balance model fit and complexity?",
                "options": ["Akaike's Final Prediction Error (FPE)", "Bayesian Information Criterion (BIC)", "Mean Absolute Error (MAE)", "Theil's U Statistic"],
                "correct": 0,
                "explanation": "The Hsiao procedure uses Akaike's FPE criterion to objectively balance prediction accuracy against model complexity."
            },
            {
                "question": "What is the major advantage of using the Hsiao Procedure over traditional Granger causality?",
                "options": ["It proves absolute physical causation instead of just predictive ability", "It avoids arbitrary lag length choices and systematically determines the best lag structure", "It automatically converts all data to white noise", "It bypasses the need for the F-Test entirely"],
                "correct": 1,
                "explanation": "The Hsiao procedure removes subjectivity in lag selection by using a data-driven criterion to find optimal lags."
            },
            {
                "question": "In practical economic applications, Granger Causality (and the Hsiao procedure) can be used to test if past levels of investment impact which of the following?",
                "options": ["Fractional integration", "Economic output / GDP growth", "Daily weather changes", "Infinite variance"],
                "correct": 1,
                "explanation": "A common application: testing whether past investment Granger-causes GDP growth, informing macroeconomic policy."
            },
            {
                "question": "Which of the following statements about Granger Causality is TRUE?",
                "options": ["It implies that knowing the past values of one variable helps predict the other variable better than using its own past values alone", "It is exactly the same as true causation", "It can only be calculated on a single variable against its own mean", "It requires data to be completely non-stationary to yield significant results"],
                "correct": 0,
                "explanation": "Granger causality means X's history adds predictive value for Y beyond what Y's own history provides — it's about prediction, not true causation."
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
        ],
        "additional_questions": [
            {
                "question": "In spectral analysis, what is the primary goal when analyzing a stationary time series?",
                "options": ["To convert the data into a purely non-stationary format", "To decompose the time series into a combination of sinusoids (sine and cosine functions) of different frequencies", "To eliminate all variance from the data", "To strictly test for unit roots"],
                "correct": 1,
                "explanation": "Spectral analysis decomposes a stationary time series into sinusoidal components at different frequencies to reveal periodic structure."
            },
            {
                "question": "From a regression standpoint, how can spectral analysis be viewed?",
                "options": ["As a multiple regression problem where the independent variables are sine and cosine functions of possible frequencies", "As a simple linear regression on past error terms", "As an autoregressive process with infinite lags", "As a logistic regression predicting binary outcomes"],
                "correct": 0,
                "explanation": "Spectral analysis can be seen as regressing the series on sine and cosine basis functions at each frequency — a harmonic regression."
            },
            {
                "question": "Which of the following is a practical application of the Fourier Transform in image processing?",
                "options": ["Removing cross-sectional dependence", "Equalizing audio channels", "Image compression, such as the JPEG format using the Discrete Cosine Transform (DCT)", "Converting images into 1-dimensional moving averages"],
                "correct": 2,
                "explanation": "JPEG uses the Discrete Cosine Transform (DCT), a variant of the Fourier Transform, to compress image data efficiently."
            },
            {
                "question": "According to the Spectral Representation Theorem, any stationary time series can be expressed as:",
                "options": ["An exponentially decaying random walk", "A combination of sinusoidal functions of different frequencies, each with its own amplitude and phase", "A strictly moving average process of order 1", "A non-stationary process with infinite variance"],
                "correct": 1,
                "explanation": "The Spectral Representation Theorem states any stationary series can be decomposed into sinusoids with random amplitudes and phases."
            },
            {
                "question": "How is the Spectral Density Function (SDF) mathematically related to the auto-covariance function?",
                "options": ["It is the inverse square root of the auto-covariance function", "It is the exact same as the auto-covariance function", "It is the Fourier transform of the auto-covariance function", "It is the first derivative of the auto-covariance function"],
                "correct": 2,
                "explanation": "The SDF and autocovariance function form a Fourier transform pair — the SDF is the Fourier transform of γ(h)."
            },
            {
                "question": "For a real-valued time series, which property holds true for the Spectral Density Function S(ω)?",
                "options": ["It is strictly negative", "It is symmetric, meaning S(ω) = S(−ω)", "It diverges to infinity at all frequencies", "It is asymmetric and only defined for positive frequencies"],
                "correct": 1,
                "explanation": "For real-valued series, the SDF is an even (symmetric) function: S(ω) = S(−ω), since the autocovariance is real."
            },
            {
                "question": "The integral of the Spectral Density Function over the range [−π, π] is equal to:",
                "options": ["The overall mean of the time series (μ)", "The total variance of the time series (γ(0))", "Zero", "The fractional difference parameter (d)"],
                "correct": 1,
                "explanation": "Integrating the SDF over all frequencies recovers the total variance γ(0) — Parseval's theorem in time series."
            },
            {
                "question": "What does the Spectral Density Function of a White Noise process look like?",
                "options": ["It is highly concentrated at low frequencies", "It forms a perfect bell curve", "It is flat and constant across all frequencies (equal to σ²/2π)", "It is strictly zero at all frequencies"],
                "correct": 2,
                "explanation": "White noise has equal power at all frequencies — a flat spectrum, hence the name 'white' (analogous to white light)."
            },
            {
                "question": "For an AR(1) process where the parameter φ is greater than 0, where is the spectral density concentrated?",
                "options": ["It is uniformly distributed", "It is dominated by high frequencies", "It diverges at the Nyquist frequency", "It is dominated by low frequencies"],
                "correct": 3,
                "explanation": "Positive φ in AR(1) creates positive autocorrelation — the spectrum peaks at low frequencies (slow-moving patterns)."
            },
            {
                "question": "How is spectral analysis practically utilized in the field of Medicine?",
                "options": ["To predict future patient demographics", "To analyze hospital resource supply chains", "To detect abnormalities in heart rhythms (arrhythmia) by identifying irregular frequencies in an ECG", "To track the spread of infectious diseases via a spatial map"],
                "correct": 2,
                "explanation": "ECG spectral analysis identifies abnormal frequency components in heart signals to detect arrhythmias and other cardiac conditions."
            },
            {
                "question": "What characterizes 'Parametric Estimation' of spectral density?",
                "options": ["It relies entirely on the periodogram without any assumptions", "It assumes a specific model for the time series (like ARMA), estimates its parameters, and computes the SDF from that model", "It divides data into overlapping segments and averages them", "It applies a Daniell kernel to raw data"],
                "correct": 1,
                "explanation": "Parametric estimation fits a model (e.g., ARMA), then derives the theoretical SDF from the estimated model parameters."
            },
            {
                "question": "Which of the following is considered a fundamental non-parametric method for estimating the spectral density function?",
                "options": ["Yule-Walker Equations", "The Ljung-Box Test", "Maximum Likelihood Estimation", "The Periodogram"],
                "correct": 3,
                "explanation": "The periodogram is the basic non-parametric spectral estimator — it directly computes power at each frequency from the data."
            },
            {
                "question": "What is a major statistical drawback of using the raw Periodogram to estimate spectral density?",
                "options": ["It is inconsistent because its variance does not decrease as the sample size increases", "It has a severe bias that grows exponentially", "It requires assuming the data is perfectly white noise", "It cannot be calculated for discrete time series"],
                "correct": 0,
                "explanation": "The raw periodogram is inconsistent — its variance remains constant regardless of sample size, making it a noisy estimator."
            },
            {
                "question": "How can the inconsistency and noise of the raw periodogram be addressed?",
                "options": ["By reducing the sample size", "By applying smoothing techniques (like kernel smoothing or averaging)", "By differentiating the series an infinite number of times", "By converting it directly to an AR(1) model"],
                "correct": 1,
                "explanation": "Smoothing (kernel smoothing, segment averaging) reduces variance at the cost of some frequency resolution."
            },
            {
                "question": "In kernel smoothing, what does the 'Daniell kernel' apply to the periodogram?",
                "options": ["Triangular weights", "Smoother weights for gradual tapering", "A simple moving average", "An exponential decay factor"],
                "correct": 2,
                "explanation": "The Daniell kernel applies equal (uniform) weights — essentially a simple moving average of periodogram ordinates."
            },
            {
                "question": "Which spectral estimation technique divides the time series into overlapping segments, computes the periodogram for each, and averages them?",
                "options": ["Bartlett's Method", "Welch's Method", "Geweke and Porter-Hudak (GPH) Method", "Whittle's Method"],
                "correct": 1,
                "explanation": "Welch's method uses overlapping, windowed segments — each gets its own periodogram, then they're averaged to reduce variance."
            },
            {
                "question": "What is a primary disadvantage of Welch's Method?",
                "options": ["It greatly increases the variance of the estimate", "It requires the data to be strictly an ARMA process", "It suffers from reduced frequency resolution due to segmenting the data", "It is highly susceptible to noise"],
                "correct": 2,
                "explanation": "Shorter segments in Welch's method mean fewer frequency bins — trading frequency resolution for reduced variance."
            },
            {
                "question": "In practical estimation, what is the purpose of applying a windowing function (like Hamming or Hann)?",
                "options": ["To introduce deterministic seasonality", "To reduce spectral leakage while maintaining reasonable frequency resolution", "To perfectly reconstruct missing data points", "To increase the overall variance of the model"],
                "correct": 1,
                "explanation": "Window functions taper the data at the edges to reduce spectral leakage — energy spreading to unrelated frequencies."
            },
            {
                "question": "When choosing a smoothing bandwidth, what is the primary trade-off?",
                "options": ["Stationarity vs. Non-stationarity", "Variance vs. Resolution (Wider bandwidth = less variance but lower resolution)", "Mean vs. Median", "Time domain vs. Fractional integration"],
                "correct": 1,
                "explanation": "Wider bandwidth → more smoothing → less variance but coarser frequency resolution. This is the fundamental bandwidth trade-off."
            },
            {
                "question": "What is the Nyquist criterion for the sampling rate (fₛ)?",
                "options": ["fₛ = fₘₐₓ", "fₛ < fₘₐₓ / 2", "fₛ > 2fₘₐₓ", "fₛ = 0"],
                "correct": 2,
                "explanation": "Nyquist theorem: the sampling rate must exceed twice the maximum frequency to avoid aliasing — fₛ > 2fₘₐₓ."
            },
            {
                "question": "If a time series is non-stationary, which advanced frequency-domain methods should be used instead of standard spectral density?",
                "options": ["Simple Moving Average", "Wavelet Transform or Short-Time Fourier Transform (STFT)", "Ordinary Least Squares (OLS)", "Augmented Dickey-Fuller Test"],
                "correct": 1,
                "explanation": "Wavelets and STFT provide time-frequency analysis — they handle non-stationary signals where frequency content changes over time."
            },
            {
                "question": "How is the 'Cross Spectrum' mathematically defined for a bivariate time series?",
                "options": ["As the Fourier transform of the cross-covariance function", "As the simple addition of two individual spectral densities", "As the cross-correlation divided by the total variance", "As the derivative of the auto-covariance function"],
                "correct": 0,
                "explanation": "The cross-spectrum is the Fourier transform of the cross-covariance function — it reveals frequency-domain relationships between two series."
            },
            {
                "question": "The real part of the Cross Spectrum is known as the:",
                "options": ["Quadrature spectrum", "Phase spectrum", "Co-spectrum", "Coherence"],
                "correct": 2,
                "explanation": "The co-spectrum (real part) measures the in-phase co-variation between two series at each frequency."
            },
            {
                "question": "The imaginary part of the Cross Spectrum is known as the:",
                "options": ["Coherence", "Quadrature spectrum", "Co-spectrum", "Amplitude spectrum"],
                "correct": 1,
                "explanation": "The quadrature spectrum (imaginary part) captures the out-of-phase (90° shifted) relationship between two series."
            },
            {
                "question": "What does the 'Squared Coherence' between two time series measure?",
                "options": ["The non-linear predictability of the series", "The strength of the linear correlation between the two time series at a specific frequency ω", "The exact phase shift between the series", "The overall mean of the combined series"],
                "correct": 1,
                "explanation": "Squared coherence is the frequency-domain analog of R² — it measures the linear association between two series at each frequency."
            },
            {
                "question": "What is the bounded range of the Squared Coherence K²ₓᵧ(ω)?",
                "options": ["−1 ≤ K²ₓᵧ(ω) ≤ 1", "0 ≤ K²ₓᵧ(ω) ≤ ∞", "0 ≤ K²ₓᵧ(ω) ≤ 1", "−∞ < K²ₓᵧ(ω) < ∞"],
                "correct": 2,
                "explanation": "Squared coherence is bounded between 0 (no linear relationship) and 1 (perfect linear relationship) at each frequency."
            },
            {
                "question": "In cross-spectral analysis, what does the 'Phase Spectrum' indicate?",
                "options": ["The sum of the amplitudes", "Whether the two series are completely independent", "The phase difference or the lead/lag relationship between the two series at a given frequency", "The exact variance of the error terms"],
                "correct": 2,
                "explanation": "The phase spectrum shows the lead/lag relationship — how much one series leads or lags the other at each frequency."
            },
            {
                "question": "If two series xₜ and yₜ are completely uncorrelated, what is the spectrum of their sum zₜ = xₜ + yₜ?",
                "options": ["fz(ω) = fxy(ω) × fyx(ω)", "fz(ω) = fx(ω) + fy(ω)", "fz(ω) = 0", "fz(ω) = fx(ω) − fy(ω)"],
                "correct": 1,
                "explanation": "For uncorrelated series, cross-spectrum is zero, so the spectrum of their sum equals the sum of individual spectra."
            },
            {
                "question": "In telecommunications, how are spectral techniques fundamentally applied?",
                "options": ["For estimating company valuations", "For analyzing and designing communication signals via modulation and demodulation", "For mapping structural stresses in buildings", "For modeling the volatility of exchange rates"],
                "correct": 1,
                "explanation": "Spectral methods are essential in telecommunications for signal design, modulation/demodulation, and channel analysis."
            },
            {
                "question": "Which kernel is characterized by applying 'triangular weights' to the periodogram?",
                "options": ["Parzen kernel", "Daniell kernel", "Bartlett kernel", "Welch kernel"],
                "correct": 2,
                "explanation": "The Bartlett kernel uses triangular (linearly decreasing) weights, giving more weight to nearby frequencies."
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
        ],
        "additional_questions": [
            {
                "question": "While ARIMA models describe the mean development of a time series, what do conditional heteroscedastic models primarily describe?",
                "options": ["The unconditional mean", "The time-varying conditional variances and covariances", "The deterministic cyclical trend", "The cross-sectional dependence"],
                "correct": 1,
                "explanation": "Conditional heteroscedastic models (ARCH/GARCH) focus on modelling how the variance changes over time, conditioned on past information."
            },
            {
                "question": "Which of the following is a recognized property of volatility in financial time series?",
                "options": ["Volatility jumps are extremely frequent", "Volatility exhibits 'clusters,' meaning it is high for certain periods and low for others", "Volatility is always strictly non-stationary", "Volatility only responds symmetrically to all market shocks"],
                "correct": 1,
                "explanation": "Volatility clustering: large changes tend to follow large changes, and small changes tend to follow small changes."
            },
            {
                "question": "What does the 'leverage effect' refer to in the context of financial volatility?",
                "options": ["Volatility responds symmetrically to all returns", "Positive returns increase volatility more than negative returns", "Volatility responds asymmetrically, typically increasing more after negative returns than positive returns", "The effect of borrowing money to invest in the stock market"],
                "correct": 2,
                "explanation": "The leverage effect: negative shocks (bad news) increase volatility more than positive shocks of the same magnitude."
            },
            {
                "question": "How is Historical Volatility (HV) mathematically defined over a specific window of time?",
                "options": ["As the mean of the raw prices", "As the standard deviation of the log returns", "As the simple moving average of the error term", "As the fractional difference of the variance"],
                "correct": 1,
                "explanation": "Historical volatility is the standard deviation of log returns over a chosen time window — a backward-looking measure."
            },
            {
                "question": "What is the standard industry practice for annualizing daily Historical Volatility?",
                "options": ["Multiply it by 365", "Divide it by 12", "Multiply it by the square root of 252 (the approximate number of trading days in a year)", "Square the daily volatility"],
                "correct": 2,
                "explanation": "Daily volatility is annualized by multiplying by √252, since variance scales linearly with time and there are ~252 trading days."
            },
            {
                "question": "Which of the following is a limitation of using Historical Volatility (HV)?",
                "options": ["It is purely forward-looking", "It assumes past market conditions are similar to future conditions, which may not hold during regime changes", "It can only be calculated on a yearly basis", "It completely ignores all extreme price movements"],
                "correct": 1,
                "explanation": "HV is backward-looking and assumes the future resembles the past — it fails during regime changes or structural breaks."
            },
            {
                "question": "In behavioral finance, how might an investor react to a rising Volatility Index (VIX)?",
                "options": ["They increase holdings in riskier assets like stocks", "They assume the market is perfectly stationary", "They reduce exposure to riskier assets and increase holdings in safe-haven assets like bonds or gold", "They stop trading entirely for the year"],
                "correct": 2,
                "explanation": "Rising VIX signals increased fear/uncertainty — investors typically shift to safe-haven assets to reduce portfolio risk."
            },
            {
                "question": "In volatility modeling notation, what does F_{t-1} represent?",
                "options": ["The forecast error at time t", "The fractional integration parameter", "The information set up to time t−1", "The F-statistic of the model"],
                "correct": 2,
                "explanation": "F_{t-1} (or ℱ_{t-1}) is the filtration — the complete information set available up to and including time t−1."
            },
            {
                "question": "Under the ARCH framework, how do shocks typically behave?",
                "options": ["Large shocks tend to be followed by another large shock", "Large shocks are immediately followed by zero volatility", "Shocks are perfectly mean-reverting within one day", "All shocks are identically zero"],
                "correct": 0,
                "explanation": "ARCH captures volatility clustering — large shocks increase the conditional variance, making subsequent large shocks more likely."
            },
            {
                "question": "In the ARCH(1) model defined by σ²ₜ = α₀ + α₁e²ₜ₋₁, what is the unconditional variance of eₜ?",
                "options": ["α₀", "α₁", "α₀/(1 − α₁)", "α₀ + α₁"],
                "correct": 2,
                "explanation": "The unconditional variance is α₀/(1 − α₁), derived by taking the unconditional expectation of the ARCH equation."
            },
            {
                "question": "Which of the following distributions is commonly assumed for the white noise term εₜ in an ARCH model?",
                "options": ["Uniform distribution", "Binomial distribution", "Standard normal, Student's t, or a generalized error distribution (GED)", "Poisson distribution"],
                "correct": 2,
                "explanation": "ARCH models commonly use Normal, Student's t (for heavy tails), or GED distributions for the standardized innovations."
            },
            {
                "question": "What is a primary limitation of the standard ARCH model?",
                "options": ["It requires the data to have an infinite mean", "It treats positive and negative shocks of the same magnitude as having the exact same effect on volatility", "It cannot be estimated using likelihood functions", "It allows the conditional variance to become negative"],
                "correct": 1,
                "explanation": "Standard ARCH uses squared residuals — it cannot distinguish between positive and negative shocks of equal magnitude."
            },
            {
                "question": "What is the Lagrange Multiplier (LM) Test specifically used to detect in time series analysis?",
                "options": ["Unit roots and non-stationarity", "Conditional heteroskedasticity (ARCH effects)", "Deterministic seasonality", "The correct moving average order"],
                "correct": 1,
                "explanation": "Engle's LM test detects ARCH effects by testing whether squared residuals are autocorrelated."
            },
            {
                "question": "What is the first step when conducting the Engle's ARCH (LM) Test?",
                "options": ["Fit the mean equation (e.g., ARMA) to the returns to get the residuals", "Take the square root of the entire dataset", "Calculate the Ljung-Box Q statistic", "Regress the raw data on its future values"],
                "correct": 0,
                "explanation": "Step 1: fit the mean model to obtain residuals, which are then tested for ARCH effects."
            },
            {
                "question": "In the LM Test, which variable is regressed against its own lagged values?",
                "options": ["The original log returns", "The raw residuals", "The squared residuals", "The moving average coefficients"],
                "correct": 2,
                "explanation": "The LM test regresses squared residuals on their own lags — significant coefficients indicate ARCH effects."
            },
            {
                "question": "What does the null hypothesis of the LM (ARCH) test state?",
                "options": ["There is infinite variance in the series", "The data has a unit root", "There are no ARCH effects (no conditional heteroskedasticity)", "The model is suffering from multicollinearity"],
                "correct": 2,
                "explanation": "H₀: no ARCH effects (α₁ = α₂ = ... = αq = 0) — the conditional variance is constant."
            },
            {
                "question": "Before formal testing, which plot is highly useful for tentatively picking the optimal order for an ARCH model?",
                "options": ["The ACF plot of the raw data", "The Partial Autocorrelation Function (PACF) plot of the squared residuals", "The standard normal Q-Q plot", "The periodogram"],
                "correct": 1,
                "explanation": "The PACF of squared residuals reveals the lag structure of volatility dependence, helping identify the ARCH order."
            },
            {
                "question": "How are GARCH models practically applied in the field of Option Pricing?",
                "options": ["To completely eliminate risk from a portfolio", "To compute the implied volatility used in dynamic pricing frameworks like Black-Scholes", "To predict the exact future price of an option", "To convert options into bonds"],
                "correct": 1,
                "explanation": "GARCH provides time-varying volatility estimates that improve option pricing beyond constant-volatility assumptions."
            },
            {
                "question": "In risk management, what is Value-at-Risk (VaR)?",
                "options": ["An estimate of the maximum profit a bank can make in a year", "An estimate of the risk of portfolio loss over a certain time horizon, often computed using GARCH to account for time-varying volatility", "The absolute variance of a single stock", "The difference between the highest and lowest price of an asset"],
                "correct": 1,
                "explanation": "VaR estimates the maximum expected loss at a given confidence level — GARCH-based VaR accounts for changing volatility."
            },
            {
                "question": "How is Actuarial Modelling in the insurance sector benefited by volatility modeling?",
                "options": ["By modeling time-varying claims risk, such as catastrophe modeling for natural disasters", "By ensuring all clients pay the exact same premium", "By eliminating the need to pay out claims", "By forecasting daily hospital admissions"],
                "correct": 0,
                "explanation": "Volatility models help insurers capture time-varying risk in claims, especially for catastrophe events with clustered losses."
            },
            {
                "question": "What does the GJR-GARCH model specifically capture that standard GARCH models fail to address?",
                "options": ["The unconditional mean of the series", "Fractional differencing parameters", "Asymmetric effects, where bad news increases volatility differently (often more) than good news", "Cross-sectional correlations"],
                "correct": 2,
                "explanation": "GJR-GARCH adds an indicator variable for negative shocks, allowing different volatility responses to good vs. bad news."
            },
            {
                "question": "In the GJR-GARCH equation, what is the role of the indicator function I(εₜ₋₁ < 0)?",
                "options": ["It equals 1 if the previous residual is negative, triggering the asymmetric volatility impact", "It equals 1 if the previous variance is exactly zero", "It forces the model to ignore positive shocks entirely", "It converts the model into an exponential framework"],
                "correct": 0,
                "explanation": "The indicator function activates (=1) for negative shocks, adding an extra volatility impact — capturing the leverage effect."
            },
            {
                "question": "Which extension of the GARCH model applies the natural logarithm to the conditional variance to avoid requiring non-negativity constraints on parameters?",
                "options": ["GJR-GARCH", "ARMA-GARCH", "Threshold GARCH", "EGARCH"],
                "correct": 3,
                "explanation": "EGARCH models log(σ²ₜ), so σ²ₜ = exp(...) is always positive regardless of parameter signs — no non-negativity constraints needed."
            },
            {
                "question": "What is a key advantage of the EGARCH model?",
                "options": ["It only models the mean, ignoring variance", "It ensures the conditional variance is always positive without requiring non-negativity constraints on the parameters", "It is mathematically identical to a random walk", "It completely ignores the leverage effect"],
                "correct": 1,
                "explanation": "By modelling log-variance, EGARCH guarantees positive variance without constraining parameters to be non-negative."
            },
            {
                "question": "In an ARMA + GARCH hybrid model, what is the specific role of the ARMA component?",
                "options": ["To model the conditional variance", "To capture asymmetric leverage effects", "To model the conditional mean and capture serial correlation", "To test for unit roots"],
                "correct": 2,
                "explanation": "ARMA handles the conditional mean dynamics (autocorrelation in returns), while GARCH handles the conditional variance."
            },
            {
                "question": "In the same ARMA + GARCH hybrid model, what does the GARCH component capture?",
                "options": ["The secular trend", "Time-varying volatility", "Deterministic seasonality", "The overall intercept"],
                "correct": 1,
                "explanation": "The GARCH component models the time-varying conditional variance — how volatility evolves based on past shocks and variance."
            },
            {
                "question": "What mathematical term represents the conditional variance in the GARCH(r,s) variance equation?",
                "options": ["μ", "εₜ", "σ²ₜ", "yₜ"],
                "correct": 2,
                "explanation": "σ²ₜ is the conditional variance at time t — the central quantity modelled by the GARCH equation."
            },
            {
                "question": "Why does the standard ARCH model struggle with modeling large, isolated shocks?",
                "options": ["It overpredicts the volatility and is slow to respond to them", "It automatically deletes outliers from the dataset", "It converts them into a negative variance", "It assigns them a weight of zero"],
                "correct": 0,
                "explanation": "ARCH can overreact to large isolated shocks and maintain elevated volatility forecasts longer than warranted."
            },
            {
                "question": "What happens to the standard ARCH model's variance restrictions as the order q increases?",
                "options": ["They become completely irrelevant", "The non-negativity parameter restrictions become too restrictive to allow for complex volatility dynamics", "The variance is forced to equal 1", "The model perfectly captures asymmetric effects"],
                "correct": 1,
                "explanation": "High-order ARCH requires many non-negative parameters — the constraints become increasingly restrictive and hard to satisfy."
            },
            {
                "question": "Why is modeling time-varying variances and covariances considered crucial in modern economic theory?",
                "options": ["Because all data is perfectly stationary", "Due to the increasing role of risk and uncertainty considerations in financial markets", "To eliminate the need for forecasting", "Because the mean is entirely irrelevant to investors"],
                "correct": 1,
                "explanation": "Risk and uncertainty are central to asset pricing, portfolio allocation, and regulation — time-varying volatility models are essential."
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
        ],
        "additional_questions": [
            {
                "question": "What is the primary purpose of non-linear time series analysis?",
                "options": ["To completely eliminate volatility in financial data", "To extend traditional methods to account for systems where relationships between variables cannot be captured by linear models", "To convert non-stationary data into purely stationary data via integration", "To simplify models into a single constant mean"],
                "correct": 1,
                "explanation": "Nonlinear time series analysis handles complex dynamics that linear models (ARMA, etc.) cannot capture."
            },
            {
                "question": "Which characteristic of a non-linear process describes a situation where the statistical properties, such as mean or variance, change over time?",
                "options": ["Non-stationarity", "Complex Dynamics", "State Dependence", "Strict Stationarity"],
                "correct": 0,
                "explanation": "Non-stationarity means statistical properties (mean, variance) are time-dependent — a common feature of nonlinear processes."
            },
            {
                "question": "The Lorenz attractor is an example of which type of non-linear dynamical system?",
                "options": ["Deterministic chaos", "Threshold Autoregression", "Artificial Neural Network", "A strict random walk"],
                "correct": 0,
                "explanation": "The Lorenz attractor demonstrates deterministic chaos — sensitive dependence on initial conditions despite deterministic equations."
            },
            {
                "question": "In a Threshold Autoregressive (TAR) model, how are the dynamics defined?",
                "options": ["They operate identically across all time periods", "They operate differently above or below certain threshold levels", "They are purely determined by moving averages", "They decompose the series into sine and cosine waves"],
                "correct": 1,
                "explanation": "TAR models switch between different linear AR regimes depending on whether a threshold variable is above or below a threshold."
            },
            {
                "question": "How are 'Abrupt Transitions' in regime-switching models defined?",
                "options": ["Changes between regimes occur gradually over a long period", "Changes are entirely governed by hidden probabilities", "Changes between regimes are instantaneous when a threshold condition is met", "Changes only occur when the process is integrated"],
                "correct": 2,
                "explanation": "Abrupt transitions switch regimes instantly once the threshold variable crosses the threshold value — a discrete jump."
            },
            {
                "question": "Which of the following is a classic example of a model that uses abrupt transitions?",
                "options": ["Artificial Neural Networks (ANN)", "Smooth Transition Autoregressive (STAR) models", "Markov Switching Models", "Self-Exciting Threshold Autoregressive (SETAR) models"],
                "correct": 3,
                "explanation": "SETAR models switch abruptly between regimes when the lagged dependent variable crosses the threshold."
            },
            {
                "question": "In models with 'Smooth Transitions', how do the regime changes occur?",
                "options": ["Instantaneously when a threshold is crossed", "Gradually over a range of values of the threshold variable", "Completely randomly according to white noise", "They strictly follow a seasonal cycle"],
                "correct": 1,
                "explanation": "Smooth transitions use continuous functions (logistic, exponential) to gradually shift between regimes."
            },
            {
                "question": "Which model provides an example of 'Probabilistic Transitions'?",
                "options": ["Markov Switching Autoregressive (MSAR) models", "Moving Average (MA) models", "Threshold Autoregressive (TAR) models", "Simple linear regression"],
                "correct": 0,
                "explanation": "MSAR models switch regimes probabilistically — the current regime depends on transition probabilities, not a deterministic threshold."
            },
            {
                "question": "In a threshold-based regime model definition (e.g., Regime 1: y_{t-d} < γ), what does the parameter γ represent?",
                "options": ["The slope of the transition function", "The fractional difference", "The threshold value", "The overall mean of the series"],
                "correct": 2,
                "explanation": "γ is the threshold value — the critical level that determines which regime is active."
            },
            {
                "question": "What specific mathematical function is frequently used in a Smooth Transition Autoregressive (STAR) model to handle the transition?",
                "options": ["A step function", "A logistic or exponential transition function", "A discrete cosine transform", "A standard normal CDF"],
                "correct": 1,
                "explanation": "STAR models use logistic (LSTAR) or exponential (ESTAR) transition functions for smooth regime switching."
            },
            {
                "question": "What does the Markov transition matrix P contain?",
                "options": ["The threshold values for different regimes", "The moving average parameters", "The probability p_ij of transitioning from regime i to regime j", "The eigenvalues of the time series"],
                "correct": 2,
                "explanation": "The transition matrix P contains all pairwise transition probabilities between regimes — P[i,j] = P(Sₜ = j | Sₜ₋₁ = i)."
            },
            {
                "question": "Which of the following is considered a primary challenge of fitting Regime Models?",
                "options": ["They cannot be applied to economic data", "Threshold Estimation can be computationally intensive", "They guarantee underfitting of the data", "They only allow for a single regime"],
                "correct": 1,
                "explanation": "Threshold estimation often requires grid search or optimization over a non-smooth likelihood surface — computationally intensive."
            },
            {
                "question": "What issue arises in threshold estimation due to 'Boundary Issues'?",
                "options": ["There is too much data at the mean", "Sparse data near the threshold value can make estimation difficult", "The model becomes perfectly linear", "The variance drops to zero"],
                "correct": 1,
                "explanation": "Few observations near the threshold make it hard to precisely estimate the threshold value — a common practical challenge."
            },
            {
                "question": "In a Self-Exciting TAR (SETAR) model, what is used as the threshold variable?",
                "options": ["An external macroeconomic variable", "The difference or momentum (Δy_{t-d})", "A completely unobservable hidden state", "The time series itself (y_{t-d})"],
                "correct": 3,
                "explanation": "SETAR uses the series' own lagged value y_{t-d} as the threshold variable — hence 'self-exciting'."
            },
            {
                "question": "Which extension of the TAR model uses the difference or momentum (Δy_{t-d}) as the threshold variable?",
                "options": ["SETAR", "STAR", "MTAR", "GARCH"],
                "correct": 2,
                "explanation": "Momentum TAR (MTAR) uses the change Δy_{t-d} as the threshold variable instead of the level y_{t-d}."
            },
            {
                "question": "Why are Smooth Transition Autoregressive (STAR) models particularly useful in practical applications?",
                "options": ["They strictly enforce sudden, instantaneous jumps in data", "They are highly suitable for capturing dynamics like policy effects, economic cycles, or gradual climate changes", "They rely exclusively on hidden unobservable states", "They do not require any parameter estimation"],
                "correct": 1,
                "explanation": "STAR models capture gradual transitions between regimes — ideal for policy effects, business cycles, and other smooth shifts."
            },
            {
                "question": "In the transition function G(z_{t-d}; γ, c) of a STAR model, what does the parameter c represent?",
                "options": ["The slope parameter determining the smoothness", "The threshold value or the location of the transition", "The white noise error term", "The unconditional mean"],
                "correct": 1,
                "explanation": "c is the location parameter — the value around which the smooth transition is centered."
            },
            {
                "question": "What does 'State Dependence' mean in the context of nonlinear processes?",
                "options": ["The system is always strictly stationary", "The errors are perfectly normally distributed", "Current values might influence future values differently based on the state of the system", "The system relies solely on the overall trend"],
                "correct": 2,
                "explanation": "State dependence: the system's dynamics change depending on which state or regime it's currently in."
            },
            {
                "question": "How do Markov Switching Models differ fundamentally from TAR or SETAR models regarding regime changes?",
                "options": ["They do not allow for multiple regimes", "Regime changes depend on observable variables in MSMs", "They allow the regime to switch probabilistically based on an unobservable (latent) state variable", "They are purely deterministic"],
                "correct": 2,
                "explanation": "MSMs use latent (unobservable) states with probabilistic transitions, unlike TAR/SETAR which use observable threshold variables."
            },
            {
                "question": "In a Markov Switching Model, what does the 'first-order Markov process' assumption imply?",
                "options": ["The current regime depends on all past regimes equally", "The current regime depends only on the previous regime", "The current regime depends entirely on the future regime", "The regime never changes"],
                "correct": 1,
                "explanation": "First-order Markov: P(Sₜ | Sₜ₋₁, Sₜ₋₂, ...) = P(Sₜ | Sₜ₋₁) — only the immediately previous regime matters."
            },
            {
                "question": "In the simple MS-AR model formulation, what does Sₜ represent?",
                "options": ["The latent state (regime) at time t", "The standard deviation of the error term", "The seasonal component", "The fractionally integrated parameter"],
                "correct": 0,
                "explanation": "Sₜ is the latent (hidden) state variable indicating which regime is active at time t."
            },
            {
                "question": "Which extension models output as a nonlinear function of past inputs and outputs (e.g., yₜ = f(yₜ₋₁, xₜ₋₁) + eₜ)?",
                "options": ["Simple Exponential Smoothing", "Nonlinear ARX Models", "Linear Filter Models", "Integrated Moving Averages"],
                "correct": 1,
                "explanation": "Nonlinear ARX (AutoRegressive with eXogenous inputs) models allow the relationship to be a nonlinear function of past values."
            },
            {
                "question": "Which type of neural network is specifically noted for handling sequential dependencies and long-term memory in nonlinear time series?",
                "options": ["Feedforward Neural Network", "Convolutional Neural Network", "Long Short-Term Memory (LSTM)", "Multi-Layer Perceptron"],
                "correct": 2,
                "explanation": "LSTMs use gating mechanisms to selectively remember or forget information, capturing long-range temporal dependencies."
            },
            {
                "question": "What does the Smooth Transition GARCH (ST-GARCH) model capture?",
                "options": ["Constant volatility", "Regime switching in the variance equation", "Deterministic linear trends", "Cross-sectional covariance"],
                "correct": 1,
                "explanation": "ST-GARCH allows the volatility equation parameters to smoothly transition between regimes — capturing regime-dependent variance."
            },
            {
                "question": "Which model is specifically useful for high-dimensional or infinite-dimensional time series data, modeling temporal changes in curves or functions?",
                "options": ["Functional Time Series", "Basic AR(1) Model", "Simple Moving Average", "Random Walk"],
                "correct": 0,
                "explanation": "Functional Time Series models treat each observation as a curve or function, handling infinite-dimensional data over time."
            },
            {
                "question": "What is a primary use of Wavelet Transform Models in nonlinear time series?",
                "options": ["To find the median of the data", "To convert the time series into a single categorical variable", "To decompose a time series into different frequency components to identify nonlinear periodic patterns", "To strictly enforce homoscedasticity"],
                "correct": 2,
                "explanation": "Wavelets provide time-frequency decomposition, revealing nonlinear periodic patterns at multiple scales simultaneously."
            },
            {
                "question": "What is a specific advantage of SETAR models regarding interpretation?",
                "options": ["They provide a single overarching linear equation", "Their piecewise linear structure is easy to understand and interpret, offering specific insights for different regimes", "They are identical to continuous random walks", "They ignore all historical data"],
                "correct": 1,
                "explanation": "SETAR's piecewise linear structure means each regime has a simple AR equation — easy to interpret within each regime."
            },
            {
                "question": "Which extension of the SETAR model smooths the regime transition using continuous functions?",
                "options": ["MTAR", "Seasonal SETAR", "CSETAR (Continuous SETAR)", "Multiple Threshold SETAR"],
                "correct": 2,
                "explanation": "CSETAR replaces the abrupt threshold switch with a continuous transition function, smoothing the regime change."
            },
            {
                "question": "What statistical test is commonly used to confirm the presence of regime switching or nonlinearity when diagnosing SETAR models?",
                "options": ["Augmented Dickey-Fuller Test", "Hansen's test", "Ljung-Box Test", "Jarque-Bera Test"],
                "correct": 1,
                "explanation": "Hansen's test is designed to test for threshold effects and regime switching in autoregressive models."
            },
            {
                "question": "Which model captures switching dynamics in time series using discrete latent states without explicitly requiring an autoregressive structure?",
                "options": ["Hidden Markov Models (HMMs)", "Standard ARIMA", "Holt-Winters Smoothing", "Linear Regression"],
                "correct": 0,
                "explanation": "HMMs model switching between hidden discrete states with observation distributions — no explicit AR structure required."
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
        ],
        "additional_questions": [
            {
                "question": "Why have machine learning models gained popularity in time series analysis?",
                "options": ["They completely eliminate the need for data preprocessing", "Because of their flexibility and ability to capture complex patterns", "They require significantly less data than classical models", "They are the only models capable of handling stationary data"],
                "correct": 1,
                "explanation": "ML models are popular due to their flexibility in capturing complex, nonlinear patterns that classical methods may miss."
            },
            {
                "question": "Which classical ML model is primarily used for forecasting when the relationship between the dependent variable and its lagged variables is linear?",
                "options": ["Random Forests", "Support Vector Machines (SVMs)", "Linear Regression", "k-Means Clustering"],
                "correct": 2,
                "explanation": "Linear Regression is the go-to model when the target has a linear relationship with its lagged predictors."
            },
            {
                "question": "Which neural network architecture is particularly effective for capturing long-term dependencies in sequential data?",
                "options": ["Perceptron", "Long Short-Term Memory (LSTMs)", "Naïve Bayes", "Linear Regression"],
                "correct": 1,
                "explanation": "LSTMs use memory cells and gating mechanisms specifically designed to capture long-term dependencies in sequences."
            },
            {
                "question": "What is a recognized simpler alternative to LSTMs that offers comparable performance in many cases?",
                "options": ["Convolutional Neural Networks (CNNs)", "Gated Recurrent Units (GRUs)", "Support Vector Machines", "Random Forests"],
                "correct": 1,
                "explanation": "GRUs simplify the LSTM architecture with fewer gates while often achieving comparable performance on sequential tasks."
            },
            {
                "question": "What is a major advantage of using classical machine learning models (like Decision Trees or Linear Regression)?",
                "options": ["They never require stationary data", "Speed and interpretability", "They automatically generate their own features without feature engineering", "They are best suited for deep image processing"],
                "correct": 1,
                "explanation": "Classical ML models are fast to train and produce interpretable results — key advantages over complex deep learning models."
            },
            {
                "question": "Which of the following is a key challenge when applying classical ML models to time series?",
                "options": ["They are entirely black-box models", "They rely heavily on the quality of feature engineering", "They cannot be applied to classification tasks", "They only work on datasets with fewer than 100 observations"],
                "correct": 1,
                "explanation": "Classical ML models require manual feature engineering (lags, rolling stats, etc.) — their performance depends heavily on feature quality."
            },
            {
                "question": "How is a univariate time series typically converted into a supervised learning problem for classical ML models?",
                "options": ["By creating lagged versions of the target variable to use as predictors", "By applying a strict random walk transformation", "By taking the natural logarithm of the entire dataset", "By permanently removing all seasonal data"],
                "correct": 0,
                "explanation": "Lagged values of the target become input features, transforming the time series into a tabular supervised learning problem."
            },
            {
                "question": "In feature engineering, what does using 'Rolling Statistics' involve?",
                "options": ["Encoding day-of-week information as dummy variables", "Creating moving averages or rolling standard deviations as predictors (e.g., using the average of the past 7 days)", "Converting all data into strict categorical bins", "Taking the second difference of the time series"],
                "correct": 1,
                "explanation": "Rolling statistics (moving averages, rolling std) capture local trends and volatility as engineered features."
            },
            {
                "question": "How are seasonality indicators typically incorporated into a machine learning feature set?",
                "options": ["By smoothing them out completely using a Bartlett kernel", "By encoding them as dummy variables (e.g., day-of-week, month, or holiday)", "By taking the fractional derivative", "By treating them as the target variable"],
                "correct": 1,
                "explanation": "Seasonal patterns are encoded as dummy/indicator variables — day-of-week, month, quarter, holiday flags, etc."
            },
            {
                "question": "What is a specific limitation of using Linear Regression for time series forecasting?",
                "options": ["It is computationally expensive", "It cannot capture any trends whatsoever", "It is highly sensitive to multicollinearity between features, such as overlapping lags", "It completely fails at tracking simple moving averages"],
                "correct": 2,
                "explanation": "Lagged variables are often highly correlated (multicollinear), which destabilizes Linear Regression coefficient estimates."
            },
            {
                "question": "In the context of Random Forests, what does the hyperparameter max_depth control?",
                "options": ["The number of trees in the forest", "The depth of each individual tree to prevent overfitting", "The learning rate of the gradient booster", "The number of lagged variables to create"],
                "correct": 1,
                "explanation": "max_depth limits how deep each tree can grow — shallower trees prevent overfitting but may underfit."
            },
            {
                "question": "What does the n_estimators hyperparameter determine in a Random Forest model?",
                "options": ["The total number of features evaluated at each split", "The total number of trees, where more trees improve robustness but increase training time", "The smoothing bandwidth of the series", "The maximum prediction horizon"],
                "correct": 1,
                "explanation": "n_estimators sets the number of trees — more trees generally improve stability but increase computation time."
            },
            {
                "question": "What is a known limitation of Random Forest models when forecasting time series?",
                "options": ["They cannot handle non-linear relationships", "They struggle with extrapolation, such as forecasting values outside the range of the training data", "They are highly susceptible to multicollinearity", "They require data to be perfectly normally distributed"],
                "correct": 1,
                "explanation": "Random Forests predict within the range of training data — they cannot extrapolate trends beyond observed values."
            },
            {
                "question": "In a comparative analysis, which algorithm offers 'Excellent' handling of non-linearity but has a 'High' computational cost and 'Poor' handling of large data?",
                "options": ["Linear Regression", "Random Forests", "Support Vector Machines (SVM / SVR)", "k-Means"],
                "correct": 2,
                "explanation": "SVMs excel at nonlinear patterns (via kernels) but scale poorly to large datasets due to high computational cost."
            },
            {
                "question": "To apply the k-Nearest Neighbors (k-NN) algorithm to a time series, how is similarity typically calculated between segments?",
                "options": ["Using the Ljung-Box Q statistic", "Using Euclidean distance, treating each time step as a vector in p-dimensional space", "By checking the Augmented Dickey-Fuller p-value", "Using the spectral density function"],
                "correct": 1,
                "explanation": "k-NN uses Euclidean distance (or similar metrics) to find the most similar historical patterns in the feature space."
            },
            {
                "question": "In k-NN regression, how is the output for a given test point computed?",
                "options": ["By finding the absolute maximum value among the nearest neighbors", "By taking the average of the k nearest neighbors", "By taking the majority class vote", "By fitting a linear trend line through the neighbors"],
                "correct": 1,
                "explanation": "k-NN regression averages the target values of the k nearest neighbors to produce the forecast."
            },
            {
                "question": "What type of machine learning algorithm is k-Means clustering?",
                "options": ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Semi-supervised learning"],
                "correct": 1,
                "explanation": "k-Means is unsupervised — it groups data into clusters without requiring labeled target variables."
            },
            {
                "question": "How can k-Means clustering be utilized for anomaly detection in time series?",
                "options": ["By forcing all anomalies into a single, pre-defined cluster", "By identifying clusters and spotting series or segments that do not fit any cluster well (outliers)", "By averaging out the anomalies across all clusters", "It cannot be used for anomaly detection"],
                "correct": 1,
                "explanation": "Points far from all cluster centers are potential anomalies — k-Means naturally identifies outliers that don't belong."
            },
            {
                "question": "Which probabilistic classifier is based on the assumption that features (like lagged values) are conditionally independent given the class label?",
                "options": ["Random Forests", "k-Nearest Neighbors", "Naïve Bayes", "Support Vector Machines"],
                "correct": 2,
                "explanation": "Naïve Bayes assumes conditional independence between features — a strong assumption that simplifies computation."
            },
            {
                "question": "What is a major limitation of Naïve Bayes when applied to time series data?",
                "options": ["It assumes independence among features, which is rarely true in time series", "It takes an exceptionally long time to train", "It requires perfectly continuous data and cannot handle categorical features", "It strictly overfits on small datasets"],
                "correct": 0,
                "explanation": "Time series features (lags) are inherently correlated — violating Naïve Bayes' independence assumption."
            },
            {
                "question": "Artificial neural networks are fundamentally based on:",
                "options": ["Purely deterministic chaos equations", "Simple mathematical models of the brain", "Box-Jenkins ARMA methodology", "Fractional integration calculus"],
                "correct": 1,
                "explanation": "Neural networks are inspired by biological neurons — simplified mathematical models of how the brain processes information."
            },
            {
                "question": "In a neural network architecture, the predictors (or inputs) generally form which part of the network?",
                "options": ["The top layer", "The hidden intermediate layers", "The bottom layer", "The activation function"],
                "correct": 2,
                "explanation": "Inputs (predictors) form the bottom (input) layer — data flows upward through hidden layers to the output."
            },
            {
                "question": "What forms the top layer of a basic neural network architecture for forecasting?",
                "options": ["The input predictors", "The forecasts or outputs", "The hidden neurons", "The loss function"],
                "correct": 1,
                "explanation": "The top (output) layer produces the forecasts or predictions — the final result of the forward pass."
            },
            {
                "question": "In the provided diagram of a basic node (the 'Perceptron'), what does the node do after summing the weighted inputs?",
                "options": ["It instantly outputs the exact sum", "It differences the data", "It passes the sum through an Activation Function to generate the final output", "It passes the sum back to the inputs to create a loop"],
                "correct": 2,
                "explanation": "The perceptron sums weighted inputs, then applies an activation function to introduce nonlinearity before outputting."
            },
            {
                "question": "Why is a standard perceptron network referred to as a 'feed forward' network?",
                "options": ["Because signals flow in multiple directions simultaneously", "Because it strictly feeds historical errors backward to update weights", "Because the network of nodes sends signals in only one direction", "Because it ignores all historical data"],
                "correct": 2,
                "explanation": "Feed-forward: signals flow strictly from input → hidden → output layers, with no backward connections during inference."
            },
            {
                "question": "In the R programming example provided in the materials, which test was conducted on the exchange rate series to check for stationarity?",
                "options": ["Ljung-Box Test", "Augmented Dickey-Fuller Test", "KPSS Test", "Shapiro-Wilk Test"],
                "correct": 1,
                "explanation": "The ADF test was used to check for unit roots — a standard stationarity test before modeling."
            },
            {
                "question": "In the R practical application example, after the USD/INR exchange rate data was differenced, what was the resulting p-value of the Augmented Dickey-Fuller test?",
                "options": ["0.2578", "1.00", "0.01", "0.05"],
                "correct": 2,
                "explanation": "After differencing, the ADF p-value dropped to 0.01 — strong evidence of stationarity, confirming differencing worked."
            },
            {
                "question": "Which of the following models combines the strengths of decision trees but reduces overfitting by training on different subsets of data?",
                "options": ["Linear Regression", "Naïve Bayes", "Random Forests", "GRUs"],
                "correct": 2,
                "explanation": "Random Forests ensemble many decision trees trained on bootstrapped subsets, reducing variance and overfitting."
            },
            {
                "question": "What type of problems are Neural Networks especially adept at solving compared to simple Linear Regression?",
                "options": ["Capturing strictly linear seasonal dummy variables", "Calculating simple historical averages", "Capturing complex non-linear relationships between the response variable and predictors", "Providing highly interpretable baseline coefficients"],
                "correct": 2,
                "explanation": "Neural networks excel at learning complex nonlinear mappings — far beyond what linear regression can capture."
            },
            {
                "question": "Which of the following is true regarding classical ML models and Data Stationarity?",
                "options": ["They easily handle raw, non-stationary data out-of-the-box", "Many models assume the data is stationary, requiring preprocessing steps like differencing before training", "Non-stationarity actually improves the speed of k-NN", "Classical models automatically convert non-stationary data into fractional integrals"],
                "correct": 1,
                "explanation": "Most classical ML models assume stationary features — non-stationary data must be differenced or detrended first."
            }
        ]
    }
}
