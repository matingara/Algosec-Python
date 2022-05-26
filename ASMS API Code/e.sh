echo "What is the name for the cookie?"
read AFACOOKIE
https --verify=no -v POST 192.168.0.237/fa/server/connection/login username=admin password=algosec --session=$AFACOOKIE
# https --verify=no -v POST 192.168.0.237/afa/api/v1/query --session=AFACOOKIE << END-OF-INPUT 
echo "USING SESSION COOKIE NAMED" $AFACOOKIE
https --verify=no -v GET 192.168.0.237/afa/api/v1/devices --session=$AFACOOKIE
https --verify=no -v POST 192.168.0.237/afa/api/v1/query --session $AFACOOKIE << END-OF-INPUT1
{
  "includeDevicesPaths": true,
  "includeRulesZones": true,
  "queryInput": [
    {
      "application": [
        "any"
      ],
      "destination": [
        "172.16.102.29, 172.16.102.30, 172.16.102.31"
      ],
      "service": [
        "tcp/7171"
      ],
      "source": [
        "172.16.2.29, 172.16.2.30, 172.16.2.31"
      ],
      "user": [
        "any"
      ]
    }
  ],
  "queryTarget": "ALL_FIREWALLS"
}
END-OF-INPUT1
echo "PIG-HOO-WEEEEEEEEEEEE"