---
title: Chart Style
pathName: chart_style
parent: language_reference
order: 5
status: imported
section: references
---

Custom Chart Styles can be used on charts to present bars information in a different visual representation. The methods and properties covered in this section are unique to custom Chart Style development. Following is an index of properties and methods documented for Chart Styles.

## Methods and Properties

{% table %}

* Name
* Description

---

* BarWidth
* The painted width of a ChartStyle bar

---

* BarWidthUI
* The Bar width value which displays on the UI

---

* ChartStyleType
* Defines a unique identifier value used to register a custom ChartStyle

---

* DownBrush
* A Brush object used to determine the color to paint the down bars for the ChartStyle

---

* DownBrushDX
* A SharpDX.Brush object used to paint the down bars for the ChartStyle

---

* GetBarPaintWidth()
* Returns the painted width of the chart bar

---

* IsTransparent
* Indicates the bars in the ChartStyle are transparent

---

* OnRender()
* An event driven method used to render content to a ChartStyle

---

* SetPropertyName()
* Sets a default property name to a custom string to be displayed on the UI

---

* TransformBrush()
* Scales a non-solid color brush used for rendering the chart style to properly display in NinjaTrader

---

* UpBrush
* A Brush object used to determine the color to paint the up bars for the ChartStyle

---

* UpBrushDX
* A SharpDX.Brush object used to paint the up bars for the ChartStyle

---
{% /table %}
