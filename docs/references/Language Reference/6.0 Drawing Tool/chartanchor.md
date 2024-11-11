---
title: ChartAnchor
pathName: chartanchor
parent: drawing_tools
status: imported
section: references
---

## Definition

Defines objects used by Drawing Tools which represent a point on the chart where the Drawing Tool is located.

## Syntax

**class ChartAnchor**

## Constructors

{% table %}

* Constructor
* Description

---

* **new ChartAnchor()**
* Initializes a new instance of the ChartAnchor object

---

* **new ChartAnchor(DateTime time, double price, [ChartControl](chartcontrol))**
* Initializes a new instance of the ChartAnchor object using time, price, and relative chart control

---

* **new ChartAnchor(DateTime time, double yValue, int currentBar, [ChartControl](chartcontrol))**
* Initializes a new instance of the ChartAnchor object using time, y-axis coordinates, current bar, and relative chart control
{% /table %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* **[CopyDataValues()](copydatavalues)**
* Copies the ChartAnchor time and price values from one anchor to another

---

* **[DisplayName](displayname)**
* A **string** value which sets the name prefix used for all properties for a chart anchor

---

* **[DrawingTool](drawingtool)**
* The drawing tool which owns a chart anchor

---

* **[DrawnOnBar](drawnonbar)**
* Gets the current bar value that the chart anchor is drawn by a NinjaScript object.

---

* **[GetPoint()](getpoint)**
* Returns a chart anchor's data points.

---

* **[IsBrowsable](isbrowsable)**
* A bool value determining if the anchor is visible on the UI.

---

* **[IsEditing](isediting)**
* A bool value determining if the anchor is currently being edited

---

* **[IsNinjaScriptDrawn](isninjascriptdrawn)**
* Indicates if the chart anchor was drawn by a NinjaScript object

---

* **[IsXPropertiesVisible](isypropertyvisibile)**
* A bool value determining if the X properties are visible on the UI

---

* **[IsYPropertyVisible](isypropertyvisibile)**
* A bool value determining if the Y data value is visible on the UI

---

* **[MoveAnchor()](moveanchor)**
* Moves a Chart Anchor's x and y values from start point by a delta point amount.

---

* **[MoveAnchorX()](moveanchorx)**
* Moves an anchor's x values from start point by a delta point amount

---

* **[MoveAnchorY()](moveanchory)**
* Moves an anchor's y values from start point by a delta point amount

---

* **[Price](price)**
* Determines the price value the chart anchor is drawn.

---

* **[SlotIndex](barindex)**
* Indicates the nearest bar slot where the anchor is drawn.

---

* **[Time](time)**
* Determines the date/time value the chart anchor is drawn.

---

* **[UpdateFromPoint()](updatefrompoint)**
* Updates an anchor's x and y values from a given point (in device pixels)

---

* **[UpdateXFromPoint()](updatexfrompoint)**
* Updates an anchor's X values from a given point (in device pixels)

---

* **[UpdateYFromPoint()](updateyfrompoint)**
* Updates an anchor's Y value from a given point (in device pixels)
{% /table %}

## Examples

```csharp

public ChartAnchor MyAnchor { get; set; } // declares the "MyAnchor" ChartAnchor object
public override IEnumerable<chartanchor> Anchors { get { return new[] { MyAnchor }; } } //adds the "MyAnchor" ChartAnchor object to a collection of anchors used to interact with your anchors
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Description = @"Drawing tool example";
     Name = "SampleDrawingTool";

     MyAnchor = new ChartAnchor(); //creates a new instance of the ChartAnchor object
     MyAnchor.IsEditing = true;
     MyAnchor.DrawingTool = this;
     MyAnchor.IsBrowsable = false;
   }
}

public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   if (DrawingState == DrawingState.Editing)
   {
     if (MyAnchor.IsEditing)
     {
         //if anchor is editing, update anchor point
         dataPoint.CopyDataValues(MyAnchor);
     }
   }

```
