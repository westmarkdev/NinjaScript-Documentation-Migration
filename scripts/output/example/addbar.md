---
title: addbar
path: addbar
created: Thursday, October 3rd 2024, 11:49:40 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

Adds new data points for the Bars Type.

## Syntax

You can use the following syntaxes to call the `AddBar` method:

```csharp
AddBar(Bars bars, double open, double high, double low, double close, DateTime time, long volume)

AddBar(Bars bars, double open, double high, double low, double close, DateTime time, long volume, double bid, double ask)
```

## Parameters

| Parameter | Description |
| --- | --- |
| bars | The Bars object of your bars type |
| open | A double value representing the open price |
| high | A double value representing the high price |
| low | A double value representing the low price |
| close | A double value representing the close price |
| time | A DateTime value representing the time |
| volume | A long value representing the volume |
| bid | A double value representing the bid price |
| ask | A double value representing the ask price |

## Examples

```csharp
AddBar(bars, open, high, low, close, time, (long)Math.Min(volumeTmp, bars.BarsPeriod.Value));
```

{% callout type="note" %}  
The initial setup for NinjaScript can be completed using the appropriate NinjaScript methods that allow data manipulation. Ensure to handle different scenarios based on your coding requirements.  
{% /callout %}
