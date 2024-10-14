---
title: "Bars"
path: bars
---

## Definition

Represents the data returned from the historical data repository. The Bars object contains several methods and properties for working with bar data.

{% callout type="warning" %}
The Bars object and its members should NOT be accessed within the [OnStateChange()](onstatechange) method before the State has reached State.DataLoaded.
{% /callout %}

## Additional Access Information

Members within the Bars class can be accessed without a null reference check in the OnBarUpdate() event handler. When the OnBarUpdate() event is triggered, there will always be a Bar object which holds the method or property. Should you wish to access these members elsewhere, check for null reference first.

```csharp
if (Bars != null)
{
    // Access members here
}
```

## Methods and Properties

| Method/Property | Description |
| --- | --- |
| [BarsSinceNewTradingDay](barssincenewtradingday) | Number of bars that have elapsed since the start of the trading day |
| [GetAsk()](getask) | Returns the Ask price |
| [GetBar()](getbar) | Returns the bar index based on time |
| [GetBid()](getbid) | Returns the Bid price |
| [GetClose()](getclose) | Returns the closing price |
| [GetDayBar()](getdaybar) | Returns a Bar object that represents a trading day whose properties for open, high, low, close, time, and volume can be accessed. |
| [GetHigh()](gethigh) | Returns the High price |
| [GetLow()](getlow) | Returns the Low price |
| [GetOpen()](getopen) | Returns the opening price |
| [GetTime()](gettime) | Returns the time |
| [GetVolume()](getvolume) | Returns the volume |
| [IsFirstBarOfSession](isfirstbarofsession) | Returns true if the bar is the first bar of a session |
| [IsFirstBarOfSessionByIndex()](isfirstbarofsessionbyindex) | Returns true if the bar is the first bar of a session |
| [IsLastBarOfSession](islastbarofsession) | Returns true if the bar is the last bar of a session |
| [IsResetOnNewTradingDay](isresetonnewtradingday) | Returns true if the chart bars should reset on a new trading day |
| [IsTickReplay](istickreplay) | Returns true if the bars are using tick replay |
| [PercentComplete](percentcomplete) | Value indicating the completion percent of a bar |
| [TickCount](tickcount) | Total number of ticks of the current bar |
| [ToChartString()](tochartstring) | Returns the bars series as a string formatted as the series would be displayed in the user interface |
