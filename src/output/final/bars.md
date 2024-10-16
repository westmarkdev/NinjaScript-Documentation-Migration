---
title: "Bars"
pathName: /docs/desktop/bars
---

## Definition

Represents the data returned from the historical data repository. The Bars object contains several methods and properties for working with bar data.

{% callout type="warning" %}
The Bars object and its members should NOT be accessed within the [OnStateChange()](/docs/desktop/onstatechange) method before the State has reached State.DataLoaded
{% /callout %}

Additional Access Information

Members within the Bars class can be accessed without a null reference check in the `OnBarUpdate()` event handler. When the `OnBarUpdate()` event is triggered, there will always be a Bar object which holds the method or property. Should you wish to access these members elsewhere, check for null reference first. For example:

```csharp
if (Bars != null)
```

## Methods and Properties

|  |  |
| --- | --- |
| [BarsSinceNewTradingDay](/docs/desktop/barssincenewtradingday) | Number of bars that have elapsed since the start of the trading day |
| [GetAsk()](/docs/desktop/getask) | Returns the Ask price |
| [GetBar()](/docs/desktop/getbar) | Returns the bar index based on time |
| [GetBid()](/docs/desktop/getbid) | Returns the Bid price |
| [GetClose()](/docs/desktop/getclose) | Returns the closing price |
| [GetDayBar()](/docs/desktop/getdaybar) | Returns a Bar object that represents a trading day whose properties for open, high, low, close, time, and volume can be accessed. |
| [GetHigh()](/docs/desktop/gethigh) | Returns the High price |
| [GetLow()](/docs/desktop/getlow) | Returns the Low price |
| [GetOpen()](/docs/desktop/getopen) | Returns the opening price |
| [GetTime()](/docs/desktop/gettime) | Returns the time |
| [GetVolume()](/docs/desktop/getvolume) | Returns the volume |
| [IsFirstBarOfSession](/docs/desktop/isfirstbarofsession) | Returns true if the bar is the first bar of a session |
| [IsFirstBarOfSessionByIndex()](/docs/desktop/isfirstbarofsessionbyindex) | Returns true if the bar is the first bar of a session |
| [IsLastBarOfSession](/docs/desktop/islastbarofsession) | Returns true if the bar is the last bar of a session |
| [IsResetOnNewTradingDay](/docs/desktop/isresetonnewtradingday) | Returns true if the chart bars should reset on a new trading day |
| [IsTickReplay](/docs/desktop/istickreplay) | Returns true if the bars are using tick replay |
| [PercentComplete](/docs/desktop/percentcomplete) | Value indicating the completion percent of a bar |
| [TickCount](/docs/desktop/tickcount) | Total number of ticks of the current bar |
| [ToChartString()](/docs/desktop/tochartstring) | Returns the bars series as a string formatted as the series would be displayed in the user interface |

