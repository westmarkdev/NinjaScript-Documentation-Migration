---
title: "Linear Regression"
pathName: /docs/desktop/linear_regression
---

## Description

The Linear Regression Indicator plots the trend of a security's price over time. That trend is determined by calculating a Linear Regression Trendline using the least squares method. This ensures the minimum distance between the data points and a Linear Regression Trendline.

## Syntax

```csharp
LinReg(int period)  
LinReg(ISeries<double> input, int period)  

Returns default value  
LinReg(int period)[int barsAgo]  
LinReg(ISeries<double> input, int period)[int barsAgo]  
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Examples

```csharp
// Prints the current value of a 20 period LinReg using default price type
double value = LinReg(20)[0];
Print("The current LinReg value is " + value.ToString());
// Prints the current value of a 20 period LinReg using high price type
double value = LinReg(High, 20)[0];
Print("The current LinReg value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
