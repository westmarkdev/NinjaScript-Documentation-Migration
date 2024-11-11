---
title: IsResetOnNewTradingDay
pathName: isresetonnewtradingday
parent: bars
section: references
status: review
---

## Definition

Indicates if the bars series is using the **Break EOD** data series property.

## Property Value

This property returns true if the bars series should reset on a new trading day; otherwise, false. This property is read-only.

## Syntax

**Bars.IsResetOnNewTradingDay**

{% callout type="note" %}

Tip: This property can be helpful in determining how to amend new bar data when working with a **BarType**.

{% /callout %}

## Examples

```csharp
protected override void OnDataPoint(Bars bars, double open, double high, double low, double close, DateTime time, long volume, bool isBar, double bid, double ask)
{
    // create a session iterator to keep track of session related information
    if(SessionIterator == null)
        SessionIterator = new SessionIterator(bars);
    
    // determine if the bars are in a new session
    bool isNewSession = SessionIterator.IsNewSession(time, isBar);
    
    if(isNewSession)
        SessionIterator.GetNextSession(time, isBar);
    
    // If bars are using "Break end of day", add a new bar for next session
    if(bars.IsResetOnNewTradingDay && isNewSession)
        AddBar(bars, open, high, low, close, time, volume);
    else
    {
        // do something with existing bar values
    }
}
```
