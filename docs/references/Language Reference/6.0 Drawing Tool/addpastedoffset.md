---
title: AddPastedOffset()
pathName: addpastedoffset
parent: drawing_tools
status: imported
section: references
---

## Definition

A [virtual method](https://msdn.microsoft.com/en-us/library/9fkccyh4.aspx) which is called every time a DrawingTool is copied and pasted to a chart. The default behavior will offset the chart anchors price value down by 1, percent. However, this behavior can be overridden for your custom drawing tool if desired.

## Method Return Value

This method does not return a value

## Syntax

You must override this method using the following syntax:

**public override void AddPastedOffset(ChartPanel panel, ChartScale chartScale)**

## Method Parameters

{% table %}

* panel
* chartScale

---

* A ChartPanel representing the the panel for the chart
* A ChartScale representing the Y-axis
{% /table %}

## Examples

```csharp
public override void AddPastedOffset(ChartPanel chartPanel, ChartScale chartScale)
{      
   foreach (ChartAnchor anchor in Anchors)
   {
     //bump each anchor 1 minute to the right
     DateTime tmpTime = anchor.Time;
     anchor.Time = tmpTime.AddMinutes(1);        
   }         
}
```
