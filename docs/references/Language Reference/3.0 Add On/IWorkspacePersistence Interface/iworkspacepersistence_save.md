---
title: Save()
pathName: iworkspacepersistence_save
parent: iworkspacepersistence_interface
section: references
status: changed
---

Saves the window to workspaces.

## Examples

```csharp
// IWorkspacePersistence member. Required for saving window to workspaces**
public void Save(XDocument document, XElement element)
{
     if (MainTabControl != null)
         MainTabControl.SaveToXElement(element);
}
```
