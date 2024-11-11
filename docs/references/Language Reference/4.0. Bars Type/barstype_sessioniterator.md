---
title: SessionIterator
pathName: barstype_sessioniterator
parent: bars_type
status: changed
section: references
---

## Definition

Provides trading session information to the bars type. Must be built using the bars object.

## Property Value

A [SessionIterator](/sessioniterator) object which is used to calculate trading day/session information.

## Syntax

**SessionIterator**

## Examples

```csharp
protected override void OnDataPoint(Bars bars, double open, double high, double low, double close, DateTime time, long volume, bool isBar, double bid, double ask)
{
   // build a session iterator from the bars object being updated
   if (SessionIterator == null)
     SessionIterator = new SessionIterator(bars);

   // check if we are in a new trading session based on the trading hours selected by the user
   bool isNewSession = SessionIterator.IsNewSession(time, isBar);

   // calculate the new trading day
   if (isNewSession)
     SessionIterator.CalculateTradingDay(time, isBar);

   Print(SessionIterator.ActualTradingDayExchange);
}
```
