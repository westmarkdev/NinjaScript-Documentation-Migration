---
title: CurrentBars
pathName: currentbars
parent: common
section: references
status: imported
---

## Definition

Holds an array of int values representing the number of the current bar in a Bars object. An **int** value is added to this array when calling the **[AddDataSeries()](adddataseries)** method. Its purpose is to provide access to the **[CurrentBar](currentbar)** of all Bars objects in a multi-instrument or multi-time frame script.

{% callout type="note" %}

In **[multi series](multi_time_frame_instruments.md)** processing, the CurrentBars starting value will be -1 until all series have processed the first bar.

{% /callout %}

## Property Value

An array of int values.

{% callout type="warning" %}

Warning: This property should NOT be accessed within the **[OnStateChange()](onstatechange)** method before the State has reached State.DataLoaded.

{% /callout %}

## Syntax

**CurrentBars[int barSeriesIndex]**

## Examples

### Indicator (**[BarsRequiredToPlot](barsrequiredtoplot)**)

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Adds a 5-minute Bars object to the script. It will automatically be assigned
         // a Bars object index of 1 since the primary data the indicator is run against
         // set by the UI takes the index of 0.
         AddDataSeries("AAPL", BarsPeriodType.Minute, 5);
     }
}

protected override void OnBarUpdate()
{
     // Evaluates to make sure we have at least 20 (default value of BarsRequiredToPlot)
     // or more bars in both Bars objects before continuing.
     if (CurrentBars[0] < BarsRequiredToPlot || CurrentBars[1] < BarsRequiredToPlot)
         return;

     // Indicator script logic calculation code...

}
```

### Strategy (**[BarsRequiredToTrade](barsrequiredtotrade)**)

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Adds a 5-minute Bars object to the script. It will automatically be assigned
         // a Bars object index of 1 since the primary data the indicator is run against
         // set by the UI takes the index of 0.
         AddDataSeries("AAPL", BarsPeriodType.Minute, 5);
     }
}

protected override void OnBarUpdate()
{
     // Evaluates to make sure we have at least 20 (default value of BarsRequiredToTrade)
     // or more bars in both Bars objects before continuing.
     if (CurrentBars[0] < BarsRequiredToTrade || CurrentBars[1] < BarsRequiredToTrade)
         return;

     // Strategy script logic calculation code...
}
```
