---
title: "Prior Day OHLC"
pathName: /docs/desktop/prior_day_ohlc
---

## Description

The prior day (session) open, high, low, and close values.

{% callout type="note" %}
Only use this indicator on intraday series.
{% /callout %}

## Syntax

```csharp
PriorDayOHLC()
PriorDayOHLC(ISeries<double> input)
```

Returns prior session open value

```csharp
PriorDayOHLC().PriorOpen[int barsAgo]
PriorDayOHLC(ISeries<double> input).PriorOpen[int barsAgo]
```

Returns prior session high value

```csharp
PriorDayOHLC().PriorHigh[int barsAgo]
PriorDayOHLC(ISeries<double> input).PriorHigh[int barsAgo]
```

Returns prior session low value

```csharp
PriorDayOHLC().PriorLow[int barsAgo]
PriorDayOHLC(ISeries<double> input).PriorLow[int barsAgo]
```

Returns prior session close value

```csharp
PriorDayOHLC().PriorClose[int barsAgo]
PriorDayOHLC(ISeries<double> input).PriorClose[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Input Data](/docs/desktop/valid_input_data_for_indicator)) |

## Example

```csharp
// Prints the value of the prior session low
double value = PriorDayOHLC().PriorLow[0];
Print("The prior session low value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
