Get()
{

	web_rest("Get",
		"URL=http://127.0.0.1:{port}/rest/api/2/issue/",
		"Method=GET",
		"Snapshot=t66456.inf",
		LAST);

	
	return 0;
}
