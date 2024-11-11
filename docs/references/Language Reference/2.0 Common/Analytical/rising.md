---
title: IsRising()
pathName: isrising
parent: analytical
section: references
status: review
---

## Definition

Evaluates a rising condition which is true when the current value is greater than the value of 1 bar ago.

## Method Return Value

This method returns true if a rising condition is present; otherwise, false.

## Syntax

**IsRising(ISeries`<double>` series)**

## Parameters

{% table %}

* Parameter
* Description

---

* **series**
* Any **Series<`double`>** type object such as an indicator, Close, High, Low, etc...
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   // If the 20 period SMA is rising (in uptrend) go long
   if (IsRising(SMA(20)))
       EnterLong();
}
```
