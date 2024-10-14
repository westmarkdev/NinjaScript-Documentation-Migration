










 


OnWindowSaved()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onwindowsaved.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
OnWindowSaved() | [Previous page](onwindowrestored.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


Called when the window is saved to a workspace, which is called before [OnWindowDestroyed()](onwindowdestroyed.htm).  This method is used to save any custom XElement data associated with your window.



Method Return Value
-------------------


This method does not return a value



Syntax
------


OnWindowSaved(Window window, XElement element)
----------------------------------------------


 


Parameters
----------




|  |  |
| --- | --- |
| window | A [Window](https://msdn.microsoft.com/en-us/library/system.windows.window(v=vs.110).aspx) object which is being saved to the workspace |
| element | A [XElement](https://msdn.microsoft.com/en-us/library/system.xml.linq.xelement(v=vs.110).aspx) object representing the workspace being saved |





Examples
--------




| ns |
| --- |
| protected override void OnWindowSaved(Window window, XElement element)
{
   Print("OnWindowSaved for " + window.GetHashCode()); 
 
   // create a new XElement to save the last state of a custom button to the workspace
   XElement xml = new XElement("SampleAddOn", new XElement("ButtonState", true));
 
   // e.g.,
   // <sampleaddon>
   //  <buttonstate>true</buttonstate>
   // </sampleaddon>
 
   // add the new element to the workspace which can be restored later
   element.Add(xml);                
 
   //Don't forget to call the base OnWindowSaved method after you've finished your operation.
   base.OnWindowSaved(window, element);
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
 
 
 



