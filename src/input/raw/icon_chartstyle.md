










 


Icon







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?icon_chartstyle.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
Icon | [Previous page](getbarpaintwidth.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


The shape which displays next to the Chart Style menu item.  Since this is a standard object, any type of icon can be used (unicode characters, custom image file resource, geometry path, etc). 


 


For more information on using images to create icons, see the [Using Images with Custom Icons](using_images_and_geometry_with_custom_icons.htm) page.


 




|  |
| --- |
| Note: When using UniCode characters, first ensure that the desired characters exist in the icon pack for the font family used in NinjaTrader. |



 


 


Property Value
--------------


A generic virtual object representing the drawing tools menu icon.  This property is read-only.


 


 


Syntax
------


You must override this property using the following syntax:



public override object Icon


 


Examples
--------




| ns |
| --- |
| public override object Icon
{         
   get 
   {
     //use a unicode character as our string which will render an arrow
     string uniCodeArrow = "\u279A";            
     return uniCodeArrow; 
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
 
 
 



