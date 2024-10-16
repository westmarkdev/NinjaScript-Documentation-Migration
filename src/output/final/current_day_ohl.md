---
title: "Current Day OHL"
pathName: /docs/desktop/current_day_ohl
---

## Description

The current day (session) open, high and low values.

{% callout type="note" %}
Only use this indicator on intraday series.
{% /callout %}

## Syntax

```csharp
CurrentDayOHL()
CurrentDayOHL(ISeries<double> input)
```

Returns current session open value

```csharp
CurrentDayOHL().CurrentOpen[int barsAgo]
CurrentDayOHL(ISeries<double> input).CurrentOpen[int barsAgo]
```

Returns current session high value

```csharp
CurrentDayOHL().CurrentHigh[int barsAgo]
CurrentDayOHL(ISeries<double> input).CurrentHigh[int barsAgo]
```

Returns current session low value

```csharp
CurrentDayOHL().CurrentLow[int barsAgo]
CurrentDayOHL(ISeries<double> input).CurrentLow[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |

## Example

```csharp
// Prints the current value of the session low
double value = CurrentDayOHL().CurrentLow[0];
Print("The current session low value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
