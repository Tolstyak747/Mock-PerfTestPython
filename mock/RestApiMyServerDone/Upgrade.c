Upgrade()
{

	web_rest("Upgrade",
		"URL=http://127.0.0.1:{port}/rest/api/2/issue/",
		"Method=PUT",
		"EncType=raw",
		"Snapshot=t156146.inf",
		"Body={\"description\": \"something\",\"priority\": 1,\"summary\": \"Update issue\"}",
		HEADERS,
		"Name=Content-Type", "Value=application/json", ENDHEADER,
		LAST);

	
	return 0;
}
