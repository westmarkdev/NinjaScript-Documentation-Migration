---
title: ActualSessionBegin
pathName: actualsessionbegin
parent: sessioniterator
section: references
status: review
---

## Definition

Obtains the sessions start date and start time converted to the user's configured Time Zone.

{% callout type="note" %}

In order to obtain historical ActualSessionBegin information, you must call [GetNextSession](getnextsession) from a stored SessionIterator object.

{% /callout %}

## Property Value

A **DateTime** structure that represents beginning of a trading session.

## Syntax

**SessionIterator.ActualSessionBegin**

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
