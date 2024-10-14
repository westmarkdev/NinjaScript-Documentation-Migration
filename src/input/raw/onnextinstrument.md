










 


OnNextInstrument()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onnextinstrument.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Import Type](import_type.htm) &gt;
OnNextInstrument() | [Previous page](import_type.htm)
[Return to chapter overview](import_type.htm)










Definifition
------------


The OnNextInstrument() method is called at the beginning of the import process for each file that is being imported.  This method is only called after it has determined the file contains a valid instrument.



Method Return Value
-------------------


This method does not return a value.



Syntax
------


See example below. The NinjaScript code wizard automatically generates the method syntax for you.


 


Example
-------




| ns |
| --- |
| private int currentInstrumentIdx = -1;
 
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
} |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



