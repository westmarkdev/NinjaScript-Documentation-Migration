---
title: "Maximum (MAX)"
pathName: /docs/desktop/maximum_max
---

## Description

Returns the highest value over the specified period.

## Syntax

```csharp
MAX(int period)
```

```csharp
MAX(ISeries<double> input, int period)
```

```csharp
// Returns default value
MAX(int period)[int barsAgo]
```

```csharp
MAX(ISeries<double> input, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([valid input data for indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Example

```csharp
// Prints the highest high value over the last 20 periods
double value = MAX(High, 20)[0];
Print("The current MAX value is " + value.ToString());
// Note the above call with a barsAgo of 0 includes the current MAX of the input high series in the value. If we want to check for example for a break of this value, storing the last bar's MAX would be needed.
double value = MAX(High, 20)[1];
if (High[0] > value)
    Draw.ArrowUp(this, CurrentBar.ToString(), true, 0, Low[0] - TickSize, Brushes.Blue);
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

