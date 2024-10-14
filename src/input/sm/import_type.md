










 


Import Type







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?import_type.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Import Type | [Previous page](zordertype.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom data Import Types can be developed to allow for the importing of historical data from any format. Two important event handler methods are documented in this section:


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [OnNextInstrument()](onnextinstrument.htm) | Called at the beginning of the import process |
| [OnNextDataPoint()](onnextdatapoint.htm) | Called for each line of data contained in the file being imported |






 
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
 
 
 



