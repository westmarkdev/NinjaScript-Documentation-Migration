---
title: "IsFirstTickOfBar"
pathName: /docs/desktop/isfirsttickofbar
---

## Definition

Indicates if the incoming tick is the first tick of a new bar. This property is only of value in scripts that run tick by tick which is when the [Calculate](/docs/desktop/calculate) property is set to Calculate.OnEachTick or Calculate.OnPriceChange.

{% callout type="warning" %}
This property should NOT be accessed outside of the [OnBarUpdate()](/docs/desktop/onbarupdate) method.
{% /callout %}

{% callout type="note" %}
If a bar type is set up to [remove the last bar](/docs/desktop/removelastbar) on a chart, IsFirstTickOfBar will automatically be set to True.
{% /callout %}

## Property Value

This property returns true if the incoming tick is the first tick of a new bar; otherwise, false.

## Syntax

IsFirstTickOfBar

{% callout type="tip" %}
In NinjaTrader's event driven framework, bar closures are signaled by the tick that opens the next bar. The price of the last tick of a bar can be referenced by checking Close[1] on IsFirstTickOfBar. For volume and tick based bars, [Bars.TickCount](/docs/desktop/tickcount) and Volume[0] can be referenced to see if the number of ticks / volume meet the criteria to build a new bar.
{% /callout %}

## Examples

```csharp
// On a tick by tick strategy the only way you know when a bar is closed is when
// the IsFirstTickOfBar is true.
protected override void OnBarUpdate()
{
    // Only process entry signals on a bar by bar basis (not tick by tick)
    if (IsFirstTickOfBar)
    {
        if (CCI(20)[1] < -250)
            EnterLong();
        return;
    }
    // Process exit signals tick by tick
    if (CCI(20)[0] > 250)
        ExitLong();
}
```
