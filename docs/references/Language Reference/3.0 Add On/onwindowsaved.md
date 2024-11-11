---
title: OnWindowSaved()
pathName: onwindowsaved
parent: add_on
section: references
status: imported
---

## Definition

Called when the window is saved to a workspace, which is called before **OnWindowDestroyed()**. This method is used to save any custom **XElement** data associated with your window.

## Method Return Value

This method does not return a value.

## Syntax

**OnWindowSaved(Window window, XElement element)**

## Parameters

{% table %}

---

* **window**
* A [Window](window) object which is being saved to the workspace

---

* **element**
* A [XElement](xelement) object representing the workspace being saved
{% /table %}

## Examples

```csharp
protected override void OnWindowSaved(Window window, XElement element)
{
    Print("OnWindowSaved for " + window.GetHashCode()); 

    // create a new XElement to save the last state of a custom button to the workspace
    XElement xml = new XElement("SampleAddOn", new XElement("ButtonState", true));

    // e.g.,
    // <sampleaddon>
    //  <buttonstate>true</buttonstate>
    // </sampleaddon>

    // add the new element to the workspace which can be restored later
    element.Add(xml);                    

    //Don't forget to call the base OnWindowSaved method after you've finished your operation.
    base.OnWindowSaved(window, element);
}
```
