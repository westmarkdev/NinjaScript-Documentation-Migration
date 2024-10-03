---
title: actualsessionbegin
path: actualsessionbegin
created: Thursday, October 3rd 2024, 11:49:50 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

Obtains the session's start date and start time converted to the user's configured Time Zone.

{% callout type="note" %}  
In order to obtain historical ActualSessionBegin information, you must call [GetNextSession()](getnextsession.htm) from a stored SessionIterator object.  
{% /callout %}

## Property Value

A `DateTime` structure that represents the beginning of a trading session.

## Syntax

```csharp
<sessioniterator>.ActualSessionBegin
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
        Print("The current session start time is " + sessionIterator.ActualSessionBegin);
    }
}
```

{% callout type="note" %}  
Ensure that you handle the session information appropriately for the trading strategy.  
{% /callout %}
