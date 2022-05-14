/* -------------------------------------------------------------------------------
	Script Title       : 
	Script Description : 
                        
                        
	Recorder Version   : 911
   ------------------------------------------------------------------------------- */

vuser_init()
{

	web_set_user("USER_6", 
		lr_unmask("623dcff4416199ca90d7"), 
		"127.0.0.1:5000");

	web_url("127.0.0.1:5000", 
		"URL=http://127.0.0.1:5000/", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t2.inf", 
		"Mode=HTML", 
		LAST);

	return 0;
}