---
title: "Make sure you have enough bars in the data series you are accessing"
pathName: /docs/desktop/make_sure_you_have_enough_bars
---

A common programming error is not checking to ensure there are enough bars contained in the data series you are accessing. This will explain some of the concepts to check for this situation.

For example:

```csharp
protected override void OnBarUpdate()
{
    if (Close[0] > Close[1])
        // Do something
}
```

In the code snippet above, the `OnBarUpdate()` method is called for each bar contained in your data series.

On the very first bar (think of the 1st bar on the chart from left to right), the value of "close of 1 bar ago" (`Close[1]`) does not yet exist and your indicator/strategy will not work and throw an exception to the Control Center Log tab: "Index was out of range...".

Following are two ways to resolve this:

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;
    if (Close[0] > Close[1])
        // Do something
}
```

The resolution above is to check how many bars we have seen (`CurrentBar`) and to exit the `OnBarUpdate()` method if an insufficient number of bars has been seen.

```csharp
protected override void OnBarUpdate()
{
    if (Close[0] > Close[Math.Min(CurrentBar, 1)])
        // Do something
}
```

The resolution above substitutes the minimum value between the current bar being processed and the desired number of bars ago value, in this case, 1.

## Multi time frame and instrument scripts

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {                
        Name = "Multi-Time Frame & Instruments Example";
    }
    else if (State == State.Configure)
    {
        // Adds a secondary bar object to the script.
        AddDataSeries(BarsPeriodType.Minute, 5);
        // Adds an additional bar object to the script.
        AddDataSeries(BarsPeriodType.Minute, 5);
    }
}

protected override void OnBarUpdate()
{
    // Checks to ensure all Bars objects contain enough bars before beginning
    // If this is a strategy, use BarsRequiredToTrade instead of BarsRequiredToPlot
    if (CurrentBars[0] <= BarsRequiredToPlot || CurrentBars[1] <= BarsRequiredToPlot || CurrentBars[2] <= BarsRequiredToPlot)
        return;
}
```

The resolution above would be used in a [Multi Time Frame](/docs/desktop/multi-time_frame__instruments) script. Since `OnBarUpdate()` processes multiple data series, we need to make sure each Data Series we reference has processed enough bars.

