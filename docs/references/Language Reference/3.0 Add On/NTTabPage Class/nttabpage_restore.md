---
title: Restore()
pathName: nttabpage_restore
parent: nttabpage
section: references
status: changed
---

## Restore()

Restores any elements in our **NTTabPage** from the workspace. (e.g. Selected accounts or instruments)

## Examples

```csharp
// NTTabPage member. Required for restoring elements from workspaces
public void Restore(XElement element)
{
    if (element == null)
        return;

    // Restore any elements you may have saved. e.g. selected accounts or instruments
}
```
