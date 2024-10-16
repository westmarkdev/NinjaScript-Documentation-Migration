---
title: "Aroon"
pathName: /docs/desktop/aroon
---

## Description

Developed by Tushar Chande in 1995, Aroon is an indicator system that can be used to determine whether a stock is trending or not and how strong the trend is. "Aroon" means "Dawn's Early Light" in Sanskrit and Chande chose that name for this indicator since it is designed to reveal the beginning of a new trend.

The Aroon indicator system consists of two lines, 'Aroon(up)' and 'Aroon(down)'. It takes a single parameter which is the number of time periods to use in the calculation. Aroon(up) is the amount of time (on a percentage basis) that has elapsed between the start of the time period and the point at which the highest price during that time period occurred. If the stock closes at a new high for the given period, Aroon(up) will be +100. For each subsequent period that passes without another new high, Aroon(up) moves down by an amount equal to (1 / # of periods) x 100.

## Syntax

```csharp
Aroon(int period)  
Aroon(ISeries<double> input, int period)  
```

Returns up value

```csharp
Aroon(int period).Up[int barsAgo]  
Aroon(ISeries<double> input, int period).Up[int barsAgo]  
```

Returns down value

```csharp
Aroon(int period).Down[int barsAgo]  
Aroon(ISeries<double> input, int period).Down[int barsAgo]  
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|                       |                                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| input                 | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period                | Number of bars used in the calculation                                          |

## Examples

```csharp
// Prints the current up/down values of a 20 period Aroon indicator
double upValue = Aroon(20).Up[0];  
double downValue = Aroon(20).Down[0];  
Print("The current Aroon up value is " + upValue);  
Print("The current Aroon down value is " + downValue);  
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
