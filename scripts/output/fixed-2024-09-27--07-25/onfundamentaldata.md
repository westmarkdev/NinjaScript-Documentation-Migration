---
path: onfundamentaldata
title: OnFundamentalData()
---

## Definition

An event driven method which is called for every change in fundamental data for the underlying instrument.

{% callout type="note" %}
This method is NOT called on historical data (backtest)

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

`## You must override the method in your strategy or indicator with the following syntax.`

protected override void OnFundamentalData(FundamentalDataEventArgs fundamentalDataUpdate)

{

}

{% callout type="note" %}
The NinjaScript code wizards can automatically generate the method syntax for you when creating a new script.

{% /callout %}

## Parameters

|  |  |
| --- | --- |
| fundamentalDataUpdate | [FundamentalDataEventArgs](fundamentaldataeventargs.md) representing the recent change in fundamental data |

## Examples

```csharp
protected override void OnFundamentalData(FundamentalDataEventArgs fundamentalDataUpdate)
{
// Print some data to the Output window
if (fundamentalDataUpdate.FundamentalDataType == FundamentalDataType.AverageDailyVolume)
Print("The current ADV is " + fundamentalDataUpdate.LongValue);
}
```  |
| --- |
| Tips
1.With [multi-time frame and instrument strategies](multi-time_frame__instruments.md), OnFundamentalData() will be called for all unique instruments in your strategy. Use the [BarsInProgress](barsinprogress.md) to filter the OnFundamentalData() method for a specific instrument. 2.Do not leave an unused OnFundamentalData() method declared in your NinjaScript object. This will unnecessarily attach a data stream to your script which uses unnecessary CPU cycles. |