---
title: IsFalling()
pathName: isfalling
parent: system_indicator_methods
section: references
status: review
---

## Definition

Evaluates a falling condition which is true when the current value is less than the value of 1 bar ago.

## Method Return Value

This method returns true if a falling condition is present; otherwise, false.

## Syntax  

**IsFalling(ISeries`<double>` series)**

## Parameters

{% table %}

---

* **series**
* Any **Series<`double`>** type object such as an indicator, Close, High, Low, etc...
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   // If the 20 period SMA is falling (in downtrend) go short
   if (IsFalling(SMA(20)))
       EnterShort();
}
```
