---
title: OnDataPoint()
pathName: ondatapoint
parent: bars_type
status: imported
section: references
---

## Definition

Called for each record in the corresponding base dataset used to build the BarType (i.e., for every tick, minute, or day). The **OnDataPoint()** method is where you should adjust data points (bar values) of your series through [**AddBar()**](addbar) and [**UpdateBar()**](updatebar). See also the [**BuiltFrom**](builtfrom) property.

{% callout type="note" %}

1. Historical data processing receives a single update for every base bar determined by the **BuiltFrom** property.  
2. When using [**TickReplay**](tick_replay), historical updates will call for every tick handled by the core regardless of the **BuiltFrom** property defined.  
3. Once transitioned to real-time, updates will call on every tick processed by the core.  
4. The bid/ask parameters will ONLY be available historically when using [**Tick Replay**](tick_replay), unless you are using a 1-tick series.  
5. **isBar** could be true in case the BarsSeries was internally copied to another BarsSeries and is only needed for [**IsTimeBased**](barstype_istimebased) = true BarsTypes (e.g. Second/Minute/Day...).
{% /callout %}

## Method Return Value

This method does not return a value.

## Method Parameters

{% table %}

---

* bars
* The Bars object of your bars type

---

* open
* A **double** value representing the open price

---

* high
* A **double** value representing the high price

---

* low
* A **double** value representing the low price

---

* close
* A **double** value representing the close price

---

* time
* A DateTime value representing the time

---

* volume
* A long value representing the volume

---

* isBar
* A bool value representing if **OnDataPoint** should treat the timestamp as an already built bar instead of an intrabar timestamp.

---

* bid
* A **double** value representing the bid price

---

* ask
* A **double** value representing the ask price
{% /table %}

## Syntax

You must override the method in your Bars Type with the following syntax.

```csharp
protected override void OnDataPoint(Bars bars, double open, double high, double low, double close, DateTime time, long volume, bool isBar, double bid, double ask)
{
}
```

## Examples

```csharp
protected override void OnDataPoint(Bars bars, double open, double high, double low, double close, DateTime time, long volume, bool isBar, double bid, double ask)
{
     int minIndex;

     // Create the first data point of our series
     if (bars.Count == 0)
     {
         minIndex = 0;
         AddBar(bars, open, high, low, close, TimeToBarTime(time, (int) bars.BarsPeriod.Value), volume);
     }
     // Update our data point with the latest information
     else if ((time.Month <= bars.LastBarTime.Month && time.Year == bars.LastBarTime.Year) || time.Year < bars.LastBarTime.Year)
     {
         if (high != bars.GetHigh(bars.Count - 1) || low != bars.GetLow(bars.Count - 1) ||
               close != bars.GetClose(bars.Count - 1) || volume > 0)
         {
               minIndex = bars.Count - 1;
               UpdateBar(bars, high, low, close, bars.LastBarTime, volume);
         }
         else
               minIndex = -1;
     }
     // Add new data points
     else
     {
         minIndex = bars.Count;
         AddBar(bars, open, high, low, close, time, (long)Math.Min(volumeTmp, bars.BarsPeriod.Value));
     }
     FirstBarAmended = minIndex;
}
```
