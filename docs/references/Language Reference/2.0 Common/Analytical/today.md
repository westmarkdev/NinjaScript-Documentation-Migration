---
title: ToDay()
pathName: today
parent: analytical
section: references
status: review
---

## Definition

Calculates an integer value representing a date.

{% callout type="note" %}

Note: Integer representation of day is format as yyyyMMdd where January 8, 2015 would be 20150108.

{% /callout %}

## Method Return Value

An **int** value representing date structure.

## Syntax

**ToDay(DateTime time)**

## Parameters

{% table %}

* Parameter
* Description

---

* **time**
* A DateTime structure to calculate. Note: See also the [Time](time) property.

{% /table %}

{% callout type="note" %}

Tip: NinjaScript uses the .NET [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structures which can be complicated for novice programmers. If you are familiar with **C#** you can directly use DateTime structure properties and methods for date and time comparisons otherwise use this method and the [ToTime()](totime) method.

{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{   
    // Compare the date of the current bar to September 15, 2014
    if (ToDay(Time[0]) > 20140915)
    {
        // Do something       
    }
}
```
