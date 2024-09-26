


GetValueAt()









 


MethodName()















Definition
----------


Defines the method/property


 




|  |
| --- |
| Note:  This important note |



 


Method Return Value
-------------------


A bool value when true; otherwise false.


 


Syntax
------


MethodName(int input)


 


 
Parameters
------------




|  |  |
| --- | --- |
| input | An int which represents the method input |




 


Examples
--------




| ns |
| --- |
| 1 |   |






 
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
 
 
 



