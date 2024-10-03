---
title: actualsessionend
pathName: actualsessionend
created: Thursday, October 3rd 2024, 11:49:45 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

Obtains the session's end date and end time converted to the user's configured Time Zone.

{% callout type="note" %}  
In order to obtain historical ActualSessionEnd information, you must call [GetNextSession()](getnextsession.htm) from a stored SessionIterator object.  
{% /callout %}

## Property Value

A DateTime structure that represents the end of a trading session.

## Syntax

`<sessioniterator>.ActualSessionEnd`

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

        Print("The current session end time is " + sessionIterator.ActualSessionEnd);
    }
}
```

{% callout type="note" %}  
With this approach, you can effectively track the end time of trading sessions in relation to your strategy's execution.  
{% /callout %}
