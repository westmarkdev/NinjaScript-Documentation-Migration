---
title: Draw.FibonacciExtensions()
pathName: draw_fibonacciextensions
parent: drawing
section: references
status: review
---

## Definition

Draws a fibonacci extension.

## Method Return Value

A **FibonacciExtensions** object that represents the draw object.

## Syntax

**Draw.FibonacciExtensions(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, int extensionBarsAgo, double extensionY)**  

**Draw.FibonacciExtensions(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, DateTime extensionTime, double extensionY)**  

**Draw.FibonacciExtensions(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, DateTime extensionTime, double extensionY, bool isGlobal, string templateName)**  

**Draw.FibonacciExtensions(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, int extensionBarsAgo, double extensionY, bool isGlobal, string templateName)**

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

* extensionBarsAgo
* The number of bars ago (x value) of the 3rd anchor point.

---

* extensionTime
* The time of the 3rd anchor point.

---

* extensionY
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
// Draws a fibonnaci extension
Draw.FibonacciExtensions(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1]);
```
