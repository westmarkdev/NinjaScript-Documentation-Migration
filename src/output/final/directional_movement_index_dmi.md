---
title: "Directional Movement Index (DMI)"
pathName: /docs/desktop/directional_movement_index_dmi
---

## Description

An indicator developed by J. Welles Wilder for identifying when a definable trend is present in an instrument. That is, the DMI tells whether an instrument is trending or not.

{% callout type="note" %}
Courtesy of [FMLabs](/docs/desktop/http://www.fmlabs.com/reference/default.htm?url=DX)
{% /callout %}

## Syntax

```csharp
DMI(int period)
DMI(ISeries<double> input, int period)

Returns default value
DMI(int period)[int barsAgo]
DMI(ISeries<double> input, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `int barsAgo` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Example

```csharp
// Prints the current value of a 20 period DMI using default price type
double value = DMI(20)[0];
Print("The current DMI value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

