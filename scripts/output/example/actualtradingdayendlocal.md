---
title: actualtradingdayendlocal
path: actualtradingdayendlocal
created: Thursday, October 3rd 2024, 11:49:55 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

Returns the session's End-Of-Day (EOD) in the user's configured timezone.

{% callout type="note" %}  
In order to obtain historical ActualTradingDayEndLocal information, you must call [GetNextSession()](getnextsession.htm) from a stored SessionIterator object.  
{% /callout %}

## Property Value

A DateTime structure that represents the end of a trading day (EOD).

## Syntax

`<sessioniterator>.ActualTradingDayEndLocal`

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

        Print("The current session end of day is " + sessionIterator.ActualTradingDayEndLocal);
    }
}
``` 

{% callout type="note" %}  
The above code example demonstrates how to utilize the `SessionIterator` to access the `ActualTradingDayEndLocal` property during the trading session.  
{% /callout %}
