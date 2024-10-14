










 


OnNextDataPoint()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onnextdatapoint.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Import Type](import_type.htm) &gt;
OnNextDataPoint() | [Previous page](onnextinstrument.htm)
[Return to chapter overview](import_type.htm)










Definifition
------------


The OnNextDataPoint() method is called for each line of data contained in the file being imported. This method is only called if the import type determines that the file has a valid data point, and will continue to be called until it reaches the end of the file, or until the data point is no longer valid.



Method Return Value
-------------------


This method does not return a value.



Syntax
------


See example below. The NinjaScript code wizards automatically generate the method syntax for you.


 


Example
-------




| ns |
| --- |
| private StreamReader reader;       
 
protected override void OnNextDataPoint()
{
   if (reader == null)
       return;
 
   // Continually read data using the StreamReader defined above
   while (true)
   {
       DataPointString = reader.ReadLine();
       // Additional data formatting here
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
 
 
 



