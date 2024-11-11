---
title: Clone()
pathName: clone
parent: common
section: references
status: review
---

## Definition

Used to override the default **NinjaScript** **Clone()** method which is called any time an instance of a **NinjaScript** object is created. By default, the **NinjaScript** **Clone()** method will copy all the [Property Info](https://msdn.microsoft.com/en-us/library/system.reflection.propertyinfo%28v=vs.110%29.aspx) and [Browsable Attributes](https://msdn.microsoft.com/en-us/library/system.componentmodel.browsableattribute%28v=vs.110%29.aspx) to the new instance when the object is created (e.g., when an optimization is ran a new instance of the strategy will be created for each iteration). However, it is possible to override this behavior if desired for custom development. There is no requirement to override the **Clone** behavior and this method will use the default constructor if not overridden.

{% callout type="note" %}

This method is reserved for advanced developers who would like to change the default behavior when a **NinjaScript** object is created.

{% /callout %}

## Method Return Value

A [virtual](https://msdn.microsoft.com/en-us/library/9fkccyh4.aspx) object representing the **NinjaScript** type.

## Syntax

**public override object Clone()**

## Parameters

This method does not take any parameters.

## Examples

```csharp

public override object Clone()
{
   // custom logic to handle before the base clone

   return base.Clone();

 // custom logic to hand after the base clone
}
```
