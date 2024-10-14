










 


CharactersReservedPerMedia







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?charactersreservedpermedia.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Share Service](share_service.htm) &gt;
CharactersReservedPerMedia | [Previous page](characterlimit.htm)
[Return to chapter overview](share_service.htm)










Definition
----------


Sets the number of characters allowed when attaching an image to ensure that character count is properly calculated.


 




|  |
| --- |
| Note:  Social networks which limit the number of characters for each post, will have a defined number of characters that are reserved when an image or other media is attached.   |





Property Value
--------------


A int value that represents the number of characters reserved when attaching an image or other media.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


CharactersReservedPerMedia


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{                        
if (State == State.SetDefaults)
{
CharactersReservedPerMedia        = 40;
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
 
 
 



