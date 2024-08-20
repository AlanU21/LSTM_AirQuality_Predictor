# Real-Time Air Quality Forecasting Using LSTM Networks

## Overview

This project implements Long Short-Term Memory (LSTM) networks to forecast particulate matter concentrations (PM2.5 and PM10) in real-time within urban environments, focusing on Philadelphia. The project utilizes time-series data from OpenAQ and OpenWeatherMap, spanning a full year, to predict air quality for 24-hour and 2-hour intervals.

## Motivation

Air quality is a critical public health concern, especially in urban areas. Poor air quality can exacerbate respiratory conditions such as asthma, which I personally struggled with growing up. This project was driven by my desire to develop predictive models that can offer real-time insights into air quality, potentially improving public health responses and policy-making. 

## Technical Details

### Data Collection
- **Sources:** OpenAQ API for air quality data, OpenWeatherMap for weather data.
- **Duration:** Data was collected from January 1st, 2023 to January 1st, 2024.
- **Challenges:** API rate limitations and computational constraints were mitigated by preprocessing the data and purchasing a historical weather dataset.

### Data Preprocessing
- **Techniques:** 
  - Standardized timestamps to pandas DateTime format.
  - Calculated rolling 24-hour averages and lagged features for PM2.5 and PM10.
  - Linearly imputed missing values and normalized the dataset for LSTM compatibility.

### Model Development
- **Tools:** TensorFlow and Keras libraries.
- **Models:** 
  - **24-hour Forecast Model:** Used previous two weeks of data to predict the next 24 hours of PM2.5 and PM10 levels.
  - **2-hour Forecast Model:** Used the previous 24 hours of data to predict the next 2 hours of PM2.5 and PM10 levels.

### Evaluation
- **Metrics:** Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R²).
- **Performance:**
  - **24-hour Model:** R² = -1.02327 for PM2.5, -0.09490 for PM10.
  - **2-hour Model:** R² = 0.89342 for PM2.5, 0.88467 for PM10.

### Visualization
- Predictive accuracy and error distributions were visualized to provide insights into model performance, with detailed graphs showing predicted vs. actual pollutant levels.
- [Supplemental Materials](https://drive.google.com/drive/folders/151-WWf5C82rLwERKpVuNiTN5zYRlnObF?usp=drive_link)

## Results

The 24-hour forecast model struggled with accuracy, highlighting the challenges of long-term air quality predictions in dynamic urban environments. In contrast, the 2-hour forecast model performed significantly better, capturing short-term changes in air quality with high accuracy. This discrepancy highlights the necessity of incorporating more complex features, such as traffic and industrial emissions data, for better predictions.

## Future Work

Future research could explore hybrid models that integrate LSTM with convolutional neural networks for processing spatial features. Additionally, implementing ensemble methods could enhance model robustness and generalization.
