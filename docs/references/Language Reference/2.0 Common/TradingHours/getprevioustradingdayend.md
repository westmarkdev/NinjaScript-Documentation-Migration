---
title: GetPreviousTradingDayEnd()
pathName: getprevioustradingdayend
parent: tradinghours
section: references
status: review
---

## Definition

Returns the end date and time of the previous trading session regarding the time passed in the methods parameters.

## Method Return Value

A **DateTime** structure representing the previous trading days end date and time.

## Syntax

**GetPreviousTradingDayEnd(DateTime timeLocal)**

{% callout type="warning" %}

This method is resource intensive and should ONLY be reserved for situations when calculations would be limited to a few specific use cases. For example, calling this method for each bar in the **OnBarUpdate()** method would NOT be recommended.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **timeLocal**
* An **DateTime** structure which is used to calculate the current trading day
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (Bars.IsFirstBarOfSession)
    {
        DateTime previousEndDate = TradingHours.GetPreviousTradingDayEnd(Time[0]);

        Print(string.Format("The current bars date is {0} - the previous trading session ended on {1}", Time[0], previousEndDate));
    }
    //Output:  The current bars date is 2/18/2015 12:35:00 PM - the previous trading session ended on 2/17/2015 3:15:00 PM
}
```
