Delete()
{

	web_rest("DELETE",
		"URL=http://127.0.0.1:{port}/rest/api/2/issue/",
		"Method=DELETE",
		"EncType=raw",
		"Snapshot=t552486.inf",
		LAST);

	
	return 0;
}
