---
section: references
parent: adddataseries
title: BarsArray
pathName: barsarray
status: imported
---

## Definition

An array holding Bars objects that are added via the [AddDataSeries()](adddataseries) method. BarsArray can be used as input for [indicator methods](docs/references/Language%20Reference/2.0%20Common/system_indicator_methods.md). This property is of primary value when working with [multi-time frame or multi-instrument scripts](multi_time_frame_instruments.md).

## Property Value

An array of [Bars](bars) objects.

{% callout type="warning" %}

This property should NOT be accessed within the [OnStateChange()](onstatechange) method before the State has reached State.DataLoaded

{% /callout %}

## Syntax

**BarsArray[int index]**

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
        // Add a 5 minute Bars object which is added to the BarArray 
        // which will take index 1 since the primary Bars object of the strategy 
        // will be index 0 
        AddDataSeries(BarsPeriodType.Minute, 5); 
    }
} 

protected override void OnBarUpdate() 
{ 
    // Ignore bar update events for the supplementary Bars object added above 
    if (BarsInProgress == 1) 
        return; 

    // Pass in a Bars object as input for the simple moving average method 
    // Evaluates if the 20 SMA of the primary Bars is greater than 
    // the 20 SMA of the secondary Bars added above 
    if (SMA(20)[0] > SMA(BarsArray[1], 20)[0]) 
        EnterLong(); 
}
```
