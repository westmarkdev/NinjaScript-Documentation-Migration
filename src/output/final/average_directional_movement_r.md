---
title: "Average Directional Movement Rating (ADXR)"
pathName: /docs/desktop/average_directional_movement_r
---

## Description

The ADXR is equal to the current [ADX](/docs/desktop/average_directional_index_adx) plus the ADX from n bars ago divided by two.

## Syntax

```csharp
ADXR(int interval, int period)
ADXR(ISeries<double> input, int interval, int period)
```

Returns default value

```csharp
ADXR(int interval, int period)[int barsAgo]
ADXR(ISeries<double> input, int interval, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([?](/docs/desktop/valid_input_data_for_indicator)) |
| interval | The interval between the first ADX value and the current ADX value |
| period | Number of bars used in the calculation |

## Example

```csharp
// Prints the current value of a 20 period ADXR using default price type
double value = ADXR(10, 20)[0];
Print("The current ADXR value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

