---
title: ExitOnSessionCloseSeconds
pathName: exitonsessioncloseseconds
parent: strategy
section: references
status: imported
---

## Definition

The number of seconds before the actual session end time that the **IsExitOnSessionCloseStrategy** function will trigger.

The time from which this property will be calculated is taken from the [Trading Hours](trading_hours) EOD property set in the strategy's Trading Hours template. The ExitOnSessionCloseSeconds property can either be set programmatically in the **OnStateChange()** method or be driven by the UI at run time.

{% callout type="note" %}

This is a real-time only property, it will not have any effect on your ExitOnSessionClose time in backtesting processing historical data.

{% /callout %}

## Property Value

An int representing the number of seconds. Default value is 30.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.

{% /callout %}

## Syntax

**ExitOnSessionCloseSeconds**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Triggers the exit on close function 30 seconds prior to trading day end 
         IsExitOnSessionCloseStrategy = true;
         ExitOnSessionCloseSeconds = 30;
     }
}
```
