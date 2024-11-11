---
section: references
title: RemoveDrawObject()
pathName: removedrawobject
parent: drawing
status: review
---

## Definition

Removes a draw object from the chart based on its tag value.

{% callout type="note" %}

This method will ONLY remove DrawObjects which were created by a NinjaScript object. User drawn objects CANNOT be removed from via NinjaScript.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**RemoveDrawObject**(string tag)

## Parameters

{% table %}

* Parameter
* Description

---

* **tag**
* A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time.
{% /table %}

## Examples

```csharp
// Removes a draw object with the tag "tag1"**
RemoveDrawObject("tag1");
```
