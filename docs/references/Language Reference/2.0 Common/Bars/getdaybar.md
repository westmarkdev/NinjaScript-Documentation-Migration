---
title: GetDayBar()
pathName: getdaybar
parent: bars
section: references
status: review
---

## Definition

Returns a virtual historical Bar object that represents a trading day whose properties for open, high, low, close, time and volume can be accessed.

{% callout type="note" %}

Notes:

1. The bar object returned is a "virtual bar" built from the underlying bar series and its configured session. Since the bar object is virtual, its property values are calculated based on session definitions contained in the trading day only. The returned bar object does NOT necessarily represent the actual day. For accessing a true "Daily" bar, please see use **AddDataSeries()** and use the **BarsPeriodType.Day** as the bars period.
2. **GetDayBar()** should ONLY be used for accessing prior trading day data. To access current trading day data, use the **CurrentDayOHL()** method.
{% /callout %}

## Method Return Value

A virtual bar object representing the current configured session. Otherwise null if there is insufficient intraday data.

## Syntax

The properties below return double values:

- **Bars.GetDayBar(int tradingDaysBack).Open**  
- **Bars.GetDayBar(int tradingDaysBack).High**  
- **Bars.GetDayBar(int tradingDaysBack).Low**  
- **Bars.GetDayBar(int tradingDaysBack).Close**  

The property below returns a [DateTime](datetime) structure:

- **Bars.GetDayBar(int tradingDaysBack).Time**  

The property below returns An **int** value:

- **Bars.GetDayBar(int tradingDaysBack).Volume**  

{% callout type="warning" %}

Warning: You must check for a null reference to ensure there is sufficient intraday data to build a trading day bar.

{% /callout %}

## Parameters

{% table %}

- Parameter
- Description

---

- **tradingDaysBack**
- An int representing the number of the trading day to get OHLCV and time information from
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Check to ensure that sufficient intraday data was supplied
    if(Bars.GetDayBar(1) != null)
        Print("The prior trading day's close is: " + Bars.GetDayBar(1).Close);
}
```
