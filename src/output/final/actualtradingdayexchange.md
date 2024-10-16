---
title: "ActualTradingDayExchange"
pathName: /docs/desktop/actualtradingdayexchange
---

## Definition

Obtains the date of a trading session defined by the exchange.

{% callout type="note" %}
1. In order to obtain historical ActualTradingDayExchange information, you must call [GetNextSession()](/docs/desktop/getnextsession) from a stored SessionIterator object. 
2. The calculated value may differ from the current date as some trading sessions will begin before the actual calendar date changes. For example, the "CME US Index Futures ETH" [actual session](/docs/desktop/accumulation_distribution_adl) started on 3/30/2015 at 5:00 PM Central Time, however the actual exchange trading day would be considered 3/31/2015 12:00:00 AM.
{% /callout %}

## Property Value

A DateTime structure that represents the trading day.

## Syntax

`<sessioniterator>.ActualTradingDayExchange`

## Example

```csharp
SessionIterator sessionIterator;

protected override void OnStateChange()
{
    if (State == State.Historical)
    {
        sessionIterator = new SessionIterator(Bars);
    }
}

protected override void OnBarUpdate()
{
    // on new bars session, find the next trading session
    if (Bars.IsFirstBarOfSession)
    {
        // use the current bar time to calculate the next session
        sessionIterator.GetNextSession(Time[0], true);
        Print("The current exchange trading day is " + sessionIterator.ActualTradingDayExchange);
    }
}
```

