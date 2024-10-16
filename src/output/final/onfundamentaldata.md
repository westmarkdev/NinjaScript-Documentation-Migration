---
title: "OnFundamentalData()"
pathName: /docs/desktop/onfundamentaldata
---

## Definition

An event driven method which is called for every change in fundamental data for the underlying instrument.

{% callout type="note" %}
This method is NOT called on historical data (backtest)
{% /callout %}

## Method Return Value

This method does not return a value.

### Syntax

```csharp
// You must override the method in your strategy or indicator with the following syntax.
protected override void OnFundamentalData(FundamentalDataEventArgs fundamentalDataUpdate)
{
}
```

{% callout type="tip" %}
The NinjaScript code wizards can automatically generate the method syntax for you when creating a new script.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| fundamentalDataUpdate | [FundamentalDataEventArgs](/docs/desktop/fundamentaldataeventargs) representing the recent change in fundamental data |

## Examples

```csharp
protected override void OnFundamentalData(FundamentalDataEventArgs fundamentalDataUpdate)
{
    // Print some data to the Output window
    if (fundamentalDataUpdate.FundamentalDataType == FundamentalDataType.AverageDailyVolume)
        Print("The current ADV is " + fundamentalDataUpdate.LongValue);
}
```

{% callout type="tip" %}

1. With [multi-time frame and instrument strategies](/docs/desktop/multi-time_frame__instruments), OnFundamentalData() will be called for all unique instruments in your strategy. Use the [BarsInProgress](/docs/desktop/barsinprogress) to filter the OnFundamentalData() method for a specific instrument.

2. Do not leave an unused OnFundamentalData() method declared in your NinjaScript object. This will unnecessarily attach a data stream to your script which uses unnecessary CPU cycles.
{% /callout %}
