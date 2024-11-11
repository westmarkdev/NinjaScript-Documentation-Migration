---
title: IsLastBarOfSession
pathName: islastbarofsession
parent: bars
section: references
status: review
---

## Definition

Indicates if the current bar processing is the last bar updated in a trading session.

{% callout type="note" %}

Notes:  

* This property will always return false on non-intraday bar periods (e.g., Day, Month, etc.)
* When running Calculate.OnEachTick / OnPriceChange, this property will always return true on the most current real-time bar since it is the last bar that is updating in the trading session. If you need to find a bar which coincides with the session end time, please use the **SessionIterator.ActualSessionEnd**.
{% /callout %}

## Property Value

This property returns true if the bar is the last processed in a session; otherwise, false. This property is read-only.

## Syntax

**Bars.IsLastBarOfSession**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print the current bar number of the first bar processed for each session on a chart
    if(Bars.IsLastBarOfSession)
        Print(string.Format("Bar number {0} was the last bar processed of the session at {1}.", CurrentBar, Time[0]));
}
```
