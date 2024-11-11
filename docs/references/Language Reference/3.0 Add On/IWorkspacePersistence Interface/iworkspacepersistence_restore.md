---
title: Restore()
pathName: iworkspacepersistence_restore
parent: iworkspacepersistence_interface
section: references
status: changed
---

Restores the window from workspaces.

## Examples

```csharp
// IWorkspacePersistence member. Required for restoring window from workspaces**
public void Restore(XDocument document, XElement)
{
     if (MainTabControl != null)
          MainTabControl.RestoreFromXElement(element);
}
```
