---
title: IsResetOnNewTradingDays
pathName: isresetonnewtradingdays
parent: onbarupdate
section: references
status: review
---

## Definition

Determines if the specified bar series iusing Break at EOD

{% callout type="note" %}

The property available on the UI will override any values set in code. Please see the help guide topic on using **Break at EOD** for more information.

{% /callout %}

## Property Value

A **bool[]** when true, indicates the specified [BarsArray](barsarray) is setup to run Break at EOD; otherwise false. Default value is false.

## Syntax

**IsResetOnNewTradingDays**[int idx]

{% callout type="warning" %}

This property should NOT be accessed within the [OnStateChange()](onstatechange) method before the State has reached State.DataLoaded.

{% /callout %}

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";
   }

   else if (State == State.Configure)
   {
     //Add AAPL 1 minute with RTH trading hours, set to break EOD
     AddDataSeries("AAPL", new BarsPeriod() { BarsPeriodType = BarsPeriodType.Minute, Value = 1 }, 50, "US Equities RTH", true);
   }

}
protected override void OnBarUpdate()
{
 //Print out the current bars series name and break EOD setting on start up
 //   IsResetOnNewTradingDays[0]  Primary
 //   IsResetOnNewTradingDays[1]  AAPL

 if (CurrentBar == 0)
   Print(BarsArray[BarsInProgress].ToChartString() + " " + IsResetOnNewTradingDays[BarsInProgress]);

 //Output:  
 //ES 03-15 (1 Minute) True
 //AAPL (1 Minute) False
```
