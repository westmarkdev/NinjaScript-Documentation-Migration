---
title: Drawing Tools
pathName: drawing_tools
parent: language_reference
order: 6
status: imported
section: references
---

Custom Drawing Tools can be used to render custom shapes to a point on the chart to represent various information. The methods and properties covered in this section are unique to custom Drawing Tools development. Following is an index of the documented properties and methods related to drawing tools.

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* **AddPastedOffset()**
* A **virtual method** which is called every time a Drawing Tool is copied and pasted to a chart

---

* **Anchors**
* Creates a collection of Chart Anchors which will represent various points of the drawing tool

---

* **AttachedTo**
* An object which holds information regarding where the drawing tool is attached

---

* **ChartAnchor**
* Defines objects used by Drawing Tools which represent a point on the chart where the Drawing Tool is located

---

* **ConvertToVerticalPixels**
* Used to convert the cursor position (pixels) to device pixels represented on the Y axis of the chart

---

* **CreateAnchor()**
* Used to create a new chart anchor at a specified mouse point

---

* **DisplayOnChartsMenus**
* Determines if the drawing tool should be listed in the chart's drawing tool menus

---

* **Dispose()**
* Releases any device resources used for the drawing tool

---

* **DrawingState**
* Represents the current state of the drawing tool in order to perform various actions, such as building, editing, or moving

---

* **DrawnBy**
* Represents the NinjaScript object by which the drawing tool was created

---

* **GetAttachedToChartBars()**
* Returns information which relate to the underlying bars series in which the drawing tool is attached

---

* **GetClosestAnchor()**
* Returns the closest chart anchor within a specified maximum distance from the mouse cursor

---

* **GetCursor()**
* An event driven method which is called when a chart object is selected

---

* **GetSelectionPoints()**
* Returns the chart object's data points where the user can interact

---

* **Icon**
* The shape which displays next to the drawing tool menu item

---

* **IgnoresSnapping**
* Determines if the drawing tool chart anchor's will use the chart's Snap Mode mouse coordinates

---

* **IgnoresUserInput**
* Determines if the drawing tool can be clicked on by the user

---

* **IsAttachedToNinjaScript**
* Indicates if the drawing tool is currently **attached to** a NinjaScript object (such an indicator or a strategy)

---

* **IsGlobalDrawingTool**
* Indicates if the drawing tool is currently set as a Global Drawing object

---

* **IsLocked**
* Determines if the drawing tool should be locked in place

---

* **IsUserDrawn**
* Indicates if the drawing tool was manually drawn by a user

---

* **OnBarsChanged()**
* An event driven method which is called any time the underlying bar series have changed for the chart where the drawing tool resides

---

* **OnMouseDown()**
* An event driven method which is called any time the mouse pointer over the chart control has the mouse button pressed

---

* **OnMouseMove()**
* An event driven method which is called any time the mouse pointer is over the chart control and a mouse is moving

---

* **OnMouseUp()**
* An event driven method is called any time the mouse pointer is over the chart control and a mouse button is being released

---

* **SupportsAlerts**
* Indicates if the drawing tool can be used for manually configured alerts through the UI

---

* **ZOrderType**
* Determines the order in which the drawing tool will be rendered
{% /table %}
