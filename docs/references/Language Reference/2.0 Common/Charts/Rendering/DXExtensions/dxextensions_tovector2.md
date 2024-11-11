---
title: ToVector2()
pathName: tovector2
parent: rendering
section: references
status: imported
---

## Definition

Converts a **System.Windows.Point** structure to a **SharpDX.Vector2** used for [SharpDX rendering](using_sharpdx_for_custom_chart_rendering).

## Method Return Value

A new **SharpDX.Vector2** constructed with the point parameters X and Y values.

## Syntax

**DxExtensions.ToVector2(this System.Windows.Point point)**  

**<`point`>.ToVector2()**

## Parameters

{% table %}

---

* point
* The [System.Windows.Point](https://msdn.microsoft.com/en-us/library/system.windows.point(v=vs.110).aspx) point to convert
{% /table %}

## Examples

```csharp
// gets the application/user WPF point and converts to a SharpDX Vector 
System.Windows.Point wpfPoint = ChartControl.MouseDownPoint;

SharpDX.Vector2 dxVector2 = wpfPoint.ToVector2();
```
