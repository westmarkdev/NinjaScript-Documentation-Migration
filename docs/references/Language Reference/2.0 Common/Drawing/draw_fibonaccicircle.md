---
title: Draw.FibonacciCircle()
pathName: draw_fibonaccicircle
parent: drawing
section: references
status: review
---

## Definition

Draws a fibonacci circle.

## Method Return Value

A **FibonacciCircle** object that represents the draw object.

## Syntax  

**Draw.FibonacciCircle(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY)**  

**Draw.FibonacciCircle(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY)**  

**Draw.FibonacciCircle(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, bool isGlobal, string templateName)**  

**Draw.FibonacciCircle(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, bool isGlobal, string templateName)**

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
* Determines if the draw object will be included in the y-axis scale. Default value is false.

---

* startBarsAgo
* The starting bar (x axis co-ordinate) where the draw object will be drawn. For example, a value of 10 would paint the draw object 10 bars back.

---

* startTime
* The starting time where the draw object will be drawn.

---

* startY
* The starting y value co-ordinate where the draw object will be drawn.

---

* endBarsAgo
* The end bar (x axis co-ordinate) where the draw object will terminate.

---

* endTime
* The end time where the draw object will terminate.

---

* endY
* The end y value co-ordinate where the draw object will terminate.

---

* isGlobal
* Determines if the draw object will be global across all charts which match the instrument.

---

* templateName
* The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead).
{% /table %}

## Examples

```csharp
// Draws a Fibonacci circle
Draw.FibonacciCircle(this, "tag1", true, 10, Low[10], 0, High[0]);
```