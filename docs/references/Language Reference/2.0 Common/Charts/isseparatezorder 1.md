---
title: IsSeparateZOrder
pathName: isseparatezorder
parent: charts
section: references
status: review
---

## Definition

Determines the **ZOrder** of the drawing object will be different than the **NinjaScript** object that drew it. When false the drawing object will share the same ZOrder.

## Property Value

This property returns true if the object is drawn on a separate ZOrder; otherwise, false. Default set to false.

## Syntax

**IsSeparateZOrder**

## Examples

```csharp

protected override void OnBarUpdate()
{
   // Instantiate a Dot object
   Dot myDot = Draw.Dot(this, "NewDot", true, 5, High[5], Brushes.Black);
 
   // Set the Dot object to use a separate Z-Order than the indicator that created it
   myDot.IsSeparateZOrder = true;
}
```
