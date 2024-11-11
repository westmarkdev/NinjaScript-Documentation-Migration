---
title: ApplyDefaultValue
pathName: applydefaultvalue
parent: bars_type
status: imported
section: references
---

## Definition

Sets the default **BarsPeriod** values used for a custom Bar Type.

## Method Return Value

This method does not return a value.

## Parameters

{% table %}

---

* period
* The **BarsPeriod** chosen by the user when utilizing this Bars type

{% /table %}

## Syntax

You must override the method in your Bars Type with the following syntax:

```csharp
public override void ApplyDefaultValue(BarsPeriod period)  
{  
}
```

## Examples

```csharp
public override void ApplyDefaultValue(BarsPeriod period)
{
 period.BarsPeriodTypeName = "MyBarType";
 period.Value = 1;
}
```
