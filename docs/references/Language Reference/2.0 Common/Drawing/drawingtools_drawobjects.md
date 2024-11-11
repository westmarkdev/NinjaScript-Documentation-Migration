---
title: DrawObjects
pathName: drawingtools_drawobjects
parent: drawing
section: references
status: changed
---

## Definition

A collection holding all of the drawn chart objects on the chart, for all series. The draw objects can be manually drawn or script generated objects.

{% callout type="note" %}

* When reloading **NinjaScript**, all objects (including manual drawing tools) are reloaded at the same time. There is no guarantee a manually drawn object will be added to the **DrawObjects** collection before an indicator starts processing data.
* **DrawObjects.ToList()** is thread safe. **DrawObjects** collection itself is still dynamic (meaning it updates live) and as a result you can still run the risk of the collection being modified while you try to read it (and thus would see the related **C#** log entry). However, **DrawObjects.ToList()** is a snapshot of **DrawObjects** collection at the time the call is made.
* Also please keep in mind that iterating over a large **DrawObjects** collection could have an impact on performance.
* Draw objects are disposed (for example on chart closing) after **State.Terminated** is seen for your custom **NinjaScript** studies potentially working with those.
{% /callout %}

## Property Value

A collection of [**IDrawingTool**](idrawingtool) objects.

## Syntax

**DrawObjects**  

**DrawObjects[string tag]**  

**DrawObjects.Count**

## Examples

### Finding the draw object of a specific tag

```csharp
protected override void OnBarUpdate()
{
   if (DrawObjects["someTag"] != null && DrawObjects["someTag"] is DrawingTools.Line)
   {
     // Do something with the drawing tool line
   }
  
   // An alternative approach to find the draw object by a tag
   if (DrawObjects["someTag"] as DrawingTools.Line != null)
   {
     // Do something drawing tool line
   }
  
   // Yet another way to find a drawing tool by a tag
   if (DrawObjects["someTag"].GetType().Name == "Line")
   {
     // Do something drawing tool line
   }
}

```

### Get the number of draw objects on a chart

```csharp
protected override void OnBarUpdate()
{
   if (DrawObjects.Count == 3)
   {
         // Do something
   }
}
```

## Looping through the collection to find specific draw objects

```csharp
protected override void OnBarUpdate()
{
   // Loops through the DrawObjects collection via a threadsafe list copy
   foreach (DrawingTool draw in DrawObjects.ToList())
   {
     // Finds line objects that are attached globally to all charts of the same instrument
     if (draw.IsGlobalDrawingTool && draw is DrawingTools.Line)
     {
         DrawingTools.Line globalLine = draw as DrawingTools.Line;

         // Changes the line color and prints its starting and end points
         globalLine.Stroke.Brush = Brushes.Black;

         Print("Start: " + globalLine.StartAnchor.SlotIndex + " End: " + globalLine.EndAnchor.SlotIndex);
     }

     // Finds non-global line objects
     else if (draw is DrawingTools.Line)
     {
         // Indicates if this is a manually drawn or script generated line
         Print("Line Object: " + draw.Tag + " Manually Drawn: " + draw.IsUserDrawn);
     }
   }
}
```

{% callout type="note" %}

Typecasting as in the example above will not function the same way in a compiled assembly (DLL). For an alternative approach, see the [Considerations For Compiled Assemblies](considerations_for_compiled_assemblies) page.

{% /callout %}
