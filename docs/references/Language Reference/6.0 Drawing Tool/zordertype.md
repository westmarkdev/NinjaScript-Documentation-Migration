---
title: ZOrderType
pathName: zordertype
parent: drawing_tools
section: references
status: imported
---

## Definition

Determines the order in which sthe drawing tool will be rendered. This will help control the [ZOrder](chart_zorder.htm) index between chart objects

## Property Value

An enum determining the drawing tool's ZOrder type.  Possible values are:

{% table %}

* Name

* Description

---

* **DrawingToolZOrder.Normal**

* Default behavior, drawing tools are rendered as they appear in the [ZOrder](chart_zorder) index

---

* **DrawingToolZOrder.AlwaysDrawnFirst**

* Ensures the drawing tool is always the first to be rendered

---

* **DrawingToolZOrder.AlwaysDrawnLast**

* Ensures the drawing tool is always the last object to be rendered

---

{% /table %}

## Syntax

**ZOrderType**

## Examples

```csharp
protected override void OnStateChange()  
{  
  if (State == State.SetDefaults)  
  {  
    Name               = @"My Drawing Tool";  
           
    // always draw this last  
    ZOrderType           = DrawingToolZOrder.AlwaysDrawnLast;  
  }  
  else if (State == State.Configure)  
  {  
  }  
}
```
