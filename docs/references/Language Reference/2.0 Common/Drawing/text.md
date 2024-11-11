---
section: references
title: Draw.Text()
pathName: draw_text
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding a Text **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* Anchor

* An **IDrawingTool's ChartAnchor** representing the point of the drawing object

---

* YPixelOffset

* An **int** value representing the offset value in pixels from within the text box area

---

* Alignment

* Possible values are:

**TextAlignment.Center**,

**TextAlignment.Left**,

**TextAlignment.Right**,

**TextAlignment.Justify** ([reference](https://msdn.microsoft.com/en-us/library/system.windows.textalignment(v=vs.110).aspx))

---

* AreaOpacity

* An **int** value representing the opacity of the area color

---

* AreaBrush

* A **Brush** class representing the fill color of the text box

---

* Text

* A **string** value representing the text to be drawn

---

* TextBrush

* A **Brush** class representing the color of the text

---

* Font

* A **Font** object representing the font for the text

---

* OutlineStroke

* The **Stroke** object used to outline the text box

---

{% /table %}

## Examples

```csharp
// Instantiate a Text object
Text myText = Draw.Text(this, "tag1", "Text to draw", 10, High[10] + (5 * TickSize), Brushes.Black);

// Change the object's DisplayText
myText.DisplayText = "New Display Text";
```
