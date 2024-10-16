---
title: "BarsPeriods"
pathName: /docs/desktop/barsperiods
---

## Definition

Holds an array of BarsPeriod objects synchronized to the number of unique Bars objects held within the parent NinjaScript object. If a NinjaScript object holds two Bars series, then BarsPeriods will hold two BarsPeriod objects.

## Property Value

An array of [BarsPeriod](/docs/desktop/barsperiod) objects.

{% callout type="warning" %}
This property should NOT be accessed within the [OnStateChange()](/docs/desktop/onstatechange) method before the State has reached State.DataLoaded
{% /callout %}

### Syntax

```csharp
BarsPeriods[int barSeriesIndex]
```

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
    {
        // Adds a 5-minute Bars object to the strategy and is automatically assigned
        // a Bars object index of 1 since the original data the strategy is ran on,
        // set by the UI, takes the index of 0.
        AddDataSeries("AAPL", BarsPeriodType.Minute, 5);
    }
}

protected override void OnBarUpdate()
{
    // Print out 5, the value of the secondary bars object
    if (BarsInProgress == 1)
        Print(BarsPeriods[1].Value);
}
```
