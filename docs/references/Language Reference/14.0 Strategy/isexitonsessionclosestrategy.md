---
title: IsExitOnSessionCloseStrategy
pathName: isexitonsessionclosestrategy
parent: strategy
section: references
status: imported
---

## Definition

Determines if the strategy will cancel all strategy generated orders on all strategy instruments and close all open strategy positions at the close of ANY session for multi-time frame/multi-instrument strategies. This property can be set programmatically in the **OnStateChange()** method or be driven by the UI at run time. See also "[ExitOnSessionCloseSeconds](exitonsessioncloseseconds)".

## Property Value

This property returns true if the strategy will exit on close; otherwise, false. Default value is set to true.

{% callout type="note" %}

Warnings:  

* This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.
* On historical data, **IsExitOnSessionCloseStrategy** will cause positions to be exited at the close of the last bar of the session. If you are using a non time-based Bar Type, such as Renko, and have "Break at EOD" set to False on the Data Series, this means that **IsExitOnSessionCloseStrategy** could trigger after the session close, since the last bar of the session can extend beyond the session close time in this scenario.
* Even if you're backtesting with a historical **order fill resolution** set to be more granular than your base primary series, the **ExitOnSessionCloseSeconds** will still be tied to the primary higher timeframe series bar. **IsExitOnSessionCloseStrategy** should not be used in combination with Daily Bars and High Order Fill Resolution since it will cause the position to close at the same time as the daily bar updates (at session close).
* This property is designed to be only used on intraday strategies.
{% /callout %}

## Syntax

**IsExitOnSessionCloseStrategy**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Triggers the exit on session close function 30 seconds prior to real-time trading day end 
        IsExitOnSessionCloseStrategy = true;
        ExitOnSessionCloseSeconds = 30;
    }
}
```
