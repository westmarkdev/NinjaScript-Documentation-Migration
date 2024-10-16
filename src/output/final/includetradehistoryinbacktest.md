---
title: "IncludeTradeHistoryInBacktest"
pathName: /docs/includetradehistoryinbacktest
---

## Definition

Determines if the strategy will save orders, trades, and execution history. When this property is set to false you will see significant memory savings at the expense of having access to the detailed trading information.

{% callout type="note" %}
• Since trade information is not stored you will only see entry/exit executions plotted on the chart with no connecting PnL trade lines.  
• This property is always defaulted to true, except when the strategy is running on the strategy tab.
{% /callout %}

## Property Value

This property returns true if the strategy will include trade history; otherwise, false. Default is set to true.

{% callout type="warning" %}
This property should ONLY be set from the [OnStateChange()](/docs/desktop/onstatechange) method during State.Configure (or State.SetDefaults when adding the script from the strategy tab).
{% /callout %}

## Syntax

IncludeTradeHistoryInBacktest

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
    {
        // Exclude trade history in a backtest to benefit from memory savings
        IncludeTradeHistoryInBacktest = false;
    }
}

protected override void OnBarUpdate()
{
    // Stop taking trades after 10 trades have been taken since the strategy was enabled
    if (SystemPerformance.AllTrades.Count >= 10)
        return;
}
```

