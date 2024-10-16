---
title: "GetTradingDay()"
pathName: /docs/desktop/gettradingday
---

## Definition

Returns the actual trading date based on the exchange, calculated from a DateTime object passed with the local time. GetTradingDay() calls CalculateTradingDay() on a custom SessionIterator object created by passing in a Bars object as an argument.

{% callout type="warning" %}
This method can ONLY be called when a SessionIterator was created with a 'Bars' parameter.
{% /callout %}

## Property Value

A DateTime object representing the [ActualTradingDayExchange](/docs/desktop/actualtradingdayexchange) property.

## Syntax

```csharp
<sessioniterator>.GetTradingDay(DateTime timeLocal)
```

## Parameters

|  |  |
| --- | --- |
| timeLocal | The DateTime value used to calculate the next trading day. |

## Example

```csharp
// Declare a new custom SessionIterator
SessionIterator mySessionIterator;

protected override void OnStateChange()
{
    if (State == State.Historical)
    {
        // Instantiate mySessionIterator once in State.Configure
        mySessionIterator = new SessionIterator(BarsArray[0]);
    }
}

protected override void OnBarUpdate()
{
    // Obtain the ActualTradingDayExchange value for mySessionIterator, based on today's date
    Print(mySessionIterator.GetTradingDay(DateTime.Now).ToString());
}
```
