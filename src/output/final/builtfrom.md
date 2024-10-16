---
title: "BuiltFrom"
pathName: /docs/desktop/builtfrom
---

## Definition

Determines the base dataset used to build the BarsType (i.e., Tick, Minute, Day). The BuiltFrom property will control the frequency in which [OnDataPoint()](/docs/desktop/ondatapoint) processes historical data.

## Property Value

A [BarsPeriodType](/docs/desktop/barsperiod) enum. Values that will be recognized include:

&bull; BarsPeriodType.Tick{% <br> %}
&bull; BarsPeriodType.Minute{% <br> %}
&bull; BarsPeriodType.Day

{% callout type="warning" %}
Using other bars period types (e.g., Range, Volume, or other custom bars types) is NOT supported. The BarsPeriodType values mentioned above represent all of the fundamental data points needed to build a bar.
{% /callout %}

## Syntax

```csharp
BuiltFrom
```

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "MyCustomBarsType";
        BarsPeriod = new BarsPeriod { BarsPeriodType = (BarsPeriodType) 15, BarsPeriodTypeName = "MyCustomBarsType(15)", Value = 1 };
        BuiltFrom = BarsPeriodType.Minute; // update OnDataPoint() every minute on historical data
        DaysToLoad = 5;
    }
    else if (State == State.Configure)
    {
    }
}
```

