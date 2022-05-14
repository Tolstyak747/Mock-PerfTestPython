Create()
{

	web_rest("Create",
		"URL=http://127.0.0.1:{port}/rest/api/2/issue/",
		"Method=POST",
		"EncType=raw",
		"Snapshot=t345017.inf",
		"Body={\"description\": \"something\",\"summary\": \"Create issue\"}",
		HEADERS,
		"Name=Content-Type", "Value=application/json", ENDHEADER,
		LAST);

	
	return 0;
}
