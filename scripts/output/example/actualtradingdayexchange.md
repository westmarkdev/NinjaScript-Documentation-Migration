---
title: actualtradingdayexchange
path: actualtradingdayexchange
created: Thursday, October 3rd 2024, 11:50:06 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

Obtains the date of a trading session defined by the exchange.

{% callout type="note" %}

1. In order to obtain historical ActualTradingDayExchange information, you must call [GetNextSession()](getnextsession.htm) from a stored SessionIterator object. 
2. The calculated value may differ from the current date as some trading sessions will begin before the actual calendar date changes. For example, the "CME US Index Futures ETH" [actual session](accumulation_distribution_adl.htm) started on 3/30/2015 at 5:00 PM Central Time, however the actual exchange trading day would be considered 3/31/2015 12:00:00 AM.  
{% /callout %}

## Property Value

A DateTime structure that represents the trading day.

## Syntax

```csharp
<sessioniterator>.ActualTradingDayExchange
```

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

{% callout type="note" %}  
Make sure to handle the session iterator correctly, as improper management may lead to incorrect trading day calculations.  
{% /callout %}
