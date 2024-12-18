---
title: Draw.Ruler()
pathName: draw_ruler
parent: drawing
section: references
status: review
---

## Definition

Draws a ruler.

## Method Return Value

A **Ruler** object that represents the draw object.

## Syntax

**Draw.Ruler(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, int textBarsAgo, double textY)**  

**Draw.Ruler(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, DateTime textTime, double textY)**  

**Draw.Ruler(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, int textBarsAgo, double textY, bool isGlobal, string templateName)**  

**Draw.Ruler(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, DateTime textTime, double textY, bool isGlobal, string templateName)**

## Parameters

{% table %}

---

* owner
* The hosting **NinjaScript** object which is calling the draw method. Typically will be the object which is calling the draw method (e.g., "this").

---

* tag
* A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time.

---

* isAutoScale
* Determines if the draw object will be included in the y-axis scale.

---

* startBarsAgo
* The number of bars ago (x value) of the 1st anchor point.

---

* startTime
* The time of the 1st anchor point.

---

* startY
* The y value of the 1st anchor point.

---

* endBarsAgo
* The number of bars ago (x value) of the 2nd anchor point.

---

* endTime
* The time of the 2nd anchor point.

---

* endY
* The y value of the 2nd anchor point.

---

* textBarsAgo
* The number of bars ago (x value) of the 3rd anchor point.

---

* textTime
* The time of the 3rd anchor point.

---

* textY
* The y value of the 3rd anchor point.

---

* isGlobal
* Determines if the draw object will be global across all charts which match the instrument.

---

* templateName
* The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead).
{% /table %}

## Examples

```csharp
// Draws a ruler measuring the primary bar series
Draw.Ruler(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1]);
```
