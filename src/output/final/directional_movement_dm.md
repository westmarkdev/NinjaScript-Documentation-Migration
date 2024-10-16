---
title: "Directional Movement (DM)"
pathName: /docs/desktop/directional_movement_dm
---

## Description

Same as the [ADX](/docs/desktop/average_directional_index_adx) indicator with the addition of the +DI and -DI values.

... Courtesy of [Investopedia](http://www.investopedia.com/terms/d/dmi.asp)

## Syntax

```csharp
DM(int period)
DM(ISeries<double> input, int period)
```

Returns default ADX value

```csharp
DM(int period)[int barsAgo]
DM(ISeries<double> input, int period)[int barsAgo]
```

Returns +DI value

```csharp
DM(int period).DiPlus[int barsAgo]
DM(ISeries<double> input, int period).DiPlus[int barsAgo]
```

Returns -DI value

```csharp
DM(int period).DiMinus[int barsAgo]
DM(ISeries<double> input, int period).DiMinus[int barsAgo]
```

## Return Value

double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Example

```csharp
// Prints the current value of a 20 period +DI using default price type
double value = DM(20).DiPlus[0];
Print("The current +DI value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

