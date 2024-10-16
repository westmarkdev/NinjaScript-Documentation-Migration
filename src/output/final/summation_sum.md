---
title: "Summation (SUM)"
pathName: /docs/desktop/summation_sum
---

## Description

Returns the sum of the values taken over a specified period.

## Syntax

```csharp
SUM(int period)
```

```csharp
SUM(ISeries<double> input, int period)
```

Returns default value.

```csharp
SUM(int period)[int barsAgo]
```

```csharp
SUM(ISeries<double> input, int period)[int barsAgo]
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
// Prints the current value of a 20 period SUM using default price type
double value = SUM(20)[0];
Print("The current SUM value is " + value.ToString());
// Prints the current value of a 20 period SUM using high price type
double value = SUM(High, 20)[0];
Print("The current SUM value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
