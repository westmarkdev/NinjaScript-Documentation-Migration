---
title: GetClosestAnchor()
pathName: getclosestanchor
parent: drawing_tools
status: imported
section: references
---

## Definition

Returns the closest chart anchor within a specified maximum distance from the mouse cursor.

## Method Return Value

This method returns an existing **ChartAnchor**.

## Syntax

GetClosestAnchor(**ChartControl** chartControl, **ChartPanel** chartPanel, **ChartScale** chartScale, double maxDist, **Point** point)

## Method Parameters

{% table %}

---

* **chartControl**
* A **ChartControl** representing the x-axis

---

* **chartPanel**
* A **ChartPanel** representing the panel for the chart

---

* **chartScale**
* A **ChartScale** representing the y-axis

---

* **maxDist**
* A **double** value representing the cursor's sensitivity used to detect the nearest anchor

---

* **point**
* A **Point** in device pixels representing the current mouse cursor position
{% /table %}

## Examples

```csharp

public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
   // get the closest anchor to where the user has clicked
   ChartAnchor closest = GetClosestAnchor(chartControl, chartPanel, chartScale, 10, point);

   if (closest != null)
   {
     // set cursor to indicate that it can be moved
     return Cursors.SizeNWSE;
   }
   // otherwise set cursor back to arrow
   else return Cursors.Arrow;
```
