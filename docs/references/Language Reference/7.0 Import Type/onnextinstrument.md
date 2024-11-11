---
title: OnNextInstrument()
pathName: onnextinstrument
parent: import_type
status: imported
section: references
---

## Definition

The **OnNextInstrument()** method is called at the beginning of the import process for each file that is being imported. This method is only called after it has determined the file contains a valid instrument.

## Method Return Value

This method does not return a value.

## Syntax

See example below. The NinjaScript code wizard automatically generates the method syntax for you.

## Examples

```csharp
private int currentInstrumentIdx = -1;

public string[] FileNames 
{ get; set; }

protected override void OnNextInstrument()
{
    if (FileNames == null)
        return;

    // Try to read from file into the FileNames array created above
    // Log an error and continue if the data is unreadable
    try
    {
        reader = new StreamReader(FileNames[currentInstrumentIdx]);
    }
    catch (Exception exp)
    {
        NinjaScript.Log(FileNames[currentInstrumentIdx], exp.Message, LogLevel.Error);
        continue;
    }
}
```
