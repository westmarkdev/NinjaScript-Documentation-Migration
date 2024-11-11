---
section: references
title: TextFixed
pathName: textfixed
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding a Text Fixed **IDrawingTool**.

## Methods and Properties

{% table %}

* Anchor
* YPixelOffset
* Alignment
* AreaOpacity
* AreaBrush
* DisplayText
* TextBrush
* Font
* OutlineStroke
* TextPosition

---

* An **IDrawingTool's ChartAnchor** representing the point of the drawing object
* An **int** value representing the offset value in pixels from within the text box area
* Possible values are:
  
  **TextAlignment.Center**  
  **TextAlignment.Far**  
  **TextAlignment.Near**  
  **TextAlignment.Justify**  
  ([reference](https://msdn.microsoft.com/en-us/library/system.windows.textalignment%28v=vs.110%29.aspx))
* An **int** value representing the opacity of the area color
* A **Brush** class representing the fill color of the text box
* A **string** value representing the text to be drawn
* A **Brush** class representing the color of the text
* A **Font** object representing the font for the text
* The **Stroke** object used to outline the text box
* Possible values are:
  
  **TextPosition.BottomLeft**  
  **TextPosition.BottomRight**  
  **TextPosition.Center**  
  **TextPosition.TopLeft**  
  **TextPosition.TopRight**
{% /table %}

## Examples

```csharp
// Instantiate a TextFixed object
TextFixed myTF = Draw.TextFixed(this, "tag1", "Text to draw", TextPosition.TopRight);
 
// Change the object's TextPosition
myTF.TextPosition = TextPosition.Center;
```
