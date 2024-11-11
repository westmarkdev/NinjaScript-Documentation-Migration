---
title: ActualTradingDayEndLocal
pathName: actualtradingdayendlocal
parent: sessioniterator
section: references
status: review
---

## Definition

Returns the session's End-Of-Day (EOD) in the user's configured timezone.

{% callout type="note" %}

In order to obtain historical ActualTradingDayEndLocal information, you must call [GetNextSession](getnextsession) from a stored SessionIterator object.

{% /callout %}

## Property Value

A DateTime structure that represents end of a trading day (EOD).

## Syntax

**SessionIterator.ActualTradingDayEndLocal**

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
