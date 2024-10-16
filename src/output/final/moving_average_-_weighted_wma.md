---
title: "Moving Average - Weighted (WMA)"
pathName: /docs/desktop/moving_average_-_weighted_wma
---

## Description

The Weighted Moving Average gives the latest price more weight than prior prices. Each prior price in the period gets progressively less weight as they become older.

## Syntax

```csharp
WMA(int period)
```

```csharp
WMA(ISeries<double> input, int period)
```

```csharp
WMA(int period)[int barsAgo]
```

```csharp
WMA(ISeries<double> input, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Examples

```csharp
// Prints the current value of a 20 period WMA using default price type
double value = WMA(20)[0];
Print("The current WMA value is " + value.ToString());
// Prints the current value of a 20 period WMA using high price type
double value = WMA(High, 20)[0];
Print("The current WMA value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

