TROUBLESHOOTING
===============

This page contains common problems found during the application development, and how to fix them.

___
**id**: 1   
**Title**: unicode encode error ascii codec cant encode character   
**Tags**: unicode, encode, error, ascii, codec, encode, character, python   

**Description**:   
When trying to read or write data get from beautiful soup, sometimes the error "unicode encode error ascii codec cant encode character"
will appear.
   
**Cause:**   
This is due to the text containing non-ascii characters (like japanese characters).

**Solution:**   
	Change the encode of the text to another one, like utf-8. [Resources](https://github.com/amcajal/gsvmind/wiki/References) 4 has a nice solution to it.
	Another option (when change encoding does not works) is to remove all non-ascii characters, as shown in 
    [Resources](https://github.com/amcajal/gsvmind/wiki/References) 13.
	Another option to remove the non-ascii characters is shown at [Resources](https://github.com/amcajal/gsvmind/wiki/References) 12, under section "Dealing with unicode errors".

**References:**   
	[RESOURCES](https://github.com/amcajal/gsvmind/wiki/References) 4, 12 and 13
___

**id**:   
**Title**:   
**Tags**: 

**Description**:   
    .
    
**Cause:**   
    .

**Solution:**   
	.

**References:**   
	.