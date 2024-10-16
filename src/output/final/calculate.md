---
title: "Calculate"
pathName: /docs/desktop/calculate
---

## Definition

Determines how often [OnBarUpdate()](/docs/desktop/onbarupdate) is called for each bar. OnBarClose means once at the close of the bar. OnEachTick means on every single tick. OnPriceChange means once for each price change. If there were two ticks in a row with the same price, the second tick would not trigger OnBarUpdate(). This can improve performance if calculations are only needed when new values are possible.

{% callout type="note" %}

1. On a historical data set, only the OHLCVT of the bar is known and not each tick that made up the bar. As a result, [State.Historical](/docs/desktop/state) data processes OnBarUpdate() only on the close of each historical bar even if this property is set to OnEachTick or OnPriceChange. You can use [TickReplay](/docs/desktop/tick_replay) or a [Multi-time frame script](/docs/desktop/multi-time_frame__instruments) to obtain intrabar data.
2. When set to Calculate OnPriceChange, the OnBarUpdate() method is ONLY called when the price has changed intrabar OR when the bar has closed.

{% /callout %}

## Property Value

An enum value determining how frequently OnBarUpdate() will be called. Default value is set to Calculate.OnBarClose.

{% callout type="warning" %}

• This property should ONLY be set from the OnStateChange() method during State.SetDefaults or State.Configure.  
• If your script relies on volume updates, OnPriceChange should NOT be used since it can potentially miss volume updates if they occur at the same price.

{% /callout %}

## Syntax

Calculate.OnBarClose

Calculate.OnEachTick

Calculate.OnPriceChange

{% callout type="tip" %}

1. Calculating indicators or systems for each incoming tick can be CPU intensive. Only calculate indicators on each incoming tick if you have a requirement to calculate it intra-bar.
2. For an example of how to separate some logic to be Calculate = Calculate.OnBarClose and other logic to be .OnEachTick, please see this [reference sample](http://www.ninjatrader.com/support/forum/showthread.php?t=19387).
3. Embedded scripts within a calling parent script should not use a different Calculate property since it is already utilizing the Calculate property of the parent script (i.e., the strategy your indicator is called from).
4. Since the parent NinjaScript therefore governs this setting, it should be set to the highest needed setting satisfying all its children.

{% /callout %}

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Calculate on the close of each bar
        Calculate = Calculate.OnBarClose;
    }
}
```
